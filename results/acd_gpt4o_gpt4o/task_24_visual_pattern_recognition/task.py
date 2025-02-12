class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "*..**...***....", "prompt": "Identify the next four symbols in the sequence."},
            "2": {"pattern": "#-##--###---", "prompt": "Identify the next three symbols in the sequence."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify or continue the visual pattern based on the given description. Here is the pattern: '{t["pattern"]}'. {t["prompt"]} Provide your answer as a continuation of the sequence in the same format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly identify or continue the pattern.",
            "The submission should be coherent and contextually appropriate."]
        pattern = t["pattern"]
        if pattern == "*..**...***....":
            correct_answer = "****....."
        elif pattern == "#-##--###---":
            correct_answer = "####----"
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission == correct_answer else 0.0
