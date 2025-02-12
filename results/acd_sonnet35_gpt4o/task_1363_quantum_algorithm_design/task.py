import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        classical_problems = [
            "Graph Coloring",
            "Integer Factorization",
            "Traveling Salesman Problem",
            "Database Search",
            "Linear Systems of Equations"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Fourier Transform",
            "Quantum Phase Estimation",
            "Amplitude Amplification"
        ]
        
        return {
            "1": {
                "classical_problem": random.choice(classical_problems),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "classical_problem": random.choice(classical_problems),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum algorithm to solve the classical problem of {t['classical_problem']}, utilizing the quantum principle of {t['quantum_principle']}. Your response should include:\n\n1. Problem Analysis (150-200 words):\n   a) Briefly explain the classical {t['classical_problem']} problem.\n   b) Discuss why this problem is challenging for classical computers.\n   c) Explain how the quantum principle of {t['quantum_principle']} could be leveraged in a quantum solution.\n\n2. Quantum Algorithm Design (250-300 words):\n   a) Propose a quantum algorithm to solve the {t['classical_problem']} problem.\n   b) Explain how your algorithm works, step by step.\n   c) Describe how your algorithm utilizes {t['quantum_principle']}.\n   d) Discuss any quantum gates or subroutines your algorithm employs.\n\n3. Quantum Advantage Analysis (150-200 words):\n   a) Compare the complexity of your quantum algorithm to the best known classical algorithm for this problem.\n   b) Explain the quantum speedup or advantage, if any.\n   c) Discuss any limitations or constraints of your quantum approach.\n\n4. Implementation Challenges (150-200 words):\n   a) Identify potential challenges in implementing your algorithm on current or near-term quantum hardware.\n   b) Propose solutions or workarounds for these challenges.\n   c) Discuss any error correction or mitigation techniques that might be necessary.\n\n5. Future Directions (100-150 words):\n   a) Suggest potential improvements or variations of your algorithm.\n   b) Propose a related quantum computing research question that builds on your algorithm.\n\nEnsure your response demonstrates a deep understanding of both quantum computing principles and the classical problem at hand. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and accuracy.\n\nFormat your response with clear headings for each section and number your paragraphs within each section for easy reference. Your total response should be between 800-1050 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep and accurate understanding of quantum computing principles and the classical problem.",
            "The proposed quantum algorithm is logically sound, correctly utilizes the specified quantum principle, and is explained in detail.",
            "The quantum advantage analysis is accurate, well-reasoned, and compares the complexity to classical algorithms.",
            "Implementation challenges are realistically identified and addressed with plausible solutions or workarounds.",
            "The response shows creativity and innovation while maintaining scientific accuracy and plausibility.",
            "The response adheres to the required word count and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
