import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        technologies = [
            'Bronze working',
            'Iron smelting',
            'Wheel and axle',
            'Writing systems',
            'Agriculture'
        ]
        regions = [
            'Mesopotamia',
            'Ancient Egypt',
            'Indus Valley',
            'Ancient China',
            'Mesoamerica'
        ]
        time_periods = [
            '3000-2000 BCE',
            '2000-1000 BCE',
            '1000 BCE - 0 CE',
            '0 - 1000 CE'
        ]
        return {
            "1": {
                "technology": random.choice(technologies),
                "starting_region": random.choice(regions),
                "time_period": random.choice(time_periods)
            },
            "2": {
                "technology": random.choice(technologies),
                "starting_region": random.choice(regions),
                "time_period": random.choice(time_periods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a computational model to simulate the spread and evolution of {t['technology']} from {t['starting_region']} during the period of {t['time_period']}. Your model should integrate archaeological data, geographical information, and cultural diffusion theories. Your response should include:

1. Model Design (300-350 words):
   a) Describe the key components and structure of your computational model.
   b) Explain how your model incorporates archaeological data, geographical factors, and cultural diffusion theories.
   c) Detail the mathematical or computational techniques used in your model (e.g., agent-based modeling, differential equations, network analysis).
   d) Include at least one mathematical equation or pseudocode snippet to illustrate a key aspect of your model.

2. Data Integration (200-250 words):
   a) Describe the types of archaeological and historical data your model would require.
   b) Explain how you would integrate diverse data types (e.g., artifact distributions, trade routes, linguistic evidence).
   c) Discuss challenges in data collection or integration specific to this historical context and how you would address them.

3. Simulation Analysis (250-300 words):
   a) Describe how you would run and analyze simulations using your model.
   b) Explain how you would validate your model against known historical and archaeological evidence.
   c) Discuss how you would use the model to generate new hypotheses about technology diffusion in the ancient world.
   d) Address the limitations of your model and potential sources of uncertainty.

4. Archaeological Insights (200-250 words):
   a) Describe two novel insights about {t['technology']} diffusion that could be gained from your model.
   b) Explain how these insights could inform our understanding of ancient trade networks or cultural interactions.
   c) Propose how your model could be applied to resolve a current debate or question in archaeology.

5. Interdisciplinary Connections (150-200 words):
   a) Discuss how your computational archaeology model could be integrated with approaches from other disciplines (e.g., genetics, climatology, or cultural anthropology).
   b) Explain how this integration could provide a more comprehensive understanding of ancient technological evolution.
   c) Propose a new research direction that combines your model with another scientific or technological domain.

Ensure your response demonstrates a deep understanding of archaeological principles, computational modeling techniques, and historical analysis. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate terminology from both archaeology and computational sciences throughout your answer.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a computational model for the spread of {t['technology']} from {t['starting_region']} during {t['time_period']}.",
            "The model demonstrates a deep understanding of both archaeological principles and computational modeling techniques.",
            "The response addresses data integration, simulation analysis, and potential insights in a thorough and creative manner.",
            "The proposed model and analysis are scientifically plausible and show rigorous thinking.",
            "The response draws meaningful interdisciplinary connections and proposes innovative research directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
