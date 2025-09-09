from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, function_tool, ModelSettings
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
)

@function_tool
def add(a:int, b:int)->int:
    return a + b


agent: Agent = Agent(
    name="Assistant",
    instructions = "you are a helpful assistant",
    tools= [add],
    model_settings=ModelSettings(tool_choice="required"),
    model = model
)

result = Runner.run_sync(
    starting_agent=agent,
    input="Sum 1000 and 3213"
)

print(result.final_output)