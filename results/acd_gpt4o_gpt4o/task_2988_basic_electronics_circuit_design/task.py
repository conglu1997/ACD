class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "circuit": "A simple LED circuit with a switch",
                "components": ["1 x LED", "1 x Resistor (330 ohm)", "1 x Switch", "1 x 9V Battery", "Connecting wires"]
            },
            "2": {
                "circuit": "A basic series circuit with two resistors",
                "components": ["2 x Resistors (1k ohm)", "1 x 9V Battery", "Connecting wires"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to design and describe step-by-step instructions for assembling the given basic electronic circuit using the provided components. Ensure your instructions are clear, precise, and easy to follow. Include any necessary safety precautions and provide a brief explanation of how the circuit works.\n\nCircuit: {t['circuit']}\nComponents: {', '.join(t['components'])}\n\nGuidelines:\n1. List all components and tools needed.\n2. Provide step-by-step assembly instructions.\n3. Describe any safety precautions.\n4. Briefly explain how the circuit operates.\n\nExample Response:\n1. List of components and tools:\n   - 1 x LED\n   - 1 x Resistor (330 ohm)\n   - 1 x Switch\n   - 1 x 9V Battery\n   - Connecting wires\n   - Soldering iron (if needed)\n2. Step-by-step instructions:\n   - Step 1: Connect the positive terminal of the 9V battery to one terminal of the switch using a connecting wire.\n   - Step 2: Connect the other terminal of the switch to the anode (longer leg) of the LED.\n   - Step 3: Connect the cathode (shorter leg) of the LED to one end of the resistor.\n   - Step 4: Connect the other end of the resistor to the negative terminal of the 9V battery.\n3. Safety precautions:\n   - Ensure the battery is disconnected while assembling the circuit.\n   - Handle the LED and resistor carefully to avoid damage.\n4. Explanation:\n   - When the switch is closed, current flows from the battery through the switch, LED, and resistor, causing the LED to light up. The resistor limits the current to protect the LED."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions are clear and precise.",
            "All components and tools are listed.",
            "Safety precautions are included.",
            "The operation of the circuit is correctly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
