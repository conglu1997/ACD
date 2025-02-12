class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Design a protocol for a hospital's emergency department to handle a sudden influx of patients during a natural disaster. The protocol should include steps for triage, resource allocation, and patient management.",
                "evaluation": "Evaluate the following protocol for a fire drill in a school. Identify any potential weaknesses and suggest improvements:\n1. Sound the alarm and ensure all students evacuate immediately.\n2. Teachers should guide students to the nearest exit in an orderly manner.\n3. Once outside, teachers should take attendance and report any missing students to the principal.\n4. The principal should coordinate with emergency services and ensure the safety of all students and staff."
            },
            "2": {
                "scenario": "Design a protocol for a remote company's onboarding process for new employees. The protocol should include steps for equipment setup, account creation, and initial training.",
                "evaluation": "Evaluate the following protocol for a library's book return system. Identify any potential weaknesses and suggest improvements:\n1. Patrons should return books to the designated return bin.\n2. Library staff should empty the return bin at the end of each day and scan the returned books.\n3. Staff should check for any damage to the books and sort them accordingly.\n4. Books should be reshelved by staff based on their category and location."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have two tasks:\n\nTask 1: Design a Protocol\nScenario: {t['scenario']}\n\nDesign a detailed protocol for the given scenario. Make sure to include all necessary steps and considerations to ensure the protocol is effective. Submit your protocol as a plain text string.\n\nTask 2: Evaluate a Protocol\nEvaluation: {t['evaluation']}\n\nEvaluate the given protocol. Identify any potential weaknesses and suggest improvements. Ensure your evaluation is thorough and well-reasoned. Submit your evaluation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The designed protocol should be detailed and logically structured.",
            "The designed protocol should address all key aspects of the scenario.",
            "The evaluation should identify potential weaknesses in the given protocol.",
            "The evaluation should suggest reasonable and effective improvements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
