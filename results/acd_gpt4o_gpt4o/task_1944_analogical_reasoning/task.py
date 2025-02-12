class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Book is to library as star is to ?", "options": ["planet", "galaxy", "telescope", "moon"]},
            "2": {"relationship": "Key is to lock as ? is to ?", "examples": ["Password is to account"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'puzzle' in t:
            return f"""Your task is to solve the following analogy puzzle:

{t['puzzle']}
Options: {', '.join(t['options'])}

Choose the option that best completes the analogy. Provide your answer in plain text format as the chosen option."""
        else:
            return f"""Your task is to generate an analogy based on the given relationship:

Relationship: {t['relationship']}
Examples: {', '.join(t['examples'])}

Generate an analogy that follows the same relationship pattern. Ensure that your analogy is both logical and creative. Provide your analogy in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'puzzle' in t:
            correct_answer = "galaxy"
            return 1.0 if submission.strip().lower() == correct_answer else 0.0
        else:
            criteria = ["The generated analogy should follow the same relationship pattern as the given example.", "The generated analogy should be logical and creative."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
