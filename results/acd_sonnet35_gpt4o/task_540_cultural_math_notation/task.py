import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "culture": "Ancient Egyptian",
                "inspiration": "Hieroglyphics",
                "math_concept": "Calculus"
            },
            {
                "culture": "Indigenous Australian",
                "inspiration": "Dot painting",
                "math_concept": "Graph theory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a mathematical notation system inspired by {t['culture']} {t['inspiration']}, and use it to represent and solve a problem in {t['math_concept']}. Your task has the following parts:

1. Notation System Design (200-250 words):
   a) Describe your notation system, explaining how it incorporates elements from {t['culture']} {t['inspiration']}.
   b) Provide examples of how basic mathematical operations and concepts are represented in your system.
   c) Explain how your system can represent complex ideas in {t['math_concept']}.

2. Cultural and Mathematical Justification (150-200 words):
   a) Explain how your notation system reflects or respects the cultural context it's inspired by.
   b) Discuss any advantages or unique features of your system for representing {t['math_concept']}.

3. Problem Representation (100-150 words):
   Present a complex problem in {t['math_concept']} using your notation system. Provide both the problem statement in English and its representation in your system.

4. Problem Solving (200-250 words):
   a) Solve the problem you presented, showing each step using your notation system.
   b) Explain your solution process, highlighting how your notation system facilitates or challenges the problem-solving process.

5. Reflection (100-150 words):
   Discuss the potential implications of your notation system for mathematics education, cross-cultural communication in STEM fields, or advancing mathematical thinking.

Ensure your response demonstrates a deep understanding of both the cultural inspiration and the mathematical concepts involved. Be creative in your system design while maintaining mathematical rigor and cultural sensitivity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The notation system clearly incorporates elements from {t['culture']} {t['inspiration']}.",
            f"The system can effectively represent complex ideas in {t['math_concept']}.",
            "The cultural and mathematical justifications are well-reasoned and insightful.",
            "The problem representation and solution using the new notation system are correct and clearly explained.",
            "The reflection demonstrates a deep understanding of the implications of the new notation system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
