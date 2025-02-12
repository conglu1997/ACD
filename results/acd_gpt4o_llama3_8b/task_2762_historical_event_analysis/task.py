class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "prompt": "Analyze the key factors that led to the signing of the Declaration of Independence and discuss its immediate impact on the American colonies."},
            "2": {"event": "The fall of the Berlin Wall in 1989.", "prompt": "Discuss the political and social implications of the fall of the Berlin Wall and hypothesize how the world might be different if the Berlin Wall had never fallen."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        prompt = t["prompt"]
        return f"""Analyze the following historical event and respond to the prompt provided:

Event: {event}

Prompt: {prompt}

Your response should be detailed, well-reasoned, and demonstrate a deep understanding of the historical context and its implications. If the prompt asks for a hypothetical scenario, ensure that it is plausible and consistent with historical facts. Submit your response as a plain text string in the following format:

Response: [Your detailed response here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
