🛠 Tool Calls in Agent SDK 

Tools let your agent connect with external logic or APIs. Instead of the agent doing everything with plain text, you give it functions as tools, and it automatically decides when to call them.

🔑 How Tool Calls Work

Define a Tool

You take a normal Python function.

Add @function_tool → This turns it into a tool.

Register Tools with Agent

Pass the tool(s) inside tools=[...] when creating the agent.

Agent Reads User Input

Agent analyzes what the user asked.

If it matches a tool, it calls the tool automatically.

Runner Executes

Use Runner.run_sync(agent, "your prompt").

Agent runs, tool is called, final answer is returned.

🔄 Tool Call Flow (Visual)
User → Agent → Tool → Agent → Final Answer


Step by step:

User: asks a question.

Agent: checks if it can solve it directly or needs a tool.

Tool: runs the registered function and returns output.

Agent: takes the tool’s output, formats a response.

Final Answer: shown to the user.

✨ Benefits

Keep agent lightweight (it doesn’t reinvent logic).

Add custom functionality (math, APIs, databases, etc.).

Fully automatic — no manual tool calling needed.
