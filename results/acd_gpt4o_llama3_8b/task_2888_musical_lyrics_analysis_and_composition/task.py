class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love", "style": "pop", "lyrics": "Just a small-town girl, living in a lonely world. She took the midnight train going anywhere."},
            "2": {"theme": "adventure", "style": "rock", "lyrics": "It's a beautiful day, don't let it get away. You're on the road, but you've got no destination."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        style = t["style"]
        lyrics = t["lyrics"]
        return f"""Complete the following tasks:\n\n1. Analyze the given musical lyrics and describe the main theme and stylistic elements.\nLyrics: {lyrics}\n\n2. Compose new lyrics based on the specified theme and style.\nTheme: {theme}\nStyle: {style}\n\nSubmit your response as a plain text string with the following sections labeled: 'Analysis' and 'Composition'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should clearly identify the main theme and stylistic elements of the given lyrics.",
            "The composed lyrics should be original, adhere to the specified theme, and match the stylistic elements described in the task.",
            "The response should follow the given format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
