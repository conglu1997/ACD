import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_periods = [
            "Ancient Greece (5th century BCE)",
            "Tang Dynasty China (8th century CE)",
            "Medieval Europe (14th century CE)",
            "Mughal India (17th century CE)",
            "Industrial Revolution England (19th century CE)",
            "Post-World War II United States (20th century CE)"
        ]
        ethical_themes = [
            "Justice and punishment",
            "Individual rights vs collective good",
            "Technological progress and its consequences",
            "Religious tolerance and freedom",
            "Environmental stewardship",
            "Economic equality and social mobility"
        ]
        document_types = [
            "Personal letter",
            "Official decree",
            "Philosophical treatise",
            "Court transcript",
            "Religious text interpretation",
            "Scientific journal entry"
        ]
        
        tasks = {}
        for i in range(1, 3):
            selected_periods = random.sample(time_periods, 3)
            ethical_theme = random.choice(ethical_themes)
            tasks[str(i)] = {
                "time_periods": selected_periods,
                "ethical_theme": ethical_theme,
                "document_types": random.sample(document_types, 3)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a set of three fictional historical documents addressing the ethical theme of {t['ethical_theme']}. Each document should be from one of the following time periods and cultures, using the specified document type:

1. {t['time_periods'][0]} - {t['document_types'][0]}
2. {t['time_periods'][1]} - {t['document_types'][1]}
3. {t['time_periods'][2]} - {t['document_types'][2]}

Each document should present a specific ethical dilemma related to the main theme, appropriate to its historical and cultural context. Ensure that the documents are interconnected, dealing with related aspects of the same overarching ethical issue.

For each document:
1. Write the document (150-200 words) in a style and format appropriate to its type and historical period.
2. Provide a brief explanation (50-75 words) of the specific ethical dilemma presented and its cultural context.

After creating the three documents, provide an analysis (400-500 words) that:
1. Compares and contrasts the ethical perspectives presented in each document.
2. Examines how the cultural and historical contexts influence the approach to the ethical theme.
3. Discusses how the ethical dilemma and its proposed solutions might be viewed in contemporary society.
4. Reflects on the enduring nature of the ethical theme and its evolution across cultures and time periods.

Ensure your response demonstrates a deep understanding of historical contexts, cultural nuances, and ethical reasoning. Be creative in your document creation while maintaining historical plausibility and cultural authenticity. Your total response should be between 1000-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes three distinct historical documents addressing the specified ethical theme",
            "Each document is appropriate to its assigned time period, culture, and document type",
            "The documents present interconnected ethical dilemmas related to the main theme",
            "The analysis effectively compares and contrasts the ethical perspectives across cultures and time periods",
            "The response demonstrates a deep understanding of historical contexts, cultural nuances, and ethical reasoning"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
