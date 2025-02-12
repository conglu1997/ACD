class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A wildfire is rapidly spreading towards a small town of 500 residents. You are in charge of the emergency response team with limited resources: 2 fire trucks, 1 helicopter, and 10 firefighters. The town has one main road leading out. Design a strategy to evacuate the town and contain the fire within the next 6 hours."},
            "2": {"scenario": "A Category 4 hurricane is expected to make landfall in 12 hours near a coastal city with a population of 100,000. You are in charge of the emergency response team with limited resources: 3 evacuation buses, 2 rescue boats, and 15 volunteers. The city has several low-lying areas prone to flooding. Design a strategy to evacuate the most vulnerable populations and secure essential infrastructure before the hurricane hits."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a time-sensitive strategy to manage the following emergency scenario, prioritizing actions and managing limited resources:\n{t['scenario']}\nSubmit your response in the following format:\nStrategy: [Your detailed strategy for managing the emergency, including prioritized actions and resource allocation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should address the main elements of the scenario (evacuation, containment, securing infrastructure).",
            "The strategy should demonstrate logical prioritization of actions and effective resource management.",
            "The response format should include a detailed strategy with clear, prioritized actions and resource allocation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
