import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        protocell_types = ['Lipid vesicles', 'Coacervates', 'Polymersomes']
        ai_architectures = ['Neural networks', 'Evolutionary algorithms', 'Reinforcement learning']
        emergent_properties = ['Self-replication', 'Metabolism', 'Information processing', 'Adaptation']
        
        tasks = [
            {
                'protocell_type': random.choice(protocell_types),
                'ai_architecture': random.choice(ai_architectures),
                'emergent_property': random.choice(emergent_properties)
            },
            {
                'protocell_type': random.choice(protocell_types),
                'ai_architecture': random.choice(ai_architectures),
                'emergent_property': random.choice(emergent_properties)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical hybrid system that combines synthetic biology protocells with artificial intelligence to create a new form of artificial life. Your system should use {t['protocell_type']} as the protocell base and {t['ai_architecture']} as the AI component. The system should demonstrate the emergent property of {t['emergent_property']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your hybrid protocell-AI system.
   b) Explain how the protocell and AI components interact and integrate.
   c) Detail the mechanisms that enable the specified emergent property.
   d) Discuss any novel techniques or approaches used in your design.

   Example: For a system using lipid vesicles and neural networks aiming for self-replication, you might describe how the neural network controls the synthesis of lipids and other essential components within the vesicle, leading to growth and division.

2. Biological-Artificial Interface (250-300 words):
   a) Explain how information is exchanged between the biological and artificial components.
   b) Describe how the AI system influences or controls the protocell's behavior.
   c) Discuss any challenges in creating a seamless interface between the two components and how you address them.

3. Emergent Behavior Analysis (200-250 words):
   a) Analyze how the specified emergent property arises from the interaction of the protocell and AI components.
   b) Compare this emergent behavior to similar phenomena in natural biological systems.
   c) Discuss the implications of this emergent property for our understanding of life and intelligence.

4. Experimental Proposal (200-250 words):
   a) Propose a series of experiments to test and validate your hybrid system's capabilities.
   b) Describe the expected outcomes and how they would demonstrate the system's unique properties.
   c) Discuss any ethical considerations in conducting these experiments.

5. Philosophical Implications (200-250 words):
   a) Analyze how your hybrid system challenges or extends current definitions of life and intelligence.
   b) Discuss the implications of your system for the concept of artificial consciousness.
   c) Explore potential societal impacts of creating such hybrid biological-artificial entities.

6. Future Developments and Applications (150-200 words):
   a) Propose potential future enhancements or extensions of your hybrid system.
   b) Discuss possible applications in fields such as medicine, environmental science, or space exploration.
   c) Speculate on how this technology might evolve over the next few decades.

Ensure your response demonstrates a deep understanding of synthetic biology, artificial intelligence, and philosophy of mind. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, artificial intelligence, and philosophy of mind.",
            "The hybrid system design is innovative, coherent, and integrates protocells and AI in a plausible manner.",
            "The explanation of the biological-artificial interface is clear and addresses potential challenges.",
            "The analysis of emergent behavior is insightful and well-reasoned.",
            "The experimental proposal is well-designed and addresses ethical considerations.",
            "The discussion of philosophical implications is thoughtful and explores key questions in the philosophy of mind and artificial life.",
            "The proposed future developments and applications are creative and plausible.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
