import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'focus': 'global atmospheric circulation',
                'quantum_feature': 'superposition',
                'climate_variable': 'temperature'
            },
            {
                'focus': 'ocean-atmosphere heat transfer',
                'quantum_feature': 'entanglement',
                'climate_variable': 'humidity'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm to simulate complex climate systems, focusing on modeling {t['focus']} and its interaction with other climate components. Your algorithm should leverage the quantum feature of {t['quantum_feature']} and primarily model the climate variable of {t['climate_variable']}. Your response should include:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the overall structure of your quantum algorithm for climate simulation.
   b) Explain how you utilize {t['quantum_feature']} in your algorithm design.
   c) Detail how your algorithm models {t['focus']} and its interactions.
   d) Discuss how you incorporate the modeling of {t['climate_variable']} into your quantum circuit.

2. Quantum-Classical Interface (250-300 words):
   a) Explain how your algorithm interfaces between quantum and classical computing components.
   b) Describe any pre-processing of climate data required for your quantum algorithm.
   c) Discuss how you handle the output from the quantum circuit and translate it into meaningful climate predictions.

3. Computational Advantages (200-250 words):
   a) Analyze the potential speed-up or improved accuracy of your quantum algorithm compared to classical methods.
   b) Discuss any limitations or challenges specific to quantum computing in this application.
   c) Explain how your approach might enable more complex or long-term climate simulations.

4. Climate Science Integration (250-300 words):
   a) Describe how your algorithm incorporates established climate models or theories.
   b) Explain how your approach might provide new insights into {t['focus']}.
   c) Discuss how your algorithm handles the complexity and chaos inherent in climate systems.

5. Validation and Testing (200-250 words):
   a) Propose methods to validate your quantum climate simulation algorithm.
   b) Describe potential experiments or comparisons with classical models to test your approach.
   c) Discuss the challenges in verifying the accuracy of quantum climate simulations.

6. Ethical Implications and Applications (150-200 words):
   a) Discuss the potential impacts of more accurate or efficient climate modeling on policy and society.
   b) Address any ethical considerations in the development and use of quantum computing for climate science.
   c) Propose guidelines for the responsible use of quantum climate simulations in decision-making.

7. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum climate simulation algorithm.
   b) Discuss how these improvements could enhance our understanding of climate systems or advance quantum computing applications.

Ensure your response demonstrates a deep understanding of quantum computing principles, climate science, and algorithm design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words. Include a brief summary (50-100 words) at the end of your response.

Your response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your algorithm design, and the thoroughness of your analysis across all sections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of quantum computing principles, particularly {t['quantum_feature']}.",
            f"The algorithm effectively models {t['focus']} and incorporates {t['climate_variable']} in a scientifically plausible manner.",
            "The quantum-classical interface is well-explained and addresses practical implementation challenges.",
            "The computational advantages of the quantum approach are clearly articulated and justified.",
            "The integration with established climate science is thorough and demonstrates deep understanding of climate systems.",
            "The validation methods and future directions proposed are innovative and scientifically sound.",
            "The ethical implications are thoughtfully considered and demonstrate an understanding of the broader impacts of this technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
