class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a manager at a tech company. One of your employees, Alice, has been accused of leaking sensitive company information. She claims she did it to expose unethical practices within the company. Simulate a dialogue where you confront Alice about this situation and try to understand her perspective while considering the company's policies and ethical implications."},
            "2": {"scenario": "You are a doctor at a hospital. One of your patients, Bob, has refused a life-saving treatment due to his personal beliefs. Simulate a dialogue where you discuss his decision, trying to respect his beliefs while emphasizing the importance of the treatment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a dialogue based on the given ethical social scenario.

Scenario: {t['scenario']}

Roles: [appropriate roles based on the scenario]

Generate a coherent and contextually appropriate dialogue between the roles. Ensure that the responses are natural, reflect the context of the scenario, and maintain relevance throughout the dialogue. Provide your dialogue in plain text format with each line prefixed by the role (e.g., 'manager: Why did you leak the information?')."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
