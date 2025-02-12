import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'artwork': 'The Ghent Altarpiece (Hubert and Jan van Eyck)',
                'damage_type': 'partial destruction during World War II',
                'cultural_context': 'Early Netherlandish Renaissance',
                'ethical_consideration': 'religious significance'
            },
            {
                'artwork': 'Peking Man fossils',
                'damage_type': 'lost during World War II',
                'cultural_context': 'Paleolithic era in China',
                'ethical_consideration': 'scientific and national importance'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for preserving and recreating the lost or damaged artwork: {t['artwork']}. Your system should address the specific damage type: {t['damage_type']}, while considering the cultural context of {t['cultural_context']} and the ethical consideration of {t['ethical_consideration']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for art restoration and recreation.
   b) Explain how your system integrates art historical knowledge, digital imaging techniques, and cultural context.
   c) Discuss how your architecture addresses the specific challenges of the given artwork and damage type.

2. Data Collection and Analysis (200-250 words):
   a) Describe the types of data your system would use for restoration and recreation.
   b) Explain how your system would analyze existing fragments or documentation of the artwork.
   c) Discuss any novel approaches to gathering or interpreting art historical data.

3. AI Model for Artistic Style Replication (250-300 words):
   a) Propose a specific AI model or algorithm for replicating the artistic style of the lost or damaged artwork.
   b) Explain how this model incorporates art historical knowledge and cultural context.
   c) Describe how your model would handle uncertainties and ambiguities in the restoration process.

4. Ethical Considerations and Cultural Sensitivity (200-250 words):
   a) Discuss the ethical implications of using AI for art restoration and recreation, particularly considering the given ethical consideration.
   b) Explain how your system ensures cultural sensitivity and respect for the artwork's original context.
   c) Propose guidelines for the responsible use and interpretation of AI-generated art restorations.

5. Visualization and Presentation (150-200 words):
   a) Describe how your system would visualize the restored or recreated artwork.
   b) Explain how you would present the AI's work alongside the original (or remaining fragments) to maintain transparency.
   c) Discuss how your presentation method would aid in public understanding and appreciation of the artwork.

6. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the accuracy and authenticity of your system's restorations or recreations.
   b) Describe how you would validate your system's output using expert knowledge and existing art historical research.
   c) Discuss the limitations of your evaluation approach and potential improvements.

Ensure your response demonstrates a deep understanding of art history, digital imaging techniques, and AI technologies. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and historical plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an AI system for preserving and recreating {t['artwork']}.",
            f"The system addresses the specific damage type: {t['damage_type']}.",
            f"The cultural context of {t['cultural_context']} is thoroughly considered in the system design.",
            f"The ethical consideration of {t['ethical_consideration']} is addressed in depth.",
            "The response demonstrates a deep understanding of art history, digital imaging techniques, and AI technologies.",
            "The proposed system integrates art historical knowledge, digital imaging techniques, and cultural context.",
            "The response includes a specific AI model or algorithm for replicating the artistic style of the artwork.",
            "Ethical implications and cultural sensitivity are thoroughly discussed.",
            "The response proposes methods for evaluating and validating the system's output."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
