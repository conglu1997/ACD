class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are tasked with planning a week-long vacation for a family of four. The family prefers a mix of relaxation and adventure activities. They have a budget of $5,000 and want to visit a location with both natural beauty and cultural attractions. Plan the itinerary, including accommodation, activities, and transportation. Ensure the plan stays within the budget and provides a balanced experience. Include specific details such as names of places, costs, and timing for each activity."},
            "2": {"scenario": "You are responsible for organizing a corporate retreat for a company with 50 employees. The retreat should include team-building activities, workshops, and leisure time. The budget is $20,000, and the retreat should last for three days. The location should be easily accessible and offer facilities for both professional and recreational activities. Provide a detailed plan that includes the schedule, activities, venue, and catering options. Include specific details such as names of venues, costs, and timing for each activity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Plan the following scenario: {t['scenario']} Submit your detailed plan as a plain text string in the following format:\n\n1. Introduction:\n- [Brief introduction to the scenario]\n\n2. Itinerary:\n- [Detailed day-by-day plan]\n\n3. Budget Breakdown:\n- [Detailed cost breakdown]\n\n4. Summary:\n- [Brief summary of how the plan meets the objectives]\n\nEnsure your plan is comprehensive, logically structured, and adheres to the given constraints."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be comprehensive and logically structured.",
            "The plan should adhere to the given constraints, including budget and duration.",
            "The plan should provide a balanced experience, considering the preferences and objectives.",
            "The plan should include all necessary details, such as accommodation, activities, transportation, and catering.",
            "The plan should include specific names, costs, and timing for each activity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
