import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        clues = [
            {"clue": "Confused, sad, lost - no energy to be greedy (10)", "answer": "AVARICIOUS", "explanation": "Anagram ('confused') of 'SAD LOST' + 'I' ('no energy') = AVARICIOUS (meaning 'greedy')"},
            {"clue": "Snack food goes back in tin (6)", "answer": "PRETZEL", "explanation": "LEZTERP ('snack food' PRETZEL backwards) goes in TIN = PRETZEL"},
            {"clue": "Chop wood endlessly for a garden tool (3)", "answer": "HOE", "explanation": "CHOP without its last letter ('endlessly') = CHO, sounds like ('wood' as in 'would') HOE"},
            {"clue": "Ape holding a fruit (5)", "answer": "PEACH", "explanation": "APE containing ('holding') A = PEACH (a fruit)"},
            {"clue": "Meal's conclusion - no starters for the dieters (7)", "answer": "DESSERT", "explanation": "DIETERS without first letters ('no starters') = ESSERT, sounds like ('meal's conclusion') DESSERT"}
        ]
        return {
            "1": random.choice(clues),
            "2": random.choice(clues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task has two parts:\n\n1. Analyze the following cryptic crossword clue: '{t['clue']}'. Explain how the clue works, breaking down its components and showing how they lead to the answer. Do not reveal the answer in your analysis.\n\n2. Create a new cryptic crossword clue for a {len(t['answer'])}-letter word. Your clue should be different from the one provided and follow standard cryptic crossword conventions.\n\nFormat your response as follows:\n\nAnalysis: [Your analysis of the given clue]\n\nNew Clue: [Your new clue]\n\nExplanation: [Explanation of how your new clue works]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The analysis correctly explains how the clue works without revealing the answer '{t['answer']}'.",
            f"A new, different clue is created for a {len(t['answer'])}-letter word.",
            "The new clue follows standard cryptic crossword conventions.",
            "The explanation of the new clue is clear and accurate.",
            "The response follows the requested format (Analysis: ... New Clue: ... Explanation: ...)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
