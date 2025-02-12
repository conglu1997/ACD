import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'name': 'Amazon Rainforest',
                'key_species': ['Jaguar', 'Harpy Eagle', 'Giant Otter'],
                'threats': ['Deforestation', 'Climate Change', 'Poaching'],
                'quantum_property': 'Superposition'
            },
            {
                'name': 'Great Barrier Reef',
                'key_species': ['Clownfish', 'Green Sea Turtle', 'Dugong'],
                'threats': ['Ocean Acidification', 'Coral Bleaching', 'Overfishing'],
                'quantum_property': 'Entanglement'
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(ecosystems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for modeling and preserving biodiversity in the {t['name']} ecosystem, incorporating principles from quantum computing, ecology, and machine learning. Your system should utilize the quantum property of {t['quantum_property']}. Provide your response in the following format:

1. Quantum-Inspired AI Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how you incorporate the quantum property of {t['quantum_property']} into your AI architecture.
   c) Detail how your system integrates ecological data and machine learning algorithms.
   d) Discuss any novel approaches or algorithms used in your design.

2. Biodiversity Modeling (250-300 words):
   a) Explain how your system models the complex interactions within the {t['name']} ecosystem.
   b) Describe how it incorporates the following key species: {', '.join(t['key_species'])}.
   c) Detail how your system predicts the impact of the following threats: {', '.join(t['threats'])}.
   d) Discuss how quantum-inspired algorithms enhance the accuracy or efficiency of your biodiversity model.

3. Conservation Strategy Generation (250-300 words):
   a) Describe how your system generates and evaluates conservation strategies.
   b) Explain how it balances competing conservation priorities and resource constraints.
   c) Provide an example of a specific conservation strategy your system might propose.

4. Implementation and Scalability (200-250 words):
   a) Discuss the computational requirements for implementing your system.
   b) Explain how your approach could be scaled to model global biodiversity.
   c) Address any technical challenges in deploying your system in real-world conservation efforts.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss ethical implications of using quantum-inspired AI for biodiversity conservation.
   b) Address potential biases or limitations in your system's modeling and decision-making processes.
   c) Propose guidelines for responsible development and use of such systems in conservation biology.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system could contribute to advancements in quantum computing, AI, and ecology.
   b) Suggest potential applications of your approach in other scientific domains.
   c) Propose future research directions based on your system's approach.

Ensure your response demonstrates a deep understanding of quantum computing principles, ecological systems, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles, particularly {t['quantum_property']}, and how they can be applied to AI systems.",
            f"The biodiversity modeling approach effectively incorporates the key species ({', '.join(t['key_species'])}) and addresses the specified threats ({', '.join(t['threats'])}).",
            "The proposed quantum-inspired AI architecture is innovative, well-explained, and plausible given current technological capabilities.",
            "The conservation strategy generation process is logical, comprehensive, and considers real-world constraints and priorities.",
            "The response addresses ethical considerations and limitations thoughtfully, proposing specific guidelines for responsible development and use.",
            "The interdisciplinary implications are well-considered, with clear connections drawn between quantum computing, AI, and ecology.",
            "The overall response is well-structured, adhering to the specified format and word count, and demonstrates creative problem-solving and interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
