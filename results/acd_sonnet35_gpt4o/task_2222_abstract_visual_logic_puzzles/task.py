import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "puzzle_type": "Fractal Symmetry",
                "mathematical_principle": "Self-similarity",
                "logical_concept": "Recursive patterns"
            },
            {
                "puzzle_type": "Topological Transformation",
                "mathematical_principle": "Homeomorphism",
                "logical_concept": "Invariance under deformation"
            },
            {
                "puzzle_type": "Geometric Progression",
                "mathematical_principle": "Exponential growth",
                "logical_concept": "Inductive reasoning"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and solve an abstract visual puzzle based on the following parameters:

Puzzle Type: {t['puzzle_type']}
Mathematical Principle: {t['mathematical_principle']}
Logical Concept: {t['logical_concept']}

Your task has the following components:

1. Puzzle Creation (200-250 words):
   a) Design an abstract visual puzzle that incorporates the given puzzle type, mathematical principle, and logical concept.
   b) Describe the visual elements and structure of your puzzle in detail.
   c) Explain how your puzzle embodies the mathematical principle and logical concept.

2. Solution Process (200-250 words):
   a) Provide a step-by-step approach to solving your puzzle.
   b) Explain the reasoning behind each step, relating it to the mathematical principle and logical concept.
   c) Discuss any potential challenges or insights that might arise during the solving process.

3. Visual Representation (150-200 words):
   a) Describe a visual representation of your puzzle using ASCII art or a detailed textual description.
   b) Ensure that your representation clearly conveys the key elements and patterns of the puzzle.

4. Variations and Extensions (150-200 words):
   a) Propose two variations of your puzzle that increase its complexity or explore different aspects of the mathematical principle or logical concept.
   b) Briefly explain how each variation changes the puzzle and its solution process.

5. Cognitive Analysis (100-150 words):
   a) Discuss the cognitive skills and reasoning processes required to solve your puzzle.
   b) Explain how your puzzle might challenge or reveal capabilities of both human and AI problem-solvers.

Ensure your response demonstrates a deep understanding of abstract reasoning, spatial cognition, and the application of mathematical and logical principles to visual problems. Be creative in your puzzle design while maintaining coherence and solvability."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed abstract visual puzzle incorporating {t['puzzle_type']}, {t['mathematical_principle']}, and {t['logical_concept']}",
            "The puzzle creation and solution process are clearly explained and logically sound",
            "A visual representation of the puzzle is provided using ASCII art or detailed textual description",
            "Two valid variations of the puzzle are proposed with explanations",
            "The cognitive analysis discusses relevant skills and reasoning processes",
            "The overall response demonstrates creativity, coherence, and deep understanding of abstract reasoning and mathematical principles"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
