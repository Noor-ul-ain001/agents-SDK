from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from rich import print
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    ),
)


math_expert_agent = Agent(
    name="Mathematician", 
    instructions="You are an expert in mathematics.",
    model=model,
    handoff_description="Handles all mathematical questions and calculations."
)

physics_expert_agent = Agent(
    name="Physicist", 
    instructions="You are an expert in physics.",
    model=model,
    handoff_description="Handles all physics-related queries and theoretical explanations."
)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions."
        "If they ask about maths, handoff to the maths agent."
        "If they ask about physics, handoff to the physics agent."
    ),
    handoffs=[math_expert_agent, physics_expert_agent],
    model=model
)

result = Runner.run_sync(starting_agent=triage_agent, input="What is 2 + 2")
print(result.final_output)
