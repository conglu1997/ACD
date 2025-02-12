class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "story_segment": "Once upon a time, in a small village nestled between rolling hills, there lived a young girl named Elara who had a special gift. She could communicate with animals. One day, while exploring the forest, she stumbled upon a wounded fox."
            },
            "2": {
                "story_segment": "In the bustling city of Metropolis, where skyscrapers kissed the clouds, Detective Harris was known for his sharp mind and keen instincts. Late one evening, as he was about to leave his office, a mysterious envelope was slipped under his door."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the beginning of a story. Your task is to continue the story in a coherent and engaging manner. Ensure that the continuation aligns with the initial segment and maintains the narrative flow.

Story Segment: {t['story_segment']}

Submit your continuation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should be coherent and maintain the narrative flow.",
            "The continuation should be engaging and align with the initial story segment.",
            "The continuation should demonstrate creativity and contextual understanding."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
