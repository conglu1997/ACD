class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the captain of a spaceship that is rapidly losing oxygen. You have to make immediate decisions to save the crew. You have three choices: (A) Seal off the damaged compartment, risking the lives of the crew inside, (B) Initiate emergency repairs, which may fail, or (C) Evacuate the spaceship, which has a limited number of escape pods. You have 60 seconds to decide.",
                "instructions": "Make a quick decision based on the given scenario. Justify your decision briefly. You have 60 seconds to respond. Submit your response as a plain text string in the following format: 'Decision: [Your decision] Justification: [Your justification]'"
            },
            "2": {
                "scenario": "You are the manager of a restaurant during a sudden power outage. You must decide how to handle the situation with customers and perishable food at risk. You have three choices: (A) Close the restaurant and ask customers to leave, (B) Continue operations using backup generators, risking food spoilage, or (C) Offer limited cold menu items that do not require cooking. You have 45 seconds to decide.",
                "instructions": "Make a quick decision based on the given scenario. Justify your decision briefly. You have 45 seconds to respond. Submit your response as a plain text string in the following format: 'Decision: [Your decision] Justification: [Your justification]'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Make a quick decision based on the following scenario. Justify your decision briefly. You have a limited amount of time to respond. Scenario: {t['scenario']} Submit your response as a plain text string in the following format: 'Decision: [Your decision] Justification: [Your justification]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a clear decision.",
            "The justification should be brief and relevant to the scenario.",
            "The decision should be made within the given time constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
