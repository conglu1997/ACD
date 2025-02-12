import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {"concept": "loop", "hint": "I repeat myself, but I'm not boring"},
            {"concept": "variable", "hint": "I hold secrets, but I'm not a safe"},
            {"concept": "function", "hint": "I'm called upon, but I'm not a phone"},
            {"concept": "array", "hint": "I keep things in order, but I'm not a librarian"},
            {"concept": "recursion", "hint": "I call myself, but I'm not narcissistic"},
            {"concept": "conditional", "hint": "I make decisions, but I'm not a judge"},
            {"concept": "class", "hint": "I'm a blueprint, but I'm not for buildings"},
            {"concept": "inheritance", "hint": "I pass things down, but I'm not a family heirloom"},
            {"concept": "algorithm", "hint": "I'm a step-by-step guide, but I'm not a recipe"},
            {"concept": "debugging", "hint": "I fix problems, but I'm not a therapist"}
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task has two parts:\n\n1. Generate a riddle for the programming concept '{t['concept']}'. The riddle should be one sentence long and include the hint: '{t['hint']}'.\n\n2. Provide a clear explanation of how the riddle relates to the programming concept.\n\nFormat your response as follows:\n\nRiddle: [Your riddle here]\n\nExplanation: [Your explanation here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The riddle accurately represents the concept of {t['concept']}.",
            f"The riddle incorporates the hint: '{t['hint']}'.",
            "The riddle is creative and not overly obvious.",
            "The explanation clearly relates the riddle to the programming concept.",
            "The response follows the requested format (Riddle: ... Explanation: ...)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
