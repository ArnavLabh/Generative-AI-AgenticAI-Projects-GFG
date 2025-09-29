import asyncio
import os
import sys

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from browser_use import Agent, ChatGoogle

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash")
    task = "Search Google for 'what is browser automation' and tell me the top 3 results"
    agent = Agent(task=task, llm=llm)
    history = await agent.run()
    
    print("\nASSIGNMENT OUTPUT: ")
    print("Visited URLs:")
    print(history.urls())
    print("-------------------------")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")