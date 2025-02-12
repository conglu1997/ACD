import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = ['Ancient Egypt', 'Maya', 'Indus Valley', 'Ancient Greece', 'Roman Empire', 'Aztec', 'Inca', 'Ancient China', 'Viking Age Scandinavia', 'Medieval Japan']
        future_scenarios = ['Post-Scarcity Society', 'Space-Faring Civilization', 'Virtual Reality-Based Culture', 'Biotechnology-Driven Society', 'AI-Integrated Civilization']
        data_types = ['Genetic', 'Linguistic', 'Architectural', 'Technological', 'Environmental']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'past_civilization': random.choice(civilizations),
                'future_scenario': random.choice(future_scenarios),
                'primary_data_type': random.choice(data_types)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses archaeological data and advanced predictive modeling to reconstruct {t['past_civilization']} and forecast a potential {t['future_scenario']}, with a focus on {t['primary_data_type']} data. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for both reconstruction and prediction.
   b) Explain how your system integrates archaeological data analysis with futuristic modeling.
   c) Detail how your AI handles the {t['primary_data_type']} data type in particular.
   d) Discuss any novel machine learning or data processing techniques your system employs.
   e) Include a diagram or flowchart of your system architecture (described in text).

2. Past Civilization Reconstruction (250-300 words):
   a) Explain how your AI reconstructs {t['past_civilization']} using available archaeological data.
   b) Describe specific algorithms or models used for this reconstruction.
   c) Discuss how your system handles uncertainties and gaps in the archaeological record.
   d) Provide an example of a unique insight your AI might generate about {t['past_civilization']}.

3. Future Civilization Prediction (250-300 words):
   a) Detail how your AI extrapolates from historical data to predict a {t['future_scenario']}.
   b) Explain the key variables and parameters your model considers for this prediction.
   c) Describe how your system accounts for potential technological advancements and societal changes.
   d) Provide an example of a specific aspect of the {t['future_scenario']} your AI might predict.

4. Data Integration and Analysis (200-250 words):
   a) Explain how your system integrates diverse types of archaeological and historical data.
   b) Describe your approach to handling the {t['primary_data_type']} data type in both reconstruction and prediction.
   c) Discuss any data preprocessing or augmentation techniques your AI employs.
   d) Explain how your system validates its findings and predictions.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues related to using AI for historical reconstruction and future prediction.
   b) Discuss the implications of your system for understanding cultural heritage and shaping future societal development.
   c) Address potential biases in your AI's analysis and how you mitigate them.
   d) Explain limitations of your approach and areas where human expertise remains crucial.

6. Interdisciplinary Applications (150-200 words):
   a) Propose two novel applications of your AI system in fields outside archaeology and futurism.
   b) Explain how insights from your system might inform current policy-making or technological development.
   c) Discuss how this AI could contribute to our understanding of long-term societal and technological trends.

Ensure your response demonstrates a deep understanding of archaeology, data science, and futurism. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system that can reconstruct {t['past_civilization']} and predict a {t['future_scenario']}, with a clear explanation of the system architecture.",
            f"The system effectively incorporates and analyzes {t['primary_data_type']} data, demonstrating a deep understanding of its role in both historical reconstruction and future prediction.",
            "The approach to past civilization reconstruction and future civilization prediction is clearly explained with specific examples, demonstrating creativity and plausibility.",
            "Ethical considerations and limitations are thoroughly addressed, including potential biases and the role of human expertise.",
            "The response demonstrates a deep understanding of archaeology, data science, and futurism, using appropriate technical terminology.",
            "The proposed system is innovative while maintaining scientific plausibility, and interdisciplinary applications are thoughtfully explored.",
            "The response adheres to the required word count (1350-1650 words) and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
