import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "Climate change mitigation",
            "Ocean plastic pollution",
            "Biodiversity loss",
            "Air pollution in urban areas",
            "Freshwater scarcity"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "challenge": random.choice(environmental_challenges),
                "quantum_principle": random.choice(quantum_principles)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired biological system to address the environmental challenge of {t['challenge']}, utilizing the quantum principle of {t['quantum_principle']}. Your response should include:

1. System Overview (300-350 words):
   a) Describe the key components of your quantum-inspired biological system.
   b) Explain how it incorporates the specified quantum principle.
   c) Outline how the system addresses the given environmental challenge.
   d) Provide a conceptual diagram of your system (describe it textually using clear, structured paragraphs).

2. Quantum-Biological Integration (250-300 words):
   a) Explain how your system integrates quantum principles with biological processes.
   b) Describe the mechanisms by which the specified quantum principle enhances the system's functionality.
   c) Discuss potential challenges in combining quantum and biological systems and how you address them.
   d) Include a mathematical or chemical formulation that represents a key aspect of your quantum-biological integration.

3. Environmental Impact Analysis (200-250 words):
   a) Analyze the potential effectiveness of your system in addressing the given environmental challenge.
   b) Compare your quantum-inspired approach to traditional methods of tackling this challenge.
   c) Discuss any potential unintended consequences or ecological impacts of implementing your system.

4. Scalability and Implementation (200-250 words):
   a) Propose a strategy for scaling up your system from laboratory to global implementation.
   b) Discuss the technical and logistical challenges of large-scale deployment.
   c) Suggest potential modifications to adapt your system to different environmental contexts.

5. Interdisciplinary Implications (150-200 words):
   a) Explore how your system might impact or advance the fields of quantum computing, synthetic biology, and environmental science.
   b) Propose two potential applications of your quantum-bio-environmental system beyond the specified challenge.
   c) Discuss how this technology might influence future approaches to environmental engineering.

6. Ethical Considerations and Future Research (150-200 words):
   a) Address potential ethical concerns related to the development and deployment of quantum-inspired biological systems for environmental intervention.
   b) Suggest guidelines for responsible research and implementation in this field.
   c) Propose a key experiment or study to further validate or improve your system.

Ensure your response demonstrates a deep understanding of quantum principles, biological systems, and environmental science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and adhere strictly to the word count limits provided for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and adheres to the specified word count limits for each section.",
            f"The system design demonstrates a deep understanding of {t['quantum_principle']} and its potential applications in biological systems to address {t['challenge']}.",
            "The proposed solution addresses the given environmental challenge in a novel and potentially effective way, clearly explaining how it improves upon traditional methods.",
            "The response shows a clear integration of concepts from quantum computing, synthetic biology, and environmental science, including a relevant mathematical or chemical formulation.",
            "The scalability and implementation section provides a realistic assessment of challenges and potential solutions for global deployment.",
            "The interdisciplinary implications and ethical considerations are thoughtfully explored, with specific examples and guidelines provided.",
            "The overall response demonstrates creativity, scientific rigor, and plausibility in its approach to quantum-bio-environmental engineering, while maintaining consistency throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
