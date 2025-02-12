import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_processes = [
            {
                "name": "Quantum coherence in photosynthesis",
                "description": "The process by which plants and some bacteria efficiently capture and transfer light energy through quantum coherence"
            },
            {
                "name": "Quantum tunneling in enzyme catalysis",
                "description": "The quantum mechanical effect that allows enzymes to catalyze biochemical reactions through proton tunneling"
            },
            {
                "name": "Quantum entanglement in avian magnetoreception",
                "description": "The proposed mechanism by which birds use quantum entanglement to detect the Earth's magnetic field for navigation"
            }
        ]
        return {
            "1": random.choice(quantum_processes),
            "2": random.choice(quantum_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum biological system inspired by {t['name']} and analyze its potential applications in medicine. Your response should include:

1. Quantum Biological Process Analysis (200-250 words):
   a) Explain the key features and mechanisms of {t['name']}.
   b) Describe how quantum effects contribute to this biological process.
   c) Discuss current scientific understanding and any controversies surrounding this quantum biological phenomenon.

2. Theoretical System Design (250-300 words):
   a) Propose a novel quantum biological system inspired by {t['name']}.
   b) Describe the key components and quantum mechanisms of your system.
   c) Explain how your system mimics or adapts the principles from the natural process.
   d) Include a simple ASCII art diagram or a mathematical representation of your system.

3. Medical Application (200-250 words):
   a) Propose a specific medical application for your quantum biological system.
   b) Explain how the quantum properties of your system could provide advantages over classical approaches.
   c) Discuss potential challenges in implementing your system in a medical context.

4. Experimental Approach (200-250 words):
   a) Design a theoretical experiment to test the quantum behavior of your system.
   b) Describe the equipment and methods you would use.
   c) Explain how you would measure and verify the quantum effects in your system.

5. Ethical and Safety Considerations (150-200 words):
   a) Discuss potential ethical implications of using your quantum biological system in medicine.
   b) Analyze possible safety concerns and propose mitigation strategies.
   c) Consider long-term effects of integrating quantum biological systems into medical treatments.

6. Future Research Directions (150-200 words):
   a) Propose two areas for further research to enhance or expand your quantum biological system.
   b) Suggest potential interdisciplinary collaborations that could advance this technology.
   c) Speculate on how this field might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and medical science. Be creative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically accurate explanation of {t['name']}.",
            "The proposed quantum biological system is novel, creative, and scientifically plausible.",
            "The medical application is well-reasoned and demonstrates a clear understanding of both quantum mechanics and medical science.",
            "The experimental approach is well-designed and appropriate for testing quantum effects in biological systems.",
            "The ethical and safety considerations are thoughtful and comprehensive.",
            "The future research directions are insightful and demonstrate an understanding of the field's potential.",
            "The overall response demonstrates a strong grasp of quantum mechanics, biology, and medical science, creatively applied to a speculative scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
