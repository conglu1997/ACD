import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Coral Reef",
                "key_species": ["coral polyps", "parrotfish", "zooplankton"],
                "environmental_factors": ["water temperature", "ocean acidification", "light penetration"],
                "human_influence": "coastal development and tourism"
            },
            {
                "name": "Boreal Forest",
                "key_species": ["spruce trees", "moose", "lynx"],
                "environmental_factors": ["temperature", "precipitation", "soil composition"],
                "human_influence": "logging and forest management"
            },
            {
                "name": "Savanna Grassland",
                "key_species": ["acacia trees", "zebras", "lions"],
                "environmental_factors": ["rainfall patterns", "fire frequency", "soil nutrients"],
                "human_influence": "agriculture and livestock grazing"
            },
            {
                "name": "Urban Ecosystem",
                "key_species": ["street trees", "pigeons", "rats"],
                "environmental_factors": ["air quality", "temperature", "noise levels"],
                "human_influence": "urban planning and development"
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a data-driven model of the {t['name']} ecosystem, incorporating multiple species interactions, environmental factors, and human influences. Your task has five parts:\n\n1. Model Design (300-350 words):\na) Describe the overall structure of your ecosystem model, including key components and their interactions.\nb) Explain how you incorporate the following elements into your model:\n   - Key species: {', '.join(t['key_species'])}\n   - Environmental factors: {', '.join(t['environmental_factors'])}\n   - Human influence: {t['human_influence']}\nc) Detail the mathematical or computational techniques you use to model these interactions (e.g., differential equations, agent-based modeling, machine learning algorithms).\nd) Explain how your model accounts for feedback loops and emergent properties within the ecosystem.\ne) Include at least one mathematical equation or formula to illustrate a key relationship in your model.\n\n2. Data Integration (200-250 words):\na) Describe the types of data your model would require and potential sources for this data.\nb) Explain how you would integrate diverse data types (e.g., satellite imagery, field observations, genetic data) into your model.\nc) Discuss any challenges in data collection or integration specific to this ecosystem and how you would address them.\n\n3. Model Analysis and Validation (250-300 words):\na) Propose a method for validating your model using real-world data.\nb) Describe how you would test the model's sensitivity to different parameters and initial conditions.\nc) Explain how you would use the model to make predictions about the ecosystem's future states under different scenarios.\nd) Discuss the limitations of your model and potential sources of uncertainty.\n\n4. Ecological Insights and Applications (200-250 words):\na) Describe two novel ecological insights that could be gained from your model.\nb) Explain how these insights could inform conservation strategies or environmental policy.\nc) Propose an innovative application of your model in ecosystem management or restoration.\n\n5. Interdisciplinary Connections (150-200 words):\na) Discuss how your ecosystem model could be integrated with models from other disciplines (e.g., climate science, economics, social sciences).\nb) Explain how this integration could provide a more comprehensive understanding of the ecosystem and its interactions with human systems.\nc) Propose a new research direction that combines your ecosystem model with another scientific or technological domain.\n\nEnsure your response demonstrates a deep understanding of ecological principles, data analysis techniques, and modeling approaches. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate scientific terminology throughout your answer.\n\nFormat your response with clear headings for each section. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should design a data-driven model for the {t['name']} ecosystem.",
            "The model design should incorporate the specified key species, environmental factors, and human influence.",
            "The response should demonstrate a deep understanding of ecological principles and modeling techniques.",
            "The model design should include at least one mathematical equation or formula.",
            "The data integration section should address challenges specific to the given ecosystem.",
            "The model analysis should include validation methods and discussion of limitations.",
            "The response should propose novel ecological insights and applications.",
            "The interdisciplinary connections should be innovative and well-reasoned.",
            "The response should adhere to the specified word count for each section (Model Design: 300-350, Data Integration: 200-250, Model Analysis and Validation: 250-300, Ecological Insights and Applications: 200-250, Interdisciplinary Connections: 150-200) and the overall total of 1100-1350 words.",
            "The response should be formatted with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
