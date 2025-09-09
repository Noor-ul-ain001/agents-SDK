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

class User(BaseModel):
    user_name: str
    user_id: int
    user_hobby: str
    
agent:Agent = Agent(
    name ="Assistant",
    instructions= "you are a helpful assistant",
    output_type=AgentOutputSchema(User, strict_json_schema=True)
)

result:Runner = Runner.run_sync(
    agent,
    "my name is noor",
    run_config=runconfig
)
print(result.final_output)