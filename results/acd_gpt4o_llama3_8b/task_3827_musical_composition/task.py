class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "music_interpretation", "piece": "Twinkle, Twinkle, Little Star", "instructions": "Interpret the given musical piece and describe its structure, melody, and harmony. Discuss the emotional impact and any notable features."},
            "2": {"task_type": "music_generation", "theme": "joy", "structure": "AABA", "instructions": "Generate a musical composition based on the given theme and structure. Ensure the composition has a clear melody and follows the specified structure. Submit your composition as a textual representation of musical notes (e.g., C D E F G A B)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'music_interpretation':
            return f"Interpret the following musical piece: {t['piece']}. {t['instructions']}\nYour response should include:\n1. A detailed description of the structure, melody, and harmony.\n2. An analysis of the emotional impact and any notable features.\nSubmit your response as a plain text string."
        elif t['task_type'] == 'music_generation':
            return f"Generate a musical composition based on the theme '{t['theme']}' and structure '{t['structure']}'. {t['instructions']}\nYour response should include:\n1. A textual representation of the musical composition (e.g., C D E F G A B).\n2. An explanation of how the composition reflects the given theme and follows the specified structure.\nSubmit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['task_type'] == 'music_interpretation':
            criteria = ["The interpretation should accurately describe the structure, melody, and harmony.", "The interpretation should discuss the emotional impact and any notable features."]
        elif t['task_type'] == 'music_generation':
            criteria = ["The composition should have a clear melody and follow the specified structure.", "The composition should reflect the given theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
