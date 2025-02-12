import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cellular_processes = ['glycolysis', 'citric acid cycle', 'electron transport chain', 'photosynthesis', 'protein synthesis']
        quantum_algorithms = ['quantum annealing', 'variational quantum eigensolver', 'quantum approximate optimization algorithm', 'quantum walks']
        applications = ['drug discovery', 'biofuel production', 'personalized nutrition', 'environmental bioremediation']
        
        return {
            "1": {
                "cellular_process": random.choice(cellular_processes),
                "quantum_algorithm": random.choice(quantum_algorithms),
                "application": random.choice(applications)
            },
            "2": {
                "cellular_process": random.choice(cellular_processes),
                "quantum_algorithm": random.choice(quantum_algorithms),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to model and optimize the {t['cellular_process']} process in cells, using principles inspired by {t['quantum_algorithm']}. The system should be applicable to {t['application']}. Your response should include the following sections:

1. Quantum-Cellular Interface (250-300 words):
   a) Explain how you will represent the {t['cellular_process']} using quantum-inspired data structures.
   b) Describe how {t['quantum_algorithm']} can be adapted to process and optimize this biological data.
   c) Discuss any challenges in mapping cellular processes to quantum-inspired algorithms and how you address them.

2. System Architecture (200-250 words):
   a) Outline the key components of your quantum-inspired cellular optimization system.
   b) Explain how these components interact to model and optimize the {t['cellular_process']}.
   c) Describe any novel techniques or algorithms you would employ in your system.

3. Optimization Strategy (250-300 words):
   a) Detail the process by which your system would optimize the {t['cellular_process']}.
   b) Explain how quantum-inspired computations enhance this optimization compared to classical approaches.
   c) Describe how you would validate the results of your quantum-inspired optimization.

4. Application to {t['application']} (200-250 words):
   a) Discuss how your optimized cellular model could be applied to {t['application']}.
   b) Explain the potential benefits and challenges of using this approach in this specific application.
   c) Propose a hypothesis that could be tested using the results of your optimization.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical implications of optimizing cellular processes for {t['application']}.
   b) Suggest ways to address these ethical concerns in the development and application of your system.
   c) Propose one potential future extension or application of your quantum-inspired cellular optimization system.

Ensure your response demonstrates a deep understanding of quantum computing principles, cellular biology, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['cellular_process']} and how it can be modeled using quantum-inspired algorithms.",
            f"The system architecture effectively integrates quantum-inspired computing with cellular biology for optimization purposes.",
            f"The optimization strategy for {t['cellular_process']} is well-explained and leverages the advantages of quantum-inspired algorithms.",
            f"The application to {t['application']} is thoughtfully discussed, including potential benefits and challenges.",
            "The ethical considerations are thoroughly addressed, and future directions are insightful and relevant.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The explanation uses appropriate technical terminology from quantum computing, biology, and AI fields.",
            "The response is well-structured, coherent, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
