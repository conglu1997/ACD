import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "smartphone",
                "period": "Ancient Rome (1st century AD)",
                "persona": "Roman philosopher"
            },
            {
                "concept": "social media",
                "period": "Medieval Europe (14th century)",
                "persona": "town crier"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the modern concept of a {t['concept']} using only the vocabulary and knowledge available in {t['period']}. Assume the persona of a {t['persona']} addressing their contemporaries. Your explanation should:

1. Use analogies and comparisons to concepts, objects, or systems that would be familiar to people of that era.
2. Avoid any anachronistic terms or ideas that would not have existed in {t['period']}.
3. Capture the essential functions and significance of a {t['concept']} in a way that would be comprehensible to your audience.
4. Be 100-150 words long.

After your explanation, provide a brief (2-3 sentences) analysis of the key challenges in translating this modern concept to the historical context, and how you addressed them.

Format your response as follows:

Explanation:
[Your explanation here]

Analysis:
[Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation should be from the perspective of a {t['persona']} in {t['period']}",
            f"The explanation should accurately convey the key aspects of a {t['concept']} without using anachronistic terms",
            "The explanation should use analogies and comparisons appropriate to the historical period",
            "The analysis should identify specific challenges in translating the concept and how they were addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
