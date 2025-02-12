class TaskFamily:
    import time

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "water_management", "initial_conditions": {"reservoir_level": 50, "incoming_flow": 10, "demand": 5, "time_limit": 60, "dynamic_conditions": {"time_intervals": [0, 10, 20, 30, 40, 50, 60], "incoming_flow": [10, 15, 20, 10, 5, 8, 12], "demand": [5, 10, 8, 6, 4, 7, 9]} }},
            "2": {"scenario": "energy_grid_management", "initial_conditions": {"grid_load": 100, "production": 120, "demand": 110, "time_limit": 60, "dynamic_conditions": {"time_intervals": [0, 10, 20, 30, 40, 50, 60], "production": [120, 130, 110, 115, 125, 130, 120], "demand": [110, 120, 105, 100, 115, 125, 110]} }}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["scenario"] == "water_management":
            instructions = f"""Your task is to manage the water levels in a reservoir to ensure that the demand is met without overflowing. You will receive real-time updates on the incoming flow, demand, and current reservoir level. You have 60 seconds to make decisions and maintain the balance.

Initial Conditions:
- Reservoir Level: {t['initial_conditions']['reservoir_level']} units
- Incoming Flow: {t['initial_conditions']['incoming_flow']} units per second
- Demand: {t['initial_conditions']['demand']} units per second
- Time Limit: {t['initial_conditions']['time_limit']} seconds

Dynamic Conditions (over time):
- Time Intervals: {t['initial_conditions']['dynamic_conditions']['time_intervals']}
- Incoming Flow: {t['initial_conditions']['dynamic_conditions']['incoming_flow']}
- Demand: {t['initial_conditions']['dynamic_conditions']['demand']}

Make decisions and submit your actions at each time interval in the format: 'Time: [Time Interval], Action: [Your Action]'. Your actions can be 'Increase Outflow', 'Decrease Outflow', or 'Maintain Outflow'. Provide your response in plain text format. Here is an example:

Time: 10, Action: Increase Outflow
Time: 20, Action: Decrease Outflow
Time: 30, Action: Maintain Outflow
"""
        else:
            instructions = f"""Your task is to manage the energy grid to ensure that the demand is met without overloading the grid. You will receive real-time updates on the grid load, production, and current demand. You have 60 seconds to make decisions and maintain the balance.

Initial Conditions:
- Grid Load: {t['initial_conditions']['grid_load']} units
- Production: {t['initial_conditions']['production']} units per second
- Demand: {t['initial_conditions']['demand']} units per second
- Time Limit: {t['initial_conditions']['time_limit']} seconds

Dynamic Conditions (over time):
- Time Intervals: {t['initial_conditions']['dynamic_conditions']['time_intervals']}
- Production: {t['initial_conditions']['dynamic_conditions']['production']}
- Demand: {t['initial_conditions']['dynamic_conditions']['demand']}

Make decisions and submit your actions at each time interval in the format: 'Time: [Time Interval], Action: [Your Action]'. Your actions can be 'Increase Production', 'Decrease Production', or 'Maintain Production'. Provide your response in plain text format. Here is an example:

Time: 10, Action: Increase Production
Time: 20, Action: Decrease Production
Time: 30, Action: Maintain Production
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include appropriate actions to manage the resource.", "The actions should be timely and based on changing conditions.", "The response should maintain the balance of the resource, avoiding overflow or overload."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
