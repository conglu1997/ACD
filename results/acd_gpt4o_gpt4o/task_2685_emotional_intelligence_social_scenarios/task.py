class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Jane was excited about her promotion at work. She shared the news with her friend Mark, but Mark seemed distracted and didn't respond enthusiastically."},
            "2": {"scenario": "During a team meeting, Alex proposed a new project idea. The team leader, Sarah, smiled and nodded, but some team members exchanged glances and whispered to each other."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and analyze the emotional and social cues in the given scenario. Here is the scenario: '{t["scenario"]}'. Provide a detailed response that includes:

1. The emotions and feelings of the main characters involved.
2. The social dynamics at play in the scenario.
3. Possible reasons for the characters' behaviors and reactions.
4. Any advice or suggestions for handling the situation better in the future."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly identify the emotions and feelings of the main characters.",
            "The submission should accurately analyze the social dynamics in the scenario.",
            "The submission should provide plausible reasons for the characters' behaviors and reactions.",
            "The advice or suggestions should be relevant and constructive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
