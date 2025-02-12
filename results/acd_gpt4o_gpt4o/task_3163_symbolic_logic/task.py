class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "If P then Q. P is true. If Q then R.", "question": "Is R true? Justify your answer."},
            "2": {"statement": "If P then Q. If Q then R. If R then S. P is true.", "question": "Is S true? Justify your answer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        question = t["question"]
        instructions = f"""Your task is to interpret and reason about the following symbolic logic statement:

{statement}

{question}

Provide a clear and logical justification for your answer. Ensure your explanation is thorough, using complete sentences and logical reasoning. Do not make any assumptions beyond what is given in the statement."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly interpret the symbolic logic statement.",
            "The response should provide a clear and logical justification for the answer.",
            "The response should be coherent and use complete sentences."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
