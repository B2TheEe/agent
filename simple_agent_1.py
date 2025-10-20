from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def main():
