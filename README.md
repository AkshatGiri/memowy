## Memowy

### Initial Rough Thoughts

- Current bottleneck for human like AI agents is memory management and retrieval.
- LLMs have a limited context. Our job is to fill the context with the most relevant information so that the model can generate the most accurate response.
- If your agent pipeline is motly stateless then memeory management and retrieval isn't as importat. But for everything else, it makes or brakes the agent.
- With a few models the context length is getting longer ( eg gemini models have context over 1mil tokens ) but most models have a context of 120k tokens ( or less ).
  - Even if we assume that context length will continue going up, we will continue to have more complex requirements and end up with the same bottleneck.
  - Not to mention the cost of continuously using hundreds of thousands of tokens per request ( even if they are cached ).
- The current rag type solutions are not very good. They consistently fail to provide good information in context.
  - Often it's irrelevant or incomplete information.
- Not only is this important for managing complex workflows, it's also imporatnt for long running threads.
  - If we infact want Jarvis level ai assistants/agents we need them to be able to have a flowing conversation where they can have an infinitely long conversation
    and be able to have a memory like a human.
