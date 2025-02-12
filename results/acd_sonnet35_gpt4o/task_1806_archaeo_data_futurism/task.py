import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            {
                "name": "Zephyria",
                "location": "Coastal region with nearby mountains",
                "climate": "Mediterranean",
                "artifacts": ["Bronze tools", "Pottery with geometric designs", "Stone temples"],
                "data_points": [
                    {"year": -3000, "population": 5000, "technology_level": 2},
                    {"year": -2500, "population": 12000, "technology_level": 3},
                    {"year": -2000, "population": 25000, "technology_level": 4}
                ]
            },
            {
                "name": "Lumina",
                "location": "River valley surrounded by dense forests",
                "climate": "Temperate",
                "artifacts": ["Iron weapons", "Astronomical instruments", "Complex irrigation systems"],
                "data_points": [
                    {"year": -2500, "population": 8000, "technology_level": 3},
                    {"year": -2000, "population": 20000, "technology_level": 4},
                    {"year": -1500, "population": 40000, "technology_level": 5}
                ]
            },
            {
                "name": "Aethoria",
                "location": "Archipelago with volcanic islands",
                "climate": "Tropical",
                "artifacts": ["Advanced sailing vessels", "Coral-based architecture", "Pearl jewelry"],
                "data_points": [
                    {"year": -2000, "population": 10000, "technology_level": 3},
                    {"year": -1500, "population": 30000, "technology_level": 4},
                    {"year": -1000, "population": 60000, "technology_level": 5}
                ]
            }
        ]
        return {str(i+1): civ for i, civ in enumerate(random.sample(civilizations, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the given archaeological data, create a detailed description of the ancient civilization of {t['name']}, then use data science techniques to predict its technological advancements and societal changes. Your response should include:

1. Civilization Description (250-300 words):
   a) Describe the civilization's location, climate, and key archaeological findings.
   b) Infer their social structure, economic activities, and cultural practices based on the artifacts.
   c) Create a plausible origin story for this civilization.

2. Data Analysis (200-250 words):
   a) Analyze the given population and technology level data points.
   b) Calculate the growth rate for population and technology level.
   c) Identify any patterns or correlations in the data.

3. Predictive Modeling (250-300 words):
   a) Using the data and growth rates, predict the civilization's population and technology level for the next 500 years (in 100-year intervals).
   b) Describe your predictive model and justify your choices.
   c) Discuss any assumptions or limitations of your model.

4. Technological Advancements (200-250 words):
   a) Based on your predictions, describe 3-5 major technological advancements this civilization might achieve.
   b) Explain how these advancements relate to their environment and existing artifacts.
   c) Discuss the potential impact of these advancements on their society.

5. Societal Changes (200-250 words):
   a) Predict how the civilization's social structure, economy, and culture might evolve over the next 500 years.
   b) Describe any potential challenges or conflicts that might arise due to these changes.
   c) Speculate on how these changes might be reflected in future archaeological findings.

6. Comparative Analysis (150-200 words):
   a) Compare the predicted development of this civilization to known historical civilizations.
   b) Discuss any similarities or differences in technological progress and societal changes.
   c) Explain how this speculative exercise might inform our understanding of real historical processes.

Ensure your response demonstrates a deep understanding of archaeology, data science, and historical processes. Use appropriate terminology and provide clear, logical explanations for your inferences and predictions. Be creative in your approach while maintaining plausibility based on the given data.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and plausible description of the civilization based on the given archaeological data",
            "The data analysis demonstrates correct calculations and interpretation of growth rates and patterns",
            "The predictive modeling is logical and well-justified, with clear explanations of the model and its limitations",
            "The technological advancements and societal changes predicted are creative yet plausible, with clear connections to the civilization's context",
            "The comparative analysis draws insightful parallels between the fictional civilization and real historical processes",
            "The response demonstrates a strong understanding of archaeology, data science, and historical processes, using appropriate terminology throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
