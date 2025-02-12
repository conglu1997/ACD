import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organoid_types = [
            "brain",
            "liver",
            "kidney",
            "pancreas"
        ]
        computational_enhancements = [
            "parallel processing",
            "quantum-inspired computing",
            "neuromorphic architecture",
            "molecular data storage"
        ]
        ai_integration_methods = [
            "neuro-symbolic AI",
            "federated learning",
            "reinforcement learning",
            "evolutionary algorithms"
        ]
        return {
            "1": {
                "organoid_type": random.choice(organoid_types),
                "computational_enhancement": random.choice(computational_enhancements),
                "ai_integration_method": random.choice(ai_integration_methods)
            },
            "2": {
                "organoid_type": random.choice(organoid_types),
                "computational_enhancement": random.choice(computational_enhancements),
                "ai_integration_method": random.choice(ai_integration_methods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-guided system for engineering synthetic {t['organoid_type']} organoids with enhanced computational capabilities, integrating {t['computational_enhancement']} and {t['ai_integration_method']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-guided synthetic organoid engineering system.
   b) Explain how your system integrates synthetic biology, computational enhancements, and AI methodologies.
   c) Discuss how the chosen AI integration method guides the organoid engineering process.
   d) Include a simple diagram (described in words using ASCII characters) illustrating the main features of your system architecture.

2. Synthetic Biology Approach (250-300 words):
   a) Describe the synthetic biology techniques used to engineer the {t['organoid_type']} organoid.
   b) Explain how you would modify the organoid to incorporate {t['computational_enhancement']}.
   c) Discuss any novel genetic circuits or biomolecular components in your design.
   d) Address potential challenges in maintaining organoid viability with these modifications.

3. Computational Enhancement Implementation (250-300 words):
   a) Provide a detailed explanation of how {t['computational_enhancement']} is implemented in the organoid.
   b) Describe the expected computational capabilities of the enhanced organoid.
   c) Compare the potential performance of your bio-computational system to traditional computing systems.
   d) Discuss any limitations or trade-offs in your approach.

4. AI Integration and Optimization (250-300 words):
   a) Explain how {t['ai_integration_method']} is used to guide and optimize the organoid engineering process.
   b) Describe the key parameters or objectives that the AI system optimizes.
   c) Discuss how the AI system adapts to unexpected results or challenges during the engineering process.
   d) Propose a method for validating the AI's decisions and outcomes.

5. Applications and Implications (200-250 words):
   a) Suggest three potential applications for your AI-guided, computationally enhanced synthetic organoid.
   b) Discuss the ethical implications of creating organoids with advanced computational capabilities.
   c) Analyze potential risks and propose safeguards for this technology.
   d) Speculate on how this technology might impact future human-machine interfaces or medical treatments.

6. Future Directions and Challenges (150-200 words):
   a) Propose two potential improvements or extensions to your system.
   b) Identify key challenges that need to be overcome for real-world implementation.
   c) Suggest areas of research that could significantly advance this field.

Ensure your response demonstrates a deep understanding of synthetic biology, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words. Please include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of an AI-guided system for engineering synthetic {t['organoid_type']} organoids with enhanced computational capabilities, integrating {t['computational_enhancement']} and {t['ai_integration_method']}.",
            "The design should demonstrate a novel integration of synthetic biology, computational enhancements, and AI methodologies, with clear explanations for each component.",
            "The response should showcase creative problem-solving in designing the system architecture (including an ASCII diagram) and implementing the computational enhancements.",
            "The proposed system should be scientifically plausible and demonstrate a deep understanding of synthetic biology, neuroscience, and artificial intelligence, using appropriate technical terminology.",
            "The response should include a thoughtful discussion of potential applications, ethical implications, and future directions for this technology, as well as addressing potential challenges and limitations.",
            "The response should adhere to the specified word count for each section and include a total word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
