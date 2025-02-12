class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'task_type': 'creation',
                'scenario': 'A group of aliens visits Earth for the first time and decides to attend a human wedding.'
            },
            '2': {
                'task_type': 'interpretation',
                'joke': 'Why don’t scientists trust atoms? Because they make up everything!'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'creation':
            return f"""Your task is to create a humorous story based on the following scenario:\n\nScenario: {t['scenario']}\n\nEnsure that your story is funny and engages the reader. Your response should be in plain text format."""
        elif t['task_type'] == 'interpretation':
            return f"""Your task is to interpret the humor in the following joke:\n\nJoke: {t['joke']}\n\nExplain why this joke is funny and what makes it humorous. Your response should be in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'creation':
            criteria = ["The story should be humorous.", "The scenario should be clearly incorporated into the story.", "The story should be engaging and well-written."]
        elif t['task_type'] == 'interpretation':
            criteria = ["The explanation should accurately interpret the humor in the joke.", "The explanation should be clear and well-articulated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
