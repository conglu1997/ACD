class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event_descriptions": [
                    "The signing of the Magna Carta in 1215.",
                    "The American Declaration of Independence in 1776."
                ]
            },
            "2": {
                "event_descriptions": [
                    "The fall of the Berlin Wall in 1989.",
                    "The end of Apartheid in South Africa in 1994."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and explain the connections between the following historical events:

Event Descriptions:
{chr(10).join('- ' + event for event in t['event_descriptions'])}

Your explanation should include detailed reasoning on how these events are connected, considering their historical context, causes, and consequences. Submit your response as a plain text string in the following format:

Connections: [Your detailed explanation here]

Example response format:
Connections: The signing of the Magna Carta influenced the development of constitutional law, which later inspired the American Declaration of Independence. Both events mark significant steps towards the establishment of individual rights and the limitation of governmental power."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be detailed and coherent.",
            "The explanation should accurately connect the given historical events.",
            "The reasoning should consider historical context, causes, and consequences."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
