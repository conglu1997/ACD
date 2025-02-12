import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Ancient Egypt",
            "Classical Greece",
            "Imperial China",
            "Medieval Islamic World",
            "Renaissance Italy",
            "Industrial Revolution Britain",
            "Meiji Japan"
        ]
        technologies = [
            "Steam Engine",
            "Printing Press",
            "Gunpowder",
            "Telescope",
            "Antibiotics",
            "Electricity",
            "Computer"
        ]
        return {
            "1": {
                "culture": random.choice(cultures),
                "technology": random.choice(technologies)
            },
            "2": {
                "culture": random.choice(cultures),
                "technology": random.choice(technologies)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an alternate historical timeline where {t['technology']} is invented in {t['culture']}. Your response should include:

1. Historical Context (200-250 words):
   a) Briefly describe the key characteristics of {t['culture']} relevant to technological development.
   b) Explain the original historical context of {t['technology']}'s invention.
   c) Discuss the potential cultural and societal factors that could lead to the earlier invention of {t['technology']} in {t['culture']}.

2. Alternate Timeline (300-350 words):
   a) Describe the hypothetical invention of {t['technology']} in {t['culture']}.
   b) Outline a plausible sequence of events leading to this invention.
   c) Explain how the cultural context influences the development and initial applications of the technology.

3. Technological Implications (200-250 words):
   a) Analyze how the earlier invention of {t['technology']} might accelerate or alter other technological developments.
   b) Discuss potential synergies with existing technologies in {t['culture']}.
   c) Propose a novel technological advancement that might emerge from this alternate history.

4. Societal Impact (200-250 words):
   a) Examine the potential social, economic, and political consequences of this alternate technological development.
   b) Discuss how it might change the balance of power within {t['culture']} and in relation to other contemporary cultures.
   c) Consider potential ethical implications or challenges that might arise.

5. Global Ripple Effects (150-200 words):
   a) Hypothesize how this alternate history might influence global technological development.
   b) Discuss potential changes to major historical events or trends.
   c) Propose how the world might be different today as a result of this alternate timeline.

Ensure your response demonstrates a deep understanding of historical, cultural, and technological dynamics. Use appropriate terminology and provide clear explanations for your reasoning. Be creative and plausible in your alternate history while maintaining logical consistency.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately represents the historical and cultural context of {t['culture']}.",
            f"The alternate timeline for the invention of {t['technology']} is plausible and well-reasoned.",
            "The analysis of technological implications is insightful and considers multiple factors.",
            "The discussion of societal impact is comprehensive and considers various aspects (social, economic, political).",
            "The global ripple effects are logically derived from the alternate timeline.",
            "The response demonstrates creativity while maintaining historical and technological plausibility.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
