import os
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    set_default_openai_client,
    set_tracing_disabled,
)

load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

set_default_openai_client = external_client

@function_tool
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

@function_tool
def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

agent: Agent = Agent(
    name="Assistant",
    instructions=(
        "You are a helpful assistant. "
        "Always use the provided tools for temperature conversions. "
        "Explain results clearly and briefly."
    ),
    model=model,
    tools=[celsius_to_fahrenheit, fahrenheit_to_celsius],
)

prompt = "Convert 37°C into Fahrenheit"
result = Runner.run_sync(agent, prompt)


print(result.final_output)
