class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specification": "Design a simple circuit to light up an LED using a 9V battery. Include a resistor to protect the LED from burning out.",
                "components": ["9V battery", "LED", "resistor", "wires"]
            },
            "2": {
                "specification": "Design a circuit with a switch to control a motor using a 12V power supply. Ensure the motor stops when the switch is off.",
                "components": ["12V power supply", "motor", "switch", "wires"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an electrical circuit based on the following specification and components.

Specification: {t['specification']}

Components: {', '.join(t['components'])}

Your response should include:
1. A detailed textual description of the circuit diagram, explaining how to connect each component. Ensure your description is logically sequenced, easy to follow, and free of ambiguous or redundant information.
2. A clear explanation of how the circuit works, including the role of each component.

Submit your response as a plain text string in the following format:

Circuit Diagram Description: [Your textual description of the circuit diagram]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The textual description of the circuit diagram should be detailed, accurate, and logically sequenced, including all specified components.",
            "The explanation should clearly describe how the circuit works and the role of each component."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
