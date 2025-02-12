class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"emoji_sequence": "😊🌞🏖️", "message": "Feeling happy and relaxed at the beach.", "synthetic_examples": ["😢🌧️🏠 - Feeling sad and staying indoors.", "😡🔥💻 - Angry while working on the computer."]},
            "2": {"message": "A cat chasing a mouse.", "emoji_sequence": "🐱🐭🏃", "synthetic_examples": ["A dog barking at a stranger - 🐶👤🔊", "A person reading a book under a tree - 📖🌳👨"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'emoji_sequence' in t:
            examples = '\n'.join(t.get('synthetic_examples', []))
            return f"""Interpret the following sequence of emojis and describe the message they convey:

{t['emoji_sequence']}

Additional examples:
{examples}"""
        else:
            examples = '\n'.join(t.get('synthetic_examples', []))
            return f"""Generate a sequence of emojis to convey the following message:

{t['message']}

Additional examples:
{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'emoji_sequence' in t:
            criteria = [f"The response should accurately interpret the emoji sequence: {t['emoji_sequence']}"]
        else:
            criteria = [f"The emoji sequence should accurately convey the message: {t['message']}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
