import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, AgentOutputSchema,enable_verbose_stdout_logging,RunContextWrapper
from dotenv import load_dotenv
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


@dataclass
class User():
    name:str
    hobby: str
def dynamic_instruction(ctx: RunContextWrapper[User], agent:Agent[User]):
    return f"The user name is {ctx.context.name} and hobby is {ctx.context.hobby}"

agent:Agent = Agent[User](
    name ="Assistant",
    instructions= dynamic_instruction,
    model = model

)
context = User(name= "noor" , hobby= "reading")

result = Runner.run_sync(agent, "Hello", context=context)
print(result.final_output)
