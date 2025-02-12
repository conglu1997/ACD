class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "destination": "Paris, France",
                "preferences": "art museums, historical landmarks, local cuisine, and a day trip outside the city",
                "constraints": "3 days, budget of $1000, travel by public transport"
            },
            "2": {
                "destination": "Kyoto, Japan",
                "preferences": "temples, gardens, traditional tea houses, and a cultural performance",
                "constraints": "5 days, budget of $1500, include at least one guided tour"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a comprehensive travel itinerary for a trip to {t['destination']}. Consider the following preferences and constraints:
- Preferences: {t['preferences']}
- Constraints: {t['constraints']}

Your itinerary should include daily activities, estimated costs, and brief descriptions of each point of interest. Ensure that your plan is practical, feasible, and within the budget. Provide your response in the following format:

Day 1:
- Activity 1: [Description, Cost]
- Activity 2: [Description, Cost]

Day 2:
- Activity 1: [Description, Cost]
- Activity 2: [Description, Cost]

..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The itinerary should include daily activities.",
            "Each activity should have a brief description and an estimated cost.",
            "The plan should be practical and feasible within the given constraints.",
            "The total cost should not exceed the budget."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
