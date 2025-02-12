import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        idioms = [
            {
                "idiom": "A bird in the hand is worth two in the bush",
                "culture": "English",
                "hint": "Consider the relative values of certainty vs. potential"
            },
            {
                "idiom": "One man's trash is another man's treasure",
                "culture": "English",
                "hint": "Think about how value can be represented differently for different people"
            },
            {
                "idiom": "Don't put all your eggs in one basket",
                "culture": "English",
                "hint": "Consider the concept of risk distribution"
            }
        ]
        return {str(i+1): idiom for i, idiom in enumerate(random.sample(idioms, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following {t['culture']} idiomatic expression into a mathematical equation:

"{t['idiom']}"

Follow these steps:
1. Analyze the meaning of the idiom and its cultural context.
2. Identify the key concepts or values expressed in the idiom.
3. Assign variables to represent these concepts.
4. Create a mathematical equation that captures the relationship between these variables, reflecting the idiom's meaning.
5. Solve the equation, assuming reasonable values for the variables.
6. Justify your assumed values.

Hint: {t['hint']}

Provide your response in the following format:
Idiom analysis: [Your analysis of the idiom's meaning]
Variable assignments: [List your variables in the format 'x = concept', one per line]
Equation: [Your mathematical equation using the assigned variables]
Assumed values: [List your assumed values in the format 'x = value', one per line]
Solution: [Solve the equation with assumed values]
Justification: [Justify your assumed values]
Explanation: [Explain how your equation and solution reflect the idiom's meaning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include an analysis of the {t['culture']} idiom: '{t['idiom']}'",
            "The response should assign variables to key concepts in the idiom",
            "The response should provide a mathematical equation that reflects the idiom's meaning",
            "The response should include a solution to the equation with assumed values",
            "The response should justify the assumed values",
            "The explanation should clearly connect the mathematical representation to the idiom's meaning",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
