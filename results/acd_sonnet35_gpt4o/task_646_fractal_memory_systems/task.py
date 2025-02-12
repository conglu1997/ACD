import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        fractal_types = [
            {
                "name": "Sierpinski Triangle",
                "dimension": 1.585,
                "base_shape": "triangle"
            },
            {
                "name": "Menger Sponge",
                "dimension": 2.727,
                "base_shape": "cube"
            },
            {
                "name": "Koch Snowflake",
                "dimension": 1.262,
                "base_shape": "hexagon"
            }
        ]
        return {str(i+1): fractal for i, fractal in enumerate(random.sample(fractal_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fractal-based memory system using the {t['name']} as its foundational structure. Your task has the following parts:

1. Fractal Memory System Design (250-300 words):
   a) Describe how you would use the {t['name']} structure to organize and store information in a memory system.
   b) Explain how the fractal's self-similarity and dimension (D ≈ {t['dimension']}) could be leveraged for efficient information encoding and retrieval.
   c) Propose a method for mapping different types of information (e.g., semantic, episodic, procedural) onto different levels or components of the fractal structure.
   d) Discuss how the base shape ({t['base_shape']}) of the fractal influences your memory system design.

2. Cognitive Process Analysis (200-250 words):
   a) Analyze how your fractal memory system might affect cognitive processes such as learning, recall, and association.
   b) Compare and contrast your fractal-based approach with traditional hierarchical or network-based models of memory.
   c) Discuss potential cognitive benefits or limitations of using a fractal structure for memory organization.

3. Mathematical Framework (200-250 words):
   a) Provide a mathematical description of your fractal memory system, including relevant equations or formulas.
   b) Explain how the fractal dimension relates to the information capacity and retrieval efficiency of your system.
   c) Describe a method for calculating the optimal depth of the fractal structure based on the amount and type of information to be stored.

4. Practical Application (150-200 words):
   a) Propose a specific real-world application for your fractal memory system (e.g., in education, artificial intelligence, or information management).
   b) Explain how the unique properties of your system would provide advantages in this application.
   c) Discuss potential challenges in implementing your system and propose solutions.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using fractal-based memory systems, particularly in relation to human cognitive enhancement or AI development.
   b) Address concerns about potential cognitive overload or information distortion that might arise from using such a system.
   c) Explain limitations of your proposed system and areas for future research and improvement.

Ensure your response demonstrates a deep understanding of fractal geometry, cognitive science, and information theory. Be creative in your approach while grounding your ideas in established mathematical and cognitive principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['name']} fractal and how its properties can be applied to memory systems.",
            "The fractal memory system design should be innovative, logically consistent, and well-explained.",
            "The mathematical framework should accurately incorporate the fractal dimension and provide relevant equations or formulas.",
            "The analysis of cognitive processes and practical applications should be insightful and grounded in current understanding of memory and cognition.",
            "The response must thoughtfully address ethical considerations and potential limitations of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
