import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        archaeological_periods = [
            "Neolithic",
            "Bronze Age",
            "Iron Age",
            "Classical Antiquity",
            "Medieval Period"
        ]
        data_types = [
            "pottery sherds",
            "stone tools",
            "metal artifacts",
            "human remains",
            "architectural remains"
        ]
        analysis_techniques = [
            "radiocarbon dating",
            "DNA analysis",
            "isotope analysis",
            "ground-penetrating radar",
            "satellite imagery analysis"
        ]
        ai_applications = [
            "pattern recognition",
            "predictive modeling",
            "natural language processing",
            "computer vision",
            "machine learning"
        ]
        
        tasks = {
            "1": {
                "period": random.choice(archaeological_periods),
                "data_type": random.choice(data_types),
                "analysis_technique": random.choice(analysis_techniques),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "period": random.choice(archaeological_periods),
                "data_type": random.choice(data_types),
                "analysis_technique": random.choice(analysis_techniques),
                "ai_application": random.choice(ai_applications)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze archaeological data, reconstruct ancient societies, and predict undiscovered archaeological sites for the {t['period']}, focusing on {t['data_type']}. Your system should incorporate {t['analysis_technique']} and utilize {t['ai_application']} as a key AI component. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall structure and components of your AI system.
   b) Explain how it integrates archaeological knowledge with AI techniques.
   c) Detail how the system incorporates {t['analysis_technique']} in its analysis.
   d) Discuss how {t['ai_application']} is utilized to enhance archaeological insights.

2. Data Processing and Analysis (250-300 words):
   a) Explain how your system processes and analyzes {t['data_type']}.
   b) Describe any novel algorithms or techniques used for pattern recognition in archaeological data.
   c) Discuss how your system handles uncertainties and gaps in archaeological evidence.

3. Ancient Society Reconstruction (250-300 words):
   a) Detail how your AI system reconstructs aspects of {t['period']} society based on the analyzed data.
   b) Provide an example of a specific insight or hypothesis your system might generate.
   c) Explain how the system validates its reconstructions against existing archaeological knowledge.

4. Predictive Modeling (200-250 words):
   a) Describe how your system predicts locations of undiscovered archaeological sites.
   b) Explain the factors and data points considered in the predictive model.
   c) Discuss the accuracy and reliability of these predictions.

5. Ethical Considerations and Limitations (150-200 words):
   a) Address ethical implications of using AI in archaeological research and heritage management.
   b) Discuss potential biases in your system and how they are mitigated.
   c) Identify limitations of your approach and areas for future improvement.

6. Interdisciplinary Impact (150-200 words):
   a) Explain how your system could benefit other fields of historical or scientific research.
   b) Propose an innovative application of your system outside of traditional archaeology.

Ensure your response demonstrates a deep understanding of both archaeology and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of an AI system for archaeological analysis and prediction.",
            f"The system effectively incorporates {t['analysis_technique']} in its analysis process.",
            f"The AI application of {t['ai_application']} is well-integrated and utilized in the system.",
            f"The system demonstrates capability in analyzing {t['data_type']} from the {t['period']}.",
            "The response addresses ethical considerations and limitations of using AI in archaeology.",
            "The proposed system shows innovative applications beyond traditional archaeology.",
            "The response demonstrates a deep understanding of both archaeology and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
