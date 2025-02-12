import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "region": "Arctic",
                "primary_factor": "Sea ice melting",
                "time_frame": "50 years"
            },
            {
                "region": "Amazon Rainforest",
                "primary_factor": "Deforestation",
                "time_frame": "30 years"
            },
            {
                "region": "Coral Triangle",
                "primary_factor": "Ocean acidification",
                "time_frame": "25 years"
            },
            {
                "region": "Sahel",
                "primary_factor": "Desertification",
                "time_frame": "40 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a predictive model for cascading environmental effects due to climate change in the {t['region']}, with {t['primary_factor']} as the primary factor, over a {t['time_frame']} period. Your task has five parts:

1. Model Design (300-350 words):
   a) Outline the key components of your predictive model, including at least five interconnected environmental factors.
   b) Explain how your model accounts for feedback loops and non-linear interactions between these factors.
   c) Describe the data sources and types of data your model would require.
   d) Discuss how your model incorporates uncertainty and variability in climate projections.

2. Cascading Effects Analysis (250-300 words):
   a) Predict and explain at least three major cascading effects that could result from the primary factor.
   b) Describe how these effects might interact with each other over time.
   c) Identify any potential tipping points or irreversible changes in the system.

3. Visualization (ASCII art or detailed description):
   Create a visual representation of your model, showing the relationships between different factors and cascading effects. ASCII art is preferred, but a detailed textual description is acceptable if it clearly conveys the model's structure and relationships.

4. Interdisciplinary Implications (200-250 words):
   Discuss how your model and its predictions might impact at least three other fields (e.g., economics, public health, agriculture). Provide specific examples for each field.

5. Model Limitations and Improvements (150-200 words):
   a) Identify at least two limitations of your proposed model.
   b) Suggest potential improvements or extensions to address these limitations.
   c) Discuss how emerging technologies or methodologies could enhance the model's accuracy or applicability.

Ensure your response demonstrates a deep understanding of climate science, ecological systems, and predictive modeling techniques. Use technical terminology appropriately and provide explanations where necessary. Strive for scientific accuracy while also being creative in your approach to this complex problem. Your response will be evaluated based on its scientific merit, creativity, and the depth of analysis provided.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of climate science and ecological systems.",
            "The predictive model effectively incorporates multiple interconnected environmental factors and their complex interactions.",
            "The cascading effects analysis is logical, well-explained, and considers long-term implications.",
            "The visualization clearly represents the model's components and their relationships.",
            "The interdisciplinary implications are insightful and well-reasoned.",
            "The discussion of model limitations and potential improvements shows critical thinking and awareness of current technological advancements.",
            "The response balances scientific accuracy with creative problem-solving in addressing the complex climate cascade prediction task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
