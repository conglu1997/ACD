class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "John was an ordinary man living a quiet life in a small town. Every day, he would visit the local bakery to get his favorite bread. One day, as he entered the bakery, he noticed something unusual..."},
            "2": {"story": "Emily had always been fascinated by the stars. She spent every night gazing at the sky, dreaming of becoming an astronaut. On her 18th birthday, she received a mysterious letter that changed everything..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        story = t["story"]
        return f"""Complete the following story by introducing a surprising but coherent plot twist. Ensure that the twist is unexpected yet logically fits within the narrative context. Your twist should be creative and enhance the overall story. Here is an example of a plot twist for a different story:\n\nExample story: Sarah was walking through the forest when she found a mysterious box. Inside the box, she found an ancient map. As she followed the map, she discovered...\nExample plot twist: ...that the map led to a hidden underground city where time had stood still for centuries, and she was the chosen one to bring it back to life.\n\nSubmit your completed story with the plot twist as a plain text string in the following format:\n\nCompleted Story: [Your completed story including the plot twist]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The plot twist should be unexpected.", "The plot twist should fit coherently within the narrative.", "The plot twist should enhance the overall story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
