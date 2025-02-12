import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Binary star system with extreme temperature fluctuations",
            "Low-gravity planet with dense atmosphere and bioluminescent flora",
            "Underwater civilization in a methane ocean"
        ]
        biological_traits = [
            "Four-dimensional perception",
            "Hive mind with distributed consciousness",
            "Silicon-based lifeforms with crystalline structures"
        ]
        mathematical_operations = [
            "Addition and multiplication",
            "Exponentiation and logarithms",
            "Trigonometric functions"
        ]
        
        return {
            "1": {
                "environment": random.choice(environments),
                "biological_trait": random.choice(biological_traits),
                "mathematical_operation": random.choice(mathematical_operations)
            },
            "2": {
                "environment": random.choice(environments),
                "biological_trait": random.choice(biological_traits),
                "mathematical_operation": random.choice(mathematical_operations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a fictional alien number system based on the following constraints:\n\nEnvironment: {t['environment']}\nBiological Trait: {t['biological_trait']}\nMathematical Operations: {t['mathematical_operation']}\n\nYour task:\n\n1. Number System Design (200-250 words):\n   a) Create a unique base number system that reflects the given environment and biological traits.\n   b) Explain how this number system represents quantities and why it's suitable for the alien species.\n   c) Describe how basic arithmetic operations work in this system.\n\n2. Numerical Representation (100-150 words):\n   a) Provide examples of how the numbers 0-10 would be represented in your alien number system.\n   b) Explain any patterns or logic behind these representations.\n\n3. Mathematical Problem (150-200 words):\n   a) Present a mathematical problem using the specified mathematical operations in your alien number system.\n   b) Solve the problem, showing your work in the alien number system.\n   c) Translate the problem and solution back into standard base-10 notation.\n\n4. Linguistic Integration (150-200 words):\n   a) Create 3-5 'words' or expressions in an alien language that incorporate aspects of your number system.\n   b) Explain how these expressions reflect the aliens' mathematical understanding and culture.\n\n5. Critique and Reflection (100-150 words):\n   a) Discuss one potential limitation or challenge of your alien number system.\n   b) Propose how the aliens might address or overcome this limitation.\n\nEnsure your response demonstrates creativity, logical consistency, and a deep understanding of numerical systems and their cultural implications. Your alien number system should be unique and well-suited to the given constraints while remaining mathematically sound."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The alien number system is unique, logically consistent, and reflects the given environmental and biological constraints.",
            "The numerical representation and arithmetic operations are clearly explained and mathematically sound.",
            "The mathematical problem is correctly presented and solved in the alien number system, with accurate translation to base-10.",
            "The linguistic integration demonstrates creativity and logical connection to the number system.",
            "The critique and reflection show thoughtful analysis of the system's limitations and potential solutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
