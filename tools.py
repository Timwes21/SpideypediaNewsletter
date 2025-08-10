from ChatModel import llm
from langchain_core.tools import tool
from google.ai.generativelanguage_v1beta.types import Tool as GenAITool  
import models
from bs4 import BeautifulSoup
import os
from utils.helper_functions import send_to_agent, get_date, tavily_search
from utils.mongodb import publish_to_mongo
import requests





@tool("publish_article", description="published the article", args_schema=models.Article)
def publish_article(article, topic):
    date_details = get_date()
    publish_to_mongo(article, topic, date_details)


@tool("get_possible_topics", description="gets links and resources that will help decide the topic")
def get_possible_topics():
    search = tavily_search()
    res = search.invoke("recent comic book or comic book movie news")
    print(res)
    return res



@tool("print_topic", args_schema=models.Topic, description="if the topic is settled on then this tool will be called")
def print_topic(topic):
    print("topic is found", topic)
    return send_to_agent("writer_agent", f"the topic is {topic}")

@tool("scrape_sources", description="scrapes the sources", args_schema=models.ListOfSources)
def scrape_sources(sources: list):
    texts = []
    for source in sources:
        i = requests.get(source)
        soup = BeautifulSoup(i.text, "html.parser")
        texts.append(soup.find("p").text)
    return texts

@tool('get_sources', description="finds the the relavant sources", args_schema=models.Topic)
def get_sources(topic: str):
    search = tavily_search()
    res = search.invoke(topic)
    return res


@tool("print_articles", description="prints off the article", args_schema=models.ArticleList)
def print_articles(article, topic):
    print(article)
    return send_to_agent("editor_agent", f"here are the articles:{article}, \nhere is the topic: {topic}")

@tool("print_article", description="prints the final draft of the article", args_schema=models.Article)
def print_article(topic, article):
    print(topic)
    print(article)
    return send_to_agent("publisher_agent", f"Topic: {topic}, \n article: {article}")



@tool("print_results", description="prints the sources", args_schema=models.Results)
def print_sources(sources, topic):
    print("here are the results")
    print(sources)
    return send_to_agent("writer_agent", f"Topic: {topic}, sources: {sources}")

# These are the test tools so i dont hit my quota testing with the main agents and tools

@tool("pass_to_test_agent2", description="pass to test agent 2")
def pass_to_test_agent2():
    print("passing to the test agent 2")
    return send_to_agent("test_agent_2", "the scehdule is 5 to 10")



@tool("print_schedule", description="prints schedule", args_schema=models.Schedule)
def print_schedule(hours: str):
    print("this is the scehduel: ", hours)