import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        paradoxes = [
            {
                'name': 'Grandfather Paradox',
                'description': 'A time traveler goes back in time and prevents their grandparents from meeting, potentially erasing their own existence.'
            },
            {
                'name': 'Bootstrap Paradox',
                'description': 'An object or information is brought back in time and becomes the cause of its own existence.'
            }
        ]
        return {str(i+1): paradox for i, paradox in enumerate(paradoxes)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a logical system to resolve the {t['name']} and apply it to a specific scenario. Your task:

1. Paradox Analysis (100-150 words):
   Analyze the {t['name']}. Explain its core logical conflict and potential implications for causality and the nature of time.

2. Resolution System Design (200-250 words):
   Create a logical system or framework to resolve this type of paradox. Your system should:
   a) Define key principles or axioms about the nature of time and causality
   b) Provide a step-by-step method for analyzing and resolving paradoxes
   c) Incorporate concepts from physics, philosophy, or other relevant fields
   Explain how your system works and its theoretical foundations.

3. Scenario Application (150-200 words):
   Apply your resolution system to the following scenario:
   {t['description']}
   Provide a detailed explanation of how your system resolves this specific paradox.

4. Implications and Limitations (100-150 words):
   Discuss the broader implications of your resolution system for our understanding of time, free will, and causality. Address any potential limitations or criticisms of your approach.

5. Interdisciplinary Connections (100-150 words):
   Explain how your resolution system might be applied or adapted to solve problems in other fields (e.g., computer science, biology, social sciences). Provide at least two specific examples.

6. Experimental Design (100-150 words):
   Propose a theoretical experiment or observational method that could test or validate your paradox resolution system. Consider both technological and ethical constraints.

Ensure your response demonstrates a deep understanding of causal logic, temporal mechanics, and creative problem-solving. Use clear, concise language and provide examples where appropriate to illustrate complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The paradox analysis is thorough and accurately describes the logical conflict.",
            "The resolution system is logically consistent, innovative, and grounded in relevant scientific or philosophical concepts.",
            "The application of the system to the specific scenario is clear, detailed, and effectively resolves the paradox.",
            "The discussion of implications and limitations shows deep understanding and critical thinking.",
            "The interdisciplinary connections are creative and well-reasoned.",
            "The proposed experiment is feasible and directly relates to validating the resolution system.",
            "The overall response demonstrates a sophisticated understanding of temporal mechanics and causal logic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
