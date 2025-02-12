import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'type': 'Coral Reef',
                'climate_factor': 'Ocean Acidification',
                'evolutionary_focus': 'Symbiotic Relationships',
                'scenario': 'Predict the impact on coral-algae symbiosis over the next 50 years'
            },
            {
                'type': 'Tropical Rainforest',
                'climate_factor': 'Increasing Temperature',
                'evolutionary_focus': 'Species Adaptation Rate',
                'scenario': 'Model the changes in tree species composition over the next century'
            },
            {
                'type': 'Arctic Tundra',
                'climate_factor': 'Permafrost Thawing',
                'evolutionary_focus': 'Genetic Diversity',
                'scenario': 'Simulate the genetic bottleneck effect on keystone species over 200 years'
            },
            {
                'type': 'Grassland Savanna',
                'climate_factor': 'Changing Precipitation Patterns',
                'evolutionary_focus': 'Interspecies Competition',
                'scenario': 'Forecast shifts in herbivore-plant dynamics over the next 75 years'
            }
        ]
        selected = random.sample(ecosystems, 2)
        return {str(i+1): selected[i] for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered ecosystem simulation that incorporates principles of evolutionary biology to model and predict the effects of climate change on biodiversity. Focus on a {t['type']} ecosystem, with particular attention to the climate factor of {t['climate_factor']} and the evolutionary focus of {t['evolutionary_focus']}. Your specific task is to {t['scenario']}.

Provide your response in the following format:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI-powered ecosystem simulation.
   b) Explain how your system integrates evolutionary algorithms with climate models.
   c) Detail the data inputs and outputs of your system.
   d) Discuss how your AI learns and adapts its predictions over time.
   e) Include a high-level diagram or pseudocode snippet illustrating a key aspect of your system.

2. Evolutionary Model (250-300 words):
   a) Explain how your model represents {t['evolutionary_focus']} in the context of {t['type']} ecosystems.
   b) Describe the genetic algorithms or other evolutionary computation techniques used.
   c) Discuss how your model handles speciation, extinction, and adaptation events.
   d) Provide an example of how a specific species or trait might evolve in your model.

3. Climate Integration (200-250 words):
   a) Detail how your system models the effects of {t['climate_factor']} on the {t['type']} ecosystem.
   b) Explain how climate data is incorporated into the evolutionary simulations.
   c) Discuss any feedback loops between ecosystem changes and local climate conditions in your model.

4. Biodiversity Metrics and Predictive Capabilities (250-300 words):
   a) Describe the metrics your system uses to quantify biodiversity.
   b) Explain how these metrics account for genetic, species, and ecosystem diversity.
   c) Discuss how your system tracks changes in biodiversity over simulated time.
   d) Explain how your system generates predictions about future biodiversity under different climate scenarios.
   e) Describe any novel insights your system might provide about {t['evolutionary_focus']} in response to {t['climate_factor']}.
   f) Discuss the limitations and uncertainties in your system's predictive capabilities.

5. Ethical Considerations and Applications (150-200 words):
   a) Discuss the potential applications of your system in conservation biology and climate change mitigation.
   b) Address any ethical concerns related to using AI to model and predict ecosystem changes.
   c) Propose guidelines for the responsible use of AI in biodiversity and climate research.

Ensure your response demonstrates a deep understanding of artificial intelligence, evolutionary biology, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1150-1400 words. Begin each section with the provided numbering and lettering scheme."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response provides a comprehensive AI system architecture for simulating a {t['type']} ecosystem, integrating evolutionary algorithms with climate models, and includes a diagram or pseudocode snippet. (0.2 points)",
            f"The evolutionary model effectively represents {t['evolutionary_focus']}, incorporates appropriate evolutionary computation techniques, and provides a specific example of evolution in the model. (0.2 points)",
            f"The climate integration accurately models the effects of {t['climate_factor']} on the ecosystem and incorporates it into evolutionary simulations. (0.15 points)",
            "The biodiversity metrics and predictive capabilities are well-defined, accounting for genetic, species, and ecosystem diversity, and clearly explain the system's predictions and limitations. (0.2 points)",
            "Ethical considerations and potential applications are thoughtfully discussed, with proposed guidelines for responsible use. (0.15 points)",
            "The response demonstrates a deep understanding of AI, evolutionary biology, and climate science, using appropriate technical terminology and maintaining scientific plausibility. (0.1 points)",
            "The response adheres to the specified format, section structure, and word count (between 1150-1400 words). (0.1 points)"
        ]
        score = sum([float(c.split('(')[-1].split()[0]) for c in criteria if eval_with_llm_judge(instructions, submission, [c])])
        return min(1.0, max(0.0, score))
