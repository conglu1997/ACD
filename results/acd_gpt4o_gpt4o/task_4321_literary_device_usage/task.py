class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'prompt': 'Describe the morning sky using a metaphor.'},
            '2': {'prompt': 'Create a simile to describe a busy city street.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a literary device based on the following prompt. After generating the literary device, provide a brief explanation of why it is effective and how it enhances the description.

Prompt: {t['prompt']}

Your response should include:
1. A literary device (e.g., metaphor, simile, personification) related to the given prompt.
2. A brief explanation of why the literary device is effective.
3. An explanation of how the literary device enhances the description.

Ensure your literary device is creative and your explanations are comprehensive. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The response should include a creative and appropriate literary device related to the given prompt.',
            'The explanation of why the literary device is effective should be clear and concise.',
            'The explanation should clearly relate how the literary device enhances the description.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
