import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                'planet_type': 'Gas giant',
                'energy_source': 'Electromagnetic fields',
                'physical_state': 'Plasma'
            },
            {
                'planet_type': 'Ocean world',
                'energy_source': 'Geothermal vents',
                'physical_state': 'Liquid'
            },
            {
                'planet_type': 'Tidally locked planet',
                'energy_source': 'Stellar radiation',
                'physical_state': 'Crystalline'
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical alien ecosystem based on a novel form of information exchange for a {t['planet_type']} with {t['energy_source']} as the primary energy source and organisms existing primarily in a {t['physical_state']} state. Your response should include:

1. Ecosystem Overview (200-250 words):
   a) Describe the key characteristics of your alien ecosystem.
   b) Explain how the environment shapes the organisms and their information exchange.
   c) Discuss the primary forms of life and their roles in the ecosystem.

2. Information Exchange Mechanism (250-300 words):
   a) Detail the novel form of information exchange used by the organisms.
   b) Explain how this mechanism is adapted to the planet's environment.
   c) Discuss how the energy source is utilized in this information exchange.
   d) Provide a simple diagram or equation representing this mechanism.

3. Evolutionary Implications (200-250 words):
   a) Describe how this form of information exchange might have evolved.
   b) Discuss its advantages and limitations compared to Earth-based biological information systems.
   c) Speculate on potential future evolutionary paths for this ecosystem.

4. Ecological Interactions (200-250 words):
   a) Explain how different organisms in the ecosystem interact using this information exchange.
   b) Describe at least one symbiotic relationship facilitated by this mechanism.
   c) Discuss how the ecosystem maintains balance and handles perturbations.

5. Astrobiological Significance (150-200 words):
   a) Analyze the implications of this ecosystem for our understanding of potential extraterrestrial life.
   b) Discuss how we might detect or study such an ecosystem from Earth.
   c) Propose a hypothesis about the prevalence of similar systems in the universe.

6. Technological Applications (150-200 words):
   a) Suggest two potential technological applications inspired by this alien information exchange system.
   b) Briefly describe how these technologies might be developed and their potential impact.

Ensure your response demonstrates a deep understanding of biology, information theory, and astrobiology. Use scientific terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, information theory, and astrobiology.",
            "The ecosystem design is creative, original, and scientifically plausible given the specified environment.",
            "The information exchange mechanism is novel, well-explained, and adapted to the planet's environment.",
            "Evolutionary implications and ecological interactions are thoroughly discussed and logically consistent.",
            "The astrobiological significance and technological applications are insightful and well-reasoned.",
            "The response includes all required sections with appropriate detail and word count.",
            "Scientific terminology is used appropriately and explanations are provided where necessary.",
            "The response includes a diagram or equation representing the information exchange mechanism.",
            "The design demonstrates interdisciplinary knowledge synthesis and creative scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
