class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "intersection_layout": "A 4-way intersection with traffic coming from all directions. Initial traffic light cycle: 30 seconds green, 30 seconds red for each direction.",
                "traffic_pattern": "Heavy traffic from the north and south during rush hour (8-9 AM). Moderate traffic from the east and west during the rest of the day.",
                "objective": "Minimize the average wait time for vehicles."
            },
            "2": {
                "intersection_layout": "A 3-way intersection (T-junction) with traffic coming from the north, east, and west. Initial traffic light cycle: 20 seconds green, 20 seconds red for each direction.",
                "traffic_pattern": "Moderate traffic from all directions, with occasional heavy traffic from the east in the evening (5-6 PM).",
                "objective": "Minimize the total delay for all vehicles."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        intersection_layout = t["intersection_layout"]
        traffic_pattern = t["traffic_pattern"]
        objective = t["objective"]
        instructions = f"""Your task is to optimize the traffic light signals at the following intersection to achieve the given objective.

Intersection Layout: {intersection_layout}
Traffic Pattern: {traffic_pattern}
Objective: {objective}

Your response should include:
1. A detailed plan for the traffic light signal timings.
2. An explanation of how your plan addresses the given traffic pattern.
3. A rationale for how your plan minimizes congestion and meets the objective.

Provide your response in plain text format, ensuring that it is comprehensive and logically sound.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a detailed and coherent plan for the traffic light signal timings.",
            "The response should explain how the plan addresses the given traffic pattern.",
            "The response should provide a rationale for how the plan minimizes congestion and meets the objective.",
            "The response should be comprehensive and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
