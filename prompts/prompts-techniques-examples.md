#

## Chain of thought

Chain-of-thought prompting is a technique that involves requesting a large language model to explain its reasoning processes. Chain-of-thought prompting is useful for solving problems that involve step-by-step reasoning.

![chain-of-thought](chain-of-thought.png)

```
Our organization assigns purchasing codes by combining an employee's department and ID number. All alphabetic characters are lowercase in the purchasing code. Review the examples and then answer the question that follows in the same manner. Explain the steps involved in determining each employee's purchasing code.

Question: Tiana B works in the Marketing department and has an ID number of 9283. What is Tiana B's purchasing code?

Answer: The purchasing code for Tiana B is marketing9283. To determine this, first combine the department (Marketing) with the ID number (9283). This results in Marketing9283. Then, change all alphabetic characters to lowercase. This creates the purchasing code marketing9283.

Question: Sylvie E works in the Sales department and has an ID number of 2379. What is Sylvie E's purchasing code?

Answer:
```

Note: You may not always be able to provide a useful example in your prompt. In that case, simply state that you want the LLM to explain its reasoning. The quality of your results will depend on your prompt and the specific LLM you’re using. Try including the following language in your prompt to get the best results:

"Solve the problem in a step-by-step manner."

"Explain each step used to determine the answer."
