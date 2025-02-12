class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The old man the boats.", "context": "At the harbor, workers are organizing the boats for departure. The manager is overseeing the process. There are several elderly workers among the staff, who are responsible for manning the boats."},
            "2": {"sentence": "I saw the man with the telescope.", "context": "While stargazing at the observatory, I noticed someone using a telescope. There was also a man standing nearby with a guidebook. The guidebook had a picture of the night sky, and the man seemed to be pointing out constellations with the telescope."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        sentence = t["sentence"]
        context = t["context"]
        instructions = f"""Your task is to interpret the following ambiguous sentence and clarify its intended meaning based on the given context.

Sentence: {sentence}

Context: {context}

Provide your response in the following format:

Explanation: [Your interpretation of the sentence with respect to the context]

Ensure that:
1. Your explanation resolves the ambiguity in a way that aligns with the provided context.
2. Your explanation is clear and concise."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should resolve the ambiguity in a way that aligns with the provided context.",
            "The explanation should be clear and concise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
