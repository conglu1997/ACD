class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a first responder at the scene of a severe car accident. One of the passengers is unconscious, not breathing, and has no pulse. Your task is to perform CPR on the passenger and provide detailed steps of the procedure, starting from when you first assess the situation until professional medical help arrives. Be sure to include checking the scene for safety, calling emergency services, and the specific steps of CPR.", "roles": {"first_responder": "You", "unconscious_passenger": "Passenger"}},
            "2": {"scenario": "You are a nurse in an emergency room where a patient arrives with symptoms of a heart attack, including chest pain, shortness of breath, and sweating. Your task is to administer the initial emergency treatment and list the steps you would take, starting from the moment the patient arrives until they are stabilized or further medical help is provided. Be sure to include initial assessment, vital signs monitoring, medication administration, and any necessary interventions.", "roles": {"nurse": "You", "patient": "Patient"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate the following emergency procedure scenario and provide a detailed step-by-step description of the actions you would take:

Scenario: {t['scenario']}

Roles:
{t['roles']}

Ensure that your response includes all critical steps in the procedure and follows the correct order. Your response should be clear, concise, and include each step numbered. Demonstrate an understanding of the emergency procedure.

Provide your response in plain text format, with each step numbered.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include all critical steps of the procedure.",
            "The steps should be in the correct order.",
            "The response should be clear and concise.",
            "The response should demonstrate an understanding of the emergency procedure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
