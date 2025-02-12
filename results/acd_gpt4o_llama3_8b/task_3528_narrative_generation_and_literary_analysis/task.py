class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Overcoming adversity",
                "instructions": "Write a short story based on the theme 'Overcoming adversity'. Your story should have a clear beginning, middle, and end, with well-developed characters and a coherent plot. Aim for a length of approximately 300-500 words. Use paragraphs to structure your story. Submit your story as a plain text string."
            },
            "2": {
                "excerpt": "'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'",
                "instructions": "Analyze the provided literary excerpt from Charles Dickens' 'A Tale of Two Cities'. Discuss its significance, the literary devices used, and its impact on the overall narrative of the novel. Your analysis should be approximately 200-300 words. Ensure your analysis is coherent and clearly articulated. Submit your analysis as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given instructions.

Instructions: {t['instructions']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            validation_criteria = [
                "The story should be based on the given theme.",
                "The story should have a clear beginning, middle, and end.",
                "The characters and plot should be well-developed.",
                "The story should be approximately 300-500 words in length.",
                "The story should use paragraphs to structure the narrative."
            ]
        else:
            validation_criteria = [
                "The analysis should discuss the significance of the excerpt.",
                "The analysis should identify and explain the literary devices used.",
                "The analysis should discuss the impact of the excerpt on the overall narrative.",
                "The analysis should be approximately 200-300 words in length.",
                "The analysis should be coherent and clearly articulated."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
