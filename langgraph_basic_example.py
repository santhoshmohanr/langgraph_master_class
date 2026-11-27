from typing import TypedDict
from langgraph.graph import StateGraph, START, END

print("langgraph example")

class State(TypedDict):
    value: int

def double(state: State):
    print(f"Double the value. Value is : {state['value']}")
    return {"value": state["value"] * 2}

def add_ten(state: State):
    print(f"Add ten. Value is : {state['value']}")
    return {"value": state['value'] + 10}

builder = StateGraph(State)
builder.add_node("double", double)
builder.add_node("add_ten", add_ten)

builder.add_edge(START, "double")
builder.add_edge("double", "add_ten")
builder.add_edge("add_ten", END)

graph = builder.compile()

result = graph.invoke({"value": 5})
print(result)
