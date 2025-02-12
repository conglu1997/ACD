class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "What word starts with E, ends with E, but contains only one letter?"},
            "2": {"puzzle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following linguistic puzzle: {t['puzzle']}\n\nProvide your answer in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "1": "envelope",
            "2": "echo"
        }
        task_id = list(TaskFamily.get_tasks().keys())[list(TaskFamily.get_tasks().values()).index(t)]
        criteria = [f"The response should be: {correct_answers[task_id]}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0