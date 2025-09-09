from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, enable_verbose_stdout_logging
from openai.types.responses import ResponseTextDeltaEvent
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
    name="Helpful Assistant",
    instructions="You are a helpful assistant",
    model=model
)
async def main():
    result = Runner.run_streamed(
        agent,"write about agentic ai", 
    )
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, flush=True, end="")
            
            
if __name__ =="__main__":
    asyncio.run(main())            
    
            
