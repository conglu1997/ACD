class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "Once upon a time, in a small village, there lived a kind-hearted girl named Lily. She loved to help everyone in the village. One day, she found a mysterious old map that led to a hidden treasure. She decided to follow the map, and after a long journey, she found the treasure chest. As she was about to open it, she heard a strange noise behind her..."},
            "2": {"story": "In a bustling city, there was a young detective named Jack who was known for solving the toughest cases. One evening, he received an anonymous tip about a planned heist at the city's largest bank. Jack decided to investigate and after piecing together various clues, he found himself face-to-face with the mastermind behind the heist. Just as he was about to make an arrest, the lights went out..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an alternate ending for the following story. Ensure that the new ending is coherent with the established narrative and maintains the characters' consistency and the setting's integrity.

{t['story']}

Submit your response as a continuation of the story. Format your response as a plain text string in the following format: 'Alternate Ending: [Your alternate ending]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alternate ending should be coherent with the established narrative.", "The alternate ending should maintain the characters' consistency.", "The alternate ending should maintain the setting's integrity.", "The response should be a continuation of the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
