import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        regions = [
            {
                "name": "Sub-Saharan Africa",
                "climate": "Tropical",
                "main_crop": "Maize",
                "malnutrition_rate": "30%",
                "agricultural_gdp": "15%"
            },
            {
                "name": "South Asia",
                "climate": "Monsoon",
                "main_crop": "Rice",
                "malnutrition_rate": "25%",
                "agricultural_gdp": "18%"
            },
            {
                "name": "Andean Region",
                "climate": "Highland",
                "main_crop": "Potatoes",
                "malnutrition_rate": "20%",
                "agricultural_gdp": "12%"
            },
            {
                "name": "Southeast Asia",
                "climate": "Tropical Monsoon",
                "main_crop": "Cassava",
                "malnutrition_rate": "22%",
                "agricultural_gdp": "14%"
            }
        ]
        return {
            "1": random.choice(regions),
            "2": random.choice(regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that optimizes the genetic engineering of {t['main_crop']} to enhance food security in the {t['name']} region, considering the {t['climate']} climate, a malnutrition rate of {t['malnutrition_rate']}, and an agricultural GDP contribution of {t['agricultural_gdp']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for crop optimization.
   b) Explain how your system integrates genetic engineering principles, environmental data, and socio-economic factors.
   c) Detail the AI techniques and algorithms used (e.g., machine learning, evolutionary algorithms, neural networks).
   d) Provide a high-level diagram or pseudocode snippet illustrating a key aspect of your system's implementation.

2. Genetic Engineering Strategies (250-300 words):
   a) Outline the primary genetic modifications your AI system would consider for optimizing {t['main_crop']}.
   b) Explain how these modifications address the specific challenges of the {t['climate']} climate and regional malnutrition.
   c) Discuss how your system balances yield improvement with nutritional enhancement.

3. Environmental and Ecological Considerations (200-250 words):
   a) Describe how your AI system models and predicts the environmental impact of the genetically engineered crops.
   b) Explain safeguards or constraints built into your system to minimize negative ecological effects.
   c) Discuss how your system adapts its recommendations based on changing environmental conditions.

4. Socio-Economic Impact Analysis (200-250 words):
   a) Detail how your AI system evaluates the potential socio-economic impacts of the optimized crops.
   b) Explain how the system considers factors such as farmer adoption, market dynamics, and food distribution.
   c) Describe how your system might help increase the agricultural GDP contribution beyond the current {t['agricultural_gdp']}.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Identify potential ethical concerns related to using AI for crop genetic engineering.
   b) Discuss how your system addresses issues of biodiversity, food sovereignty, and long-term sustainability.
   c) Propose guidelines for transparent and responsible use of your AI system in agricultural policy-making.

6. Implementation and Scaling Strategy (150-200 words):
   a) Outline a plan for implementing and scaling your AI system in the {t['name']} region.
   b) Discuss potential challenges and how they might be overcome.
   c) Describe how your system could be adapted for other crops or regions.

7. Future Directions and Innovations (150-200 words):
   a) Propose two potential future enhancements to your AI system.
   b) Discuss how emerging technologies (e.g., CRISPR, synthetic biology) could be integrated into your system.
   c) Suggest a novel research direction that combines AI, genetic engineering, and sustainable agriculture.

Ensure your response demonstrates a deep understanding of artificial intelligence, genetic engineering, agriculture, and global development. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implementation and ethical implications.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, genetic engineering, agriculture, and global development.",
            "The AI system architecture is well-defined and integrates multiple disciplines effectively.",
            "Genetic engineering strategies are clearly explained and address the specific regional challenges.",
            "Environmental and ecological considerations are thoroughly analyzed.",
            "Socio-economic impacts are carefully evaluated and linked to the region's context.",
            "Ethical considerations are thoughtfully addressed with proposed safeguards.",
            "The implementation strategy is practical and considers scaling challenges.",
            "Future directions and innovations are creative and well-reasoned.",
            "The overall response is coherent, well-structured, and demonstrates strong interdisciplinary reasoning.",
            "The response adheres to the specified word limits for each section and does not exceed 1800 words in total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
