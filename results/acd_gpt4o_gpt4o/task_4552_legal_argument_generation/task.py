class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "scenario": "A company is being sued for breach of contract. The company claims that the contract was void due to fraudulent misrepresentation by the other party.", "criteria": "The argument should address the elements of fraudulent misrepresentation and explain why the contract should be considered void. Include references to relevant legal principles or precedents if applicable. Use hypothetical examples to support your points."},
            "2": {"task_type": "interpret", "legal_text": "According to the principle of 'actus reus' in criminal law, a person cannot be found guilty unless it is proven that they committed a criminal act. This principle requires both the act itself and a guilty state of mind.", "question": "What must be proven for a person to be found guilty under the principle of 'actus reus'? Provide examples if necessary."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            instructions = f"""Your task is to generate a legal argument based on the following scenario:

Scenario: {t['scenario']}

Ensure your argument addresses the elements of fraudulent misrepresentation and explains why the contract should be considered void. Include any relevant legal principles or precedents and use hypothetical examples to support your points. Provide your argument in plain text format, clearly structured with each point logically following from the previous one. For example:

1. Define fraudulent misrepresentation.
2. Explain how fraudulent misrepresentation applies to the given scenario.
3. Reference any relevant legal principles or precedents.
4. Use hypothetical examples to support your points.
5. Conclude why the contract should be considered void based on your argument."""
        else:
            instructions = f"""Your task is to interpret the following legal principle and answer the question based on the information provided:

Legal Text: {t['legal_text']}

Question: {t['question']}

Provide your answer in plain text format, clearly stating what must be proven for a person to be found guilty under the principle of 'actus reus'. Include examples if necessary."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            criteria = ["The argument should address the elements of fraudulent misrepresentation.", "The argument should explain why the contract should be considered void.", "The argument should include references to relevant legal principles or precedents.", "The argument should use hypothetical examples to support the points.", "The argument should be clear, logical, and well-structured."]
        else:
            criteria = ["The response should correctly identify what must be proven for a person to be found guilty under the principle of 'actus reus'.", "The response should include examples if necessary."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
