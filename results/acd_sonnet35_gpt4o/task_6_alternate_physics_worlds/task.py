import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constants = [
            "speed of light",
            "gravitational constant",
            "Planck's constant",
            "electron charge",
            "Boltzmann constant"
        ]
        phenomena = [
            "formation of stars",
            "behavior of black holes",
            "evolution of life",
            "properties of atoms",
            "flow of time"
        ]
        return {
            "1": {"constant": random.choice(constants), "phenomenon": random.choice(phenomena)},
            "2": {"constant": random.choice(constants), "phenomenon": random.choice(phenomena)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Imagine an alternate universe where the {t['constant']} is significantly different from our universe. Describe how this change would affect the {t['phenomenon']} in that universe. Your response should be scientifically grounded but creative in exploring the consequences. Provide a clear, concise explanation in 3-5 sentences."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates accurate understanding of the physical constant and phenomenon.",
            "The explanation is scientifically plausible and logically consistent.",
            "The response shows creativity in exploring the consequences of the changed constant.",
            "The explanation is clear, concise, and well-articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
