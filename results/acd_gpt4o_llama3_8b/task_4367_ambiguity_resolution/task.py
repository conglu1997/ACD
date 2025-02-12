class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a detective trying to solve a case with the following clues: A witness saw a red car speeding away from the scene. Another witness mentioned hearing a loud noise before seeing a person running. The scene of the incident has a broken window and a misplaced chair. Describe your theory of what happened and provide a possible sequence of events. Consider potential motives, actions of individuals involved, and any other relevant details."
            },
            "2": {
                "scenario": "You are an archaeologist interpreting an ancient text with missing fragments. The text reads: 'In the year of the great flood, the kingdom of [missing] was submerged. The people fled to the mountains, carrying with them [missing]. They left behind their [missing], which were later discovered by [missing] explorers.' Fill in the missing fragments with plausible words or phrases and provide a brief explanation for each choice. Consider historical context, cultural artifacts, and any other relevant details."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scenario' in t:
            return f"""Interpret the following scenario and provide your response based on the given information:

Scenario: {t['scenario']}

Ensure that your interpretation is logical and creative. Submit your response as a plain text string in the format:

Interpretation:
[Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should be logical based on the given clues.", "The interpretation should demonstrate creativity in filling gaps in information.", "The response should include a coherent sequence of events or plausible explanations for the missing fragments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
