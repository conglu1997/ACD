import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_operations = [
            {
                "name": "Semantic Superposition",
                "description": "Create a quantum circuit that represents word meanings in superposition"
            },
            {
                "name": "Syntactic Entanglement",
                "description": "Design a quantum circuit that models syntactic dependencies between words"
            }
        ]
        
        quantum_gates = [
            "Hadamard",
            "CNOT",
            "Pauli-X",
            "Pauli-Y",
            "Pauli-Z",
            "Phase"
        ]
        
        return {
            "1": {
                "operation": random.choice(linguistic_operations),
                "gates": random.sample(quantum_gates, 3)
            },
            "2": {
                "operation": random.choice(linguistic_operations),
                "gates": random.sample(quantum_gates, 3)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum circuit for {t['operation']['name']} in natural language processing. Your task has the following components:

1. Circuit Design (250-300 words):
   a) Create a quantum circuit that implements {t['operation']['description']}.
   b) Your circuit must use the following quantum gates: {', '.join(t['gates'])}.
   c) Explain how each gate is used in your circuit and its role in processing linguistic information.
   d) Provide a textual description or ASCII art representation of your circuit.

2. Linguistic Representation (200-250 words):
   a) Explain how linguistic information (e.g., words, meanings, or syntactic structures) is encoded in your quantum states.
   b) Discuss any advantages or unique properties of this quantum representation compared to classical NLP approaches.

3. Circuit Analysis (200-250 words):
   a) Describe the expected output of your circuit and how it relates to the linguistic task.
   b) Analyze potential quantum effects (e.g., superposition, entanglement) in your circuit and their linguistic implications.
   c) Discuss any limitations or challenges in your approach.

4. Potential Applications (150-200 words):
   a) Propose two potential applications of your quantum linguistic circuit in NLP or cognitive science.
   b) Explain how these applications could advance our understanding of language or improve existing NLP technologies.

5. Quantum-Classical Interface (100-150 words):
   a) Briefly explain how the results of your quantum circuit could be measured and interpreted classically.
   b) Discuss any challenges in this quantum-to-classical transition for linguistic processing.

Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistic concepts. Use appropriate terminology from both fields and provide clear explanations for complex ideas. Be creative in your circuit design while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and linguistics, using appropriate terminology from both fields.",
            f"The quantum circuit design correctly incorporates the specified gates ({', '.join(t['gates'])}) and addresses the given linguistic operation ({t['operation']['name']}).",
            "The explanation of linguistic information encoding in quantum states is clear and plausible.",
            "The circuit analysis shows insightful understanding of quantum effects and their linguistic implications.",
            "The proposed applications are innovative and demonstrate the potential impact of quantum computing on NLP or cognitive science.",
            "The response is well-structured, following the specified format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
