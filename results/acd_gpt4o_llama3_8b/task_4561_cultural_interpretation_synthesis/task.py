class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artifact": "A painting by Vincent van Gogh: The Starry Night", "task": "Write a short story inspired by the painting, capturing its mood and atmosphere."},
            "2": {"artifact": "A traditional Japanese tea ceremony", "task": "Compose a poem that reflects the principles and aesthetics of the tea ceremony."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        artifact = t['artifact']
        task = t['task']
        return f"""You are given the following cultural artifact: {artifact}.

Your task is to {task}

Submit your response as a plain text string in the following format:

Response: [Your creative content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should creatively interpret the given cultural artifact.",
            "The response should be coherent and maintain the mood or principles of the artifact.",
            "The response should be well-structured and free from grammatical errors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
