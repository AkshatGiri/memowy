## Evaluating LLM Memory Management

## Brainstorm

The better our evaluation system, the better we can understand, improve, and compare different solutions.

What we can't measure we can't improve.

First, we'll need a set of demo use cases to evaluate.

Then we'll need test data for that.

- Long running conversations

  - Switching between different topics
  - Switching between tasks
  - Group chat conversations
  - Handling conversations across different channels

- Chats with documents and big resources

After we have the data we want to eval against, then we'll need a composable / injectable system to easily swap out the different memory management systems and llms and leave the rest of the testing pipeline the same.

In this system we'll want to know how many tokens are being used ( input and outupt ).

After that we'll need a way to evaluate the quality of the output. This could be done by comparing the output to the expected output ( can be done by passing the expected type of output to an smart llm like claude and have it return an eval score ) or by using a more general metric. Ideally our metric would not be tied to results from another llm but that would be an easy way to get started.

### Datasets

- LMSYS-Chat-1M
- UltraDomain?
- Needle in a haystack seems pretty interest

Might just be a good idea to start creating our own specialized dataset with the exact situations we want to be
able to handle. Slowly we'll be able to grow over time and see how well we can do.
