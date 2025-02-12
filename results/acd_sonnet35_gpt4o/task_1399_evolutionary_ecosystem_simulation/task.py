import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                'environment': 'Extreme heat desert',
                'key_resource': 'Water',
                'evolutionary_pressure': 'Radiation resistance'
            },
            {
                'environment': 'Deep sea thermal vent',
                'key_resource': 'Chemical energy',
                'evolutionary_pressure': 'High pressure adaptation'
            },
            {
                'environment': 'Floating sky ecosystem',
                'key_resource': 'Sunlight',
                'evolutionary_pressure': 'Gravity manipulation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated ecosystem with evolving artificial life forms in a {t['environment']} environment. Your simulation should incorporate principles from evolutionary biology and complex systems theory. The key resource in this environment is {t['key_resource']}, and the main evolutionary pressure is {t['evolutionary_pressure']}. Your response should include:

1. Ecosystem Design (250-300 words):
   a) Describe the overall structure and key components of your simulated ecosystem.
   b) Explain how you model the availability and distribution of the key resource.
   c) Detail how you implement the specified evolutionary pressure in your simulation.
   d) Discuss any unique features or challenges of the given environment.

2. Artificial Life Forms (200-250 words):
   a) Design at least three distinct types of artificial life forms that could evolve in this ecosystem.
   b) Explain their basic structures, behaviors, and how they interact with the environment and each other.
   c) Describe how these life forms compete for or utilize the key resource.
   d) Explain how these life forms might adapt to the main evolutionary pressure over time.

3. Evolutionary Mechanisms (200-250 words):
   a) Detail the genetic representation you use for your artificial life forms.
   b) Explain the mechanisms of mutation, recombination, and selection in your simulation.
   c) Describe how you model fitness and reproductive success in this ecosystem.
   d) Discuss any unique evolutionary strategies that might emerge in this environment.

4. Complex Systems Analysis (200-250 words):
   a) Identify and explain at least three emergent phenomena that could arise in your ecosystem.
   b) Discuss how you model and analyze feedback loops within the system.
   c) Explain how you would measure and analyze the overall stability and diversity of the ecosystem.
   d) Describe any potential tipping points or critical thresholds in your simulated ecosystem.

5. Simulation Implementation (150-200 words):
   a) Provide a high-level overview of how you would implement this simulation computationally.
   b) Discuss any key algorithms or data structures you would use.
   c) Explain how you would balance computational efficiency with biological realism.
   d) Describe how you would visualize or represent the results of your simulation.

6. Scientific Implications (150-200 words):
   a) Discuss how your simulation could contribute to our understanding of real-world ecosystems or evolutionary processes.
   b) Propose a specific hypothesis that could be tested using your simulation.
   c) Explain how results from your simulation could inform conservation efforts or ecological management strategies.
   d) Discuss any limitations of your model in representing real-world evolutionary processes.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of creating and manipulating simulated ecosystems and artificial life.
   b) Propose guidelines for the responsible development and use of such simulations in scientific research.
   c) Suggest potential extensions or modifications to your simulation for future research.
   d) Speculate on how this type of simulation might impact our understanding of life and evolution in the long term.

Ensure your response demonstrates a deep understanding of evolutionary biology, complex systems theory, and computational modeling. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility and addressing the specified environmental conditions and evolutionary pressures.

Format your response using clear headings for each section. Your total response should be between 1300-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, complex systems theory, and computational modeling.",
            "The ecosystem design effectively incorporates the specified environment, key resource, and evolutionary pressure.",
            "The artificial life forms are creatively designed and plausibly adapted to the given environment.",
            "The evolutionary mechanisms are well-explained and scientifically sound.",
            "The complex systems analysis identifies relevant emergent phenomena and system dynamics.",
            "The simulation implementation overview is clear and computationally feasible.",
            "The scientific implications and proposed hypothesis are meaningful and well-reasoned.",
            "Ethical considerations are thoughtfully addressed.",
            "The response uses technical terminology appropriately and provides clear explanations for complex concepts.",
            "The overall response demonstrates strong interdisciplinary knowledge integration, creative problem-solving, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
