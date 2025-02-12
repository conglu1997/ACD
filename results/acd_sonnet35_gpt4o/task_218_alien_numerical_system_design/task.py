import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_civilizations = [
            {
                "name": "Octopodians",
                "description": "Eight-limbed creatures living in deep ocean environments with bioluminescent abilities",
                "base_number": 8
            },
            {
                "name": "Binary Beings",
                "description": "Silicon-based lifeforms with binary thought processes living on a planet with extreme temperature fluctuations",
                "base_number": 2
            }
        ]
        
        mathematical_operations = [
            {"name": "addition and multiplication", "problem": "Calculate the sum and product of the alien equivalent of 1234 and 5678 in base 10."},
            {"name": "exponentiation and logarithms", "problem": "Calculate the alien equivalent of 2^10 and log_2(1024) in base 10."},
            {"name": "calculus and integration", "problem": "Find the derivative and integral of the alien equivalent of f(x) = x^3 + 2x^2 - 5x + 3."}
        ]
        
        return {
            "1": {
                "civilization": random.choice(alien_civilizations),
                "operation": random.choice(mathematical_operations)
            },
            "2": {
                "civilization": random.choice(alien_civilizations),
                "operation": random.choice(mathematical_operations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a unique numerical system for the {t['civilization']['name']} civilization. They are described as: {t['civilization']['description']}. Their numerical system should be based on the number {t['civilization']['base_number']}.

Your task:

1. Numerical System Design (200-250 words):
   a) Describe the basic numerals and their representation in this system.
   b) Explain how place value works in this system.
   c) Discuss any unique features of this system that reflect the alien biology or environment.

2. Mathematical Operations (150-200 words):
   a) Explain how the operations of {t['operation']['name']} work in this numerical system.
   b) Provide an example calculation for each operation, showing the step-by-step process.

3. Problem Solving (200-250 words):
   a) Solve the following problem using the alien numerical system: {t['operation']['problem']}
   b) Show all your work, including intermediate steps and final results in the alien number system.
   c) Explain the significance of this problem and its solution in the context of the alien civilization.

4. Comparative Analysis (150-200 words):
   a) Compare and contrast this alien numerical system with the decimal system used by humans.
   b) Discuss potential advantages and disadvantages of this system for mathematical and scientific advancement.

Format your response using clear headings for each section. For all calculations, show your work in the alien number system, and provide translations to base 10 where appropriate. Be sure to explain your reasoning at each step."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The numerical system design is coherent, creative, and clearly reflects the given alien civilization's characteristics and base number.",
            "The explanation of mathematical operations is clear, consistent with the designed numerical system, and includes correct step-by-step examples.",
            f"The solution to the problem '{t['operation']['problem']}' is correctly calculated using the designed alien numerical system, with all work shown and explained.",
            "The comparative analysis demonstrates insightful understanding of numerical systems and their implications for mathematical and scientific advancement.",
            "The response follows the specified format with clear headings and includes all required elements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
