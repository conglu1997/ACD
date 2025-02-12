class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'project': 'Assemble a flat-pack bookshelf', 'issues': ['missing screws', 'uneven shelves']},
            '2': {'project': 'Fix a leaky kitchen faucet', 'issues': ['water still leaking', 'reduced water pressure']}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a detailed set of DIY instructions for the following household project: {t['project']}\n\nYour instructions should include:\n1. A list of required materials and tools.\n2. Step-by-step instructions to complete the project.\n3. Safety precautions and tips for success.\n\nNext, provide troubleshooting steps for the following common issues that may arise during the project: {', '.join(t['issues'])}.\n\nYour troubleshooting steps should include:\n1. A clear description of the issue.\n2. Possible causes for the issue.\n3. Detailed steps to resolve the issue.\n\nSubmit your response as a plain text string in the following format:\n\nDIY Instructions:\n[Your instructions here]\n\nTroubleshooting Steps:\n[Your troubleshooting steps here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should be clear, detailed, and logically structured.", "The troubleshooting steps should accurately address the given issues and provide practical solutions.", "Both the instructions and troubleshooting steps should be feasible and useful for an average person to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
