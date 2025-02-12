class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "experiment": "A plant growth experiment is conducted with two sets of plants. Set A is watered with pure water, while Set B is watered with a nutrient solution. Both sets are kept under identical light and temperature conditions. After 2 weeks, the height of the plants is measured."
            },
            "2": {
                "experiment": "A chemical reaction experiment is conducted by mixing two clear solutions, Solution X and Solution Y, in a beaker. The beaker is then placed on a magnetic stirrer to ensure thorough mixing. After 5 minutes, the temperature of the mixture is measured. Solution X contains an exothermic reactant while Solution Y is a catalyst."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following scientific experiment and predict the likely outcome:

Experiment: {t['experiment']}

Your response should include:
1. A brief description of the experiment.
2. The scientific principles involved in the experiment.
3. A prediction of the likely outcome based on the given data and principles.
4. An explanation of the reasoning behind your prediction.

Ensure that your response is thorough, well-reasoned, and demonstrates a deep understanding of the scientific context. Submit your response as a plain text string in the following format:

Description: [Your brief description]
Principles: [Scientific principles involved]
Prediction: [Your predicted outcome]
Reasoning: [Explanation of your reasoning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a brief description of the experiment.",
            "The response should explain the scientific principles involved.",
            "The response should provide a prediction of the likely outcome.",
            "The response should include a well-reasoned explanation of the prediction."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
