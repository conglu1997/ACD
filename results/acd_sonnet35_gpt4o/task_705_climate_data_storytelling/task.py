import random
import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "phenomenon": "Ocean Acidification",
                "data_set": "Global ocean pH levels from 1988 to 2022",
                "narrative_style": "Personal journal of a coral polyp"
            },
            {
                "phenomenon": "Arctic Sea Ice Decline",
                "data_set": "September Arctic sea ice extent from 1979 to 2023",
                "narrative_style": "News reports from the future"
            },
            {
                "phenomenon": "Global Temperature Rise",
                "data_set": "Global land-ocean temperature index from 1880 to 2023",
                "narrative_style": "Letters between two time-traveling scientists"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the provided climate data set and create a narrative that explains the complex environmental phenomenon through storytelling. Your task has the following components:

1. Data Analysis (200-250 words):
   a) Describe the key trends and patterns in the {t['data_set']}.
   b) Identify any significant turning points or anomalies in the data.
   c) Explain the implications of these trends for the {t['phenomenon']}.

2. Scientific Explanation (200-250 words):
   a) Provide a clear, scientifically accurate explanation of the {t['phenomenon']}.
   b) Discuss the main causes and potential consequences of this phenomenon.
   c) Relate your explanation to the trends observed in the data set.

3. Creative Narrative (400-500 words):
   Create a story in the style of a {t['narrative_style']} that effectively communicates the scientific concept and data trends. Your narrative should:
   a) Accurately represent the scientific phenomenon and data trends.
   b) Engage the reader through vivid imagery and creative storytelling.
   c) Make complex scientific concepts accessible to a general audience.
   d) Incorporate at least three specific data points or trends from your analysis.

4. Reflection (150-200 words):
   a) Explain how your narrative effectively communicates the scientific concept and data trends.
   b) Discuss any challenges you faced in translating complex data into a narrative format.
   c) Suggest how this approach to science communication could be used in other contexts.

Ensure your response demonstrates a deep understanding of climate science, data analysis, and creative writing. Be innovative in your narrative approach while maintaining scientific accuracy. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a data analysis of the {t['data_set']}",
            f"The scientific explanation should accurately describe the {t['phenomenon']}",
            f"The creative narrative should be in the style of a {t['narrative_style']}",
            "The narrative should incorporate at least three specific data points or trends",
            "The response should demonstrate a deep understanding of climate science and data analysis",
            "The storytelling should make complex scientific concepts accessible to a general audience",
            "The reflection should thoughtfully discuss the challenges and potential of this science communication approach"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
