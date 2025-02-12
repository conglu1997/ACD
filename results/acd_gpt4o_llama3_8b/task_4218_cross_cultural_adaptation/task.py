class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are attending a traditional Japanese tea ceremony. Describe your actions and responses to show respect and understanding of Japanese culture. Mention specific actions such as how you enter the room, how you interact with the host, and how you consume the tea."},
            "2": {
                "scenario": "You are a guest at an Indian wedding. Describe how you would dress, what gifts you would bring, and how you would behave to show respect for Indian traditions. Mention specific customs such as how you greet the hosts, participate in ceremonies, and interact with other guests."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a culturally appropriate response or content based on the following scenario:

Scenario: {t['scenario']}

Your response should demonstrate an understanding of the cultural norms and sensitivities involved. Submit your response as a plain text string in the following format:

Response: [Your detailed response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should demonstrate an understanding of the cultural norms and sensitivities relevant to the scenario.",
            "The actions and responses described should be appropriate and respectful within the cultural context.",
            "The response should mention specific actions or customs relevant to the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
