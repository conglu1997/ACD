class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about an unexpected friendship between a robot and a human.", "evaluation_criteria": ["The story should have a clear beginning, middle, and end.", "The characters should be well-developed.", "The plot should be engaging and coherent.", "The story should be at least 300 words long."]},
            "2": {"prompt": "Write a short story set in a post-apocalyptic world where hope is found in the most unlikely place.", "evaluation_criteria": ["The story should have a clear beginning, middle, and end.", "The setting should be vividly described.", "The plot should evoke emotions and be coherent.", "The story should be at least 300 words long."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Task: Write a creative story based on the following prompt.\nPrompt: {t['prompt']}\n\nEnsure your story meets the following criteria:\n- {t['evaluation_criteria'][0]}\n- {t['evaluation_criteria'][1]}\n- {t['evaluation_criteria'][2]}\n- {t['evaluation_criteria'][3]}\n\nResponse Format:\n[Your story]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t['evaluation_criteria']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
