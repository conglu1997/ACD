class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_problem": "You have 10 liters of water and three containers with capacities of 7 liters, 4 liters, and 3 liters. How can you measure out exactly 5 liters?", "new_constraint": "One of the containers can no longer be used. Choose and specify which container, then solve the problem again."},
            "2": {"initial_problem": "You need to arrange a meeting for 5 people with different availabilities. The available time slots are: A: 9-10 AM, B: 10-11 AM, C: 11-12 PM, D: 1-2 PM, E: 2-3 PM. Find a suitable time slot for all participants.", "new_constraint": "One participant's availability changes. Person A is now only available from 11-12 PM. Recalculate the meeting time."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Task: Solve the following problem and then adapt your solution when a new constraint is introduced.\nInitial Problem: {t['initial_problem']}\nNew Constraint: {t['new_constraint']}\n\nResponse Format:\n1. Initial Solution: [Your solution to the initial problem]\n2. Adapted Solution: [Your solution after applying the new constraint]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The initial problem should be solved correctly.",
            "The solution should adapt correctly to the new constraint.",
            "The response should clearly specify the chosen container in Task 1 or the recalculated time slot in Task 2.",
            "The response should follow the specified format: 1. Initial Solution, 2. Adapted Solution.",
            "The adapted solution should logically follow from the new constraint applied to the initial problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
