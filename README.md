## Memowy 💖

The latest LLMs are really good. So why don't we have something like Jarvis yet? An AI agent that's your friend / coworker. With whom you can have an indefinite conversation and as you do it understands you more, learns from past interactions, works on tasks while you're away and other than having a physical form interacts like a human.

Jarvis ( or a human ) doesn't forget about the conversation you had yesterday. It doens't get amnesia every time you start a new "chat". Dammit why do we have to start a "new chat" anyways?

Well it's a side effect of the underlying architecture of LLMs. Once a model is trained it's "weights" are frozen. At that point it's more like a calculator. It takes input and produces outputs, but doesn't inherently have a memory to store new intormation. You can think of it as a processing unit or reasoning engine if you will. It can only produce outputs based on the information given to it. For something like ChatGPT this is just the chat history. But there's a limit to the amount of information we can input and output at a time. This is the "context window" of the model. It's defined by the number of tokens the model can process at a time. Most models currently have a context window of 200k tokens or less ( around 150k words ).

That's a good amount of context window and it's a growing number with more advanced models. Now, our job is to figure out how to fill this context window with the most relevant information to get the best outputs. To have the models behave in the way we want them to behave. This is a fairly difficult problem to solve. The current solutions have serious limitations which is why systems require us to start a new chat after a while or when starting a topic discussion. And honestly this is fine if you're using the model for narrow tasks or using the seperate chats like an organization tool. But it's not fine if you're trying to build Jarvis or any sort of complex AI Agent.

One of the main reasons building a true Jarvis like AI assistant remains a challenge is because of a robust memory management system. The ability to remember past interactions, user preferences, context and retrieve relevent information when needed is critical. In order to bridge the gap between mostly statelemess LLMs and AI Agents to agents that act and feel like humans we need to fix the memory problem.

So, Memowy is a project focused on researching and developing advanced memory management and retrieval systems for LLMs and AI agents.

### The Dream

Enabling a powerful context management and memory retrieval system would allow us to unlock quite a few powerful things.

- Indefinite conversations with AI agents where they actually learn about you, your preferences, and adapt their interaction style accordingly. Retrieve information about previous discussions. Resume old conversations without losing context etc.

- Cross-platform consistency. Imagine your agent helping you on Discord, reviewing your PRs on GitHub, and catching up with you on Telegram - all while maintaining the same personality and context. Your friends don't forget about you across different platforms, and neither should AI Agents.

- True multi-tasking capabilities. The agent can work on multiple projects, pause when you need something urgent, and resume without losing context. Just like how you can ask a coworker "hey, remember that authentication system we were working on last week? Can we add OAuth to that?".

- Complex project management where the agent actually understands the evolution of the project. It remembers architectural decisions, previous discussions about trade-offs, and why you chose certain approaches over others.

### Current Solutions

Right now, we have a few approaches to handle memory in AI systems:

1. The most common approach is RAG (Retrieval Augmented Generation) combined with vector databases. We take chunks of text, turn them into vectors, store them in a database, and retrieve them based on similarity. It's like having a really smart search engine. But it's not really memory - it's more like having a bunch of sticky notes that you frantically search through when needed.

2. We also use summarization. Take a long conversation, compress it into key points, and hope we didn't lose anything important. Spoiler alert: we always lose something important.

3. Some systems keep a list of facts about users and contexts. "User prefers TypeScript. User has a dog named Max."

These approaches are useful tools, but they're not enough but they have shortfalls.

### Why Current Solutions Fall Short

Current solutions have specific limitations that prevent them from achieving human-like memory capabilities:

Vector Databases & Embeddings:

- The chunking process often breaks apart related information, leading to loss of context
- Similarity search is a fairly shallow way to search for information. It's like searching through a book by only looking at individual paragraphs
- Even with good chunking, retrieved information is often incomplete because related information exists in other chunks
- Embeddings lose information during the compression process

Summarization:

- Misses crucial nuances in conversations and documents
- Difficult to automatically determine what details are actually important for future use
- Can't effectively capture complex relationships and dependencies
- Loses temporal aspects and evolution of discussions
- Often creates overly generic summaries that lack actionable details

Fact Storage:

- Too rigid and structured for natural interaction
- Misses implicit information and context
- Can't capture how relationships and understanding evolve over time
- Struggles with contradictions and updates to stored information
- No mechanism for priority or relevance scoring
- Grows large over time without a way to fetch only relevant information

While each one of them have their usecases and have been successful in their own right, they haven't been effective in building a true AI agent that can act and feel like a human.

### The Approach

Here's where things get interesting. If you look at major breakthroughs in LLM development, they often mirror human cognition:

- Neural nets ≈ Human neurons
- Transformer architecture ≈ Human attention mechanisms ( Sensory Memory )
- Chain of thought / Test time compute ≈ Human longer, harder and step-by-step for better results

So why not apply the same principle to memory? Human memory systems have evolved over millions of years to be incredibly efficient at storing and retrieving relevant information. We have mechanisms for:

- Pattern completion (remembering entire scenes from small triggers)
- Priming (preparing related memories based on context)
- Memory consolidation (moving information from short-term to long-term storage)
- Retrieval-induced forgetting (actively suppressing irrelevant memories)

### Research Direction

To build a better memory system, we need to first understand and formalize our current problems with concrete examples. We'll create various scenarios that highlight the limitations of current memory systems. This will help us properly evaluate different solutions.

After we have properly quantified the problems we're trying to solve, we can start implementing solutions based on human memory systems. We'll start by implementing and testing each mechanism separately:

Pattern Completion:
When you remember something, you don't need the complete memory to recall it. A small trigger can help you remember the entire context. We need to build systems that can do the same - reconstruct complete contexts from partial information.

Priming and Retrieval:
Your brain doesn't just retrieve memories - it prepares related ones for quick access. When you're working on a React project, your brain primes memories about JavaScript, web development, and your project's architecture. We need systems that can pre-load relevant context based on the current situation.

Memory Competition:
When you try to remember something, your brain activates multiple competing memories and then selectively filters out irrelevant ones. This is way more sophisticated than current similarity search approaches. We need ranking systems that can:

- Evaluate memory relevance based on current context
- Consider how recently memories were accessed
- Account for emotional significance and frequency of use
- Actively suppress irrelevant competing memories

Memory Evolution:
Memories aren't static - they evolve as you gain new information. That funny bug you encountered last week becomes more significant when you realize it's a pattern in your codebase. Our systems need to:

- Update stored information based on new context
- Strengthen or weaken memory connections over time
- Merge related information from different interactions
- Handle contradictions and updates gracefully

### Project Phases

1. Evaluation Phase
   First, we need to properly understand what we're trying to solve. We'll create benchmark scenarios that test different aspects of memory management:

- Long-running conversations with context switches
- Multi-project task management
- Cross-platform interaction consistency
- Knowledge evolution and updates

2. Research Implementation
   We'll implement each bio-inspired mechanism separately and evaluate its effectiveness:

- Build pattern completion systems
- Implement priming and retrieval mechanisms
- Create sophisticated ranking systems
- Develop memory evolution capabilities

3. Integration
   The real challenge comes in combining these systems effectively:

- Balancing different memory mechanisms
- Managing computational resources
- Ensuring real-time performance
- Handling edge cases and conflicts

4. Testing and Iteration
   Finally, we'll need extensive testing in real-world scenarios:

- Long-term conversation testing
- Multi-user environment testing
- Cross-platform consistency testing
- Performance and resource usage optimization
