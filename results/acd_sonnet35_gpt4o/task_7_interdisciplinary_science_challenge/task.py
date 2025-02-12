import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "problem": "design a new type of renewable energy source",
                "disciplines": ["physics", "chemistry", "biology"]
            },
            {
                "problem": "propose a method for terraforming Mars",
                "disciplines": ["astronomy", "geology", "environmental science"]
            },
            {
                "problem": "develop a novel approach to extend human lifespan",
                "disciplines": ["biology", "genetics", "nanotechnology"]
            },
            {
                "problem": "create a new form of secure quantum communication",
                "disciplines": ["quantum physics", "computer science", "mathematics"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to {t['problem']} by combining principles from {', '.join(t['disciplines'])}. Provide a detailed explanation of your proposed solution, including:\n\n1. A brief overview of the solution (1-2 sentences)\n2. How principles from each discipline contribute to the solution (1-2 sentences per discipline)\n3. Potential challenges and how they might be addressed (2-3 sentences)\n\nEnsure your solution is scientifically plausible and creative, demonstrating a clear understanding of the relevant scientific principles."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution demonstrates a clear understanding of principles from all specified disciplines.",
            "The proposed idea is creative and original, while remaining scientifically plausible.",
            "The explanation is well-structured, following the requested format (overview, contribution of each discipline, challenges).",
            "The response addresses potential challenges and proposes reasonable ways to overcome them.",
            "The overall solution is logically consistent and demonstrates interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
