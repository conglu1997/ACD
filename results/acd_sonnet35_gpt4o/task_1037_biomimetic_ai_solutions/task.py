import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "challenge": "Urban Water Management",
                "biological_inspiration": "Plant root systems",
                "ai_component": "Reinforcement learning"
            },
            {
                "challenge": "Sustainable Energy Distribution",
                "biological_inspiration": "Honeybee colonies",
                "ai_component": "Swarm intelligence"
            },
            {
                "challenge": "Adaptive Manufacturing",
                "biological_inspiration": "Chameleon color changing",
                "ai_component": "Generative adversarial networks"
            },
            {
                "challenge": "Waste Reduction and Recycling",
                "biological_inspiration": "Fungal decomposition networks",
                "ai_component": "Graph neural networks"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered technological solution inspired by biological systems to address the challenge of {t['challenge']}. Your solution should incorporate principles from {t['biological_inspiration']} and utilize {t['ai_component']} as a key AI component. Provide a detailed response addressing the following points:

1. Biomimetic Analysis (150-200 words):
   a) Explain the key features of {t['biological_inspiration']} relevant to {t['challenge']}.
   b) Describe how these biological principles can be applied to address the challenge.

2. AI Integration (200-250 words):
   a) Explain how {t['ai_component']} works and its relevance to the challenge.
   b) Describe how you would integrate this AI technique with the biomimetic approach.

3. System Design (250-300 words):
   a) Provide a detailed description of your proposed solution, including its main components and their interactions.
   b) Explain how the solution addresses the specific challenges of {t['challenge']}.
   c) Include a high-level diagram or pseudocode representing the system's architecture.

4. Sustainability Impact and Implementation (150-200 words):
   a) Analyze the potential environmental benefits of your solution.
   b) Discuss potential challenges in implementing the system and propose strategies to overcome them.

Ensure your response demonstrates an understanding of biological systems, artificial intelligence, and sustainability principles. Be creative while maintaining scientific and technological plausibility.

Format your response using clear headings for each section (e.g., '1. Biomimetic Analysis', '2. AI Integration', etc.). Your total response should be between 750-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a basic understanding of {t['biological_inspiration']} and how it relates to {t['challenge']}.",
            f"The proposed solution integrates {t['ai_component']} with biomimetic principles.",
            "The system design addresses the specific challenges presented and includes a high-level diagram or pseudocode.",
            "The sustainability impact and implementation considerations are discussed.",
            "The response is well-structured, follows the given format, and demonstrates interdisciplinary knowledge in biomimicry and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
