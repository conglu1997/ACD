import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_effect': 'quantum tunneling',
                'biological_process': 'enzyme catalysis',
                'ai_technique': 'reinforcement learning',
                'target_disease': 'neurodegenerative disorders'
            },
            {
                'quantum_effect': 'quantum coherence',
                'biological_process': 'photosynthesis',
                'ai_technique': 'generative adversarial networks',
                'target_disease': 'cancer'
            },
            {
                'quantum_effect': 'quantum entanglement',
                'biological_process': 'magnetoreception',
                'ai_technique': 'quantum neural networks',
                'target_disease': 'autoimmune disorders'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that leverages quantum biology principles to enhance drug discovery processes, focusing on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}. Your system should utilize the AI technique of {t['ai_technique']} and target {t['target_disease']}. Then, analyze its potential impact on pharmaceutical research and ethical implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for quantum biology-enhanced drug discovery.
   b) Explain how your system incorporates the specified quantum effect and biological process.
   c) Detail how you implement the given AI technique in your drug discovery pipeline.
   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually, no actual images required).

2. Quantum-Biological Modeling (250-300 words):
   a) Explain how your system models the quantum effect in the context of the biological process.
   b) Discuss any novel approaches or algorithms used to simulate quantum-biological interactions.
   c) Describe how this quantum-biological model interfaces with the AI-driven drug discovery process.

3. AI-Driven Drug Discovery Process (250-300 words):
   a) Detail the step-by-step process of how your AI system discovers potential drug candidates.
   b) Explain how the quantum-biological model enhances the drug discovery process.
   c) Provide an example of how your system might identify a promising drug candidate for the specified target disease.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum biology-enhanced AI system to traditional drug discovery methods.
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze how your system might accelerate or improve the drug discovery process for the target disease.

5. Ethical Implications and Safeguards (200-250 words):
   a) Discuss ethical considerations in using AI and quantum biology principles for drug discovery.
   b) Address potential risks or concerns associated with this technology.
   c) Propose guidelines or safeguards for responsible development and use of such systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research to enhance your system.
   b) Discuss how advancements in quantum biology might influence future AI-driven drug discovery.

7. Conclusion (100-150 words):
   Summarize the key aspects of your system and its potential impact on pharmaceutical research and healthcare.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, artificial intelligence, and drug discovery processes. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively incorporates the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}.",
            f"The AI system utilizes {t['ai_technique']} technique in a relevant and innovative way for drug discovery.",
            f"The approach demonstrates potential for enhancing drug discovery for {t['target_disease']}.",
            "The response shows a deep understanding of quantum biology, AI, and drug discovery processes.",
            "The ethical implications and safeguards are thoroughly discussed and relevant to the proposed system.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The comparative analysis provides a balanced view of the system's advantages and limitations.",
            "The future research directions are relevant and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
