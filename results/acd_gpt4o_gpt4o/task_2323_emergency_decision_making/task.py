class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "hospital_fire", "constraints": {"time_limit": "5 minutes", "resources": ["fire extinguishers", "evacuation routes"], "priorities": ["patient safety", "fire containment"]}},
            "2": {"scenario": "flooded_city", "constraints": {"time_limit": "10 minutes", "resources": ["boats", "helicopters"], "priorities": ["rescue stranded people", "prevent further flooding"]}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['scenario'] == 'hospital_fire':
            return f"""Your task is to make optimal decisions to handle a fire emergency in a hospital. You have the following constraints and priorities:

Time Limit: {t['constraints']['time_limit']}
Resources: {', '.join(t['constraints']['resources'])}
Priorities: {', '.join(t['constraints']['priorities'])}

Ensure that your decisions are coherent, prioritize the given constraints, and address the priorities. Provide your response in plain text format as a series of decisions and actions."""
        elif t['scenario'] == 'flooded_city':
            return f"""Your task is to make optimal decisions to handle a flood emergency in a city. You have the following constraints and priorities:

Time Limit: {t['constraints']['time_limit']}
Resources: {', '.join(t['constraints']['resources'])}
Priorities: {', '.join(t['constraints']['priorities'])}

Ensure that your decisions are coherent, prioritize the given constraints, and address the priorities. Provide your response in plain text format as a series of decisions and actions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['scenario'] == 'hospital_fire':
            criteria.append("The decisions should prioritize patient safety and fire containment.")
            criteria.append("The decisions should make effective use of the given resources.")
        elif t['scenario'] == 'flooded_city':
            criteria.append("The decisions should prioritize rescuing stranded people and preventing further flooding.")
            criteria.append("The decisions should make effective use of the given resources.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
