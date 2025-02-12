class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "time", "example_riddle": "I fly without wings, I cry without eyes. Whenever I go, darkness flies. What am I?"},
            "2": {"theme": "nature", "example_riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        example_riddle = t["example_riddle"]
        instructions = f"""Your task is to perform two activities related to riddles.

1. Interpret the following riddle and provide a clear and concise explanation of its meaning and answer.
Example Riddle: {example_riddle}

Please provide your interpretation in the following format:
- Meaning: [Your explanation]
- Answer: [Your answer]

2. Generate a new riddle based on the given theme.
Theme: {theme}

Ensure that your generated riddle is creative, coherent, and logically solvable. Provide the generated riddle in the following format:
- Riddle: [Your riddle]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should accurately explain the meaning and answer of the given riddle.",
            "The generated riddle should be creative, coherent, and logically solvable.",
            "The riddle should adhere to the given theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
