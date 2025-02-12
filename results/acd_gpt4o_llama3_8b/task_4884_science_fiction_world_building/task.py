class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a science fiction world set on a distant planet. Your world should include details about its geography, culture, technology, and history. Provide a narrative that ties these elements together and explains how they interact. The narrative should be between 300 to 500 words.",
                "task_type": "create"
            },
            "2": {
                "prompt": "Create a science fiction world set in a future version of Earth. Your world should include details about changes in geography, culture, technology, and history. Provide a narrative that ties these elements together and explains how they interact. The narrative should be between 300 to 500 words.",
                "task_type": "create"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['prompt']}

Your response should be a cohesive narrative that ties together the elements of geography, culture, technology, and history. Ensure that your world is logically consistent and imaginative. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should include detailed descriptions of geography, culture, technology, and history.",
            "The narrative should be cohesive and logically consistent.",
            "The world-building should be imaginative and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
