class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Begin your story with a character waking up in a strange place and discovering a mysterious object. Create at least three branching paths for what the character decides to do next.", "criteria": ["The story must include at least three branching paths.", "Each branch should be coherent and logically consistent with the setup.", "The story should be engaging and maintain narrative consistency.", "Each branch should be at least 150 words long."]},
            "2": {"prompt": "Start your story with a character receiving an urgent message. Create at least three branching paths for how the character responds to the message.", "criteria": ["The story must include at least three branching paths.", "Each branch should be coherent and logically consistent with the setup.", "The story should be engaging and maintain narrative consistency.", "Each branch should be at least 150 words long."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create an interactive story based on the following prompt. Ensure that the story includes at least three branching paths and that each branch is coherent and logically consistent with the setup. The story should be engaging and maintain narrative consistency. Each branch should be at least 150 words long.

Prompt:
{t['prompt']}

Provide your interactive story below:"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t['criteria']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
