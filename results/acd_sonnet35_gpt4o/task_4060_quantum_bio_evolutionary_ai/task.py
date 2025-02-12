import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation"
        ]
        ai_applications = [
            "pattern recognition",
            "decision making",
            "natural language processing"
        ]
        
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ai_application": random.choice(ai_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired evolutionary algorithm that simulates the potential role of quantum effects in biological information processing and applies this to artificial intelligence development. Focus on the quantum effect of {t['quantum_effect']}, the biological process of {t['biological_process']}, and the AI application of {t['ai_application']}. Your response should include the following sections:

1. Quantum-Bio-AI Model (300-350 words):
   a) Describe your quantum-inspired model of the specified biological process.
   b) Explain how you incorporate the given quantum effect into this model.
   c) Detail how your model translates to the specified AI application.
   d) Include a diagram or mathematical representation of your model (describe it textually).

2. Evolutionary Algorithm Design (250-300 words):
   a) Outline the key components of your quantum-inspired evolutionary algorithm.
   b) Explain how your algorithm simulates the quantum-biological process.
   c) Describe how the algorithm optimizes for the AI application.
   d) Discuss any novel features or modifications to standard evolutionary algorithms.

3. Simulation and Analysis (250-300 words):
   a) Describe a hypothetical simulation of your algorithm, including key parameters and variables.
   b) Analyze the expected results and how they would be interpreted.
   c) Compare the potential performance of your quantum-bio-inspired AI to traditional approaches.
   d) Discuss any emergent behaviors or unexpected outcomes you might anticipate.

4. Theoretical Implications (200-250 words):
   a) Discuss how your model and results might contribute to our understanding of quantum effects in biology.
   b) Explain potential implications for theories of biological information processing.
   c) Analyze how this approach could influence the development of quantum-inspired AI systems.

5. Practical Applications (150-200 words):
   a) Propose three potential real-world applications of your quantum-bio-inspired AI system.
   b) Discuss the advantages and challenges of implementing such a system.
   c) Suggest industries or fields that could benefit most from this technology.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical concerns related to the development of quantum-bio-inspired AI.
   b) Discuss any risks or unintended consequences of mimicking quantum-biological processes in AI.
   c) Propose future research directions to further explore and validate your approach.

Ensure your response demonstrates a deep understanding of quantum biology, evolutionary computation, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum biology, evolutionary computation, and artificial intelligence.",
            "The quantum-bio-AI model effectively incorporates the specified quantum effect, biological process, and AI application.",
            "The evolutionary algorithm design is well-explained and incorporates quantum-inspired elements.",
            "The simulation and analysis section provides a clear hypothetical scenario with thoughtful interpretation.",
            "The theoretical implications are well-reasoned and demonstrate interdisciplinary thinking.",
            "Practical applications are innovative and well-justified.",
            "Ethical considerations are thoughtfully addressed.",
            "The response is creative and scientifically plausible throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
