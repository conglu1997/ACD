class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"culture": "Japanese", "theme": "Perseverance", "details": "A story about a samurai who overcomes numerous challenges to achieve his goal."},
            "2": {"culture": "Indian", "theme": "Unity in Diversity", "details": "A story about a village where people from different backgrounds come together to solve a common problem."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a story based on the following cultural context, theme, and details:

Culture: {t['culture']}
Theme: {t['theme']}
Details: {t['details']}

Provide your story in plain text format. After completing the story, analyze it by addressing the following points:
1. How does the story reflect the cultural context?
2. What narrative techniques did you use to convey the theme?
3. How does the story align with or differ from traditional narratives of the specified culture?

Format your response as follows:

Story: [Your story]
Analysis:
1. Cultural Reflection: [Your analysis]
2. Narrative Techniques: [Your analysis]
3. Cultural Alignment: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and reflect the specified cultural context.",
            "The story should effectively convey the given theme.",
            "The analysis should address how the story reflects the cultural context, the narrative techniques used, and how the story aligns with or differs from traditional narratives of the specified culture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
