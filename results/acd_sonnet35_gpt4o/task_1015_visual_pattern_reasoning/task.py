import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        pattern_types = [
            "Fractal",
            "Tessellation",
            "Optical Illusion",
            "Symmetry",
            "Cellular Automaton"
        ]
        rules = [
            "Recursive subdivision",
            "Rotation and translation",
            "Contrast and perspective",
            "Reflection and glide reflection",
            "Local interaction rules"
        ]
        return {
            "1": {"pattern": random.choice(pattern_types), "rule": random.choice(rules)},
            "2": {"pattern": random.choice(pattern_types), "rule": random.choice(rules)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate, analyze, and solve a problem involving a complex visual pattern based on the following information:

Pattern Type: {t['pattern']}
Rule: {t['rule']}

Complete the following steps:

1. Pattern Generation (200-250 words):
   a) Describe a complex visual pattern that combines the given pattern type and rule.
   b) Explain how the rule is applied to create or modify the pattern.
   c) Discuss any unique features or properties of your generated pattern.

2. Pattern Analysis (150-200 words):
   a) Identify key components or elements of your pattern.
   b) Explain how these components interact or relate to each other.
   c) Discuss any emergent properties or phenomena that arise from the pattern.

3. Problem Formulation (100-150 words):
   a) Create a problem or puzzle based on your generated pattern.
   b) Clearly state the objective or question to be solved.

4. Solution Process (200-250 words):
   a) Provide a step-by-step solution to the problem you formulated.
   b) Explain your reasoning at each step, referencing specific aspects of the pattern and rule.
   c) Discuss any insights or strategies that were crucial to solving the problem.

5. Generalization and Implications (150-200 words):
   a) Propose a generalization of your pattern or problem-solving approach.
   b) Discuss potential applications of this type of visual reasoning in fields such as mathematics, computer science, or cognitive psychology.
   c) Suggest how this pattern or problem-solving method could be extended or combined with other concepts.

Ensure your response demonstrates a deep understanding of visual patterns, logical reasoning, and creative problem-solving. Use clear and precise language to describe visual concepts, and provide detailed explanations of your thought processes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated pattern accurately combines the given pattern type and rule.",
            "The pattern analysis demonstrates a deep understanding of the pattern's structure and properties.",
            "The formulated problem is clear, challenging, and directly related to the generated pattern.",
            "The solution process is logical, well-explained, and effectively solves the formulated problem.",
            "The generalization and implications discussion shows creative thinking and broader understanding of the concept's applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
