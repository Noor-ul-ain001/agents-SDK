import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig
from dotenv import load_dotenv
import asyncio
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.5-flash", openai_client=client
            ),
    )

    result = await Runner.run(
        agent,
        "I am learning Agentic AI please provide some information related..",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
