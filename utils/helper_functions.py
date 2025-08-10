import datetime
from langgraph.types import Command, Send
import os
from langchain_tavily import TavilySearch

api_key = os.environ["TAVILY_API_KEY"]


def get_date():
    today = str(datetime.datetime.now())
    date, time = today.split(" ")
    year, month, day = date.split("-")
    time = ":".join(time.split(":")[:2])
    return {"time": time, "year": year, "month": month, "day": day}


def send_to_agent(agent_name, message):
    return Command(
            goto=Send(agent_name, {"messages": message}),
            graph=Command.PARENT
        )

def tavily_search():
    search = TavilySearch(
        max_results=10,
        topic="general",
        tavily_api_key=api_key
        # include_answer=False,
        # include_raw_content=False,
        # include_images=False,
        # include_image_descriptions=False,
        # search_depth="basic",
        # time_range="day",
        # include_domains=None,
        # exclude_domains=None
    )

    return search