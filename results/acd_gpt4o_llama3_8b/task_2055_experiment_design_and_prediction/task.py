class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "parameters": [
                    "You have a sample of plant seeds.",
                    "You want to test the effects of different light conditions on germination.",
                    "You have three light conditions: natural light, artificial light, and darkness.",
                    "You have 30 seeds in total.",
                    "You have 10 pots and soil."]
            },
            "2": {
                "parameters": [
                    "You have a chemical reaction between substance A and substance B.",
                    "You want to test the effect of temperature on the reaction rate.",
                    "You have three temperature conditions: 0°C, 25°C, and 50°C.",
                    "You have three identical reaction vessels.",
                    "You have a stopwatch and a thermometer."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        parameters = "\n".join(f"- {param}" for param in t["parameters"])
        return f"""Design a scientific experiment based on the following parameters and predict the outcomes. Ensure your experiment design is detailed and includes a clear method, controls, and variables. Then, provide a prediction of the outcomes based on your understanding of the scientific principles involved. Here are the parameters:\n{parameters}\n\nSubmit your response as a plain text string in the following format: 'Experiment Design: [Your experiment design]\nPrediction: [Your prediction]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The experiment design should be detailed and include a clear method, controls, and variables.", "The prediction should logically follow from the experiment design and scientific principles involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
