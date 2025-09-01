🧩 What is clone()?

The clone() method creates a duplicate agent from an existing one.

It preserves the instructions and model.

It allows you to create a new agent instance without rewriting all configuration details.

It is helpful in workflows where you may want multiple agents with the same behavior but different contexts.

🎯 Why Use clone()?

Reusability → Quickly create new agents with the same base configuration.

Isolation → Keep the original agent unchanged while experimenting with the clone.

Flexibility → You can later modify the cloned agent (e.g., change its instructions) without affecting the original one.
