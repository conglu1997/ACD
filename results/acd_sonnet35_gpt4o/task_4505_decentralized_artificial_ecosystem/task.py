import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        resources = ['water', 'oxygen', 'food', 'energy', 'waste management']
        colony_sizes = [100, 500, 1000, 5000]
        environmental_challenges = ['radiation', 'microgravity', 'dust storms', 'temperature fluctuations']
        return {
            "1": {
                "resources": random.sample(resources, 3),
                "colony_size": random.choice(colony_sizes),
                "challenge": random.choice(environmental_challenges)
            },
            "2": {
                "resources": random.sample(resources, 3),
                "colony_size": random.choice(colony_sizes),
                "challenge": random.choice(environmental_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a decentralized artificial ecosystem using blockchain technology and complex adaptive systems principles to simulate and optimize resource allocation in a hypothetical space colony. Your ecosystem should focus on managing the following resources: {', '.join(t['resources'])}. The colony has a population of {t['colony_size']} and faces the environmental challenge of {t['challenge']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your decentralized artificial ecosystem.
   b) Explain how blockchain technology is integrated into the system.
   c) Detail how complex adaptive systems principles are applied to resource management.
   d) Provide a high-level diagram or pseudocode snippet illustrating a key component of your system.

2. Resource Allocation Mechanism (250-300 words):
   a) Explain how your system optimizes the allocation of the specified resources.
   b) Describe how the system adapts to changing demands and environmental conditions.
   c) Discuss how decentralization enhances resource management efficiency.

3. Environmental Challenge Adaptation (200-250 words):
   a) Detail how your system addresses the specified environmental challenge.
   b) Explain how the artificial ecosystem evolves to mitigate the impact of this challenge.
   c) Propose a novel approach to leveraging the challenge for potential benefits.

4. Blockchain Implementation (250-300 words):
   a) Describe the structure of your blockchain and its role in the ecosystem.
   b) Explain how smart contracts are used to automate resource allocation and decision-making.
   c) Discuss security measures to protect the integrity of the ecosystem.

5. Simulation and Optimization (200-250 words):
   a) Propose a method for simulating the artificial ecosystem's performance.
   b) Describe key metrics for evaluating the system's efficiency and adaptability.
   c) Explain how machine learning could be integrated to further optimize the ecosystem.

6. Ethical Considerations and Governance (150-200 words):
   a) Discuss potential ethical issues in using a decentralized AI system to manage critical resources.
   b) Propose a governance model for the artificial ecosystem that balances efficiency with fairness.
   c) Address potential risks and unintended consequences of the system.

Ensure your response demonstrates a deep understanding of blockchain technology, complex adaptive systems, and space colonization challenges. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use numbered lists where appropriate. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively addresses the management of {', '.join(t['resources'])} for a colony of {t['colony_size']} facing {t['challenge']}",
            "The system architecture demonstrates a clear integration of blockchain technology and complex adaptive systems principles",
            "The resource allocation mechanism is well-explained and adapts to changing conditions",
            "The blockchain implementation is detailed and includes smart contract usage",
            "The simulation and optimization methods are clearly described with relevant metrics",
            "Ethical considerations and governance models are thoughtfully addressed",
            "The response is creative, scientifically plausible, and demonstrates interdisciplinary knowledge"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
