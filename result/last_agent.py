#type:ignore
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from pydantic import BaseModel
import os, asyncio

load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise KeyError("Does not found an api key") 

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant", 
        model=model
    )
    result = await Runner.run(agent, "Hello")
    print(result.final_output)
    print(f"result.last_agent: {result.last_agent}")
    
if __name__ == "__main__":
    asyncio.run(main())    

