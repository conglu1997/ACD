class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"relationship": "Bird is to Sky as Fish is to ___", "expected_output": "Water"},
            "2": {"analogy": "Time is to Clock as Temperature is to Thermometer", "interpretation": "A clock measures time just as a thermometer measures temperature."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'relationship' in t:
            return f"""Your task is to complete the analogy based on the given relationship. Here is the relationship:
{t['relationship']}
Please provide the missing word to complete the analogy as a single word."""
        elif 'analogy' in t:
            return f"""Your task is to interpret the meaning of the given analogy. Here is the analogy:
{t['analogy']}
Please provide a clear and concise interpretation of the analogy in one or two sentences."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'relationship' in t:
            criteria = ["The response should correctly complete the analogy."]
        elif 'analogy' in t:
            criteria = ["The response should accurately interpret the analogy."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
