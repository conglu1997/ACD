class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You have a budget of $1000 to organize a community event. The event must include food, entertainment, and decorations. Additionally, you need to ensure there is enough seating for 100 people and a contingency fund of at least $100. Provide a detailed allocation of your budget to cover these aspects, ensuring that the event is enjoyable for attendees. Include the cost for each aspect and justify your allocation."
            },
            "2": {
                "scenario": "You are managing a team of 5 people for a software development project with a tight deadline of 2 weeks. Allocate the tasks among the team members to maximize efficiency and ensure the project is completed on time. Consider the skills and expertise of each team member in your allocation and provide a detailed plan. Additionally, ensure there is a daily progress review meeting and a buffer time of 2 days for unexpected delays."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Allocate the given resources to achieve the specified goals in the following scenario:

Scenario: {t['scenario']}

Provide a detailed allocation plan, including justifications for your decisions. Ensure that your plan is logical, efficient, and feasible. Submit your response as a plain text string with the following format:

Allocation Plan: [Your detailed allocation plan here]
Justification: [Your justification for the allocation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The allocation plan should be logical, efficient, and feasible.", "The justification should clearly explain the reasoning behind the allocation decisions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
