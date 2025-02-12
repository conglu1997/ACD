class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "idiom": "kick the bucket",
                "context": "After years of battling illness, John finally kicked the bucket."
            },
            "2": {
                "scenario": "A person who suddenly becomes very wealthy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'idiom' in t:
            idiom = t['idiom']
            context = t['context']
            return f"""Interpret the meaning of the following idiomatic expression in the given context:

Idiom: '{idiom}'
Context: '{context}'

Provide a plain text interpretation of the idiom in the context provided. Submit your interpretation as a plain text string in the following format:

Interpretation: [Your interpretation]"""
        else:
            scenario = t['scenario']
            return f"""Generate a new idiomatic expression for the following scenario:

Scenario: '{scenario}'

Provide a plain text idiom along with its meaning. Submit your response as a plain text string in the following format:

Idiom: [Your idiom]
Meaning: [Explanation of your idiom]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'idiom' in t:
            criteria = [
                "The interpretation should accurately reflect the meaning of the idiom in the given context."
            ]
        else:
            criteria = [
                "The generated idiom should be creative and relevant to the given scenario.",
                "The meaning of the generated idiom should be clear and appropriate."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
