class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "style": "classical",
                "length": 8,
                "requirements": "Compose a short piece of music notation in a classical style. The piece should be 8 bars long and include at least two different instruments. Submit your composition using ABC notation."
            },
            "2": {
                "theme": "friendship",
                "requirements": "Write song lyrics based on the theme of friendship. The lyrics should be at least 100 words long and follow a coherent structure (e.g., verse-chorus format). Ensure that the lyrics are original, creative, and relevant to the theme. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'style' in t:
            return f"Compose a short piece of music notation in the {t['style']} style. The piece should be {t['length']} bars long and include at least two different instruments. Submit your composition using ABC notation. Example format: X:1\nT:Example\nM:4/4\nL:1/4\nK:C\nC D E F | G A B c | ..."
        elif 'theme' in t:
            return f"Write song lyrics based on the theme of {t['theme']}. The lyrics should be at least 100 words long and follow a coherent structure (e.g., verse-chorus format). Ensure that the lyrics are original, creative, and relevant to the theme. Submit your response as a plain text string. Example format:\nVerse 1:\n[Your verse here]\nChorus:\n[Your chorus here]\nVerse 2:\n[Your verse here]\nChorus:\n[Your chorus here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Optional criteria to ensure response meets specific requirements
        criteria = []
        if 'style' in t:
            criteria.append("The composition should be 8 bars long.")
            criteria.append("The composition should include at least two different instruments.")
        elif 'theme' in t:
            criteria.append("The lyrics should be at least 100 words long.")
            criteria.append("The lyrics should follow a coherent structure (e.g., verse-chorus format).")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
