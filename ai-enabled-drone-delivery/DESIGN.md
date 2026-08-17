# Drone Delivery Exercise — Design Document

Complete conversation dump to replicate the exercise from scratch.

---

## 1. Context & Goal

Create a new AI-enabled interview exercise for `work-faang-preparation` repo, alongside the existing Wordle solver in `ai-enabled-coding/`. Requirements:

- Heuristic optimization problem (not a guessing/deduction game like Wordle)
- Optimal solution is almost impossible (NP-hard), but greedy baseline is easy
- Interesting observations / "aha moments" along the way
- Rich class structure (inspired by Amani MapReduce workers)
- Some tests with bugs in provided code that fail
- Something the user has to extend (not just implement from scratch)
- No docstrings

---

## 2. Problem Selection

### Research done

Searched for problems from Google Hash Code, AtCoder Heuristic, Kaggle optimization, Huawei Challenge, Reply Code Challenge, CodinGame, Topcoder Marathon.

### Top candidates considered

| Problem | Source | Why interesting |
|---------|--------|----------------|
| Book Scanning | Hash Code 2020 | Dynamic marginal value greedy |
| Self-Driving Rides | Hash Code 2018 | Wait-for-bonus tradeoff |
| Photo Slideshow | Hash Code 2019 | min() formula insight (~1/3 overlap) |
| **Drone Delivery** | **Hash Code 2016** | **Splitting orders, multi-drone parallelism** |
| Ad Rectangle Placement | AtCoder AHC001 | Visual packing |
| Traffic Signaling | Hash Code 2021 | Simulation + local search |

### Chosen: Drone Delivery

Reasons:
- Explainable in 2-3 minutes
- Greedy baseline codeable in 15-20 min
- Key insights: batch loads, split orders across drones, pick closest warehouse
- Class hierarchy is naturally rich (World, Drone, Command, Simulator, Planner)
- Scales difficulty with scenario size (TINY → SMALL → MEDIUM)
- NP-hard (multi-vehicle pickup-delivery with capacity)

---

## 3. Architecture

### Class Hierarchy

```
models.py
├── Position        — (row, col) with ceil(euclidean) distance
├── Product         — id, weight
├── Warehouse       — id, position, inventory dict
└── Order           — id, position, items list, delivery tracking

commands.py
├── Command (ABC)   — abstract describe()
├── Load            — drone_id, warehouse_id, product_id, quantity
├── Deliver         — drone_id, order_id, product_id, quantity
└── Wait            — drone_id, turns
    [User adds: Move — drone_id, destination Position]

drone.py
└── Drone           — id, position, max_payload, carried dict, busy_until

world.py
└── World           — grid config, products, warehouses, orders, create_drones()
                      factory: World.from_dict(scenario)

scenarios.py        — TINY, SMALL, MEDIUM dicts

simulator.py
├── SimulationError — exception class
├── SimulationResult — score, completed, total_orders, max_turn, max_turns
└── Simulator       — run(commands), _execute(cmd), _calculate_score()

planner.py
└── Planner         — skeleton, user implements plan() -> list[Command]
```

### File Structure

```
ai-enabled-drone-delivery/
├── .cpad                  # CoderPad run targets
├── INSTRUCTIONS.md        # Brief for candidate
├── requirements.txt       # black, ipdb
├── Notes.md               # Empty scratch pad
└── src/
    ├── models.py
    ├── commands.py
    ├── drone.py
    ├── world.py
    ├── scenarios.py
    ├── simulator.py       # HAS 2 BUGS
    ├── planner.py         # SKELETON
    ├── main.py
    ├── test_simulator.py  # 15 pass, 2 fail, 1 commented
    └── test_planner.py    # 1 pass, 3 commented
```

---

## 4. Planted Bugs

### Bug 1: Score calculation uses floor instead of ceil

**File:** `simulator.py`, method `_calculate_score()`

**Buggy code:**
```python
score += math.floor((T - turn) / T * 100)
```

**Fix:**
```python
score += math.ceil((T - turn) / T * 100)
```

**Test that catches it:** `test_score_calculation`
- Delivers order at turn 7, max_turns=30
- Expected: ceil((30-7)/30 * 100) = ceil(76.67) = 77
- Actual with bug: floor(76.67) = 76

### Bug 2: No drone capacity validation on Load

**File:** `simulator.py`, method `_execute()`, inside `isinstance(cmd, Load)` branch

**Buggy code:** Missing check before `wh.remove_product()` / `drone.load()`

**Fix:** Add before the load:
```python
if not drone.can_carry(cmd.product_id, cmd.quantity, self.world.products):
    raise SimulationError(f"drone {drone.id} overloaded")
```

**Test that catches it:** `test_overloaded_drone_rejected`
- Loads 3x product weighing 20 = 60 > max_payload 50
- Expected: raises Exception
- Actual with bug: silently succeeds

---

## 5. Extension Point: Move Command

The candidate must create a new `Move` command and handle it in the simulator.

### New class in commands.py:
```python
class Move(Command):
    def __init__(self, drone_id, destination):
        self.drone_id = drone_id
        self.destination = destination

    def describe(self):
        return f"D{self.drone_id} MOVE {self.destination}"
```

### New branch in simulator._execute():
```python
elif isinstance(cmd, Move):
    travel = drone.position.distance_to(cmd.destination)
    drone.busy_until += travel  # no +1, just travel
    drone.position = cmd.destination
```

### Commented test in test_simulator.py:
```python
def test_move_command(self):
    world = make_world()
    from commands import Move
    commands = [
        Move(0, Position(5, 5)),    # fly to (5,5): ceil(sqrt(50))=8
        Load(0, 0, 0),              # back to W0: 8 travel + 1 = 9
        Deliver(0, 0, 0),           # to O0(3,3): 5 travel + 1 = 6
    ]
    result = Simulator(world).run(commands)
    self.assertEqual(result.max_turn, 23)  # 8 + 9 + 6
    self.assertTrue(result.on_time)
```

---

## 6. Scenarios

### TINY (1 drone, trivial)
- 10x10 grid, 1 drone, payload 50, 30 turns
- 3 products (w=10,20,5), 1 warehouse at (0,0), 2 orders
- Purpose: debug and verify basic planner

### SMALL (3 drones, requires strategy)
- 20x20 grid, 3 drones, payload 100, 60 turns
- 5 products, 2 warehouses, 5 orders
- Purpose: test multi-drone planning, warehouse selection

### MEDIUM (5 drones, real optimization)
- 100x100 grid, 5 drones, payload 200, 250 turns
- 10 products, 3 warehouses, 15 orders
- Purpose: stress test, needs good heuristics

---

## 7. Candidate Flow (Expected 45-60 min)

### Phase 1: Explore & Fix (15-20 min)
1. Read INSTRUCTIONS.md
2. Read models.py, commands.py, drone.py — understand class hierarchy
3. Read simulator.py — understand execution flow
4. Run tests → 2 fail
5. **Fix Bug 1:** change `floor` to `ceil` in `_calculate_score`
6. **Fix Bug 2:** add capacity check in `_execute` Load branch
7. All 15 tests pass

### Phase 2: Extend (5-10 min)
1. Uncomment `test_move_command`
2. Create `Move` class extending `Command`
3. Handle `Move` in `Simulator._execute`
4. Test passes

### Phase 3: Implement Planner (20-30 min)
1. Uncomment planner tests
2. Implement basic greedy planner:
   - For each order, find closest warehouse with products
   - Assign drone, generate Load + Deliver commands
3. **Insight 1:** Batch multiple loads at same warehouse (1 trip, multiple products)
4. **Insight 2:** Use multiple drones in parallel for different orders
5. **Insight 3:** Pick warehouse by distance to order, not just to drone
6. **Insight 4:** Split large orders across drones when payload is tight
7. Pass `test_planner_score_above_150`

### Optimization layers (if time):
- Greedy: ~50-100 score on SMALL
- Batched loads + multi-drone: ~150-250
- Closest warehouse selection: ~250-350
- Full optimization (SA/beam search): ~400+

---

## 8. Key "Aha Moments"

1. **Batching loads saves turns** — Loading P0 and P1 at the same warehouse costs 2 turns (no travel between), vs making separate trips
2. **Multiple drones = parallelism** — 3 drones handling 3 orders simultaneously beats 1 drone doing all 5 sequentially
3. **Warehouse selection matters** — Order near W1 should load from W1 even if drone starts at W0; the travel to W1 first saves total distance
4. **Order splitting** — If an order needs 3 heavy products and the drone can only carry 2, send one drone with 2 and another with 1 (parallel delivery)
5. **Delivery order affects score** — Delivering nearby orders first gets higher per-order score (earlier completion → higher ceil((T-t)/T*100))
6. **Score is non-linear** — An order completed at turn 10 vs turn 20 (with T=60) scores 84 vs 67. Early orders are disproportionately valuable.

---

## 9. Simulation Mechanics (Reference)

### Turn cost per command:
- **Load:** `ceil(euclidean(drone, warehouse)) + 1`
- **Deliver:** `ceil(euclidean(drone, order)) + 1`
- **Wait:** `N` turns
- **Move:** `ceil(euclidean(drone, destination))` (no +1)

### Score formula:
```
per_order_score = ceil((max_turns - completion_turn) / max_turns * 100)
total_score = sum of per_order_score for all completed orders
```

### Constraints:
- Drone payload: sum of carried product weights <= max_payload
- Warehouse inventory: can't remove more than available
- Order items: can't deliver more than needed
- Commands executed sequentially per drone (busy_until tracks availability)

---

## 10. Test Results (Before Fixes)

```
test_simulator.py:
  TestModels (8 tests)      — ALL PASS
  TestDrone (3 tests)        — ALL PASS
  TestSimulator:
    test_single_delivery           — PASS
    test_two_deliveries_sequential — PASS
    test_wait_command              — PASS
    test_unknown_command_raises    — PASS
    test_score_calculation         — FAIL (76 != 77)
    test_overloaded_drone_rejected — FAIL (Exception not raised)
    test_move_command              — COMMENTED OUT

test_planner.py:
    test_planner_returns_commands  — PASS
    test_planner_completes_tiny    — COMMENTED OUT
    test_planner_completes_small   — COMMENTED OUT
    test_planner_score_above_150   — COMMENTED OUT
```
