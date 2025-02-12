import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "process": "Photosynthesis",
                "key_feature": "Light harvesting and energy transfer",
                "quantum_aspect": "Quantum coherence in energy transfer"
            },
            {
                "process": "DNA replication",
                "key_feature": "High-fidelity information copying",
                "quantum_aspect": "Quantum tunneling in proton transfer"
            },
            {
                "process": "Enzyme catalysis",
                "key_feature": "Accelerated chemical reactions",
                "quantum_aspect": "Quantum tunneling in hydrogen transfer"
            },
            {
                "process": "Magnetoreception in birds",
                "key_feature": "Sensing of Earth's magnetic field",
                "quantum_aspect": "Quantum entanglement in radical pairs"
            }
        ]
        return {
            "1": random.choice(biological_processes),
            "2": random.choice(biological_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum computing system inspired by the biological process of {t['process']}. Your task is to create a detailed proposal for this bio-inspired quantum computing system, addressing the following points:

1. System Overview (150-200 words):
   - Describe the key components of your quantum computing system.
   - Explain how it incorporates the principle of {t['key_feature']} from {t['process']}.
   - Discuss how the system utilizes the quantum aspect of {t['quantum_aspect']}.

2. Quantum Architecture (200-250 words):
   - Detail the quantum architecture of your system, including qubit implementation and control mechanisms.
   - Explain how the biological inspiration enhances or modifies traditional quantum computing approaches.
   - Discuss any potential advantages this bio-inspired architecture might have over conventional quantum computing systems.

3. Information Processing (150-200 words):
   - Describe how information is encoded, processed, and read out in your system.
   - Explain how the biological inspiration influences the information processing capabilities.
   - Discuss any unique computational properties that arise from this bio-inspired approach.

4. Potential Applications (150-200 words):
   - Propose at least two novel applications for your bio-inspired quantum computing system.
   - Explain how these applications leverage the unique features of your system.
   - Discuss the potential impact of these applications on science, technology, or society.

5. Challenges and Future Directions (150-200 words):
   - Identify at least two major challenges in realizing this bio-inspired quantum computing system.
   - Propose potential solutions or research directions to address these challenges.
   - Speculate on future developments or extensions of your system.

Ensure your response demonstrates a deep understanding of both quantum mechanics and the chosen biological process. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum computing principles and the specified biological process.",
            f"The proposed quantum computing system clearly incorporates the key feature of {t['key_feature']} from {t['process']}.",
            f"The system effectively utilizes the quantum aspect of {t['quantum_aspect']} in its design.",
            "The quantum architecture is well-explained and logically connects the biological inspiration to quantum computing concepts.",
            "The information processing description is clear and demonstrates how the bio-inspired approach influences computational capabilities.",
            "The proposed applications are innovative and clearly leverage the unique features of the bio-inspired system.",
            "The challenges and future directions are thoughtfully considered, with plausible solutions or research paths proposed.",
            "The response maintains scientific rigor while showcasing creativity in system design and problem-solving.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
