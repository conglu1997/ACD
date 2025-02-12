class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A friend is feeling down because they didn't get the job they applied for.", "goal": "Cheer them up and motivate them to keep trying."},
            "2": {"scenario": "A colleague is considering quitting their job due to stress.", "goal": "Persuade them to take a break and consider other stress-management techniques before making a final decision."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Write a persuasive letter based on the following scenario: {t['scenario']} Your goal is to {t['goal']} Ensure your letter is empathetic, understanding, and persuasive. Submit your letter as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The letter should demonstrate empathy.", "The letter should be persuasive and address the recipient's feelings or situation.", "The letter should be coherent and well-written."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
