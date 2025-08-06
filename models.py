from pydantic import BaseModel, Field
from typing import TypedDict, Union, Annotated
import operator



class GetPossibleTopicsModel(BaseModel):
    query: str = Field(description="a dynamic search query to get relavant sources for relavant and current comic book media updates")






class Topic(BaseModel):
    topic: str = Field(description="The name of the topic you settled on")

class PossibleTopics(BaseModel):
    possible_topics: list[str]

class Schedule(BaseModel):
    hours: str


class Results(BaseModel):
    results: list[str] = Field("a list of possible sources")

class Source(BaseModel):
    source: str

class ListOfSources(BaseModel):
    sources: list[str]

class ArticleList(BaseModel):
    article: list[str]
    topic: str

class Article(BaseModel):
    topic: str
    article: str

class State(TypedDict):
    current_date: str
    input: str
    messages: Annotated[list, operator.add]
    topic: str
    schedule: str


