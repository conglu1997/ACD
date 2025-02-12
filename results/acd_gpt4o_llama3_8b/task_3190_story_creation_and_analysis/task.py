class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": "A young boy, a magical forest, a hidden treasure, and a talking animal.",
                "task_type": "creation"
            },
            "2": {
                "story": "Once upon a time, in a small village, there lived a young girl named Emily. She loved exploring the nearby forest, which was said to be magical. One day, she found an ancient map that led to a hidden treasure. With the help of a wise old owl, Emily embarked on an adventure to find the treasure. Along the way, she faced various challenges but learned valuable lessons about bravery and friendship. In the end, Emily discovered that the real treasure was the friendships she made along the way.",
                "task_type": "analysis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'creation':
            return f"""Create a short story that includes the following elements: {t['elements']}. Ensure that your story has a clear beginning, middle, and end. Develop the characters and the plot, and include descriptions of the settings and any important events. Submit your story as a plain text string."""
        else:
            return f"""Analyze the following story: {t['story']}. Identify the main themes, characters, and plot structure. Provide a detailed analysis, including the story's message, the development of characters, and the sequence of events. Submit your analysis in the following format:

Themes: [Your identification of the themes]
Characters: [Your identification of the characters]
Plot Structure: [Your analysis of the plot structure]
Message: [Your interpretation of the story's message]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'creation':
            validation_criteria = ["The story should include all the given elements.", "The story should have a clear beginning, middle, and end.", "The characters and plot should be well-developed.", "Descriptions of settings and important events should be included."]
        else:
            validation_criteria = ["The analysis should accurately identify the main themes, characters, and plot structure.", "The analysis should provide a detailed and coherent interpretation of the story's message."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
