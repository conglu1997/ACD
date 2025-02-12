import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_principle": "Genetic code and protein synthesis",
                "linguistic_feature": "Syntax and word formation"
            },
            {
                "biological_principle": "Cellular communication and signaling pathways",
                "linguistic_feature": "Pragmatics and context-dependent meaning"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional language based on the biological principle of {t['biological_principle']}, focusing on the linguistic feature of {t['linguistic_feature']}. Your task is to:

1. Briefly explain the given biological principle and linguistic feature (2-3 sentences each).

2. Design a language system that incorporates the biological principle into the specified linguistic feature. Describe its key components and functioning (5-6 sentences).

3. Provide two specific examples of how your language works, demonstrating the biological principle in action within the linguistic feature.

4. Analyze how this language system could potentially offer insights into both biology and linguistics (3-4 sentences).

5. Discuss possible challenges in using or learning this language and how they might be addressed (2-3 sentences).

6. Explore the potential applications or implications of this biologically-inspired language in fields such as AI, cognitive science, or communication theory (3-4 sentences).

Format your response as follows:

Concept Explanation:
[Your explanation of the biological principle and linguistic feature]

Language Design:
[Your description of the fictional language system]

Language Examples:
1. [First example]
2. [Second example]

Interdisciplinary Insights:
[Your analysis of potential insights]

Challenges and Solutions:
[Your discussion of challenges and potential solutions]

Broader Implications:
[Your exploration of potential applications or implications]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system clearly incorporates the biological principle of {t['biological_principle']} into the linguistic feature of {t['linguistic_feature']}.",
            "The language design is creative, coherent, and demonstrates a strong understanding of both biology and linguistics.",
            "The provided examples effectively demonstrate how the biological principle is applied in the language system.",
            "The analysis of interdisciplinary insights is thoughtful and well-reasoned.",
            "The discussion of challenges and solutions is practical and shows consideration for real-world application.",
            "The exploration of broader implications demonstrates a deep understanding of the potential impact of this biologically-inspired language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
