class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A young hero sets out on a quest to find a lost artifact in an enchanted forest. Include at least three branching storylines with different outcomes."},
            "2": {"prompt": "A detective is investigating a mysterious disappearance in a small town. Include at least three branching storylines with different outcomes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""Create an interactive fiction narrative based on the following prompt:

Prompt: {prompt}

Your narrative should include at least three branching storylines, each leading to a different outcome. Ensure that each branch is logically coherent, maintains consistency with the overall storyline, and offers a unique perspective or twist. The narrative should be engaging and creative.

Format your response as follows:

Branch 1:
[Your narrative for branch 1]

Branch 2:
[Your narrative for branch 2]

Branch 3:
[Your narrative for branch 3]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        branches = submission.split('\n\nBranch')
        if len(branches) < 4:  # branches[0] is empty due to split
            return 0.0
        criteria = ["Each branch must be logically coherent.", "Each branch must maintain consistency with the overall storyline.", "Each branch must offer a unique perspective or twist."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
