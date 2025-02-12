class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Two friends, Alex and Jordan, have a disagreement over a missed appointment. Alex feels hurt that Jordan didn't show up, while Jordan feels overwhelmed with other responsibilities. Generate a detailed social interaction scenario describing their conversation and analyze the emotions and motivations of both characters."
            },
            "2": {
                "prompt": "A manager, Casey, has to give constructive feedback to an employee, Sam, who has been underperforming. Casey wants to be supportive but also needs to address the issues. Generate a detailed social interaction scenario describing their conversation and analyze the emotions and motivations of both characters."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed social interaction scenario based on the following prompt. Ensure that the interaction is realistic and captures the emotional dynamics between the characters. After generating the scenario, analyze the emotions and motivations of each character involved. Your response should include the following sections: Scenario, Emotional Analysis. Here is the prompt:

{t["prompt"]}

Submit your response as a plain text string with each section clearly labeled."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a detailed and realistic scenario.",
            "The emotional analysis should accurately reflect the emotions and motivations of the characters.",
            "Each section should be clearly labeled as Scenario and Emotional Analysis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
