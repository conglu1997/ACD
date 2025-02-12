class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You are organizing a conference with the following events: \n1. Keynote speech\n2. Workshop\n3. Networking session\n4. Panel discussion\n5. Closing remarks\nThe events must be scheduled in such a way that: \n- The keynote speech is the first event.\n- The workshop must happen before the networking session.\n- The panel discussion must happen after the workshop.\n- The closing remarks must be the last event.\nProvide a valid schedule for the events in the order they should occur."},
            "2": {"description": "You are planning a day trip with the following activities: \n1. Breakfast\n2. Museum visit\n3. Lunch\n4. Park walk\n5. Dinner\nThe activities must be scheduled in such a way that: \n- Breakfast is the first activity.\n- The museum visit must happen before lunch.\n- The park walk must happen after lunch but before dinner.\nProvide a valid schedule for the activities in the order they should occur."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following temporal reasoning problem. Arrange the events/activities in the correct order based on the given constraints. Provide your answer in plain text format as a list of events/activities in the correct order.\n\n{t['description']}\n\nFormat: [Event/Activity 1], [Event/Activity 2], [Event/Activity 3], [Event/Activity 4], [Event/Activity 5]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The schedule must satisfy all the given constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
