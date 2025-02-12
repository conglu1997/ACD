class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Generate a reference to a well-known event in Greek mythology that involves transformation."},
            "2": {"reference": "To be or not to be, that is the question."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "criteria" in t:
            return f"Your task is to generate a cultural reference based on the following criteria: {t['criteria']} Ensure that the reference is clear and logically fits the given criteria. Provide the reference and its source in the following format:\n\nReference: [Your reference]\nSource: [The source]"
        else:
            return f"Your task is to recognize the source of the following cultural reference:\n\nReference: {t['reference']}\n\nProvide your answer in the following format:\n\nSource: [The source]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "criteria" in t:
            criteria = [
                "The reference should logically fit the given criteria.",
                "The reference should be clear and culturally relevant."
            ]
        else:
            criteria = [
                "The source should correctly identify the origin of the reference provided." 
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
