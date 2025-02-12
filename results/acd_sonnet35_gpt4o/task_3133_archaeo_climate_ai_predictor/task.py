import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        regions = [
            {
                "region": "Mediterranean Basin",
                "time_period": "Bronze Age (3300-1200 BCE)",
                "archaeological_data": ["pollen records", "tree rings", "lake sediments"]
            },
            {
                "region": "Mesoamerica",
                "time_period": "Classic Maya period (250-900 CE)",
                "archaeological_data": ["cave deposits", "lake cores", "isotope analysis of human remains"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(regions, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses archaeological data to reconstruct ancient climates and predict future climate changes for the {t['region']} during the {t['time_period']}. Your system should incorporate machine learning techniques and climate modeling. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for archaeo-climate reconstruction and prediction.
   b) Explain how your system integrates archaeological data, machine learning, and climate modeling.
   c) Detail how your system handles the specific archaeological data types: {', '.join(t['archaeological_data'])}.
   d) Include a diagram or detailed textual description of your system architecture.

2. Data Processing and Analysis (250-300 words):
   a) Explain how your system processes and analyzes the given archaeological data types.
   b) Describe any novel machine learning techniques used for pattern recognition in archaeological data.
   c) Discuss how your system accounts for uncertainties and biases in archaeological records.

3. Climate Reconstruction Process (250-300 words):
   a) Detail the step-by-step process your system uses to reconstruct ancient climates from archaeological data.
   b) Explain how your system integrates multiple data sources to create a coherent climate model.
   c) Describe how your system validates its reconstructions against known climate proxies.

4. Future Climate Prediction (200-250 words):
   a) Explain how your system extrapolates from past climate reconstructions to predict future climate changes.
   b) Describe any additional data sources or models your system incorporates for future predictions.
   c) Discuss how your system accounts for modern anthropogenic climate change in its predictions.

5. Interdisciplinary Integration (200-250 words):
   a) Analyze how your system bridges the gaps between archaeology, climate science, and artificial intelligence.
   b) Discuss any challenges in integrating these diverse fields and how your system addresses them.
   c) Explain how insights from one field inform and enhance the others in your system.

6. Ethical Considerations and Limitations (150-200 words):
   a) Address potential ethical issues in using AI to interpret archaeological data and predict climate changes.
   b) Discuss the limitations of your system and potential sources of error or uncertainty.
   c) Propose guidelines for the responsible use and interpretation of your system's outputs.

Ensure your response demonstrates a deep understanding of archaeology, climate science, and artificial intelligence. Use appropriate terminology from all fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of archaeology, climate science, and artificial intelligence.",
            "The proposed AI system architecture is well-designed and clearly explained.",
            f"The system effectively integrates and analyzes the specified archaeological data types: {', '.join(t['archaeological_data'])}.",
            "The climate reconstruction and future prediction processes are logically sound and innovative.",
            "The response shows strong interdisciplinary integration and addresses ethical considerations thoughtfully.",
            "The overall response is creative, well-structured, and demonstrates strong problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
