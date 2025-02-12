import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_bio_phenomena = [
            {
                "phenomenon": "Quantum coherence in photosynthesis",
                "biological_system": "Light-harvesting complexes in plants",
                "application": "Improving solar energy capture efficiency",
                "example_data": "Coherence lifetime: 660 femtoseconds, Energy transfer efficiency: 95%"
            },
            {
                "phenomenon": "Quantum tunneling in enzyme catalysis",
                "biological_system": "Enzyme active sites",
                "application": "Designing more efficient biocatalysts for industrial processes",
                "example_data": "Tunneling rate: 10^7 s^-1, Activation energy reduction: 30%"
            }
        ]
        
        tasks = {}
        for i in range(2):
            phenomenon = random.choice(quantum_bio_phenomena)
            tasks[str(i+1)] = phenomenon
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to model and predict quantum effects in biological processes, focusing on {t['phenomenon']} in {t['biological_system']}. Your system should be capable of simulating this quantum biological phenomenon and proposing potential applications in {t['application']}. Use the following example data as a starting point for your model: {t['example_data']}

Your response should include the following sections:

1. Quantum Biology Framework (200-250 words):
   a) Explain the quantum effect involved in {t['phenomenon']} and its role in {t['biological_system']}.
   b) Discuss the current scientific understanding of this phenomenon and its biological significance.
   c) Describe the challenges in modeling this quantum biological process.
   d) Provide a simple mathematical formula or equation related to this quantum biological phenomenon.

2. AI System Architecture (300-350 words):
   a) Design the key components of your AI system for modeling {t['phenomenon']}.
   b) Explain how your system integrates quantum mechanics, biological processes, and AI algorithms.
   c) Describe any novel approaches or techniques used in your design.
   d) Provide a high-level diagram of your system architecture (describe it textually).
   e) Specify at least one machine learning algorithm and one quantum algorithm used in your system.

3. Quantum-Biological Modeling Approach (250-300 words):
   a) Explain your AI system's approach to simulating {t['phenomenon']} in {t['biological_system']}.
   b) Describe the key algorithms or methods used for quantum-biological modeling.
   c) Discuss how your system handles the interplay between quantum and classical effects in biological systems.
   d) Explain how your system incorporates the example data provided.

4. Predictive Capabilities and Applications (200-250 words):
   a) Explain how your AI system can make predictions about {t['phenomenon']}.
   b) Describe potential applications in {t['application']}.
   c) Discuss any limitations of your system and how they might be addressed.
   d) Provide an example prediction your system could make, including numerical estimates.

5. Validation and Experimental Design (150-200 words):
   a) Propose a method to validate your AI system's predictions experimentally.
   b) Describe an experiment that could test the accuracy of your quantum-biological model.
   c) Discuss potential challenges in experimentally validating your model's predictions.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using AI to model quantum effects in biological systems.
   b) Propose guidelines for responsible development and use of such AI systems in scientific research.
   c) Suggest future research directions or potential extensions of your system.

7. Conclusion (50-100 words):
   Summarize the key features of your AI system, its potential impact on understanding {t['phenomenon']}, and its broader implications for the field of quantum biology.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed explanation of {t['phenomenon']} in {t['biological_system']}, referencing the provided example data: {t['example_data']}",
            "The response provides a simple mathematical formula or equation related to the quantum biological phenomenon",
            "The AI system architecture integrates quantum mechanics, biological processes, and AI algorithms with clear explanations of each component, including at least one machine learning algorithm and one quantum algorithm",
            f"The response discusses potential applications in {t['application']} with specific examples, including a numerical prediction",
            "The response proposes a detailed method to validate the AI system's predictions experimentally, including a specific experimental design and discussion of potential challenges",
            "The response demonstrates a deep understanding of quantum physics, biology, and artificial intelligence, using appropriate technical terminology",
            "The response is well-organized with clear headings for each of the seven required sections, numbered as specified",
            "The response is innovative while maintaining scientific plausibility, providing novel approaches or techniques in the system design",
            "The response includes a concise conclusion summarizing the key points of the proposed system",
            "The total word count is between 1300-1650 words, with a word count provided at the end of the response"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
