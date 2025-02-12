import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            'Ocean plastic pollution',
            'Atmospheric carbon dioxide reduction',
            'Soil degradation and desertification',
            'Toxic waste cleanup',
            'Invasive species control'
        ]
        ai_capabilities = [
            'Distributed decision-making',
            'Adaptive learning',
            'Swarm intelligence',
            'Predictive modeling',
            'Pattern recognition'
        ]
        organism_types = [
            'Bacteria',
            'Algae',
            'Fungus',
            'Plant',
            'Synthetic multicellular organism'
        ]
        
        tasks = [
            {
                'environmental_challenge': random.choice(environmental_challenges),
                'ai_capability': random.choice(ai_capabilities),
                'organism_type': random.choice(organism_types)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-enhanced synthetic organism to address the environmental challenge of {t['environmental_challenge']}. Your synthetic organism should be based on {t['organism_type']} and incorporate the AI capability of {t['ai_capability']}. Your response should include:

1. Organism Design (300-350 words):
   a) Describe the key features and genetic modifications of your synthetic organism.
   b) Explain how it addresses the specified environmental challenge.
   c) Detail how the AI capability is integrated into the organism's functioning.
   d) Discuss any novel biological mechanisms or structures you've incorporated.

2. AI Integration (250-300 words):
   a) Explain how the specified AI capability is implemented at the cellular or organism level.
   b) Describe the data inputs and outputs for the AI system within the organism.
   c) Discuss how the AI enhances the organism's ability to address the environmental challenge.
   d) Address any energy or resource requirements for the AI functionality.

3. Environmental Impact Analysis (200-250 words):
   a) Predict the potential positive impacts of your organism on the environment.
   b) Discuss possible unintended consequences or risks.
   c) Propose a method for monitoring and controlling the organism's spread and impact.
   d) Suggest a timeline for deployment and expected results.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to releasing this AI-enhanced synthetic organism.
   b) Discuss how these concerns might be addressed or mitigated.
   c) Propose guidelines for responsible development and use of such organisms.

5. Scalability and Future Applications (150-200 words):
   a) Discuss how your organism could be scaled up to address the environmental challenge globally.
   b) Suggest two potential future applications or modifications of your organism for other environmental issues.
   c) Predict how this technology might evolve in the next 20 years.

Ensure your response demonstrates a deep understanding of synthetic biology, environmental science, and artificial intelligence. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and addressing real-world challenges.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, environmental science, and artificial intelligence.",
            f"The synthetic organism design effectively addresses {t['environmental_challenge']}.",
            f"The AI capability of {t['ai_capability']} is well-integrated and explained at the cellular or organism level.",
            f"The organism design is based on {t['organism_type']} and includes plausible genetic modifications.",
            "The environmental impact analysis is thorough and considers both positive and negative effects.",
            "Ethical considerations are thoughtfully addressed with proposed mitigation strategies.",
            "The response is well-structured, using appropriate technical terminology and clear explanations.",
            "The proposed organism and its applications are creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
