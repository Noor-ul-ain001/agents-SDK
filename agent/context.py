import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, AgentOutputSchema,enable_verbose_stdout_logging, RunContextWrapper, function_tool
from dotenv import load_dotenv
from pydantic import BaseModel
import asyncio
from dataclasses import dataclass
enable_verbose_stdout_logging()
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("api key not found....")

client: AsyncOpenAI = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= client
)

runconfig:RunConfig = RunConfig(
    model_provider=client,
    model=model,
    tracing_disabled=True
)

@dataclass
class User():
    name:str
    user_id: int
    
    
@function_tool
def fetch_user_detail(wrapper:RunContextWrapper[User])->str:
    """return the name and user id"""
    return f"the name of user is {wrapper.context.name} and user id is {wrapper.context.user_id}"



async def main():
    user_info = User(name= "noor", user_id = 123)
    agent:Agent = Agent[User](
    name ="Assistant",
    instructions= "you are a helpful assistant",
    tools = [fetch_user_detail],
    model = model
)
    result = await Runner.run(
        agent, "what is the name of user and user id",
        run_config=runconfig,
        context = user_info
    )
    print(result.final_output)
    
if __name__ =="__main__":
    asyncio.run(main())    