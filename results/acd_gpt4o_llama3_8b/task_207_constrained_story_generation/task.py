class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": ["a brave knight", "a cunning dragon"],
                "settings": ["an ancient forest", "a hidden cave"],
                "plot_points": ["the knight must find a magical sword", "the dragon guards a treasure"]
            },
            "2": {
                "characters": ["a curious scientist", "a talking cat"],
                "settings": ["a futuristic city", "an abandoned laboratory"],
                "plot_points": ["the scientist discovers a secret", "the cat helps solve a mystery"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and engaging story that includes the following elements:

Characters:
- {t['characters'][0]}
- {t['characters'][1]}

Settings:
- {t['settings'][0]}
- {t['settings'][1]}

Plot Points:
- {t['plot_points'][0]}
- {t['plot_points'][1]}

Ensure that your story integrates all the characters, settings, and plot points in a logical and engaging manner. The story should be between 300 and 500 words. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should include all specified characters.",
            "The story should include all specified settings.",
            "The story should include all specified plot points.",
            "The story should be coherent and engaging.",
            "The story should be between 300 and 500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
