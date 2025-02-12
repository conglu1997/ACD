class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A detective investigating a series of mysterious disappearances in a small town.", "genre": "Mystery/Thriller"},
            "2": {"prompt": "A group of friends discovering a hidden treasure while on a camping trip.", "genre": "Adventure/Comedy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a brief movie script based on the given prompt and genre.

Prompt: {t['prompt']}
Genre: {t['genre']}

Your script should include:
1. A title for the movie.
2. A brief description of the main characters.
3. At least two scenes, including dialogues and actions.
4. A clear beginning, middle, and end.

Ensure your script is engaging and appropriate for the given genre. Provide your response in plain text format.

Response Format:
Title: [Your Title]
Characters: [Brief description of main characters]
Scene 1: [Description of the scene, including dialogues and actions]
Scene 2: [Description of the scene, including dialogues and actions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The script should include a title, character descriptions, and at least two scenes.",
            "The script should have a clear beginning, middle, and end.",
            "The dialogues and actions should be engaging and appropriate for the given genre."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
