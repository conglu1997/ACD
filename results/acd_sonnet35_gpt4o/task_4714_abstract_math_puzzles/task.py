import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        puzzles = [
            {
                "concept": "Möbius addition",
                "description": "An operation ⊕ on real numbers defined as a ⊕ b = (a + b) / (1 + ab) for a, b ≠ -1",
                "question": "Find x such that 0.5 ⊕ x = 0.8"
            },
            {
                "concept": "Hyperbolic rotation",
                "description": "A transformation in hyperbolic geometry defined as tanh(a + b) = (tanh(a) + tanh(b)) / (1 + tanh(a)tanh(b))",
                "question": "If tanh(a) = 0.6 and tanh(b) = 0.8, find tanh(a + b)"
            }
        ]
        return {
            "1": random.choice(puzzles),
            "2": random.choice(puzzles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following abstract mathematical puzzle:\n\nConcept: {t['concept']}\nDescription: {t['description']}\nQuestion: {t['question']}\n\nProvide your solution and explain your reasoning step by step. Then, create a new puzzle using the same concept but with different numbers or a slightly modified operation. Your response should include:\n\n1. Solution to the given puzzle (100-150 words)\n2. Step-by-step explanation of your solution (150-200 words)\n3. A new puzzle you created using the same concept (50-100 words)\n4. The solution to your new puzzle (100-150 words)\n\nEnsure that your explanations are clear and that your new puzzle is challenging but solvable."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution to the given puzzle is correct and well-explained",
            "The step-by-step explanation is clear, logical, and demonstrates understanding of the concept",
            "The new puzzle created is based on the same concept and is both challenging and solvable",
            "The solution to the new puzzle is provided and is correct",
            "The response demonstrates creativity and abstract mathematical thinking"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
