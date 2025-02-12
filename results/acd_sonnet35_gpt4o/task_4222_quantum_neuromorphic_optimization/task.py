import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_problems = [
            {
                "problem": "Protein folding prediction",
                "domain": "Computational biology",
                "constraint": "Energy minimization"
            },
            {
                "problem": "Supply chain optimization",
                "domain": "Logistics",
                "constraint": "Real-time adaptability"
            },
            {
                "problem": "Financial portfolio optimization",
                "domain": "Quantitative finance",
                "constraint": "Risk management"
            },
            {
                "problem": "Drug discovery",
                "domain": "Pharmaceutical research",
                "constraint": "Multi-objective optimization"
            }
        ]
        return {
            "1": random.choice(optimization_problems),
            "2": random.choice(optimization_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-neuromorphic computing system for solving the complex optimization problem of {t['problem']} in the domain of {t['domain']}, with a focus on addressing the constraint of {t['constraint']}. 

A quantum-neuromorphic system combines quantum computing principles (such as superposition and entanglement) with neuromorphic engineering (brain-inspired computing architectures) to create a novel computational paradigm.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your hybrid quantum-neuromorphic system.
   b) Explain how quantum and neuromorphic elements are integrated.
   c) Detail how your system addresses the specified optimization problem and constraint.
   d) Include a high-level diagram or pseudocode representing the system's architecture.

2. Quantum-Neuromorphic Integration (250-300 words):
   a) Discuss how quantum principles enhance neuromorphic computing in your system.
   b) Explain any novel quantum-inspired algorithms or neuromorphic circuits in your design.
   c) Analyze potential challenges in integrating quantum and neuromorphic components and how you address them.

3. Optimization Approach (250-300 words):
   a) Describe your system's approach to solving the specified optimization problem.
   b) Explain how it leverages quantum and neuromorphic properties to improve upon classical methods.
   c) Discuss how your system handles the given constraint.
   d) Provide a mathematical formulation or pseudocode for a key optimization algorithm in your system.

4. Performance Analysis (200-250 words):
   a) Predict the potential performance improvements of your system compared to classical approaches.
   b) Discuss any trade-offs or limitations in your design.
   c) Propose a method to benchmark your system against existing optimization techniques.

5. Broader Applications (200-250 words):
   a) Suggest two other optimization problems your system could potentially solve.
   b) Discuss how your system might be adapted to these new problems.
   c) Analyze the potential impact of your system on the field of {t['domain']}.

6. Ethical and Practical Considerations (150-200 words):
   a) Discuss any ethical implications of using quantum-neuromorphic systems for optimization in {t['domain']}.
   b) Address potential risks or challenges in implementing your system in real-world scenarios.
   c) Propose guidelines for the responsible development and use of such hybrid computing systems.

Ensure your response demonstrates a deep understanding of quantum computing, neuromorphic engineering, and optimization theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing, neuromorphic engineering, and optimization theory.",
            "The proposed system effectively integrates quantum and neuromorphic elements to address the specified optimization problem and constraint.",
            "The optimization approach leverages quantum and neuromorphic properties to improve upon classical methods.",
            "The performance analysis and broader applications are well-reasoned and plausible.",
            "Ethical and practical considerations are thoughtfully addressed.",
            "The response is well-structured, innovative, and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
