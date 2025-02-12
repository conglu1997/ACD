class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": ["Alice wakes up late due to her alarm not ringing.", "She rushes to get ready for work, skipping breakfast.", "She misses her usual bus by just a few seconds.", "Frustrated, she decides to walk to work despite the long distance.", "On the way, she encounters an old friend she hasn't seen in years."], "title": "A Morning Adventure"},
            "2": {"events": ["John impulsively buys a lottery ticket at a convenience store.", "He forgets about the ticket and leaves it in a drawer.", "Months later, while cleaning, he finds the ticket and remembers the lottery.", "Excited, he checks the numbers against the winning ones online.", "To his amazement, he realizes he has won the jackpot, changing his life forever."], "title": "A Stroke of Luck"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events = "\n\n".join(t["events"])
        title = t["title"]
        instructions = f"""Your task is to create a coherent and engaging narrative based on the following sequence of events:\n\n{events}\n\nTitle: {title}\n\nEnsure that the narrative logically follows from the given events and includes appropriate details to make the story engaging. Provide your response in plain text format in the following structure:\n\n1. Title: {title}\n2. Narrative: <Your narrative>\n\nEnsure your narrative is detailed and includes logical connections between the events."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should logically follow from the given sequence of events.",
            "The narrative should be coherent and engaging.",
            "The narrative should include appropriate details to enhance the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
