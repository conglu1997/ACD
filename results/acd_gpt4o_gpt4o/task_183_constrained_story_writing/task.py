class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"characters": ["a brave knight", "a clever dragon"], "setting": "an enchanted forest", "plot": "The knight and the dragon must work together to find a hidden treasure."},
            "2": {"characters": ["a curious scientist", "a talking robot"], "setting": "a futuristic city", "plot": "The scientist and the robot uncover a conspiracy that threatens the entire city."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        characters = ", ".join(t["characters"])
        setting = t["setting"]
        plot = t["plot"]
        instructions = f"""Your task is to write a creative story based on the following constraints:

Characters: {characters}
Setting: {setting}
Plot: {plot}

Ensure that the story is engaging, coherent, and includes all specified characters, setting, and plot elements. The story should be between 300 and 500 words long. Provide your story in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should include all specified characters.",
            "The story should be set in the specified setting.",
            "The story should follow the specified plot.",
            "The story should be engaging and coherent.",
            "The story should be between 300 and 500 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
