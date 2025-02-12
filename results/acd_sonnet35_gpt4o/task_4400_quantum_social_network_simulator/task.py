import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "spread of misinformation during a global pandemic",
            "adoption of a new technology in a competitive market",
            "emergence of social movements in response to climate change",
            "formation of political coalitions in a multi-party system",
            "diffusion of cultural trends across diverse communities"
        ]
        quantum_concepts = [
            "quantum superposition",
            "quantum entanglement",
            "quantum annealing",
            "quantum walks",
            "quantum Fourier transform"
        ]
        social_network_properties = [
            "small-world effect",
            "scale-free degree distribution",
            "community structure",
            "homophily",
            "weak ties"
        ]
        return {
            "1": {
                "scenario": random.choice(scenarios),
                "quantum_concept": random.choice(quantum_concepts),
                "network_property": random.choice(social_network_properties)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "quantum_concept": random.choice(quantum_concepts),
                "network_property": random.choice(social_network_properties)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based system to simulate and analyze complex social networks and their evolution, then use it to predict the spread of information or behaviors in the following scenario: {t['scenario']}. Your system should specifically incorporate the quantum computing concept of {t['quantum_concept']} and address the social network property of {t['network_property']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum social network simulator.
   b) Explain how your system integrates quantum computing principles with social network analysis.
   c) Detail how you incorporate {t['quantum_concept']} into your model.
   d) Include a diagram or flowchart of your system architecture (describe it in words if you can't generate images).

2. Quantum-Social Network Mapping (250-300 words):
   a) Explain how your system maps social network structures and dynamics to quantum states or processes.
   b) Describe how you model {t['network_property']} using quantum computing techniques.
   c) Discuss any challenges in this mapping process and how your system addresses them.

3. Simulation Process (250-300 words):
   a) Detail the step-by-step process of how your system simulates the evolution of social networks.
   b) Explain how your system handles the complexity and scale of real-world social networks.
   c) Describe how you implement {t['quantum_concept']} in the simulation process.

4. Prediction and Analysis for the Given Scenario (200-250 words):
   a) Apply your quantum social network simulator to the scenario: {t['scenario']}.
   b) Describe the specific predictions your system would make about information or behavior spread.
   c) Explain how {t['network_property']} influences these predictions.

5. Advantages and Limitations (200-250 words):
   a) Discuss the potential advantages of your quantum-based approach over classical social network analysis methods.
   b) Identify limitations of your system and areas for future improvement.
   c) Consider the scalability and real-world applicability of your approach.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss potential ethical implications of using quantum computing to simulate and predict social behaviors.
   b) Address privacy concerns and propose guidelines for responsible use of such technology.
   c) Speculate on the potential societal impacts of highly accurate social behavior predictions.

Ensure your response demonstrates a deep understanding of quantum computing, social network theory, and complex systems analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Demonstrates a deep understanding of quantum computing principles, social network theory, and complex systems analysis",
            f"Effectively incorporates the quantum computing concept of {t['quantum_concept']} into the system design",
            f"Adequately addresses the social network property of {t['network_property']}",
            "Provides a detailed and plausible system architecture for quantum social network simulation",
            "Clearly explains the mapping between quantum states/processes and social network structures/dynamics",
            f"Applies the system to the given scenario ({t['scenario']}) with specific, well-reasoned predictions",
            "Discusses advantages, limitations, ethical considerations, and potential societal impacts of the proposed system",
            "Uses appropriate technical terminology and provides clear explanations for complex concepts",
            "Demonstrates creativity and innovation while maintaining scientific plausibility",
            "Adheres to the specified word count and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
