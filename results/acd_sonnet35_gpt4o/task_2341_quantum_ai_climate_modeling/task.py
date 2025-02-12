class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"quantum_principle": "superposition", "climate_variable": "ocean circulation patterns", "ai_technique": "reinforcement learning"},
            "2": {"quantum_principle": "entanglement", "climate_variable": "atmospheric carbon dioxide levels", "ai_technique": "generative adversarial networks"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for advanced climate modeling and propose novel approaches to mitigate climate change using this system. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on modeling {t['climate_variable']}, and utilize the AI technique of {t['ai_technique']}. Provide your response in the following format:

1. Quantum-AI Integration (250-300 words):
   a) Explain how the specified quantum principle can be applied to enhance AI capabilities for climate modeling.
   b) Describe the architecture of your quantum-inspired AI system, including key components and their interactions.
   c) Discuss how the chosen AI technique is integrated with quantum principles in your system.

2. Climate Modeling Approach (200-250 words):
   a) Detail how your system models the specified climate variable.
   b) Explain the advantages of your quantum-AI approach over classical climate modeling methods.
   c) Discuss any potential limitations or challenges in your modeling approach.

3. Data Processing and Analysis (200-250 words):
   a) Describe how your system processes and analyzes climate data.
   b) Explain any novel data representation or encoding methods used in your quantum-AI system.
   c) Discuss how your system handles the high dimensionality and complexity of climate data.

4. Predictive Capabilities (200-250 words):
   a) Explain the predictive capabilities of your system for the specified climate variable.
   b) Describe a specific scenario where your system could provide more accurate or detailed predictions than current models.
   c) Discuss how uncertainty is quantified and represented in your system's predictions.

5. Climate Change Mitigation Strategies (250-300 words):
   a) Propose two novel approaches to mitigate climate change based on insights from your quantum-AI climate modeling system.
   b) Explain how these approaches leverage the unique capabilities of your system.
   c) Discuss the potential impact and feasibility of implementing these strategies.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss any ethical implications of using quantum-AI systems for climate modeling and decision-making.
   b) Address potential societal impacts of implementing your proposed mitigation strategies.
   c) Suggest guidelines for responsible development and use of advanced climate modeling technologies.

7. Future Research Directions (100-150 words):
   a) Propose two potential improvements or extensions to your quantum-AI climate modeling system.
   b) Suggest a research question that could further the development of quantum-AI approaches in climate science.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and climate science. Be creative in your system design and mitigation strategies while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, AI, and climate science principles.",
            "The quantum-AI system design is innovative, scientifically plausible, and effectively integrates the specified quantum principle and AI technique.",
            "The climate modeling approach and data processing methods are well-explained and showcase advantages over classical methods.",
            "The proposed climate change mitigation strategies are novel, feasible, and clearly leverage the capabilities of the quantum-AI system.",
            "The response addresses ethical considerations and societal impacts thoughtfully.",
            "The writing is clear, well-structured, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
