import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Tropical rainforest",
            "Coral reef",
            "Arctic tundra",
            "Savanna grassland",
            "Temperate deciduous forest",
            "Mangrove swamp",
            "Alpine meadow"
        ]
        endangered_species = [
            "Amur leopard",
            "Vaquita",
            "Black rhino",
            "Mountain gorilla",
            "Hawksbill turtle",
            "Sumatran orangutan",
            "Pangolin"
        ]
        data_sources = [
            "Satellite imagery",
            "Environmental DNA (eDNA)",
            "Acoustic sensors",
            "Drone surveillance",
            "Citizen science observations",
            "Camera traps",
            "GPS tracking devices"
        ]
        conservation_challenges = [
            "Habitat fragmentation",
            "Climate change impacts",
            "Poaching",
            "Human-wildlife conflict",
            "Invasive species",
            "Disease outbreaks",
            "Pollution"
        ]
        
        tasks = {}
        for i in range(2):
            ecosystem = random.choice(ecosystems)
            species = random.choice(endangered_species)
            data_source = random.choice(data_sources)
            challenge = random.choice(conservation_challenges)
            
            tasks[str(i+1)] = {
                "ecosystem": ecosystem,
                "species": species,
                "data_source": data_source,
                "challenge": challenge
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for global biodiversity monitoring and conservation, with a focus on the {t['ecosystem']} ecosystem and the endangered {t['species']}. Your system should incorporate {t['data_source']} as a key data source and address the conservation challenge of {t['challenge']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI biodiversity monitoring system.
   b) Explain how your system integrates multiple data sources, including {t['data_source']}.
   c) Detail how the system processes and analyzes data to track and protect the {t['species']}.
   d) Include a high-level diagram of your system architecture (describe it in words).

2. Data Collection and Processing (200-250 words):
   a) Explain your approach to collecting and processing data from {t['data_source']}.
   b) Discuss how you ensure data quality and handle potential biases or gaps in the data.
   c) Describe any novel techniques or algorithms used for data fusion or feature extraction.

3. Species Tracking and Prediction (200-250 words):
   a) Detail how your AI system tracks and predicts the movements and population dynamics of the {t['species']}.
   b) Explain any machine learning models or algorithms used for predictive analysis.
   c) Discuss how your system accounts for the specific challenges of monitoring species in the {t['ecosystem']}.

4. Conservation Strategies (200-250 words):
   a) Describe how your AI system would generate and evaluate conservation strategies for the {t['species']}, specifically addressing {t['challenge']}.
   b) Explain how the system balances short-term and long-term conservation goals.
   c) Discuss how your system could adapt its strategies based on new data or changing environmental conditions.

5. Ethical Considerations and Stakeholder Engagement (150-200 words):
   a) Identify potential ethical issues in using AI for biodiversity monitoring and conservation.
   b) Propose guidelines for responsible development and deployment of your system.
   c) Discuss how your system would engage with local communities and indigenous knowledge.

6. System Evaluation and Improvement (150-200 words):
   a) Propose metrics to evaluate the effectiveness of your AI system in biodiversity monitoring and conservation.
   b) Describe how you would validate the system's predictions and recommendations.
   c) Suggest approaches for continual learning and improvement of the system.

7. Broader Implications (100-150 words):
   a) Discuss how your AI system could contribute to global biodiversity conservation efforts.
   b) Explore potential applications of your system beyond the specified ecosystem and species.

Ensure your response demonstrates a deep understanding of AI, environmental science, and conservation biology. Be creative in your approach while maintaining scientific accuracy. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where indicated. Your total response should be between 1250-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, environmental science, and conservation biology",
            f"The proposed system architecture effectively integrates {t['data_source']} with other data sources",
            f"The approach to species tracking and prediction is innovative and tailored to the {t['species']} in the {t['ecosystem']}",
            f"The conservation strategies generated by the AI system effectively address {t['challenge']}",
            "Ethical considerations and stakeholder engagement are thoroughly addressed, including engagement with local communities",
            "The system evaluation and improvement methods are well-thought-out and include specific metrics for assessing effectiveness",
            "The response follows the required format with clear headings and subheadings, and falls within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
