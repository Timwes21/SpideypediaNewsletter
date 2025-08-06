from langgraph.prebuilt import create_react_agent
from tools import (
    get_possible_topics,
    print_topic, 
    pass_to_test_agent2, 
    print_schedule, 
    scrape_sources,
    get_sources,
    print_articles,
    print_article
    )
import os
from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ["GOOGLE_API_KEY"]
from ChatModel import llm



# publisher_agent = create_react_agent(
#     model=llm,
#     prompt="""You are to take the finished article and post it """,
#     tools=[publish_article]
# )


editor_agent = create_react_agent(
    model=llm,
    prompt="""
    You are to take the drafts given to you and form a complete and cohesive article based on the given topic and have it fromatted:
    once you do:
    - print article by using the tool print_article
    """,
    tools=[print_article]

)


writer_agent = create_react_agent(
    model=llm,
    prompt="""Based on the content, write a one thousand essay about the topic:
    you are to:
    - get the sources for the article from the tool get_sources
    - Pick three of the best looking sources and pass them to scrape_sources
    - with the text you get from scrape sources piece together a list of drafts around 300 words each, around 4 of them, then print the article with print_articles
    """,
    tools=[get_sources, scrape_sources, print_articles],
    name="writer_agent"
)




topic_agent = create_react_agent(
    model=llm,
    prompt="""You are in charge of seraching for a topic to write about. 
    You are to:
    - get possible topics by choosing the get_possible_topics
    - choose the best topic based on the criteria below
    - print the topic by choosing the print_topic tool

    Out of the possible topics choose one that BEST fits the criteria:
    - about comic books and/or comic book movies spefically Marvel or DC
    - must be new/ in the past week
    - interesting and people will want to read
    - Not talked about much
    - Nothing about comic book movie sales or comic book sales unless it effects the writers and artists
    - shocking and surprising/unexpected sounding would be perfect. For example batman is powerless but if you were 
      to see anything about batman getting powers that would be a good topic.,
               
    """,
    tools=[get_possible_topics, print_topic],
    name="topic_agent"
)

# res = topic_agent.invoke({"messages": [{"role": "user", "content": "give me a topic"}]})
# print(res)




test_agent_1 = create_react_agent(
    model=llm,
    prompt="This is a test, do the tool pass_to_agent_2 to proceed",
    tools=[pass_to_test_agent2],
    name="test_agent_1"
)

test_agent_2 = create_react_agent(
    model=llm,
    prompt="do the tool print_schedule",
    tools=[print_schedule],
    name="test_agent_2"
)

