import random
import sympy

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "domain": "Language",
                "description": "Create a language system where word length and sentence structure are determined by prime numbers."
            },
            {
                "domain": "Architecture",
                "description": "Design an architectural style where building proportions and city layouts are based on prime number relationships."
            },
            {
                "domain": "Social Structure",
                "description": "Develop a social hierarchy or political system founded on prime number principles."
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a cultural system based on prime numbers in the domain of {t['domain']}. Your task is to:

1. Design a system that incorporates prime numbers as a fundamental principle in {t['domain']}. {t['description']}

2. Explain how your system works, providing at least three specific examples or rules (3-4 sentences). Include at least one mathematical equation or formula in your explanation.

3. Analyze the potential implications of this system on the culture's development and daily life (3-4 sentences).

4. Describe one advantage and one limitation of this prime number-based system compared to conventional systems in our world (2-3 sentences for each).

5. Propose a creative way this system could interact with or influence another domain of the culture (e.g., if your system is linguistic, how might it affect art or economics?) (2-3 sentences).

6. Suggest an experiment or study that could be conducted to further explore the effects of this prime number-based system on the culture (2-3 sentences).

7. Briefly discuss potential ethical implications or concerns that might arise from implementing this system (2-3 sentences).

Ensure your response is creative yet grounded in mathematical principles and cultural anthropology concepts. Organize your answer using clear headings for each section. Your total response should not exceed 500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must create a system in the domain of {t['domain']} based on prime numbers",
            "The system should be logically consistent and demonstrate understanding of prime number properties",
            "The response should provide specific examples or rules as requested, including at least one mathematical equation or formula",
            "The analysis should consider cultural implications and be grounded in anthropological concepts",
            "The response should demonstrate creativity in applying prime number concepts to cultural systems",
            "The proposed experiment or study should be relevant and potentially insightful",
            "The response should discuss potential ethical implications or concerns",
            "The response should be well-organized with clear headings for each section",
            "The total response should not exceed 500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
