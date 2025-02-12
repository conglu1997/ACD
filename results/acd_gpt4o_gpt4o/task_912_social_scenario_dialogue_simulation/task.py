class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are at a job interview. The interviewer asks you about a time you faced a challenge at work and how you handled it.", "roles": ["interviewer", "candidate"]},
            "2": {"scenario": "You are at a dinner party. A guest makes a controversial statement about politics. You decide to engage in a polite discussion.", "roles": ["guest1", "guest2"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a dialogue based on the given social scenario.

Scenario: {t['scenario']}

Roles: {', '.join(t['roles'])}

Generate a coherent and contextually appropriate dialogue between the roles. Ensure that the responses are natural, reflect the context of the scenario, and maintain relevance throughout the dialogue. Provide your dialogue in plain text format with each line prefixed by the role (e.g., 'interviewer: Tell me about a time you faced a challenge at work.')."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent and contextually appropriate.", "The responses should reflect the roles and context of the scenario.", "The dialogue should progress naturally and maintain relevance to the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
