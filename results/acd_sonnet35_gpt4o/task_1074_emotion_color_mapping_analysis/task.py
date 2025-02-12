import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion_set": ["joy", "sadness", "anger", "fear", "disgust"],
                "cultural_context": "Western"
            },
            {
                "emotion_set": ["contentment", "grief", "rage", "anxiety", "shame"],
                "cultural_context": "East Asian"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for mapping emotions to colors, analyze cross-cultural data on color-emotion associations, and create visualizations based on the findings. Focus on the following emotion set: {', '.join(t['emotion_set'])} in the {t['cultural_context']} cultural context. Your task has the following parts:

1. Color-Emotion Mapping System (200-250 words):
   a) Describe your system for mapping emotions to colors.
   b) Explain the psychological and cultural factors you considered in your design.
   c) Discuss how your system accounts for variations in individual perceptions.

2. Cross-Cultural Data Analysis (250-300 words):
   a) Describe a hypothetical dataset of color-emotion associations from multiple cultures.
   b) Analyze the data, focusing on similarities and differences across cultures.
   c) Identify any patterns or trends in the color-emotion associations.
   d) Discuss how these findings relate to the {t['cultural_context']} cultural context.

3. Visualization Design (200-250 words):
   a) Propose an innovative visualization method to represent your color-emotion mapping and cross-cultural analysis.
   b) Describe the key features of your visualization and how it conveys complex information.
   c) Explain how your visualization could be interactive or customizable for different users or purposes.

4. Practical Application (150-200 words):
   a) Suggest a practical application of your color-emotion mapping system and visualization in a real-world context (e.g., product design, mental health, user experience).
   b) Discuss potential benefits and limitations of using this system in your chosen application.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in using color-emotion associations in your proposed application.
   b) Suggest guidelines for responsible use of this system, considering cultural sensitivity and individual differences.

Ensure your response demonstrates a deep understanding of color theory, emotional psychology, and data visualization techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and length.",
            f"The color-emotion mapping system is well-designed and considers the {t['cultural_context']} cultural context.",
            "The cross-cultural data analysis is thorough and insightful.",
            "The visualization design is innovative and effectively represents the color-emotion mapping.",
            "The practical application is well-reasoned and considers both benefits and limitations.",
            "Ethical considerations are thoughtfully addressed with appropriate guidelines.",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of color theory and emotional psychology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
