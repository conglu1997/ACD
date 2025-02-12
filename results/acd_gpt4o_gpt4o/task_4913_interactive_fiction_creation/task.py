class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write an interactive fiction story where the protagonist is a detective investigating a mysterious disappearance in a small town. Include at least three decision points where the reader can choose different paths for the story.",
                "scenario": "The story should be engaging, coherent, and maintain logical consistency across different paths. Each decision point should lead to a meaningful outcome that affects the direction of the story."
            },
            "2": {
                "prompt": "Write an interactive fiction story set in a fantasy world where the protagonist is a young wizard on a quest to find a legendary artifact. Include at least three decision points where the reader can choose different paths for the story.",
                "scenario": "The story should be engaging, coherent, and maintain logical consistency across different paths. Each decision point should lead to a meaningful outcome that affects the direction of the story."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate an engaging and coherent interactive fiction story based on the given prompt. Ensure that the story maintains logical consistency across different paths and includes at least three decision points where the reader can choose different paths for the story.\n\nPrompt:\n\"{t['prompt']}\"\n\nScenario:\n\"{t['scenario']}\"\n\nProvide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be engaging and coherent.",
            "The story should maintain logical consistency across different paths.",
            "The story should include at least three decision points where the reader can choose different paths.",
            "Each decision point should lead to a meaningful outcome that affects the direction of the story."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
