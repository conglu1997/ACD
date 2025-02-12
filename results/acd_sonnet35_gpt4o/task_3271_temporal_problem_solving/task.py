import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modern_problems = [
            "Climate change mitigation",
            "Cybersecurity threats",
            "Misinformation on social media",
            "Urban traffic congestion",
            "Global pandemic response"
        ]
        historical_periods = [
            "Ancient Rome (27 BC - 476 AD)",
            "Tang Dynasty China (618 - 907 AD)",
            "Medieval Europe (5th - 15th century)",
            "Renaissance Italy (14th - 17th century)",
            "Industrial Revolution Britain (18th - 19th century)"
        ]
        
        return {
            "1": {
                "modern_problem": random.choice(modern_problems),
                "historical_period": random.choice(historical_periods)
            },
            "2": {
                "modern_problem": random.choice(modern_problems),
                "historical_period": random.choice(historical_periods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the modern problem of '{t['modern_problem']}' using only the knowledge, technology, and methods available during {t['historical_period']}. Then, translate your solution into contemporary terms. Your response should include:

1. Historical Context (150-200 words):
   a) Briefly describe the relevant aspects of the specified historical period.
   b) Explain the state of knowledge and technology during this time.
   c) Discuss any societal or cultural factors that might influence problem-solving approaches.

2. Problem Analysis (150-200 words):
   a) Reframe the modern problem in terms that would be understandable in the historical period.
   b) Identify any similar challenges that existed during that time.
   c) Discuss potential misconceptions or knowledge gaps that might affect the historical approach.

3. Historical Solution (250-300 words):
   a) Propose a detailed solution to the problem using only resources and methods available in the specified period.
   b) Explain the rationale behind your approach, citing relevant historical knowledge or practices.
   c) Describe how this solution would be implemented given the constraints of the time.

4. Contemporary Translation (200-250 words):
   a) Translate your historical solution into modern terms and technologies.
   b) Compare and contrast the historical and modern approaches.
   c) Discuss any insights or novel perspectives gained from the historical approach.

5. Feasibility and Implications (150-200 words):
   a) Analyze the potential effectiveness of your translated solution in addressing the modern problem.
   b) Discuss any ethical considerations or unintended consequences of applying this historically-inspired approach.
   c) Propose how this solution might complement or challenge current approaches to the problem.

Ensure your response demonstrates a deep understanding of both the historical period and the modern problem. Use appropriate terminology for both time periods and provide clear explanations for any complex concepts. Be creative in your problem-solving approach while maintaining historical accuracy and plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified historical period and its technological limitations.",
            "The proposed solution is creative and plausible within the historical context.",
            "The translation to contemporary terms is clear and insightful.",
            "The response shows a deep understanding of both the historical and modern aspects of the problem.",
            "The analysis of feasibility and implications is thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
