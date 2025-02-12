class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "In a distant kingdom, a king declared that anyone who could solve his riddle would receive half of his kingdom. A poor farmer successfully solved the riddle and was promised the land. However, the next day, the king stated that the farmer must first defeat a dragon to claim his prize. The farmer, with no prior experience or training, miraculously defeated the dragon without any help. Additionally, the kingdom had a strict law that no one was allowed to kill dragons as they were considered sacred.", "type": "identify"},
            "2": {"story": "In a futuristic city, a scientist developed a time machine that could only travel to the past. She used the machine to prevent a catastrophic event, but upon returning, she realized that the event never happened and the machine had no record of her travel. However, her assistant claimed to have witnessed the event and the travel process. Furthermore, the scientist found herself carrying an object from the future that she had not taken with her initially.", "type": "solve"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "identify":
            return f"""Your task is to identify any logical inconsistencies in the following fictional story: {t["story"]}. Provide a clear explanation of the inconsistencies in 2-3 sentences."""
        else:
            return f"""Your task is to solve the logical inconsistencies in the following fictional story: {t["story"]}. Provide a plausible correction or explanation that resolves the inconsistencies in 2-3 sentences."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "identify":
            criteria = ["The response should clearly identify all logical inconsistencies in the story."]
        else:
            criteria = ["The response should provide a plausible correction or explanation that resolves all logical inconsistencies in the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
