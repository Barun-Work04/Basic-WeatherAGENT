from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.memory import InMemoryMemoryService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

# Use a low-cost model alias with reliable quota availability for this API key.
root_agent_model = "gemini-flash-lite-latest"

APP_NAME = "weather_app"

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()


def say_hello(name: str = "there") -> str:
	"""Provides a simple greeting, optionally addressing the user by name."""
	print(f"--- Tool: say_hello called with name: {name} ---")
	return f"Hello, {name}!"


def say_goodbye() -> str:
	"""Provides a simple farewell message to conclude the conversation."""
	print("--- Tool: say_goodbye called ---")
	return "Goodbye! Have a great day."


def get_weather(city: str) -> dict:
	"""Retrieves the current weather report for a specified city."""
	if city.lower() == "new york":
		return {
			"status": "success",
			"report": (
				"The weather in New York is sunny with a temperature of 25 degrees "
				"Celsius (77 degrees Fahrenheit)."
			),
		}

	return {
		"status": "error",
		"error_message": f"Weather information for the specified city '{city}' is not available.",
	}


root_agent = Agent(
	name="root_agent",
	model=root_agent_model,
	description="The main weather agent. Handles greetings, farewells, and weather requests.",
	instruction=(
		"You are a weather assistant. Handle three intents directly using tools: "
		"1) Greeting intent (e.g., hi/hello) -> call 'say_hello'. "
		"2) Farewell intent (e.g., bye/goodbye) -> call 'say_goodbye'. "
		"3) Weather intent (e.g., weather in <city>) -> call 'get_weather'. "
		"If user provides a name in a greeting, pass it to 'say_hello'. "
		"For anything else, respond appropriately or state you cannot handle it."
	),
	tools=[say_hello, say_goodbye, get_weather],
)

runner_root = Runner(
	app_name=APP_NAME,
	session_service=session_service,
	memory_service=memory_service,
	agent=root_agent,
	auto_create_session=True,
)
