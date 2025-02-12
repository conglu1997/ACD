class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a counselor helping a client through a difficult personal issue. The client is struggling with anxiety and stress due to work-related pressures. Engage in a dialogue with the client, offering support, asking relevant questions, and providing helpful advice. The conversation should be empathetic, supportive, and aim to help the client find practical solutions to manage their anxiety.", "client": "I don't know how to handle the pressure at work. It's overwhelming and I feel anxious all the time. What should I do?"},
            "2": {"scenario": "You are a detective interviewing a suspect in a theft case. The suspect has been accused of stealing a valuable item from a museum. Engage in a dialogue with the suspect, asking questions to gather information, assess their responses, and determine if they are telling the truth. The conversation should be thorough, logical, and aim to uncover the truth behind the theft.", "suspect": "I didn't steal anything from the museum. I was just there to look at the exhibits. You have the wrong person."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to engage in an interactive dialogue based on the given scenario. Ensure that your responses are coherent, relevant, and demonstrate emotional intelligence and decision-making skills. The dialogue should be detailed and aim to achieve the objective stated in the scenario. Format your response as follows:

1. Scenario: [The given scenario]
2. Dialogue:
[Your dialogue with the other party, including their responses and your replies]
""".format(t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent, relevant, and demonstrate emotional intelligence and decision-making skills. It should aim to achieve the objective stated in the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
