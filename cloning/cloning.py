import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash"
)


assistant_agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

cloned_agent = assistant_agent.clone()


def main():
    result = Runner.run_sync(
        cloned_agent,
        input="Hello, how are you?"
    )
    print(result.final_output)

if __name__ == "__main__":
    main()
