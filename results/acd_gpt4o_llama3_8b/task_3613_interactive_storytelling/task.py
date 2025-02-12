class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Start a story set in a magical forest where a young wizard discovers an ancient artifact. The story should introduce the setting, main characters, and initial conflict. Then, adapt the story based on the following constraint: The artifact has a hidden curse that affects the wizard's powers in unexpected ways.",
                "constraint": "The artifact has a hidden curse that affects the wizard's powers in unexpected ways."
            },
            "2": {
                "prompt": "Begin a story in a futuristic city where a detective is investigating a series of mysterious disappearances. The story should introduce the setting, main characters, and initial conflict. Then, adapt the story based on the following constraint: The detective finds a clue that leads to a powerful corporation involved in illegal experiments.",
                "constraint": "The detective finds a clue that leads to a powerful corporation involved in illegal experiments."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and adapt a story based on the given prompt and constraint. Your response should include:
1. An engaging introduction that sets the scene, introduces main characters, and establishes the initial conflict.
2. A continuation of the story that incorporates the given constraint, ensuring narrative coherence and engagement.
3. Any additional details that enhance the story and make it compelling.

Prompt:
{t['prompt']}

Constraint:
{t['constraint']}

Submit your response in the following format:
Introduction: [Your engaging introduction]
Continuation: [Your continuation incorporating the constraint]
Details: [Any additional details]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The introduction should effectively set the scene, introduce main characters, and establish the initial conflict.",
            "The continuation should incorporate the given constraint in a coherent and engaging manner.",
            "The story should be compelling and maintain a logical narrative flow.",
            "The response should follow the specified format: Introduction, Continuation, Details."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
