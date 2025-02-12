class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input_type": "art", "input": "A vibrant abstract painting with swirling colors, geometric shapes, and a prominent red spiral in the center.", "output_type": "story", "prompt": "Write a short story inspired by the artwork. Your story should be between 300 and 500 words."},
            "2": {"input_type": "music", "input": "A piece of classical music with a slow, melancholic melody, dominated by a solo violin.", "output_type": "description", "prompt": "Describe a scene that could accompany this piece of music. Your description should be between 150 and 250 words."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate creative content based on the given input.

Input type: {t['input_type']}
Input: {t['input']}
Output type: {t['output_type']}
Prompt: {t['prompt']}

Ensure that your response is imaginative, coherent, and captures the essence of the input. Provide your response in plain text format. Ensure that your response adheres to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be imaginative and coherent.",
            "The response should capture the essence of the input.",
            "The response should adhere to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
