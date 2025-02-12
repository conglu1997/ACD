import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "artifact_type": "ancient manuscript",
                "historical_period": "Medieval Europe",
                "ai_technique": "natural language processing"
            },
            {
                "artifact_type": "archaeological site",
                "historical_period": "Pre-Columbian America",
                "ai_technique": "computer vision"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze and interpret historical artifacts, focusing on {t['artifact_type']} from {t['historical_period']}, using {t['ai_technique']} as the primary AI technique. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for artifact analysis.
   b) Explain how your system integrates {t['ai_technique']} with historical knowledge.
   c) Discuss any novel features or algorithms specific to analyzing {t['artifact_type']}.
   d) Address how your system handles uncertainties and ambiguities in historical data.

2. Data Processing and Analysis (200-250 words):
   a) Explain how your AI system processes and analyzes {t['artifact_type']}.
   b) Describe the types of features or patterns your system looks for.
   c) Discuss how your system integrates contextual information about {t['historical_period']}.
   d) Explain how your system handles multilingual or multimodal data, if applicable.

3. Case Study Application (250-300 words):
   a) Present a specific case study of your AI system analyzing a {t['artifact_type']} from {t['historical_period']}.
   b) Describe the inputs, analysis process, and outputs of your system for this case.
   c) Explain how your system's analysis contributes to historical understanding.
   d) Discuss any surprising or counterintuitive findings your system might uncover.

4. Validation and Collaboration (200-250 words):
   a) Propose methods to validate your AI system's interpretations.
   b) Describe how your system could collaborate with human historians and archaeologists.
   c) Discuss the balance between AI analysis and human expertise in historical research.
   d) Address potential biases in your AI system and how to mitigate them.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI to analyze cultural heritage.
   b) Address issues of data ownership, privacy, and cultural sensitivity.
   c) Propose guidelines for responsible use of AI in historical research.

6. Future Directions and Implications (150-200 words):
   a) Suggest potential extensions or improvements to your AI system.
   b) Discuss how your approach could be adapted to other types of artifacts or historical periods.
   c) Explore the potential impact of AI-driven historical analysis on education, tourism, or policy-making.

Ensure your response demonstrates a deep understanding of AI techniques, historical research methods, and cultural studies. Use appropriate terminology from both technical and humanities fields. Be innovative in your approach while maintaining scientific and historical accuracy. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['ai_technique']} and its application to analyzing {t['artifact_type']}.",
            f"The AI system design is innovative and specifically tailored for artifacts from {t['historical_period']}.",
            "The case study application is detailed and demonstrates how the AI system contributes to historical understanding.",
            "Ethical considerations and guidelines for responsible use are thoughtfully addressed.",
            "The response shows interdisciplinary knowledge integration of AI, history, and cultural studies.",
            "The proposed validation methods and collaboration with human experts are well-explained and feasible.",
            "Future directions and potential impacts are insightfully analyzed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
