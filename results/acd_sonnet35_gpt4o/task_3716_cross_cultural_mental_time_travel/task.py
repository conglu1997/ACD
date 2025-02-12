import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Ancient Egypt",
                "time_period": "2686 BC - 2181 BC (Old Kingdom)",
                "language": "Ancient Egyptian",
                "key_concept": "Ma'at (cosmic order and balance)"
            },
            {
                "name": "Edo Japan",
                "time_period": "1603 AD - 1867 AD",
                "language": "Classical Japanese",
                "key_concept": "Bushido (the way of the warrior)"
            }
        ]
        scenarios = [
            {
                "type": "past",
                "prompt": "Reconstruct a typical day in the life of a common citizen"
            },
            {
                "type": "future",
                "prompt": "Project a scenario 100 years into the future, imagining how the culture might evolve"
            }
        ]
        tasks = []
        for culture in cultures:
            for scenario in scenarios:
                tasks.append({
                    "culture": culture,
                    "scenario": scenario
                })
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t['culture']
        scenario = t['scenario']
        return f"""Engage in mental time travel within the context of {culture['name']} during the {culture['time_period']} period. Your task is to {scenario['prompt']}.

Your response should be written in the style and perspective of someone from that culture and time period, using appropriate linguistic features of {culture['language']}. Incorporate the key concept of {culture['key_concept']} into your narrative.

Provide your response in the following format:

1. Cultural and Linguistic Context (150-200 words):
   Briefly explain the key cultural and linguistic features you'll be incorporating into your response.

2. Mental Time Travel Narrative (400-500 words):
   Present your {'reconstruction' if scenario['type'] == 'past' else 'projection'} in the form of a first-person narrative.

3. Analysis (200-250 words):
   Explain how you incorporated the cultural context, linguistic features, and key concept into your narrative. Discuss any challenges you faced in adapting to this cultural and temporal perspective.

4. Comparative Reflection (150-200 words):
   Briefly compare and contrast the cultural elements in your narrative with those of contemporary global culture. Identify any universal human experiences or values that transcend time and culture.

Ensure your response demonstrates deep understanding of the specified culture, linguistic authenticity, and creative application of historical or futuristic thinking. Be detailed and imaginative while maintaining cultural accuracy and sensitivity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate deep understanding of {t['culture']['name']} culture during the {t['culture']['time_period']} period.",
            f"The narrative should incorporate linguistic features of {t['culture']['language']}.",
            f"The key concept of {t['culture']['key_concept']} must be meaningfully integrated into the narrative.",
            f"The {'reconstruction' if t['scenario']['type'] == 'past' else 'projection'} should be creative yet culturally and historically plausible.",
            "The analysis should provide insightful explanations of how cultural and linguistic elements were incorporated.",
            "The comparative reflection should identify meaningful connections between the depicted culture and contemporary global culture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
