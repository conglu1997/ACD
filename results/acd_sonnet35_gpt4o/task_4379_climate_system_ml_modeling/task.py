import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'climate_phenomenon': 'El Niño Southern Oscillation (ENSO)',
                'chaos_principle': 'Butterfly effect',
                'complex_system_aspect': 'Feedback loops',
                'prediction_timeframe': '6-12 months'
            },
            {
                'climate_phenomenon': 'Arctic sea ice extent',
                'chaos_principle': 'Strange attractors',
                'complex_system_aspect': 'Tipping points',
                'prediction_timeframe': '5-10 years'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a machine learning system to model and predict the {t['climate_phenomenon']}, incorporating the chaos theory principle of {t['chaos_principle']} and the complex adaptive systems concept of {t['complex_system_aspect']}. Your system should aim to make predictions on a {t['prediction_timeframe']} timescale. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your machine learning system.
   b) Explain how it incorporates the specified chaos theory principle and complex adaptive systems concept.
   c) Detail the data inputs, processing steps, and output format of your system.
   d) Include a high-level diagram or pseudocode representing your system's structure.

2. Climate Modeling Approach (250-300 words):
   a) Explain how your system models the specified climate phenomenon.
   b) Describe the key variables and interactions considered in your model.
   c) Discuss how your approach handles the inherent complexity and uncertainty in climate systems.

3. Machine Learning Implementation (200-250 words):
   a) Specify the type(s) of machine learning algorithms used in your system.
   b) Explain why these algorithms are suitable for modeling the given climate phenomenon.
   c) Describe your approach to training and validating the model.

4. Chaos and Complexity Integration (200-250 words):
   a) Detail how the specified chaos theory principle is implemented in your system.
   b) Explain how the complex adaptive systems concept influences your model's behavior.
   c) Discuss any novel techniques you've developed to handle chaotic or complex behaviors.

5. Prediction Capabilities (200-250 words):
   a) Describe the specific predictions your system can make about the climate phenomenon.
   b) Explain how your system quantifies and communicates uncertainty in its predictions.
   c) Discuss the limitations of your predictive capabilities and potential ways to improve them.

6. Validation and Testing (150-200 words):
   a) Propose a method to validate your system's predictions against real-world data.
   b) Describe potential challenges in testing a system that models complex climate phenomena.
   c) Suggest metrics for evaluating the performance of your system.

7. Implications and Applications (150-200 words):
   a) Discuss the potential impact of your system on climate science and policy-making.
   b) Propose two novel applications of your system beyond climate prediction.
   c) Speculate on how your approach could be extended to other complex systems.

Ensure your response demonstrates a deep understanding of climate science, chaos theory, complex adaptive systems, and machine learning. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, chaos theory, complex adaptive systems, and machine learning.",
            f"The system effectively incorporates the chaos theory principle of {t['chaos_principle']} and the complex adaptive systems concept of {t['complex_system_aspect']}.",
            f"The approach to modeling and predicting {t['climate_phenomenon']} is scientifically plausible and innovative.",
            "The machine learning implementation is well-justified and appropriate for the task.",
            "The system's prediction capabilities and limitations are clearly explained.",
            "The proposed validation and testing methods are appropriate and well-reasoned.",
            "The implications and applications discussed are insightful and demonstrate creative thinking.",
            "The response is well-structured, clear, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
