class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Two friends are meeting at a café after not seeing each other for years. One of them has a secret they want to reveal during the conversation."
            },
            "2": {
                "scenario": "A mentor is advising their young protégé on how to handle a difficult decision at work. The protégé is uncertain and needs guidance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed and engaging dialogue script for the following scenario. Ensure that the dialogue is coherent, contextually appropriate, and captures the emotions and interactions between the characters. The script should include dialogue tags (e.g., 'John:') and should aim for a length of 300-500 words.

Scenario: {t['scenario']}

Provide your dialogue script in plain text format as follows:

[Character Name]: [Dialogue]
[Character Name]: [Dialogue]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent and contextually appropriate.", "The dialogue should capture the emotions and interactions between the characters."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
