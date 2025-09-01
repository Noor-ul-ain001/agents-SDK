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


class Output(BaseModel):
    user_email: str
    email_subject: str
    email_body: str
    email_date: int
    
    

class Output_Schema(AgentOutputSchema):
    def is_plain_text(self):
        return False
    
    def name(self) -> str:
        return "emailreview"
    
    def json_schema(self):
        res= {
            "user_email": "abc@gmail.com",
            "email_subject": "leave",
            "email_body": "hello",
            "email_date": 25
        }
        return res
    def is_strict_json_schema(self):
        return True 

agent: Agent = Agent(
    name="EmailExtractor",
    instructions=(
        "You are an assistant that extracts email details from user input. "
        "Always return a JSON object that follows the schema strictly. "
        "The schema has 4 fields: user_email (string), email_subject (string), "
        "email_body (string), and email_date (integer for the day of the month). "
        "If user_email is missing, fill it with 'unknown@example.com'."
    ),
    output_type=Output,
    model=model
)


res = Runner.run_sync(
    agent,
    "Please prepare an email. The subject is 'leave', the body is 'hello', the date is 25, and the sender email is abc@gmail.com."
)

print(res.final_output)
















