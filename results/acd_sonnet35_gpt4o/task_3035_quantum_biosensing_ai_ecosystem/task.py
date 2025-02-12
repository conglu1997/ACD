import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'tunneling']
        ecosystem_types = ['marine', 'forest', 'grassland', 'tundra']
        environmental_challenges = ['climate change', 'biodiversity loss', 'pollution']
        
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'ecosystem_type': random.choice(ecosystem_types),
                'environmental_challenge': random.choice(environmental_challenges)
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'ecosystem_type': random.choice(ecosystem_types),
                'environmental_challenge': random.choice(environmental_challenges)
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that utilizes quantum biosensing principles to monitor and optimize ecosystem health on a global scale. Your system should focus on the quantum principle of {t['quantum_principle']}, apply it to the {t['ecosystem_type']} ecosystem, and address the environmental challenge of {t['environmental_challenge']}. Your response should include the following sections:

1. Quantum Biosensing Framework (300-350 words):
   a) Explain the quantum principle of {t['quantum_principle']} and its relevance to biosensing.
   b) Describe how this principle can be applied to monitor the {t['ecosystem_type']} ecosystem.
   c) Outline the key components of your quantum biosensing system.
   d) Discuss any novel technologies or approaches in your design.

2. AI System Architecture (250-300 words):
   a) Detail the overall structure of your AI system for ecosystem monitoring and optimization.
   b) Explain how the AI integrates with the quantum biosensing components.
   c) Describe the data processing pipeline, from quantum sensors to actionable insights.
   d) Discuss any machine learning or deep learning techniques used in your system.

3. Ecosystem Monitoring and Optimization (250-300 words):
   a) Explain how your system monitors key indicators of {t['ecosystem_type']} ecosystem health.
   b) Describe how the AI analyzes and interprets the quantum biosensor data.
   c) Detail the strategies your system employs to address {t['environmental_challenge']}.
   d) Provide an example scenario of how your system would detect and respond to an ecosystem threat.

4. Global Implementation (200-250 words):
   a) Propose a strategy for deploying your system on a global scale.
   b) Discuss challenges in implementing the system across different geographical and political regions.
   c) Explain how your system ensures data consistency and reliability across diverse ecosystems.
   d) Address potential issues of international cooperation and data sharing.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Identify potential ethical concerns related to global ecosystem monitoring and intervention.
   b) Discuss the implications of using AI and quantum technologies in environmental management.
   c) Propose guidelines for responsible development and use of your system.
   d) Address issues of data privacy, security, and potential dual-use applications.

6. Performance Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the effectiveness of your quantum biosensing AI system.
   b) Suggest metrics for measuring improvements in ecosystem health and environmental challenges.
   c) Discuss potential limitations of your approach and areas for future research and development.
   d) Speculate on how advances in quantum computing might enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of quantum biology, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world environmental challenges.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum biology, artificial intelligence, and environmental science.",
            "The proposed quantum biosensing AI system is innovative while maintaining scientific plausibility.",
            "The integration of the specified quantum principle, ecosystem type, and environmental challenge is well-explained and logically sound.",
            "The potential advantages and challenges of the proposed system are thoroughly discussed.",
            "The global implementation strategy and ethical considerations are thoughtfully explored.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
