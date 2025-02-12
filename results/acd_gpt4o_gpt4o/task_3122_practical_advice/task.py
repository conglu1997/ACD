class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a team leader at a tech company, and two of your team members are having a conflict over the direction of a project. One member wants to adopt a new technology that the other member is unfamiliar with, causing tension and delays. Provide advice on how to resolve the conflict and ensure the project progresses smoothly."
            },
            "2": {
                "scenario": "You are a college student feeling overwhelmed by the amount of coursework and exams coming up. You have been procrastinating and now have multiple deadlines approaching. Provide advice on how to manage stress, overcome procrastination, and effectively organize your time."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to provide actionable and practical advice based on the given scenario. "
            "Ensure your advice is relevant, empathetic, and provides clear steps or strategies to address the situation. "
            "Your response should be at least 150 words long and cover all aspects of the scenario provided. "
            "Provide your response in plain text format, structured as follows:\n\n"
            "1. Summary of the situation\n"
            "2. Identification of key issues\n"
            "3. Detailed advice with actionable steps\n"
            "4. Conclusion"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The advice should be relevant to the given scenario.",
            "The advice should be empathetic, showing an understanding of the emotional aspects involved.",
            "The advice should provide clear, actionable steps or strategies to address the situation.",
            "The response should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
