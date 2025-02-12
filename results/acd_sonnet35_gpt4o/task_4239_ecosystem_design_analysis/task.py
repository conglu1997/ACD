import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'name': 'Tropical Rainforest',
                'climate': 'hot and humid',
                'key_species': ['jaguars', 'toucans', 'orchids'],
                'environmental_threat': 'deforestation',
                'annual_rainfall': '2000-4000 mm',
                'average_temperature': '25-28°C'
            },
            {
                'name': 'Arctic Tundra',
                'climate': 'cold and dry',
                'key_species': ['polar bears', 'arctic foxes', 'mosses'],
                'environmental_threat': 'global warming',
                'annual_rainfall': '150-250 mm',
                'average_temperature': '-10 to -20°C'
            }
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = random.choice(ecosystems)
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical ecosystem based on the {t['name']} biome, simulate its dynamics, and analyze its resilience to environmental changes. Your task includes:

1. Ecosystem Design (300-350 words):
   a) Describe the key abiotic factors of your {t['name']} ecosystem, including climate (annual rainfall: {t['annual_rainfall']}, average temperature: {t['average_temperature']}), soil type, and topography.
   b) List and describe at least 10 key species in your ecosystem, including producers, consumers, and decomposers. Include the {', '.join(t['key_species'])}.
   c) Explain the main ecological relationships (e.g., predator-prey, mutualism) between these species.
   d) Create a simple food web diagram for your ecosystem (describe it textually).

2. Ecosystem Dynamics Simulation (250-300 words):
   a) Propose a mathematical model to simulate the population dynamics of three key species in your ecosystem.
   b) Explain the variables and parameters in your model and how they relate to ecological principles.
   c) Describe how you would simulate this model over a 50-year period.
   d) Discuss potential limitations of your model.

3. Resilience Analysis (250-300 words):
   a) Analyze how your ecosystem might respond to the threat of {t['environmental_threat']}.
   b) Identify potential tipping points that could lead to ecosystem collapse.
   c) Propose three measurable indicators of ecosystem health and explain how they would change under stress.

4. Data Analysis and Visualization (200-250 words):
   a) Describe how you would collect and analyze data on your ecosystem's health indicators.
   b) Propose two types of data visualizations that would effectively communicate the ecosystem's status and trends.
   c) Explain how these visualizations could inform conservation strategies.

5. Conservation Strategies (150-200 words):
   a) Based on your analysis, propose three specific conservation strategies to enhance your ecosystem's resilience.
   b) Explain how each strategy addresses the identified threats and supports key species.

6. Ethical Considerations (100-150 words):
   a) Discuss the ethical implications of managing and potentially modifying natural ecosystems.
   b) Address potential conflicts between conservation goals and human needs.

Ensure your response demonstrates a deep understanding of ecological principles, mathematical modeling, and data analysis. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Ecosystem Design:') on a new line, followed by your response for that section. Use subheadings (a, b, c, d) where specified. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if len(submission.split()) < 1000:  # Minimum word count
            return 0.0
        criteria = [
            f"The response includes a detailed description of the {t['name']} ecosystem with at least 10 key species (including {', '.join(t['key_species'])}) and their ecological relationships.",
            "A mathematical model for simulating population dynamics of three key species is proposed and clearly explained.",
            f"The analysis of the ecosystem's response to {t['environmental_threat']} is thorough, scientifically plausible, and includes potential tipping points.",
            "Three measurable indicators of ecosystem health are proposed and their changes under stress are explained.",
            "Data analysis and visualization techniques are appropriately described and justified, with two specific types of visualizations proposed.",
            "Three specific conservation strategies are proposed and clearly linked to the ecosystem analysis and identified threats.",
            "The response demonstrates a deep understanding of ecological principles and systems thinking, using appropriate scientific terminology throughout.",
            "The ethical implications of ecosystem management and potential conflicts between conservation and human needs are thoughtfully discussed.",
            "The response follows the specified format with clear headings and subheadings, and falls within the 1250-1550 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
