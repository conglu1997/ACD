import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'event': 'The assassination of Julius Caesar in 44 BCE',
                'ethical_principle': 'Minimize violence and promote peaceful transitions of power'
            },
            {
                'event': 'The burning of the Library of Alexandria',
                'ethical_principle': 'Preserve knowledge and cultural heritage'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a time-traveling ethicist tasked with analyzing a historical event and proposing an ethical intervention. Your task is to address the following historical event:

{t['event']}

Your ethical guiding principle is: {t['ethical_principle']}

Provide your response in the following format:

1. Historical Context (2-3 sentences): Briefly describe the event and its historical significance.

2. Ethical Analysis (3-4 sentences): Analyze the ethical implications of the event, considering your guiding principle.

3. Proposed Intervention (3-4 sentences): Suggest a minimal intervention that aligns with your ethical principle. Explain how it would be implemented.

4. Potential Consequences (4-5 sentences): Discuss the potential short-term and long-term consequences of your intervention. Consider both positive and negative outcomes.

5. Ethical Justification (2-3 sentences): Justify your intervention from an ethical standpoint, addressing any potential criticisms.

Ensure your response is thoughtful, historically accurate, and ethically sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates accurate historical knowledge about the event.",
            "The ethical analysis is thoughtful and considers multiple perspectives.",
            "The proposed intervention is creative, minimal, and aligns with the given ethical principle.",
            "The analysis of potential consequences is comprehensive and considers both short-term and long-term effects.",
            "The ethical justification is well-reasoned and addresses potential criticisms."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
