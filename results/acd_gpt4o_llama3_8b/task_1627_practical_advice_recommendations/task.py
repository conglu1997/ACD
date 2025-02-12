class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are planning a week-long camping trip in a remote forest area. Provide a detailed list of essential items to pack, considering factors such as weather, safety, and sustenance."
            },
            "2": {
                "scenario": "You have been asked to organize a small wedding ceremony with a budget of $5000. Provide a detailed plan that includes venue, food, decorations, and any other necessary arrangements."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide practical advice and recommendations based on the following scenario:

{t['scenario']}

Ensure your advice is comprehensive, realistic, and takes into account all relevant factors. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The advice should be comprehensive and cover all relevant aspects of the scenario.",
            "The recommendations should be realistic and practical.",
            "The response should demonstrate an understanding of the scenario's context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
