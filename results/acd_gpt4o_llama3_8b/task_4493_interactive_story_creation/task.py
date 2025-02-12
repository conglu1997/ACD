class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "interactive_creation",
                "initial_prompt": "Start a story with a character named Alex who finds a mysterious map.",
                "follow_up_prompts": [
                    "What does Alex decide to do with the map? Provide specific actions and motivations.",
                    "Describe the first challenge Alex faces on the journey in detail.",
                    "How does Alex overcome the challenge? Include any tools or help received.",
                    "Conclude the story with an unexpected twist that ties back to the map's origin."
                ]
            },
            "2": {
                "task_type": "interactive_creation",
                "initial_prompt": "Begin a story about a scientist named Dr. Lee who discovers a new element.",
                "follow_up_prompts": [
                    "What unusual properties does the element have? Describe at least two properties.",
                    "How does Dr. Lee plan to use the element? Include potential benefits and risks.",
                    "Describe a complication that arises during the experiment with specific details.",
                    "End the story with a surprising discovery that changes the initial understanding of the element."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = """Create an interactive story based on the following initial prompt: {initial_prompt}\n\nRespond to the follow-up prompts iteratively, maintaining narrative consistency and creativity. Ensure the story is engaging and coherent throughout. Format your response as follows:\n\nInitial Story: [Your initial response]\nFollow-up 1: [Your response to follow-up prompt 1]\nFollow-up 2: [Your response to follow-up prompt 2]\nFollow-up 3: [Your response to follow-up prompt 3]\nFollow-up 4: [Your response to follow-up prompt 4]\n\nFollow-up Prompts:\n{follow_up_prompts}"""
        return instructions.format(initial_prompt=t['initial_prompt'], follow_up_prompts='\n'.join(t['follow_up_prompts']))

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and consistent with the initial prompt.",
            "Each follow-up prompt should be addressed appropriately.",
            "The narrative should be creative and engaging.",
            "The story should maintain consistency across all prompts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
