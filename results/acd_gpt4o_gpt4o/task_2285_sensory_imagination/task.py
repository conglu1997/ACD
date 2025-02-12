class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe the smell and taste of a freshly baked loaf of bread in vivid detail. Your description should be imaginative and evoke the sensory experience. Provide your response in plain text format."},
            "2": {"prompt": "Imagine you are at a beachside restaurant. Describe the smell and taste of a seafood dish that you would have there. Your description should be vivid and evoke the sensory experience. Provide your response in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a vivid and imaginative description based on the given prompt. Ensure that your description evokes the sensory experience as much as possible:\n\n{t['prompt']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid and evoke the sensory experience.", "The response should be imaginative and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
