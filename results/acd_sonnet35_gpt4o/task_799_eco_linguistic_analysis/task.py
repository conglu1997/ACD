import random
import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            {
                "issue": "Ocean Acidification",
                "data": {
                    "pH_levels": [8.2, 8.1, 8.0, 7.9, 7.8],
                    "years": [1950, 1980, 2000, 2020, 2040],
                    "coral_cover": [80, 60, 40, 20, 10]
                }
            },
            {
                "issue": "Deforestation",
                "data": {
                    "forest_area": [4.1, 4.0, 3.9, 3.8, 3.7],
                    "years": [1990, 2000, 2010, 2020, 2030],
                    "species_count": [1000, 950, 900, 850, 800]
                }
            }
        ]
        return {
            "1": random.choice(environmental_issues),
            "2": random.choice(environmental_issues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given environmental data on {t['issue']} using linguistic techniques and create a narrative report that effectively communicates the scientific findings to a non-expert audience. Your task has the following parts:

1. Data Analysis (200-250 words):
   a) Examine the provided data and identify key trends or patterns.
   b) Use appropriate linguistic techniques (e.g., metaphor, analogy) to describe these trends.
   c) Explain the significance of the data in the context of {t['issue']}.

2. Narrative Construction (250-300 words):
   a) Create a compelling narrative that communicates the data findings to a non-expert audience.
   b) Use storytelling techniques to make the information engaging and accessible.
   c) Incorporate at least three vivid metaphors or analogies to explain complex concepts.

3. Linguistic Devices (150-200 words):
   a) Identify and explain the specific linguistic devices you used in your narrative.
   b) Discuss how these devices enhance understanding of the environmental issue.

4. Emotional Impact (100-150 words):
   a) Describe how you've balanced scientific accuracy with emotional resonance in your narrative.
   b) Explain your choice of language to evoke an appropriate emotional response.

5. Call to Action (100-150 words):
   a) Conclude your narrative with a clear, motivating call to action.
   b) Explain how your linguistic choices in this section aim to inspire action.

Ensure your response demonstrates a deep understanding of both the environmental issue and effective science communication techniques. Be creative in your use of language while maintaining scientific accuracy.

Here's the data for {t['issue']}:
{json.dumps(t['data'], indent=2)}

Your total response should be between 800-1050 words. Use clear headings for each section in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately analyzes and interprets the provided environmental data.",
            "The narrative effectively communicates scientific findings to a non-expert audience.",
            "The response incorporates at least three vivid metaphors or analogies to explain complex concepts.",
            "The linguistic devices used enhance understanding of the environmental issue.",
            "The narrative balances scientific accuracy with emotional resonance.",
            "The call to action is clear, motivating, and linguistically appropriate.",
            "The response demonstrates creativity in language use while maintaining scientific accuracy.",
            "The response adheres to the specified word count and uses clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
