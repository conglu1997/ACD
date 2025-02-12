import random
from typing import List, Dict, Any

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ecosystem_type': 'Marine',
                'environmental_factor': 'Ocean acidification',
                'evolutionary_mechanism': 'Epigenetic inheritance',
                'system_property': 'Resilience',
                'initial_parameters': {
                    'population_sizes': {'Phytoplankton': 10000, 'Zooplankton': 5000, 'Small Fish': 1000, 'Large Fish': 100},
                    'pH_level': 8.1,
                    'temperature': 20
                }
            },
            {
                'ecosystem_type': 'Terrestrial',
                'environmental_factor': 'Increased atmospheric CO2',
                'evolutionary_mechanism': 'Horizontal gene transfer',
                'system_property': 'Biodiversity',
                'initial_parameters': {
                    'population_sizes': {'Grasses': 50000, 'Shrubs': 10000, 'Trees': 1000, 'Herbivores': 500, 'Carnivores': 50},
                    'CO2_level': 415,
                    'temperature': 25
                }
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated digital ecosystem that evolves over time, incorporating principles from evolutionary biology, artificial life, and complex systems theory. Your ecosystem should be based on the following parameters:

Ecosystem Type: {t['ecosystem_type']}
Environmental Factor: {t['environmental_factor']}
Evolutionary Mechanism: {t['evolutionary_mechanism']}
System Property to Analyze: {t['system_property']}
Initial Parameters: {t['initial_parameters']}

Your response should include the following sections:

1. Ecosystem Design (300-350 words):
   a) Describe the key components of your digital ecosystem, including types of organisms and their interactions.
   b) Explain how you model the specified environmental factor and its effects on the ecosystem.
   c) Detail how you implement the given evolutionary mechanism in your simulation.
   d) Provide a diagram or detailed text description of your ecosystem's structure and interactions.

2. Simulation Architecture (250-300 words):
   a) Outline the main algorithms or computational techniques used in your simulation.
   b) Explain how you model time and generations in your ecosystem.
   c) Describe how you handle interactions between organisms and their environment.
   d) Discuss any novel approaches you've developed for this simulation.

3. Evolutionary Dynamics (250-300 words):
   a) Explain how evolution occurs in your simulated ecosystem.
   b) Describe how the specified evolutionary mechanism influences the system's development.
   c) Discuss how your simulation accounts for factors like genetic drift, selection pressure, and adaptation.
   d) Provide an example of how a specific trait might evolve in response to the environmental factor.

4. System Analysis (200-250 words):
   a) Describe how you measure and analyze the specified system property in your simulation.
   b) Explain any patterns or emergent behaviors you would expect to observe.
   c) Discuss how the environmental factor and evolutionary mechanism might influence this property.
   d) Propose a hypothesis about how this property might change over time in your simulation.

5. Implications and Applications (200-250 words):
   a) Discuss the potential insights your simulation could provide for real-world ecosystems.
   b) Explore how your model could be used to predict or understand the effects of environmental changes.
   c) Suggest potential applications of your simulation in fields like conservation biology or climate science.

6. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your simulation and how they might affect its results.
   b) Propose potential improvements or extensions to your model.
   c) Suggest a novel research question that could be explored using your simulation.

7. Reflection (100-150 words):
   a) Discuss the most challenging aspect of designing this digital ecosystem simulation.
   b) Reflect on how this task has influenced your understanding of ecosystem dynamics and evolution.
   c) Suggest one way this simulation could be extended to explore additional aspects of complex adaptive systems.

Ensure your response demonstrates a deep understanding of evolutionary biology, artificial life, and complex systems theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Adhere to the word limits for each section to maintain conciseness and focus. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, artificial life, and complex systems theory.",
            "The ecosystem design is creative, coherent, and accurately incorporates the given parameters, including the initial conditions.",
            "The simulation architecture is well-thought-out and uses appropriate computational techniques for modeling complex systems.",
            "The evolutionary dynamics are clearly explained, scientifically plausible, and correctly implement the specified evolutionary mechanism.",
            "The system analysis shows insightful understanding of the specified system property and potential emergent behaviors.",
            "The implications and applications section demonstrates the ability to connect the simulation to real-world issues and potential scientific applications.",
            "The limitations and future directions show critical thinking and the ability to extend the research.",
            "The reflection section demonstrates deep engagement with the task and insights into the challenges of modeling complex adaptive systems.",
            "The overall response is well-structured, using appropriate terminology and clear explanations, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
