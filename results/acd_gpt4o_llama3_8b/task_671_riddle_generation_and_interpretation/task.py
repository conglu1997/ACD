class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "context": "forest"},
            "2": {"theme": "technology", "context": "internet"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        context = t["context"]
        return f"""Generate a riddle based on the theme of {theme} within the context of {context}. Ensure the riddle is engaging, logically coherent, and solvable. Submit your riddle as a plain text string.\n\nExample for theme 'nature' and context 'forest':\nI speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\n\nExample for theme 'technology' and context 'internet':\nI can be cracked, made, told, and played. What am I?\n\nSubmit your response in the following format:\nRiddle: [Your riddle]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The riddle should be based on the given theme.", "The riddle should be contextually appropriate.", "The riddle should be engaging and logically coherent.", "The riddle should be solvable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
