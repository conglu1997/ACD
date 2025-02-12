import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "process": "Photosynthesis",
                "quantum_effect": "Quantum coherence",
                "computing_task": "Optimization"
            },
            {
                "process": "DNA replication",
                "quantum_effect": "Quantum tunneling",
                "computing_task": "Pattern recognition"
            },
            {
                "process": "Enzyme catalysis",
                "quantum_effect": "Quantum entanglement",
                "computing_task": "Cryptography"
            },
            {
                "process": "Neural signaling",
                "quantum_effect": "Quantum superposition",
                "computing_task": "Machine learning"
            }
        ]
        return {
            "1": random.choice(biological_processes),
            "2": random.choice(biological_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-biological computing system inspired by {t['process']} that leverages {t['quantum_effect']} for {t['computing_task']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your quantum-biological computing system.
   b) Explain how it incorporates principles from {t['process']}.
   c) Detail how {t['quantum_effect']} is utilized in your system.
   d) Discuss how your system is optimized for {t['computing_task']}.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how quantum effects are maintained and controlled in a biological environment.
   b) Describe the mechanisms for information transfer between quantum and biological components.
   c) Discuss any novel materials or structures required for your system.

3. Information Processing Mechanism (250-300 words):
   a) Detail how information is encoded, processed, and read out in your system.
   b) Explain how your system performs {t['computing_task']}.
   c) Compare the efficiency of your system to classical computing approaches for this task.

4. Theoretical Performance Analysis (200-250 words):
   a) Provide a quantitative estimate of your system's performance for {t['computing_task']}.
   b) Compare this to the theoretical limits of classical computing for the same task.
   c) Discuss any quantum advantages or speedups your system might offer.

5. Implementation Challenges (200-250 words):
   a) Identify the main technical challenges in realizing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss the feasibility of your system with current or near-future technologies.

6. Ethical Implications and Future Applications (150-200 words):
   a) Discuss potential societal impacts and ethical considerations of your system.
   b) Propose two novel applications of your quantum-biological computing system beyond {t['computing_task']}.
   c) Suggest how your system might influence future research in quantum computing and synthetic biology.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and computer science. Use appropriate technical terminology and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum physics, biology, and information theory.",
            f"The proposed quantum-biological computing system effectively incorporates principles from {t['process']} and utilizes {t['quantum_effect']}.",
            f"The system's design and information processing mechanism are well-explained and optimized for {t['computing_task']}.",
            "The quantum-biological interface is adequately addressed, including mechanisms for maintaining quantum effects in a biological environment.",
            "The theoretical performance analysis provides meaningful quantitative estimates and comparisons.",
            "Implementation challenges are thoroughly discussed with plausible solutions or research directions proposed.",
            "The ethical implications and future applications are thoughtfully considered.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The submission is well-structured with clear sections as requested in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
