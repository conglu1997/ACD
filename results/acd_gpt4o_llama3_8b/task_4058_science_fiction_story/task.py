class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "In a distant future where humans have colonized Mars, a mysterious artifact is discovered beneath the surface. Describe the discovery and its potential implications for humanity.", "word_count": "300-500"},
            "2": {"prompt": "Humans have developed the ability to upload their consciousness into a digital utopia. However, unforeseen consequences arise. Write a story exploring one such consequence.", "word_count": "300-500"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short science fiction story based on the following prompt: '{t['prompt']}'. Ensure that your story is between {t['word_count']} words and adheres to the conventions of the science fiction genre. Your story should be coherent, imaginative, and engaging.

Submit your response as a plain text string in the following format:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be between the specified word count.", "The story should adhere to science fiction genre conventions.", "The story should be coherent, imaginative, and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
