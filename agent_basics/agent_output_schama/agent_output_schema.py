from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, enable_verbose_stdout_logging, AgentOutputSchema
from dotenv import load_dotenv
from pydantic import BaseModel
import os

enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

class User(BaseModel):
    user_name: str
    user_id: int
    user_hobby: list

agent: Agent = Agent(
    name="assistant",
    instructions="Extract user details (name, id, and hobbies) and return them strictly in JSON schema that matches the User model.",
    output_type=AgentOutputSchema(User, strict_json_schema=False),
    model=model
)


result = Runner.run_sync(
    agent,
    "The user's name is Noor, the ID is 123, and the hobbies are playing and reading."
)

print(result.final_output)
