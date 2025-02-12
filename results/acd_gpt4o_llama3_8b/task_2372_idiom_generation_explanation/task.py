class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "A situation where someone is working very hard without getting recognized.", "synthetic_examples": ["Context: A person who always helps others without expecting anything in return.", "Context: An employee who consistently does more than required but never gets a promotion."]},
            "2": {"context": "A moment when someone realizes an obvious truth that was previously overlooked.", "synthetic_examples": ["Context: Someone finally understands the importance of health after a medical scare.", "Context: A person realizes they have been in love with their best friend all along."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Generate an idiomatic expression for the following context and explain its meaning:

Context: {t['context']}

Your idiomatic expression should be creative, culturally relevant, and clearly related to the given context. Ensure your explanation demonstrates a clear understanding of both the idiom and the context. Submit your response in the following format:

Idiom: [Your idiom]
Explanation: [Your explanation]

Additional examples:\n{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include an idiomatic expression.", "The idiom should be creative and culturally relevant.", "The explanation should demonstrate a clear understanding of the idiom and context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
