class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."},
            "2": {"excerpt": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        excerpt = t["excerpt"]
        return f"""Identify and explain the literary devices used in the following excerpt: '{excerpt}'. After identifying and explaining the devices, create a new example that employs each of those techniques. Ensure your explanations are clear and your new examples are creative and original. Submit your response as a plain text string with the following sections labeled: 'Identification', 'Explanation', and 'New Example'.

Example format:
Identification:
1. Literary device 1
2. Literary device 2

Explanation:
1. Explanation of literary device 1
2. Explanation of literary device 2

New Example:
1. New example using literary device 1
2. New example using literary device 2

Example response:
Identification:
1. Juxtaposition
2. Metaphor

Explanation:
1. Juxtaposition: Placing two contrasting elements together to highlight their differences.
2. Metaphor: A figure of speech that describes an object or action as something else, to highlight a particular quality.

New Example:
1. Juxtaposition: It was the darkest of nights, it was the brightest of days.
2. Metaphor: Her smile was a beacon of hope in the storm."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The literary devices should be correctly identified.",
            "The explanations should be clear and accurate.",
            "The new examples should creatively and correctly employ the identified techniques.",
            "The response should follow the provided format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
