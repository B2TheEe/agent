from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def main():

    nutrition_agent = Agent(name="Simple Nutritiion Assistent",instructions="""You are a helpful asssistebt who gives nutrition advice."You give consesive answers""")
    with trace("Simple Nutrition Agent"):
      result = await Runner.run(nutrition_agent, "How healthy are bananas?")

    print(result)
    response_stream = Runner.run_streamed(nutrition_agent, "How healthy are bananas?")

    async for event in response_stream.stream_events():
        if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":


    asyncio.run(main())
