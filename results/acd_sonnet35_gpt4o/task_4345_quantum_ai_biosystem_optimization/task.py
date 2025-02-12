import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_process': 'Photosynthesis',
                'global_challenge': 'Crop yield improvement in arid regions',
                'quantum_principle': 'Superposition',
                'ai_technique': 'Reinforcement learning',
                'target_crop': 'Drought-resistant wheat',
                'environmental_constraint': 'Average annual rainfall < 250mm'
            },
            {
                'biological_process': 'Nitrogen fixation',
                'global_challenge': 'Reducing fertilizer dependence in agriculture',
                'quantum_principle': 'Entanglement',
                'ai_technique': 'Evolutionary algorithms',
                'target_crop': 'Legumes (e.g., soybeans)',
                'environmental_constraint': 'Soil nitrogen content < 0.2%'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to optimize the biological process of {t['biological_process']} for addressing the global food security challenge of {t['global_challenge']}. Your system should incorporate the quantum principle of {t['quantum_principle']} and utilize the AI technique of {t['ai_technique']}. Focus on the target crop: {t['target_crop']}, considering the environmental constraint: {t['environmental_constraint']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how you incorporate the specified quantum principle into your AI architecture.
   c) Detail how your system interfaces with and optimizes the given biological process.
   d) Include a high-level diagram or pseudocode representing the core algorithm of your system.

2. Quantum-AI Integration (250-300 words):
   a) Explain how the quantum principle enhances the chosen AI technique.
   b) Describe any novel algorithms or techniques you've developed for this integration.
   c) Discuss potential quantum advantages in optimizing complex biological systems.

3. Biological Process Optimization (300-350 words):
   a) Detail how your system models and interacts with the specified biological process.
   b) Explain your approach to optimizing this process for the given global challenge.
   c) Describe expected improvements or novel functionalities in the biological system.
   d) Provide a specific example of how your system would optimize the target crop under the given environmental constraint.

4. Global Impact Analysis (250-300 words):
   a) Analyze the potential impact of your optimized biological system on global food security.
   b) Discuss scalability and implementation challenges in real-world agricultural settings.
   c) Propose methods to measure and validate the effectiveness of your system.
   d) Present a case study of implementing your system in a specific geographic region facing the given environmental constraint.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues in using quantum-AI systems to modify biological processes.
   b) Discuss the implications of your technology on biodiversity and ecosystem balance.
   c) Propose guidelines for responsible development and deployment of your system.
   d) Address potential socio-economic impacts on farming communities.

6. Future Developments (150-200 words):
   a) Suggest two potential extensions or applications of your system to other biological processes or global challenges.
   b) Briefly describe how these developments could contribute to addressing other UN Sustainable Development Goals.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and bioengineering. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, and bioengineering, including their integration.",
            f"The system architecture effectively incorporates the quantum principle of {t['quantum_principle']} and the AI technique of {t['ai_technique']}.",
            f"The approach to optimizing {t['biological_process']} for {t['global_challenge']} is well-explained and scientifically plausible.",
            f"A specific example is provided for optimizing {t['target_crop']} under the constraint of {t['environmental_constraint']}.",
            "The global impact analysis includes a relevant case study and considers real-world implementation challenges.",
            "Ethical considerations are thoughtfully addressed, including socio-economic impacts on farming communities.",
            "The future developments suggested are innovative and relevant to other global challenges.",
            "The response is well-structured, clear, uses appropriate technical terminology, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
