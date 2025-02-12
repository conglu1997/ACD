class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a pun involving a fruit.",
                "constraints": [
                    "The pun should involve at least one type of fruit.",
                    "The pun should be clear and understandable.",
                    "The pun should be humorous."]
            },
            "2": {
                "prompt": "Create a pun related to a famous historical figure.",
                "constraints": [
                    "The pun should involve a well-known historical figure.",
                    "The pun should be clear and understandable.",
                    "The pun should be humorous."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a humorous pun based on the following prompt:

Prompt: {t['prompt']}

Ensure that your pun adheres to the following constraints:
1. {t['constraints'][0]}
2. {t['constraints'][1]}
3. {t['constraints'][2]}

Provide your pun in plain text format. The pun should be clear, understandable, and humorous. Format your response as follows:

Pun: <Your pun here>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The pun should involve the required element (fruit or historical figure).",
            "The pun should be clear and understandable.",
            "The pun should be humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
