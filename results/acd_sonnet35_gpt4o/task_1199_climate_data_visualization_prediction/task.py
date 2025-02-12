import random
import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_phenomena = [
            {
                "phenomenon": "El Niño-Southern Oscillation (ENSO)",
                "data_sources": ["sea surface temperatures", "atmospheric pressure patterns", "wind data"],
                "impact_areas": ["global precipitation patterns", "tropical cyclone activity", "marine ecosystems"]
            },
            {
                "phenomenon": "Arctic Sea Ice Decline",
                "data_sources": ["satellite imagery", "ice thickness measurements", "ocean temperature profiles"],
                "impact_areas": ["global albedo", "polar ecosystems", "Northern Hemisphere weather patterns"]
            }
        ]
        return {
            "1": random.choice(climate_phenomena),
            "2": random.choice(climate_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a data visualization and predictive modeling system for the climate phenomenon: {t['phenomenon']}. Your task includes:\n\n1. Data Integration and Preprocessing (200-250 words):\n   a) Describe how you would integrate and preprocess data from the following sources: {', '.join(t['data_sources'])}.\n   b) Explain any challenges in combining these diverse data types and how you would address them.\n   c) Propose a method for handling missing or inconsistent data.\n   d) Discuss at least one novel approach to data normalization or feature extraction specific to this climate phenomenon.\n\n2. Visualization Design (250-300 words):\n   a) Create a detailed description of an innovative visualization technique that effectively communicates the complex dynamics of {t['phenomenon']}.\n   b) Explain how your visualization incorporates multiple data sources and represents uncertainty.\n   c) Describe how the visualization would change over time to reflect the dynamic nature of the phenomenon.\n   d) Include a textual representation of your visualization design (as if describing an image).\n   e) Propose an interactive element that would enhance user understanding of the data.\n\n3. Predictive Modeling (200-250 words):\n   a) Propose a machine learning or statistical modeling approach to predict future states of {t['phenomenon']}.\n   b) Explain how your model accounts for the complex interactions between different variables.\n   c) Describe how you would validate your model and quantify prediction uncertainty.\n   d) Discuss how your model could be updated in real-time as new data becomes available.\n\n4. Impact Analysis (150-200 words):\n   a) Discuss how your system could be used to analyze and predict impacts on: {', '.join(t['impact_areas'])}.\n   b) Propose a method for visualizing these potential impacts alongside your primary visualization.\n   c) Describe a specific scenario where your system could be used to inform policy decisions.\n\n5. Ethical Considerations and Limitations (100-150 words):\n   a) Discuss any ethical implications of your system, particularly regarding data use and the communication of uncertainty.\n   b) Address potential limitations of your approach and suggest areas for future improvement.\n   c) Consider the potential for misuse or misinterpretation of your system's outputs and propose safeguards.\n\n6. Case Study (150-200 words):\n   Provide a brief case study demonstrating how your system would be applied to a specific real-world situation related to {t['phenomenon']}. Include hypothetical data inputs, system outputs, and potential real-world impacts.\n\nEnsure your response demonstrates a deep understanding of climate science, data analysis, and visualization techniques. Be innovative in your approach while maintaining scientific accuracy and practical feasibility. Use appropriate technical terminology and provide clear explanations of complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the climate phenomenon {t['phenomenon']} and incorporates all specified data sources.",
            "The data integration and preprocessing section demonstrates a clear understanding of working with diverse data sources and includes a novel approach to data handling.",
            "The visualization design is innovative, clearly described, and effectively communicates complex climate dynamics, including an interactive element.",
            "The predictive modeling approach is well-reasoned, accounts for the complexity of the phenomenon, and includes a method for real-time updates.",
            f"The impact analysis adequately covers the specified areas: {', '.join(t['impact_areas'])} and includes a policy-relevant scenario.",
            "Ethical considerations and limitations are thoughtfully addressed, including potential misuse and safeguards.",
            "The case study effectively demonstrates the practical application of the proposed system.",
            "The response shows creativity, interdisciplinary knowledge integration, and technical proficiency throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
