class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Observations: Plants A and B exposed to sunlight grow faster than Plants C and D kept in the dark. Details: All plants are of the same species and are watered equally."},
            "2": {"data": "Observations: Mice given a high-fat diet gain more weight than mice given a normal diet. Details: All mice are of the same age and are kept in identical conditions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a scientific hypothesis based on the given data and design an experiment to test it.

Data: {t['data']}

Your response should include:
1. A clear and concise hypothesis.
2. A detailed experimental design to test the hypothesis, including:
   - The independent and dependent variables
   - The control group and experimental group setup
   - The procedure to be followed
   - The type of data to be collected
3. An explanation of how the data will be analyzed to confirm or reject the hypothesis.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be clear and concise.",
            "The experimental design should include independent and dependent variables.",
            "The experimental design should include a control group and an experimental group setup.",
            "The procedure should be detailed and feasible.",
            "The type of data to be collected should be specified.",
            "The explanation of how the data will be analyzed should be clear and logical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
