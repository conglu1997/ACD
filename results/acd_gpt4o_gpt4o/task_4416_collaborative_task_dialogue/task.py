class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {'task': 'Plan a surprise birthday party for a mutual friend.', 'roles': ['Friend A', 'Friend B']},
            '2': {'task': 'Organize a project timeline for a team assignment.', 'roles': ['Team Leader', 'Team Member']}
        }
        assert len(tasks) == 2, 'There should be exactly two tasks.'
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a dialogue between two agents collaborating on the following task:

Task: {t['task']}
Roles: {', '.join(t['roles'])}

1. Ensure the dialogue is coherent and contextually appropriate.
2. Both agents should contribute meaningfully to the task.
3. The dialogue should lead to the completion of the task.

Provide the dialogue in plain text format, with each line prefixed by the agent’s role (e.g., Friend A: [utterance])."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ['The dialogue should be coherent and contextually appropriate.', 'Both agents should contribute meaningfully to the task.', 'The dialogue should lead to the completion of the task.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
