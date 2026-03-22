from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import Session
from google.adk.memory import InMemoryMemoryService
from dotenv import load_dotenv

load_dotenv('./.env')



def say_hello(name: str = "there") -> str:
    """Provides a simple greeting, optionally addressing the user by name.

    Args:
        name (str, optional): The name of the person to greet. Defaults to "there".

    Returns:
        str: A friendly greeting message.
    """
    print(f"--- Tool: say_hello called with name: {name} ---")
    return f"Hello, {name}!"


def say_goodbye() -> str:
    """Provides a simple farewell message to conclude the conversation."""
    print(f"--- Tool: say_goodbye called ---")
    return "Goodbye! Have a great day."


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error message.
    """
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
        "error_message": f"Weather information for the specified city '{city}' is not available."
    }

