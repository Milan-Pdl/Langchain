3. Sequential Chains
Now let's make the workflow more complex.

Suppose you're building an AI-powered educational application.

You want to:
1. Generate a summary from a research paper.
2. Generate quiz questions based on that summary.
Here, the second operation depends on the output of the first operation.

This is where Sequential Chains become useful.
Research Paper

Chain 1: Summarization

LLM generates a summary

Chain 2: Quiz Generation

Uses the summary from Chain 1

Final Quiz

Questions and answers


The important concept is:

Output of Chain 1 → Input of Chain 2.


4. Parallel Chains
Now imagine a slightly different requirement.

You have a research paper, and you want your application to generate:
- A summary.
- Five quiz questions.
- Important keywords.
All three operations use the same input, and none depends on the others.

Should we execute them one after another?

Not necessarily!

We can execute them in parallel using RunnableParallel.
Research Paper

RunnableParallel

Summary

Chain 1


Quiz

Chain 2


Keywords

Chain 3



Combined Output


Code example
from langchain_core.runnables import RunnableParallelparallel_chain = RunnableParallel(    summary=summary_chain,    quiz=quiz_chain,    keywords=keyword_chain)result = parallel_chain.invoke({    "paper": "Your research paper content..."})print(result["summary"])print(result["quiz"])print(result["keywords"])



What happens here?

RunnableParallel sends the same input to all three chains and collects their results into a dictionary.

Conceptually:
{    "summary": "...",    "quiz": "...",    "keywords": "..."}



Why is this useful?

It can reduce total execution time because independent operations can run concurrently. Actual speed depends on model/API limits and execution overhead.

5. Conditional Chains
Now let's understand something interesting.

Suppose you're building a customer feedback analysis system.

Users submit feedback, and you want your application to respond differently depending on the sentiment.

For example:
- Positive feedback → Generate a thank-you message.
- Negative feedback → Generate an apology and suggest a solution.
- Neutral feedback → Generate an acknowledgment.
You don't want to execute every chain for every user.

Instead, you want to choose the appropriate execution path based on a condition.

This is called conditional execution.

In LangChain, RunnableBranch helps implement this.
User Feedback

"The service was excellent!"

Sentiment Classification

RunnableBranch

Positive

Thank-you message


Negative

Apology and solution


Neutral

Acknowledgment