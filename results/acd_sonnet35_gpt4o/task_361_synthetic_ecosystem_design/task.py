import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Low gravity (0.16g) environment",
            "High radiation exposure",
            "Limited water availability",
            "Extreme temperature fluctuations",
            "Confined space with artificial lighting"
        ]
        constraints = [
            "Maximize oxygen production",
            "Minimize waste",
            "Ensure food security",
            "Maintain biodiversity",
            "Psychological well-being of inhabitants"
        ]
        return {
            str(i+1): {
                "environment": random.choice(environments),
                "constraint": random.choice(constraints)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic ecosystem for a space station with the following specifications:

Environment: {t['environment']}
Key Constraint: {t['constraint']}

A synthetic ecosystem is an artificially created, self-sustaining biological system designed to mimic natural ecosystems while serving specific purposes in controlled environments.

Your task is to create a coherent and innovative ecosystem that addresses the given environmental challenge and key constraint. Your response should include:

1. Ecosystem Overview (100-150 words):
   a) Briefly describe the main components of your ecosystem.
   b) Explain how these components interact to form a functional system.

2. Environmental Adaptation (100-150 words):
   a) Describe how your ecosystem is adapted to the specified environment.
   b) Explain any novel biological or technological solutions you've incorporated.

3. Constraint Solution (100-150 words):
   a) Detail how your ecosystem addresses the key constraint.
   b) Discuss any trade-offs or potential issues with your approach.

4. Keystone Species (75-100 words):
   a) Identify and describe a keystone species or critical process in your ecosystem.
   b) Explain its role and importance in maintaining ecosystem balance.

5. Feedback Mechanisms (75-100 words):
   a) Describe at least one positive and one negative feedback mechanism in your ecosystem.
   b) Explain how these mechanisms contribute to system stability.

6. Long-term Sustainability (100-150 words):
   a) Discuss the long-term sustainability of your ecosystem.
   b) Identify potential challenges and propose solutions for ecosystem maintenance.

7. Interdisciplinary Connections (50-75 words):
   Briefly explain how your design integrates principles from biology, engineering, and environmental science.

Ensure your ecosystem design is scientifically plausible, creative, and demonstrates a deep understanding of ecological principles and systems thinking. Use appropriate scientific terminology throughout your response to showcase your technical knowledge.

Format your answer with clear headings for each section. Your total response should be between 600-875 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections",
            "The ecosystem design is coherent and scientifically plausible",
            f"The design adequately addresses the environmental challenge: {t['environment']}",
            f"The design effectively addresses the key constraint: {t['constraint']}",
            "The response demonstrates integration of biology, engineering, and environmental science principles",
            "The ecosystem includes realistic and well-explained feedback mechanisms",
            "The response shows creativity and innovation in ecosystem design",
            "Appropriate scientific terminology is used throughout the response"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
