import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Indian', 'Nigerian', 'Brazilian', 'Russian']
        modern_concepts = [
            'Social media addiction',
            'Remote work burnout',
            'Cryptocurrency volatility',
            'Online privacy concerns',
            'Artificial intelligence ethics'
        ]
        
        tasks = {}
        for i in range(1, 3):
            culture = random.choice(cultures)
            concept = random.choice(modern_concepts)
            tasks[str(i)] = {
                'culture': culture,
                'concept': concept
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to create and analyze a culturally-specific idiom for a modern concept.\n\n" \
               f"Culture: {t['culture']}\n" \
               f"Modern Concept: {t['concept']}\n\n" \
               f"1. Create an original idiom in English that expresses the given modern concept in a way that would be culturally appropriate and meaningful for the specified culture. The idiom should be 5-10 words long. (1 sentence)\n\n" \
               f"2. Explain the meaning of your idiom and how it relates to the modern concept. (2-3 sentences)\n\n" \
               f"3. Analyze how your idiom reflects specific cultural elements, traditions, or values of the given culture. (3-4 sentences)\n\n" \
               f"4. Discuss potential challenges in translating this idiom to other languages or cultures, and suggest how these challenges might be addressed. (2-3 sentences)\n\n" \
               f"5. Propose a situation or context where this new idiom might be particularly useful or impactful in the given culture. (2-3 sentences)\n\n" \
               f"Format your response with clear numbering for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The idiom is original, 5-10 words long, and appropriate for {t['culture']} culture.",
            f"The idiom effectively expresses the concept of {t['concept']}.",
            "The explanation of the idiom's meaning is clear and relates well to the modern concept.",
            f"The analysis demonstrates understanding of {t['culture']} cultural elements, traditions, or values.",
            "The discussion of translation challenges and the proposed usage context are insightful and well-reasoned.",
            "The response follows the requested format and addresses all parts of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
