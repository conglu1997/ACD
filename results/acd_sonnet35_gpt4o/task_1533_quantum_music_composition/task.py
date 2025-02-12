import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_gates = [
            {"name": "Hadamard", "symbol": "H", "effect": "Creates superposition"},
            {"name": "CNOT", "symbol": "CNOT", "effect": "Entangles qubits"},
            {"name": "Phase Shift", "symbol": "R", "effect": "Adjusts phase"}
        ]
        musical_elements = [
            {"name": "Pitch", "quantum_mapping": "Qubit state"},
            {"name": "Rhythm", "quantum_mapping": "Measurement timing"},
            {"name": "Harmony", "quantum_mapping": "Entanglement"}
        ]
        return {
            "1": {
                "quantum_gate": random.choice(quantum_gates),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "quantum_gate": random.choice(quantum_gates),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm for generating musical compositions using the {t['quantum_gate']['name']} gate ({t['quantum_gate']['symbol']}) to manipulate the {t['musical_element']['name']} element of music. The {t['quantum_gate']['name']} gate {t['quantum_gate']['effect']}, and the {t['musical_element']['name']} will be mapped to {t['musical_element']['quantum_mapping']}.

Your response should include:

1. Algorithm Design (250-300 words):
   a) Describe your quantum algorithm for music generation, explaining how it uses the specified quantum gate and musical element mapping.
   b) Provide a step-by-step explanation of how your algorithm works, including initialization, quantum operations, and measurement.
   c) Include a simple circuit diagram or pseudocode to illustrate your algorithm (describe it textually).

2. Musical Analysis (200-250 words):
   a) Explain how your algorithm's output translates into musical elements.
   b) Discuss the potential range of musical variations your algorithm can produce.
   c) Analyze how quantum principles like superposition and entanglement contribute to the musical output.

3. Quantum-Classical Integration (150-200 words):
   a) Describe how you would interface your quantum algorithm with classical music software or hardware.
   b) Discuss any challenges in translating quantum states to traditional musical notation.

4. Creative Applications (150-200 words):
   a) Propose an innovative musical application of your quantum algorithm (e.g., interactive performances, AI-assisted composition).
   b) Explain how this application leverages the unique properties of quantum computation.

5. Limitations and Future Directions (100-150 words):
   a) Discuss the limitations of your approach and potential areas for improvement.
   b) Suggest future research directions for quantum music composition.

Ensure your response demonstrates a deep understanding of both quantum computing principles and music theory. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific accuracy.

Format your response with clear headings for each section. Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum gate and its application in music generation.",
            "The algorithm design is well-explained and logically sound, showing how quantum principles are used to manipulate musical elements.",
            "The musical analysis shows insight into how quantum states translate to musical output and the potential variations.",
            "The quantum-classical integration is thoughtfully addressed, including potential challenges.",
            "The creative application proposed is innovative and leverages unique quantum properties.",
            "Limitations and future directions are realistically assessed and proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
