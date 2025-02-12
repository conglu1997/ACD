import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'name': 'Coral Reef',
                'key_species': ['coral polyps', 'parrotfish', 'zooplankton'],
                'environmental_factors': ['water temperature', 'ocean acidity', 'light penetration']
            },
            {
                'name': 'Tropical Rainforest',
                'key_species': ['emergent trees', 'epiphytes', 'jaguars'],
                'environmental_factors': ['rainfall', 'soil composition', 'canopy cover']
            },
            {
                'name': 'Arctic Tundra',
                'key_species': ['caribou', 'arctic fox', 'lichen'],
                'environmental_factors': ['permafrost depth', 'snow cover', 'wind speed']
            },
            {
                'name': 'Savanna Grassland',
                'key_species': ['acacia trees', 'lions', 'termites'],
                'environmental_factors': ['fire frequency', 'grazing pressure', 'seasonal rainfall']
            }
        ]
        environmental_challenges = ['Climate Change Adaptation', 'Biodiversity Loss', 'Pollution Mitigation', 'Resource Depletion']
        return {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "challenge": random.choice(environmental_challenges)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "challenge": random.choice(environmental_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic AI ecosystem that simulates complex ecological interactions and emergent behaviors based on the {t['ecosystem']['name']} ecosystem. Then, analyze its potential applications in solving the real-world environmental challenge of {t['challenge']}. Your response should include:

1. Ecosystem Modeling (250-300 words):
   a) Describe the key components and interactions of your AI ecosystem model, incorporating at least two of the key species: {', '.join(t['ecosystem']['key_species'])}.
   b) Explain how you incorporate biomimetic principles in your design, considering the environmental factors: {', '.join(t['ecosystem']['environmental_factors'])}.
   c) Detail at least three emergent behaviors your system can simulate.
   d) Provide a high-level pseudocode (10-15 lines) to illustrate your model's structure.

2. AI Agents and Interactions (200-250 words):
   a) Describe at least three types of AI agents in your ecosystem and their roles.
   b) Explain how these agents interact and adapt within the system.
   c) Discuss how you model competition, cooperation, and other ecological processes.

3. Learning and Evolution (200-250 words):
   a) Explain how your AI agents learn and evolve over time.
   b) Describe any novel algorithms or techniques used in your system.
   c) Discuss how your system balances exploration and exploitation in agent behavior.

4. Environmental Challenge Application (250-300 words):
   a) Propose how your biomimetic AI ecosystem could be applied to address {t['challenge']}.
   b) Describe a specific scenario where your system could be implemented, including potential stakeholders and expected outcomes.
   c) Discuss potential benefits and limitations of using your approach.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss at least two ethical implications of using biomimetic AI for environmental problem-solving.
   b) Propose two potential extensions or improvements to your system.
   c) Suggest one area for future research in biomimetic AI ecosystems.

Ensure your response demonstrates a deep understanding of ecology, artificial intelligence, and environmental science. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section and use subheadings (a, b, c, d) as outlined above. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']['name']} ecosystem, incorporating at least two of the specified key species and considering the given environmental factors.",
            "The biomimetic AI ecosystem design effectively simulates at least three emergent behaviors.",
            f"The proposed application convincingly addresses the environmental challenge of {t['challenge']}.",
            "The AI agents and their interactions are well-explained, with at least three types of agents described.",
            "The response includes innovative approaches in learning and evolution while maintaining scientific plausibility.",
            "At least two ethical considerations are adequately addressed.",
            "The response proposes two meaningful extensions and a future research direction.",
            "The pseudocode provided effectively illustrates the model's structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
