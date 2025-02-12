import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        biological_systems = [
            "Neuronal networks",
            "DNA-based computation",
            "Protein folding dynamics",
            "Cellular signaling pathways"
        ]
        information_processes = [
            "Pattern recognition",
            "Error correction",
            "Data compression",
            "Cryptography"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_system": random.choice(biological_systems),
                "information_process": random.choice(information_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_system": random.choice(biological_systems),
                "information_process": random.choice(information_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological hybrid system for information processing, focusing on the quantum principle of {t['quantum_principle']}, the biological system of {t['biological_system']}, and the information process of {t['information_process']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-biological hybrid system.
   b) Explain how your system incorporates the specified quantum principle.
   c) Detail how the biological system is integrated into the quantum framework.
   d) Discuss how your system implements the specified information process.

2. Quantum-Biological Interface (250-300 words):
   a) Explain the mechanisms by which quantum effects are maintained or utilized in the biological component.
   b) Describe how information is transferred between the quantum and biological parts of the system.
   c) Address potential issues of decoherence and propose innovative solutions.

3. Information Processing Capabilities (250-300 words):
   a) Describe the unique information processing capabilities of your hybrid system.
   b) Compare its theoretical performance to classical computing, quantum computing, and natural biological systems.
   c) Explain how the quantum-biological interface enhances the specified information process.

4. Experimental Design (300-350 words):
   a) Propose an experiment to test the information processing capabilities of your system.
   b) Describe the methodology, including any novel measurement techniques required.
   c) Predict potential outcomes and their implications for quantum biology and information theory.
   d) Discuss any ethical considerations related to your experimental design.

5. Implications and Applications (200-250 words):
   a) Discuss the potential impact of your system on quantum computing, biology, and information science.
   b) Propose two potential applications in fields such as medicine, cryptography, or artificial intelligence.
   c) Address any philosophical implications regarding the nature of computation or life itself.

6. Challenges and Future Directions (200-250 words):
   a) Identify key technological or scientific barriers to realizing your system.
   b) Propose approaches to overcome these challenges.
   c) Suggest two directions for future research in quantum-biological information processing.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum mechanics, biology, and information theory.",
            "The proposed system effectively integrates the specified quantum principle, biological system, and information process.",
            "The quantum-biological interface is explained in a scientifically plausible manner.",
            "The experimental design is well-thought-out and addresses potential challenges.",
            "The implications and applications are insightful and consider multiple perspectives.",
            "The response identifies relevant challenges and proposes innovative future directions.",
            "The overall response is well-structured, scientifically grounded, and demonstrates creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
