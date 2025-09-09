
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, ModelSettings
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
)


config = RunConfig(
    tracing_disabled=True,
    model=model,
    model_provider=client,
    model_settings=ModelSettings(
        temperature=0.5,
    ),
)

result = Runner.run_sync(
    starting_agent=agent,
    input="Who is the founder of USA",
    run_config=config
)

print(f"FIRST OUTPUT\n {result.final_output}")
