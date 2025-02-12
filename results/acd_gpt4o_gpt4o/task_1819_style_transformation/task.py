class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "formal_to_informal", "text": "Dear Sir or Madam, I am writing to express my gratitude for your kind assistance during my recent visit to your establishment."},
            "2": {"type": "author_style", "text": "It was a bright cold day in April, and the clocks were striking thirteen.", "target_author": "J.K. Rowling"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'formal_to_informal':
            return f"""Your task is to transform the following passage from a formal style to an informal style:

{t['text']}

Ensure that you preserve the original meaning while making the text more casual and conversational. Here is an example transformation for a different passage:

Formal: 'I would like to request your assistance in this matter.'
Informal: 'Can you help me out with this?'

Provide your response in plain text format."""
        elif t['type'] == 'author_style':
            return f"""Your task is to rewrite the following passage in the style of {t['target_author']}:

{t['text']}

Ensure that you capture the stylistic nuances of the target author while preserving the original meaning. Here is an example transformation for a different passage:

Original: 'The sun set over the horizon, casting a warm glow over the landscape.'
Target Author (e.g., J.K. Rowling): 'As the sun dipped below the horizon, it bathed the landscape in a golden light, reminiscent of the enchanted evenings at Hogwarts.'

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'formal_to_informal':
            criteria.append("The text should be more casual and conversational while maintaining the original meaning.")
            criteria.append("The transformation should not alter any factual information or key details.")
        elif t['type'] == 'author_style':
            criteria.append("The text should capture the stylistic nuances of the target author and maintain the original meaning.")
            criteria.append("The transformation should use language and expressions characteristic of the target author.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
