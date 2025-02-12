class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Existentialism", "prompt": "Explain the concept of existentialism and discuss its implications on human freedom and responsibility."},
            "2": {"concept": "Utilitarianism", "prompt": "Explain the concept of utilitarianism and generate a fictional dialogue between two individuals debating its application in a real-world scenario."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following philosophical concept and complete the associated task: '{t["concept"]}'. The explanation should be at least 300 words long and should cover the key aspects of the concept. For the additional task, ensure it is engaging, coherent, and demonstrates a deep understanding of the concept. Submit your response as a plain text string in the following format:

Explanation: [Your explanation]
Additional Task: [Your response to the additional task]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately cover the key aspects of the philosophical concept.", "The additional task should be engaging, coherent, and demonstrate a deep understanding of the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
