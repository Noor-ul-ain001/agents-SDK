from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, enable_verbose_stdout_logging, ModelSettings
from dotenv import load_dotenv
import os
import asyncio
# enable_verbose_stdout_logging()
load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash",
)
agent = Agent(
    name= "assistant",
    instructions="you are a helpful assistant",
    model = model
)
async def main():
    result =await Runner.run(
    agent,"hello"
)

    print(result.final_output)
    
    
if __name__ =="__main__":
    asyncio.run(main())
    
