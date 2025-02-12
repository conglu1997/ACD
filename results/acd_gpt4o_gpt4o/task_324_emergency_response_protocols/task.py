class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "scenario": "fire in a residential building", "criteria": "The instructions should include steps for alerting residents, contacting emergency services, evacuating the building, and providing first aid."},
            "2": {"task_type": "interpret", "protocol": "1. Alert all residents immediately. 2. Contact emergency services (dial 911). 3. Evacuate the building using the nearest fire exits. 4. Assist those with disabilities. 5. Provide first aid to those in need. 6. Do not re-enter the building until cleared by authorities.", "question": "What should be done after alerting residents?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            instructions = f"""Your task is to generate detailed instructions for handling the following emergency situation:

Scenario: {t['scenario']}

Ensure your instructions include steps for alerting residents, contacting emergency services, evacuating the building, and providing first aid. Provide your instructions in plain text format, with each step clearly labeled. For example:

1. Alert all residents immediately by activating the fire alarm.
2. Contact emergency services (dial 911) and provide them with the necessary details.
3. Evacuate the building using the nearest fire exits, ensuring everyone is aware of the evacuation routes.
4. Assist those with disabilities or those who require help in evacuating.
5. Provide first aid to anyone who is injured, if it is safe to do so.
6. Do not re-enter the building until it has been cleared by the authorities."""
        else:
            instructions = f"""Your task is to interpret the following emergency protocol and answer the question based on the information provided:

Protocol: {t['protocol']}

Question: {t['question']}

Provide your answer in plain text format, clearly stating the steps to be taken after alerting residents."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            criteria = ["The instructions should include steps for alerting residents, contacting emergency services, evacuating the building, and providing first aid.", "The instructions should be clear, actionable, and formatted with each step clearly labeled."]
        else:
            criteria = ["The response should correctly identify the steps to be taken after alerting residents."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
