class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "story_generation", "prompt": "A young boy discovers a magical portal in his backyard.", "analysis_task": "Provide a summary of the story."},
            "2": {"task_type": "story_generation", "prompt": "An astronaut gets stranded on an alien planet.", "analysis_task": "Analyze the main character's motivations and challenges."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == "story_generation":
            return f"Generate a coherent and logical short story based on the following prompt: {t['prompt']} Submit your story as a plain text string in the following format: 'Story: [Your story] Analysis: [Your analysis]'. After generating the story, {t['analysis_task']} Ensure your analysis is detailed and accurately reflects the content of your story."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be coherent and logically consistent.", "The story should follow a clear narrative structure with a beginning, middle, and end.", "The analysis should accurately reflect the content of the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
