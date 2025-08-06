from langgraph.graph import StateGraph, START, END
from agents import topic_agent, writer_agent, editor_agent, test_agent_1, test_agent_2
import models




graph = (
    StateGraph(models.State)
    .add_node("topic_agent", topic_agent)
    .add_node("writer_agent", writer_agent)
    .add_node("editor_agent", editor_agent)
    .add_edge(START, "topic_agent")
    .add_edge("topic_agent", "writer_agent")
    .add_edge("writer_agent", "editor_agent")
    .compile()
)



test_graph = (     
    StateGraph(models.State)
    .add_node("test_agent_1", test_agent_1)
    .add_node("test_agent_2", test_agent_2)
    .add_edge(START, "test_agent_1")
    .add_edge("test_agent_1", "test_agent_2")
    .add_edge("test_agent_2", END)
    .compile()
)
test_input = "this is a test"
input = "Give me a topic"
messages = {"messages": [{"role": "user", "content": input}]}
# test_graph.invoke(messages)
print("invoking graph")

print("graph should be invoked")