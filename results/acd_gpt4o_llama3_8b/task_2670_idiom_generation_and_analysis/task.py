class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "hard work",
                "context": "In the context of a challenging project at work, analyze the usage of the idiom 'burning the midnight oil.'"
            },
            "2": {
                "theme": "luck",
                "context": "In the context of a surprising success, analyze the usage of the idiom 'a stroke of luck.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an original idiom based on the following theme and then analyze the meaning and usage of the given idiom in the specified context.

Theme: {t['theme']}

Context: {t['context']}

Your response should include:
1. A newly generated, original idiom based on the given theme. Ensure the idiom is not a well-known existing idiom.
2. An analysis of the meaning and usage of the given idiom in the specified context. Your analysis should include:
   a. The literal and figurative meanings of the idiom.
   b. How the idiom fits into the given context.
   c. Any cultural or historical relevance if applicable.

Submit your response as a plain text string in the following format:

Generated Idiom: [Your generated idiom]
Analysis: [Your analysis of the given idiom]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated idiom should be original and relevant to the given theme.",
            "The generated idiom should not be a well-known existing idiom.",
            "The analysis should accurately explain the literal and figurative meanings of the given idiom.",
            "The analysis should correctly discuss how the idiom fits into the given context.",
            "The analysis should mention any cultural or historical relevance if applicable.",
            "The generated idiom and analysis should be clearly separated in the submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
