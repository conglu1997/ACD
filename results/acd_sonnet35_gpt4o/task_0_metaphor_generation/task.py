import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time", "love", "knowledge", "freedom", "happiness",
            "sadness", "anger", "fear", "hope", "creativity",
            "success", "failure", "justice", "peace", "wisdom"
        ]
        return {
            "1": {"concept": random.choice(concepts)},
            "2": {"concept": random.choice(concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a novel and insightful metaphor that compares the abstract concept of '{t['concept']}' to a concrete object or experience. Your metaphor should be expressed in a single sentence following the format '[Abstract concept] is [metaphor].' Be creative, avoid clichés, and do not use personification. For example, a good metaphor for 'knowledge' might be: 'Knowledge is a vast ocean, with depths yet to be explored and treasures waiting to be discovered.'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be a single sentence in the format '[Abstract concept] is [metaphor].'",
            "The metaphor should compare the given abstract concept to a concrete object or experience.",
            "The metaphor should be novel and insightful, avoiding common clichés.",
            "The metaphor should not use personification.",
            "The metaphor should illuminate some aspect of the abstract concept in a meaningful way."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
