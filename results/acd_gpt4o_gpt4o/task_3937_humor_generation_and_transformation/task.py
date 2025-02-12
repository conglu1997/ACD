class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "technology", "task": "generate"},
            "2": {"joke": "Why don't scientists trust atoms? Because they make up everything!", "style": "Shakespearean", "task": "transform"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'generate':
            return f"""Your task is to generate a joke based on the following topic:

Topic: {t['topic']}

Ensure your joke is humorous, coherent, and relevant to the topic. Avoid using common or overused jokes. Provide your joke in plain text format.

Desired format:
Joke: [Your joke]"""
        elif t['task'] == 'transform':
            return f"""Your task is to transform the following joke into the given style:

Original Joke: {t['joke']}
Target Style: {t['style']}

Ensure your transformed joke maintains the humor and meaning of the original joke but is presented in the target style. Avoid simply rephrasing the joke; instead, adapt it to fit the style authentically. Provide your transformed joke in plain text format.

Desired format:
Transformed Joke: [Your transformed joke]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'generate':
            criteria = [
                "The joke should be humorous and coherent.",
                "The joke should be relevant to the given topic.",
                "The joke should be original and not a common or overused joke."
            ]
        elif t['task'] == 'transform':
            criteria = [
                "The transformed joke should maintain the humor and meaning of the original joke.",
                "The transformed joke should be presented in the target style authentically.",
                "The transformed joke should not simply rephrase the original joke but adapt it to the new style."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
