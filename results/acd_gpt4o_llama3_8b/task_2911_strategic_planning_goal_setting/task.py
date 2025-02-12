class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "goal": "Launch a new product in the market within 6 months.",
                "constraints": "Limited budget, team of 5 people, must include market research, product development, marketing, and sales strategy."
            },
            "2": {
                "goal": "Organize an international conference on AI in 1 year.",
                "constraints": "Must include venue selection, speaker invitations, sponsorship acquisition, marketing, and attendee registration."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a goal and constraints. Your task is to create a strategic plan to achieve the goal within the given constraints. Break down the goal into actionable steps, assign timelines to each step, and ensure that the plan is coherent and feasible.

Goal: {t['goal']}
Constraints: {t['constraints']}

Submit your strategic plan as a plain text string in the following format:

Strategic Plan:
1. [Step 1: Description and Timeline]
2. [Step 2: Description and Timeline]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should include all necessary steps to achieve the goal.",
            "Each step should have a clear description and a realistic timeline.",
            "The plan should consider the given constraints and be feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
