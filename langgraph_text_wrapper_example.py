import re
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class TextState(TypedDict):
    raw_text: str
    cleaned: str
    word_count: str
    summary: str


def clean_text(state: TextState):
    cleaned = re.sub(r'\s+',' ', state["raw_text"].strip()).lower()
    return {'cleaned': cleaned}

def count_words(state: TextState):
    return {"word_count": len(state['cleaned'].split())}

def format_result(state: TextState):
    print(state['word_count'])
    preview=state['cleaned'][:50] + ('...' if len(state['cleaned']) > 50 else '')
    summary=(
        '=== Text Analysis Summary === \n'
        f"Word Count     : {state['word_count']}\n"
        f"Preview        : {preview}\n"
        "-----------------------------"
    )

    return {"summary": summary}


builder = StateGraph(TextState)

builder.add_node("clean_text", clean_text)
builder.add_node("count_words", count_words)
builder.add_node("format_result", format_result)

builder.add_edge(START, "clean_text")
builder.add_edge("clean_text", "count_words")
builder.add_edge("count_words", "format_result")
builder.add_edge("format_result", END)

graph = builder.compile()
result = graph.invoke({
    "raw_text": "   LanGraph makes building AI pipelines clean and easy!. And it used to Agentic AI    "
})

print(result['summary'])