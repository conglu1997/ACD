class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "visual_prompt": "Imagine a bustling medieval marketplace. Describe the scene in vivid detail, focusing on the various stalls, the people, and the atmosphere."
            },
            "2": {
                "visual_prompt": "Visualize a serene beach at sunset with waves gently crashing against the shore. Write a poem that captures the tranquility and beauty of the setting." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        visual_prompt = t["visual_prompt"]
        instructions = f"""Your task is to generate creative content based on the following visual prompt:

Visual Prompt: {visual_prompt}

Provide your response in plain text format. Ensure that your content is vivid, imaginative, and effectively captures the essence of the visual scene described in the prompt.

Your response should be well-structured, creative, and engaging."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The content should be vivid and imaginative.",
            "The content should effectively capture the essence of the visual scene described in the prompt.",
            "The response should be well-structured and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
