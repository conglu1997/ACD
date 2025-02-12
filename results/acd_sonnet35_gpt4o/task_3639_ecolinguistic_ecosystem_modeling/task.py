import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Coral reef",
            "Tropical rainforest",
            "Arctic tundra",
            "Grassland savanna",
            "Mangrove swamp"
        ]
        linguistic_principles = [
            "Semantic networks",
            "Morphological adaptation",
            "Syntactic structures",
            "Phonological patterns",
            "Pragmatic context"
        ]
        environmental_factors = [
            "Climate change",
            "Habitat fragmentation",
            "Invasive species",
            "Pollution",
            "Resource depletion"
        ]
        
        tasks = {}
        for i in range(2):
            ecosystem = random.choice(ecosystems)
            principle = random.choice(linguistic_principles)
            factor = random.choice(environmental_factors)
            tasks[str(i+1)] = {
                "ecosystem": ecosystem,
                "linguistic_principle": principle,
                "environmental_factor": factor
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that uses linguistic principles to simulate and predict ecosystem dynamics for a {t['ecosystem']}, focusing on the linguistic principle of {t['linguistic_principle']} and the environmental factor of {t['environmental_factor']}. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your ecolinguistic ecosystem model.
   b) Explain how you incorporate the specified linguistic principle into your model.
   c) Detail how your model simulates ecosystem dynamics and environmental changes.
   d) Include a high-level diagram or pseudocode to illustrate your model's structure.

2. Linguistic-Ecological Mapping (250-300 words):
   a) Explain how you map ecological concepts to linguistic elements or structures.
   b) Describe how the specified linguistic principle enhances the modeling of ecosystem dynamics.
   c) Discuss any novel insights this linguistic approach might offer to ecological theory.

3. Environmental Factor Integration (200-250 words):
   a) Describe how your model incorporates the specified environmental factor.
   b) Explain how this factor influences the linguistic representation of ecosystem dynamics.
   c) Discuss potential feedback loops between linguistic structures and environmental changes in your model.

4. Simulation and Prediction (250-300 words):
   a) Outline the process of running a simulation using your model.
   b) Provide a brief example of your model's output, showing ecosystem changes over time.
   c) Explain how your model can be used to predict future ecosystem states or biodiversity patterns.

5. Evaluation and Implications (200-250 words):
   a) Propose methods to evaluate the accuracy and usefulness of your model.
   b) Discuss potential implications of your ecolinguistic approach for understanding ecosystem dynamics and biodiversity conservation.
   c) Explore how this technology might impact fields such as ecology, linguistics, and environmental management.

6. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations of your proposed model.
   b) Identify challenges in implementing or scaling your ecolinguistic ecosystem model.
   c) Suggest possible ways to address these limitations and challenges in future research.

Ensure your response demonstrates a deep understanding of ecology, linguistics, and computational modeling. Use technical terminology appropriately and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of ecology, linguistics, and computational modeling",
            "The model effectively integrates the specified linguistic principle with ecological concepts",
            "The approach to incorporating the environmental factor is innovative and well-explained",
            "The simulation and prediction aspects of the model are clearly described and plausible",
            "The evaluation methods and implications discussed are thoughtful and relevant",
            "Limitations and future directions are addressed comprehensively",
            "The response is well-structured with clear headings for each section",
            "The total word count is between 1350-1650 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
