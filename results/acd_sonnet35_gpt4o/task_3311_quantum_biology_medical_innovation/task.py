import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum entanglement",
            "Superposition"
        ]
        biological_systems = [
            "Photosynthesis",
            "Enzyme catalysis",
            "DNA mutation repair",
            "Magnetoreception in birds"
        ]
        medical_applications = [
            "Cancer treatment",
            "Drug delivery",
            "Diagnostic imaging",
            "Neurological disorders"
        ]
        return {
            "1": {
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "biological_system": random.choice(biological_systems),
                "medical_application": random.choice(medical_applications)
            },
            "2": {
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "biological_system": random.choice(biological_systems),
                "medical_application": random.choice(medical_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum biological system for medical applications, focusing on the quantum phenomenon of {t['quantum_phenomenon']}, the biological system of {t['biological_system']}, and its potential application in {t['medical_application']}. Then, propose and analyze experiments to test its efficacy and safety. Your response should include:

1. Theoretical Foundation (250-300 words):
   a) Explain the key concepts of {t['quantum_phenomenon']} and how it relates to biological systems.
   b) Describe the biological mechanism of {t['biological_system']} and its relevance to {t['medical_application']}.
   c) Discuss how these concepts might interact to create a novel quantum biological system.
   d) Provide a specific example or case study that illustrates the potential of this interaction.
   e) Briefly explain how your proposed system adheres to or challenges current understanding of quantum mechanics in biological systems.

2. Quantum Biological System Design (300-350 words):
   a) Propose a detailed design for your quantum biological system, integrating {t['quantum_phenomenon']} with {t['biological_system']}.
   b) Explain how your system could be applied to {t['medical_application']}.
   c) Describe the potential advantages of your quantum biological approach over conventional methods.
   d) Include a conceptual diagram or detailed description of your system's components and their interactions.
   e) Discuss potential limitations or challenges of your proposed system.

3. Experimental Design (250-300 words):
   Propose two experiments to test your quantum biological system:
   a) Experiment 1: Design an in vitro experiment to test the basic principles of your system.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would validate (or invalidate) your system's quantum biological mechanisms.
   b) Experiment 2: Design an in vivo experiment to evaluate your system's efficacy and safety for {t['medical_application']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would demonstrate your system's potential for clinical application.

4. Safety and Ethical Considerations (150-200 words):
   a) Discuss potential risks and safety concerns associated with your quantum biological system.
   b) Address ethical implications of using quantum biological systems in medicine.
   c) Propose guidelines for responsible development and testing of such systems.

5. Future Directions and Implications (150-200 words):
   a) Discuss the potential long-term implications of your quantum biological system for medical science.
   b) Explore how your system might be extended or applied to other areas of medicine or biotechnology.
   c) Propose two directions for future research based on your quantum biological system.
   d) Discuss potential interdisciplinary connections beyond medicine and biology.

6. Concise Summary (50-75 words):
   Provide a brief summary that encapsulates the key innovations and potential impact of your proposed quantum biological system.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and medical science. Be creative and innovative in your design while maintaining scientific plausibility and accuracy. Use technical terminology appropriately and provide explanations where necessary. Your total response should be between 1150-1425 words.

Format your response with clear headings for each section, and number subsections as shown above. Provide citations for any specific scientific claims or data you include.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['quantum_phenomenon']} and its potential role in biological systems, with a specific example or case study provided.",
            f"The proposed quantum biological system must effectively integrate {t['quantum_phenomenon']} with {t['biological_system']} for application in {t['medical_application']}, including a discussion of potential limitations or challenges.",
            "The experimental designs must be well-thought-out and directly test the key features and potential efficacy of the proposed system.",
            "The response must show creativity and originality in the system design while maintaining scientific plausibility and accuracy.",
            "The discussion of safety, ethical considerations, and future implications must demonstrate a broad understanding of the potential impacts of quantum biology in medicine.",
            "The response must include a discussion of interdisciplinary connections beyond medicine and biology.",
            "The overall response must exhibit strong interdisciplinary knowledge integration and advanced reasoning in quantum physics, biology, and medical science.",
            "The response must adhere to the specified format and word count limits for each section, including the concise summary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
