import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, AgentOutputSchema,enable_verbose_stdout_logging
from dotenv import load_dotenv
from pydantic import BaseModel

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
agent:Agent = Agent(
    name ="Assistant",
    instructions= "you are a helpful assistant",
)
agent_2 = agent.clone()

result = Runner.run_sync(
    agent_2,
     "hello",
        run_config=runconfig
)
print(result.final_output)
