import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'biological_process': 'photosynthesis',
                'quantum_effect': 'quantum coherence',
                'evolutionary_goal': 'increase energy efficiency',
                'environmental_factor': 'varying light intensity'
            },
            {
                'biological_process': 'enzyme catalysis',
                'quantum_effect': 'quantum tunneling',
                'evolutionary_goal': 'optimize reaction rates',
                'environmental_factor': 'fluctuating temperature'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired artificial intelligence system that simulates and optimizes the biological evolution of {t['biological_process']} at the molecular level. Your system should incorporate the quantum effect of {t['quantum_effect']} and use evolutionary computation techniques to {t['evolutionary_goal']}, while considering the environmental factor of {t['environmental_factor']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-bio-AI evolution simulator.
   b) Explain how quantum biology principles are integrated into the system.
   c) Detail how evolutionary computation and machine learning techniques are implemented.
   d) Discuss any novel approaches or algorithms you've incorporated.

2. Quantum-Biological Modeling (250-300 words):
   a) Explain how {t['quantum_effect']} is modeled in your system for {t['biological_process']}.
   b) Describe how quantum effects are integrated with classical biological processes.
   c) Discuss any approximations or simplifications made in the quantum-biological simulations.

3. Evolutionary Optimization Process (250-300 words):
   a) Detail how your system simulates and optimizes the evolution of {t['biological_process']}.
   b) Explain the key parameters and fitness functions used in the evolutionary algorithm.
   c) Describe how quantum effects influence the evolutionary process in your model.
   d) Explain how your system accounts for {t['environmental_factor']} in the evolutionary process.

4. Machine Learning Integration (200-250 words):
   a) Explain how machine learning is used to enhance the evolutionary optimization.
   b) Describe any predictive models or decision-making components in your system.
   c) Discuss how the ML components interact with the quantum-biological simulations.

5. Performance Evaluation (200-250 words):
   a) Propose methods to validate your system's predictions and optimizations.
   b) Discuss how you would benchmark your system against existing approaches.
   c) Address potential limitations and propose strategies to overcome them.

6. Case Study (200-250 words):
   Provide a specific example of how your system would be applied to optimize {t['biological_process']} under varying conditions of {t['environmental_factor']}. Include details on:
   a) Initial conditions and parameters
   b) Simulated evolutionary trajectory
   c) Predicted optimizations and their potential impact

7. Implications and Future Directions (150-200 words):
   a) Discuss the potential impact of your system on understanding and optimizing {t['biological_process']}.
   b) Explore possible applications in fields such as bioengineering or drug design.
   c) Propose future extensions or improvements to your quantum-bio-AI evolution simulator.

Ensure your response demonstrates a deep understanding of quantum biology, evolutionary computation, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each subsection with the corresponding letter. Your total response should be between 1550-1850 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum biology, particularly {t['quantum_effect']} in the context of {t['biological_process']}.",
            "The system architecture effectively integrates principles from quantum biology, evolutionary computation, and machine learning.",
            f"The evolutionary optimization process is well-designed to {t['evolutionary_goal']} for {t['biological_process']}, considering {t['environmental_factor']}.",
            "The case study provides a concrete and plausible example of the system's application.",
            "The response shows creativity and innovation in combining multiple complex scientific domains.",
            "The proposed system is scientifically plausible and addresses potential limitations and challenges.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
