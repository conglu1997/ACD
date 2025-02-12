import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modern_concepts = [
            "artificial intelligence",
            "social media",
            "climate change",
            "space exploration",
            "genetic engineering"
        ]
        
        historical_periods = [
            {"era": "Ancient Greece", "year": "400 BCE"},
            {"era": "Medieval Europe", "year": "1200 CE"},
            {"era": "Renaissance Italy", "year": "1500 CE"},
            {"era": "Edo Period Japan", "year": "1700 CE"},
            {"era": "Industrial Revolution England", "year": "1800 CE"}
        ]
        
        return {
            "1": {
                "concept": random.choice(modern_concepts),
                "period1": random.choice(historical_periods),
                "period2": random.choice(historical_periods)
            },
            "2": {
                "concept": random.choice(modern_concepts),
                "period1": random.choice(historical_periods),
                "period2": random.choice(historical_periods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the modern concept of {t['concept']} using only the vocabulary and knowledge available in two different historical periods. Your task:

1. For {t['period1']['era']} ({t['period1']['year']}):
   a) Provide an explanation of {t['concept']} in 100-150 words, using analogies, metaphors, and concepts that would be familiar to people of that era.
   b) Avoid any anachronistic terms or ideas that would not have existed in that time period.
   c) Capture the essential aspects of {t['concept']} in a way that would be comprehensible to your audience.

2. For {t['period2']['era']} ({t['period2']['year']}):
   a) Provide another explanation of {t['concept']} in 100-150 words, adapting your language and analogies to this different historical and cultural context.
   b) Ensure this explanation is distinct from the first one, reflecting the changes in knowledge and worldview between the two periods.

3. Comparative Analysis (100-150 words):
   a) Discuss the key differences in your approach to explaining {t['concept']} between the two historical periods.
   b) Analyze how the available vocabulary, knowledge, and cultural context influenced your explanations.
   c) Identify any aspects of {t['concept']} that were particularly challenging to convey in each period, and how you addressed these challenges.

Format your response as follows:

{t['period1']['era']} Explanation:
[Your explanation here]

{t['period2']['era']} Explanation:
[Your explanation here]

Comparative Analysis:
[Your analysis here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanations should use vocabulary and concepts appropriate to {t['period1']['era']} and {t['period2']['era']} respectively.",
            "The explanations should avoid anachronisms and reflect the knowledge available in each historical period.",
            f"The core concept of {t['concept']} should be effectively communicated in both explanations.",
            "The comparative analysis should provide insightful observations about the differences in explanations and the challenges faced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
