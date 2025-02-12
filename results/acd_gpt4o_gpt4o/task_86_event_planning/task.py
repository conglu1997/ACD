class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "Plan a wedding", "constraints": "Budget: $10,000, Time: 6 months, Venue: Outdoor, Guests: 100, Must include: Catering, Music, Photography"},
            "2": {"goal": "Organize a corporate conference", "constraints": "Budget: $50,000, Time: 3 months, Venue: Conference hall, Attendees: 300, Must include: Keynote speaker, Catering, Networking sessions"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to plan a sequence of activities to achieve the following goal:

Goal: {t['goal']}

Constraints: {t['constraints']}

Ensure that your plan is detailed, feasible, and considers all given constraints. Provide your plan in a step-by-step format, including any necessary justifications for your decisions. Your response should include:
1. A list of major activities
2. A timeline for each activity
3. A budget allocation for each major aspect
4. Justifications for your decisions

Provide your response in the following format:

Major Activities:
- [Activity 1]
- [Activity 2]
...

Timeline:
- [Activity 1]: [Time period]
- [Activity 2]: [Time period]
...

Budget Allocation:
- [Aspect 1]: [Amount]
- [Aspect 2]: [Amount]
...

Justifications:
- [Justification for Activity/Aspect 1]
- [Justification for Activity/Aspect 2]
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be detailed and feasible.",
            "The plan should consider all given constraints.",
            "The plan should be presented in a step-by-step format.",
            "The plan should include justifications for decisions.",
            "The plan should cover all major aspects specified in the constraints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
