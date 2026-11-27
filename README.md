# Langgraph : 

- *LangGraph* is a python library for building stateful, multi-step AI applications as a graph.
- Think of an AI applications as a flowchart: 
    - Each box is the flowchart is a node (a step that does some work)
    - Each arrow is an edge(it decide where to go next)
    - A shared state(a dictionary of data) flows through the boxes and gets updated along the way.

- LangGraph lets you describe this flowchart in code, then runs it for you - keeping track of state, deciding which nodes runs next, looping when needed, and even pausing for a human to approve something.
- *One line definition:* LangGraph = build your AI app as a graph of steps that share and update a common state.


*Important Component: *
- Node
- Edge
- State

![alt text](image.png)

*5 important things : *
- Define the State
- Define the Node
- Connect the edge
- Compile
- Run

# LangChain vs LangGraph : 

*LangChain : *
- LangChain is a toolkit of LLM building blocks.

*LangGraph :* 
- Langgraph is a framework, built by the same team, for running stateful agent workflows that can loop and branch. 
- Used to create a Multi-Step Stateful AI Agent.
- Human in the Loop : Ask for confirmation or question from the user and execute the workflow again.

# Comparison : LangChain vs LangGraph

| Feature | LangChain | LangGraph |
|---|---|---|
| **Core Idea** | Components (models, prompts, retrievers, tools, output parsers) chained together | Workflow as a graph: nodes are steps, and edges decide what runs next |
| **Control Flow** | Mostly linear (A → B → C) | Loops, branches, retries, multiple agents |
| **State** | Little built-in state management; data is passed along the chain | A shared state object that every node reads and updates |
| **Persistence** | No built-in workflow checkpointing | Checkpointing: pause, resume, replay ("time travel") |
| **Human-in-the-loop** | Manual implementation | Built-in: interrupt before or after a node for approval |
| **Best For** | RAG, simple chains, prompt → LLM → parse, quick prototypes | Agents that run for many steps, use tools repeatedly, invoke several agents, or need production reliability |


# How they fit together:
- They are not competitors, LangGraph nodes often use LangChanin pieces such as ChatModel, tools and retrieves. In recent versions, LangChain’s own create_agent runs on LangGraph under the hood.

# Rule of thumb: 
- If the flow is fixed and runs once from start to finish, use LangChain.
- If the LLM decides what happens next, or you need loops, memory across turns, or human approval, use LangGraph.
