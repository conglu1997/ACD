class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "love",
                "style": "pop",
                "details": "A catchy, upbeat pop song about falling in love for the first time."
            },
            "2": {
                "theme": "resilience",
                "style": "rock",
                "details": "An empowering rock song about overcoming life's challenges and staying strong."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        style = t["style"]
        details = t["details"]
        return f"""Your task is to generate song lyrics based on the following theme and musical style.

Theme: {theme}
Style: {style}
Details: {details}

Your lyrics should:
1. Adhere to the specified theme and style.
2. Include at least three verses and a chorus.
3. Be engaging and coherent.

Provide your lyrics in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The lyrics should adhere to the specified theme and style.",
            "The lyrics should include at least three verses and a chorus.",
            "The lyrics should be engaging and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
