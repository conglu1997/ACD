class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": ["a magical forest", "a talking animal", "a hidden treasure"],
                "plot_twist": "The treasure is cursed."
            },
            "2": {
                "elements": ["a futuristic city", "a rebellious teenager", "a secret organization"],
                "plot_twist": "The teenager discovers they are the organization's leader."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a coherent and engaging story that incorporates the following elements and includes the given plot twist.

Elements: {', '.join(t['elements'])}
Plot Twist: {t['plot_twist']}

Your story should be at least 500 words long and must integrate all the elements and the plot twist in a natural and engaging way. Ensure that your narrative is coherent, with well-developed characters and a logical progression of events.

Submit your story as a plain text string in the following format:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should integrate all the given elements in a natural way.",
            "The plot twist should be incorporated effectively and should make sense within the story.",
            "The narrative should be coherent, with well-developed characters and logical progression.",
            "The story should be at least 500 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
