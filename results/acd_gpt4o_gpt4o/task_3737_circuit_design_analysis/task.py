class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specifications": "Design a simple series circuit with a total resistance of 10 ohms and a total voltage of 5V. Specify the values of at least two resistors and the current through the circuit.",
                "parameters": ["Ohm's Law", "Series Circuits", "Resistor Values"]
            },
            "2": {
                "specifications": "Analyze the given parallel circuit and calculate the total resistance, current through each branch, and the voltage across each resistor. The circuit consists of a 12V battery and three resistors with values of 4 ohms, 6 ohms, and 12 ohms.",
                "parameters": ["Ohm's Law", "Parallel Circuits", "Resistor Values"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to {t['specifications']}

Make sure to use the relevant principles of electrical engineering, such as Ohm's Law and the laws governing series and parallel circuits. Provide your response in plain text format, structured as follows:

1. Circuit Diagram (optional, described in text format if included)
2. Calculations
3. Final Values

Ensure your analysis and design are accurate and adhere to the given specifications. If you include a circuit diagram, describe it clearly in text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design/analysis should adhere to the given specifications.",
            "The calculations should be accurate and follow electrical engineering principles.",
            "The final values should match the specified requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
