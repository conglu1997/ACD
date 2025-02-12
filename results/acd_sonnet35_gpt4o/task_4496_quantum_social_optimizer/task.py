import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        societal_issues = [
            "Climate change mitigation",
            "Global food security",
            "Pandemic preparedness",
            "Urban transportation optimization"
        ]
        quantum_algorithms = [
            "Quantum annealing",
            "Quantum approximate optimization algorithm (QAOA)",
            "Variational quantum eigensolver (VQE)",
            "Quantum amplitude estimation"
        ]
        return {
            "1": {
                "issue": random.choice(societal_issues),
                "algorithm": random.choice(quantum_algorithms)
            },
            "2": {
                "issue": random.choice(societal_issues),
                "algorithm": random.choice(quantum_algorithms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to optimize solutions for the societal issue of {t['issue']} using the {t['algorithm']} quantum algorithm. Your response should include the following sections:

1. Problem Formulation (250-300 words):
   a) Analyze the complexities of {t['issue']} and why it's challenging to solve with classical computing.
   b) Identify specific aspects of the problem that make it suitable for quantum optimization.
   c) Describe how you would model this problem in a way that can be addressed by quantum computing.

2. Quantum System Design (300-350 words):
   a) Explain the basic principles of {t['algorithm']} and why it's appropriate for this problem.
   b) Describe the key components of your quantum computing system, including both hardware and software elements.
   c) Detail how your system implements {t['algorithm']} to address {t['issue']}.
   d) Discuss any novel approaches you've incorporated to enhance the algorithm's effectiveness for this specific problem.

3. Optimization Process (250-300 words):
   a) Outline the steps your quantum system would take to optimize solutions for {t['issue']}.
   b) Explain how the quantum nature of the system provides advantages over classical approaches.
   c) Describe how you would interpret and translate the quantum results into actionable solutions.
   d) Discuss potential limitations of your approach and how you might address them.

4. Comparative Analysis (200-250 words):
   a) Compare the expected performance of your quantum system to current classical methods for addressing {t['issue']}.
   b) Estimate the potential impact of your system in terms of solution quality and computational efficiency.
   c) Discuss any trade-offs between your quantum approach and classical methods.

5. Ethical and Societal Implications (200-250 words):
   a) Analyze potential ethical concerns related to using quantum computing for {t['issue']}.
   b) Discuss how the implementation of quantum-optimized solutions might affect different stakeholders.
   c) Propose guidelines for responsible development and use of quantum systems for societal problem-solving.

6. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum system.
   b) Discuss how advances in quantum hardware might enhance your system's capabilities.
   c) Propose a related societal issue that could benefit from a similar quantum approach.

Ensure your response demonstrates a deep understanding of quantum computing, {t['algorithm']}, and the complexities of {t['issue']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of quantum computing principles, especially {t['algorithm']}.",
            f"The proposed system effectively addresses the complexities of {t['issue']} using quantum optimization.",
            "The solution is innovative yet scientifically plausible.",
            "The response thoroughly addresses ethical considerations and societal impacts.",
            "The writing is clear, well-structured, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
