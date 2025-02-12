class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "Section 1: All individuals have the right to freedom of speech. Section 2: Freedom of speech does not include the right to incite violence.", "scenario": "An individual gives a public speech encouraging people to vandalize public property. Does this fall under the right to freedom of speech? Justify your answer."},
            "2": {"document": "Section 3: Any contract made under duress is void. Section 4: Duress includes threats of physical harm or severe economic loss.", "scenario": "A person signs a contract after being threatened with severe economic loss. Is this contract valid? Justify your answer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given legal document and scenario:

1. Review the provided legal document.
2. Apply the principles from the document to the hypothetical scenario.
3. Provide a well-reasoned justification for your conclusion.

Submit your response as a plain text string in the following format:

Legal Analysis: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately interpret the legal principles from the provided document.",
            "The analysis should correctly apply the legal principles to the given scenario.",
            "The justification should be well-reasoned and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
