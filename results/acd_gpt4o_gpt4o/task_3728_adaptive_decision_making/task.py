class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "You are managing a rescue operation in a forest. Initially, you have a team of 5 people, 2 vehicles, and a medical kit. You receive information that there are 3 injured hikers in different locations, and a storm is approaching in 2 hours. Additionally, one of the vehicles breaks down, and you receive a call about a fourth injured hiker. Plan the rescue operation, considering the changing weather, limited resources, and new information. Provide your plan in plain text format."
            },
            "2": {
                "description": "You are organizing a large event in a city park. Initially, you have 10 volunteers, a budget of $5,000, and a main stage performer. You receive news that the main stage performer has canceled, there is a sudden increase in the number of attendees, and the sound system has malfunctioned. Adjust your event plan to accommodate these changes, ensuring the event's success. Provide your revised plan in plain text format."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to make real-time decisions based on the evolving scenario described below. Consider the initial conditions and any new information provided. Ensure your response is in plain text format and clearly outlines your plan or decision. Here is the scenario:\n\n{description}\n\nSubmit your response in plain text format. Your response should follow this structure:\n1. Initial Plan\n2. Adjusted Plan based on new information\n3. Justification for Adjustments""".format(description=t['description'])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate adaptability to new information.",
            "The response should be clear and logically consistent.",
            "The response should effectively address the evolving scenario and constraints.",
            "The response should follow the specified structure: Initial Plan, Adjusted Plan based on new information, Justification for Adjustments."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
