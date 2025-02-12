import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        biological_systems = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation"
        ]
        medical_applications = [
            "cancer treatment",
            "neurodegenerative disease therapy",
            "antibiotic resistance mitigation"
        ]
        
        tasks = [
            {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems),
                "medical_application": random.choice(medical_applications)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum biological mechanism for targeted drug delivery based on {t['quantum_effect']} in {t['biological_system']}, and analyze its potential application in {t['medical_application']}. Your response should include:

1. Quantum Biological Mechanism (250-300 words):
   a) Explain how the specified quantum effect could be leveraged in the given biological system for drug delivery.
   b) Describe the proposed mechanism in detail, including its components and functioning.
   c) Discuss how this mechanism differs from classical drug delivery methods.

2. Medical Application (200-250 words):
   a) Analyze how your proposed mechanism could be applied to the specified medical application.
   b) Discuss potential advantages and challenges of using this quantum biological approach.
   c) Compare the effectiveness of your approach to current treatment methods.

3. Implementation and Technology (150-200 words):
   a) Describe the technological requirements for implementing your proposed mechanism.
   b) Discuss any gaps between current technology and what would be needed.
   c) Propose a timeline for the development and clinical application of this technology.

4. Ethical Implications (150-200 words):
   a) Identify at least two ethical concerns raised by this quantum biological approach to medicine.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of this technology.

5. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research to advance this field.
   b) Discuss how these research directions could address current limitations or challenges.

6. Conclusion (50-100 words):
   Summarize the key points of your proposal and its potential impact on medicine and society.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and medical science. Be creative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology throughout your answer.

Format your response using the following structure:

1. Quantum Biological Mechanism:
   [Your content here]

2. Medical Application:
   [Your content here]

3. Implementation and Technology:
   [Your content here]

4. Ethical Implications:
   [Your content here]

5. Future Research Directions:
   [Your content here]

6. Conclusion:
   [Your content here]

Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must incorporate {t['quantum_effect']} in {t['biological_system']} for drug delivery",
            f"The medical application of {t['medical_application']} must be thoroughly addressed",
            "The proposed mechanism should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration",
            "Ethical implications must be thoughtfully considered",
            "The implementation and technology section should provide a realistic assessment of current capabilities and future needs",
            "Future research directions should be relevant and well-justified",
            "The conclusion should effectively summarize the key points of the proposal",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (900-1200 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
