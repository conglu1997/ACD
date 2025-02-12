class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "conference", "days": 2, "sessions_per_day": 4, "constraints": ["Morning sessions should be 2 hours", "Afternoon sessions should be 1.5 hours", "Include a keynote speech on the first day morning", "Include a networking event on the second day evening"]},
            "2": {"event": "workshop", "days": 3, "sessions_per_day": 3, "constraints": ["Each session should last 3 hours", "Include a lunch break between sessions", "Include a hands-on activity in each session"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        days = t["days"]
        sessions_per_day = t["sessions_per_day"]
        constraints = t["constraints"]
        constraints_str = "; ".join(constraints)
        return f"""Create a detailed schedule for a {event} spanning {days} days. Each day should have {sessions_per_day} sessions. Follow these constraints: {constraints_str}. Ensure that the schedule is clear, logically sequenced, and feasible. Submit your schedule as a plain text string with each day and session clearly labeled. Format each day's schedule as follows:\nDay X: \nSession 1: description \nSession 2: description \n...\nSession N: description\nFor example: \nDay 1: \nSession 1: Opening remarks and introductions \nSession 2: Keynote speech \nSession 3: Panel discussion \nSession 4: Networking event."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The schedule should span the specified number of days.",
            "Each day should have the specified number of sessions.",
            "The schedule should respect the given constraints.",
            "The schedule should be clear, logically sequenced, and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
