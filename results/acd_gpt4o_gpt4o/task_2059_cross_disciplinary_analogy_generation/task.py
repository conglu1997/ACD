class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept1": "human brain", "concept2": "computer"},
            "2": {"concept1": "photosynthesis", "concept2": "solar panel"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate and explain an analogy between the following two concepts from different fields:

Concept 1: {t['concept1']}
Concept 2: {t['concept2']}

Ensure your analogy clearly highlights the similarities and differences between the concepts, and provides a detailed explanation of why the analogy is appropriate. Provide your response in the following format:

Analogy: [Your analogy]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
