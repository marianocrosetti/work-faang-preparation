Welcome to your practice interview. Use this session to familiarize yourself with the environment that you will be using in your AI-Enabled SWE Coding interview.

# Drone Delivery

A fleet of drones must deliver products from warehouses to customers on a 2D grid.

- Drones start at warehouse 0 and execute commands: Load, Deliver, Wait.
- Each Load/Deliver costs 1 turn plus travel time (ceiling of Euclidean distance).
- Orders are complete when all requested products are delivered.
- Score per completed order: `ceil((T - t) / T * 100)`, where T = max turns, t = turn completed.
- Higher total score is better.

# Your tasks

- Explore the code. Understand how the classes fit together.
- Run the unit tests. Some fail — there are bugs in the provided code. Fix them.
- There are commented-out tests. Uncomment them when ready.
- Implement the Planner to generate an efficient delivery plan.
- Use the AI Assistant as much or as little as you would like.
