import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                'challenge': 'sustainable urban water management',
                'organism': 'Namib desert beetle',
                'biological_feature': 'water harvesting from fog'
            },
            {
                'challenge': 'renewable energy storage',
                'organism': 'electric eel',
                'biological_feature': 'bioelectric organ for energy generation and storage'
            }
        ]
        return {str(i+1): task for i, task in enumerate(challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biomimetic solution for {t['challenge']}, drawing inspiration from the {t['organism']} and its {t['biological_feature']}. Your response should include:

1. Biological System Analysis (150-200 words):
   a) Describe the key features and mechanisms of the {t['biological_feature']} in the {t['organism']}.
   b) Explain how this biological system is particularly well-suited to inspire solutions for {t['challenge']}.

2. Biomimetic Solution Design (250-300 words):
   a) Propose a detailed design for your biomimetic solution, explaining how it mimics or is inspired by the biological system.
   b) Describe the key components and mechanisms of your solution.
   c) Explain how your solution addresses the specific challenges related to {t['challenge']}.

3. Implementation and Scalability (200-250 words):
   a) Discuss how your solution could be implemented in real-world settings.
   b) Address potential challenges in scaling up your solution from a prototype to wide-scale implementation.
   c) Propose strategies to overcome these challenges.

4. Environmental and Social Impact (150-200 words):
   a) Analyze the potential environmental impacts (both positive and negative) of implementing your solution.
   b) Discuss the social implications of your solution, considering factors such as accessibility, equity, and cultural acceptance.

5. Comparative Analysis (100-150 words):
   a) Compare your biomimetic solution to existing non-biomimetic approaches to {t['challenge']}.
   b) Discuss the potential advantages and limitations of your approach.

6. Future Developments (100-150 words):
   a) Propose two potential areas for further research or development that could enhance your biomimetic solution.
   b) Briefly describe how these developments could improve the effectiveness or applicability of your solution.

Ensure your response demonstrates a deep understanding of both the biological system and the global challenge. Be creative and innovative in your design while maintaining scientific plausibility and addressing real-world constraints.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified biological system and its relevance to the global challenge.",
            "The biomimetic solution design is innovative, well-explained, and clearly inspired by the biological system.",
            "The implementation and scalability discussion addresses real-world challenges and proposes plausible solutions.",
            "The environmental and social impact analysis is comprehensive and considers both positive and negative consequences.",
            "The comparative analysis provides meaningful insights into the advantages and limitations of the biomimetic approach.",
            "The proposed future developments are relevant and have the potential to significantly enhance the solution.",
            "The overall response shows interdisciplinary creativity, combining concepts from biology, engineering, and environmental science in a novel way."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
