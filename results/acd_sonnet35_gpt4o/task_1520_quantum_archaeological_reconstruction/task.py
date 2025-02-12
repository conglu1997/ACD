import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "artifact": "Ancient clay tablet with cuneiform writing",
                "quantum_property": "Quantum tunneling",
                "ethical_dilemma": "Privacy concerns of reconstructing personal information"
            },
            {
                "artifact": "Fossilized DNA fragments from an extinct species",
                "quantum_property": "Quantum entanglement",
                "ethical_dilemma": "Potential for de-extinction and ecosystem disruption"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based system for reconstructing historical information from archaeological artifacts, specifically for a {t['artifact']}. Your system should incorporate the quantum property of {t['quantum_property']}. Analyze the system's potential applications, limitations, and ethical implications, with a focus on the ethical dilemma of {t['ethical_dilemma']}.

Your response should include the following sections:

1. Quantum Archaeological System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum-based archaeological reconstruction system.
   b) Explain how your system utilizes {t['quantum_property']} to extract information from the {t['artifact']}.
   c) Discuss how your system integrates principles from quantum physics, archaeology, and information theory.
   d) Provide a diagram or detailed description of the system architecture.

2. Information Reconstruction Process (250-300 words):
   a) Explain the step-by-step process of how your system would reconstruct historical information from the {t['artifact']}.
   b) Describe the type of historical information your system aims to reconstruct (e.g., text, images, sounds, or other data).
   c) Discuss how your system would handle uncertainty and incomplete data in the reconstruction process.

3. Quantum-Classical Interface (200-250 words):
   a) Explain how your system translates quantum information into classical, interpretable data.
   b) Discuss any potential loss of information or fidelity in this translation process.
   c) Propose a method for verifying the accuracy of the reconstructed information.

4. Limitations and Challenges (150-200 words):
   a) Identify potential limitations of your quantum archaeological system.
   b) Discuss technical challenges in implementing this system with current or near-future technology.
   c) Propose potential solutions or areas for future research to address these limitations.

5. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of using your system, focusing on {t['ethical_dilemma']}.
   b) Discuss potential misuses of this technology and propose safeguards against them.
   c) Consider the broader societal impact of having access to previously unattainable historical information.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your quantum archaeological system might impact or revolutionize traditional archaeological methods.
   b) Explore potential applications of your system in other scientific fields.
   c) Speculate on how this technology might change our understanding of history and human civilization.

Ensure your response demonstrates a deep understanding of quantum physics, archaeology, and information theory. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed design of a quantum-based system for reconstructing historical information from a {t['artifact']}",
            f"The system design should incorporate the quantum property of {t['quantum_property']}",
            f"The ethical analysis should address the dilemma of {t['ethical_dilemma']}",
            "The response should demonstrate a deep understanding of quantum physics, archaeology, and information theory",
            "The proposed system should be creative and innovative while maintaining scientific plausibility",
            "The response should include all required sections with appropriate detail and word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
