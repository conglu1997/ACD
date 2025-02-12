class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Plan a corporate team-building retreat for 50 employees. The retreat should last for 3 days and include activities that promote teamwork and communication. Provide a detailed schedule and outline including location, activities, and any necessary materials or preparations. Ensure the plan includes at least one outdoor activity, one indoor workshop, and one team-building game."},
            "2": {"prompt": "Organize a charity fundraiser gala for a local non-profit organization. The event should include a dinner, a silent auction, and live entertainment. Provide a detailed plan including the venue, menu, entertainment, auction items, and a timeline of the event. Ensure the plan includes a theme for the gala, a list of potential sponsors, and a promotional strategy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to plan and manage the following event. Provide a detailed outline and schedule, including all necessary elements to ensure the event is successful. Your plan should be creative, practical, and well-organized. The response should include:

1. Event name and theme
2. Detailed schedule and timeline
3. Venue and setup arrangements
4. Activities and materials needed
5. Any additional creative elements to enhance the event

{t['prompt']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be detailed and well-organized.",
            "The plan should include all necessary elements such as location, schedule, and materials.",
            "The plan should be practical and feasible.",
            "The plan should include creative elements to enhance the event.",
            "The plan should promote the specific goals of the event (e.g., teamwork for a retreat, fundraising for a gala).",
            "The plan should include the required constraints (e.g., specific activities for the retreat, theme and promotional strategy for the gala)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
