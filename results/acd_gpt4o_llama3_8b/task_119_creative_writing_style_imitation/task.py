class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "author": "Edgar Allan Poe",
                "prompt": "Write a short story about a mysterious event in a dark, gothic setting. The story should include elements of suspense and horror, and be written in the style of Edgar Allan Poe."
            },
            "2": {
                "author": "Jane Austen",
                "prompt": "Write a passage describing a social gathering in a 19th-century English countryside setting. The passage should focus on character interactions, social norms, and include some witty dialogue, written in the style of Jane Austen."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a short story or passage based on the specified prompt:

Author: {t['author']}
Prompt: {t['prompt']}

Ensure that your writing mimics the style of the specified author, includes the specified elements, and adheres to the thematic and stylistic guidelines. Your submission should be around 200-300 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The writing should mimic the style of the specified author.", "The story or passage should include the specified elements.", "The writing should adhere to the thematic and stylistic guidelines.", "The submission should be around 200-300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
