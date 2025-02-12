class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A loud, continuous noise like that of an engine running.", "categories": ["Engine noise", "Bird chirping", "Water flowing", "People talking"]},
            "2": {"situation": "A calm evening by the beach.", "requirement": "Describe the sounds you would expect to hear in this situation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            return f"""Match the following sound description to the most appropriate category:

Description: {t['description']}

Categories: {', '.join(t['categories'])}

Submit your response in the following format:
Matched Category: [Your selected category]"""
        else:
            return f"""Generate a plausible sound description for the following situation:

Situation: {t['situation']}

Requirement: {t['requirement']}

Submit your response in the following format:
Sound Description: [Your sound description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = ["The response should correctly match the given sound description to one of the provided categories."]
        else:
            criteria = ["The sound description should be plausible and contextually appropriate for the given situation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
