import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "joy", "description": "A feeling of great pleasure and happiness"},
            {"emotion": "melancholy", "description": "A feeling of pensive sadness, typically with no obvious cause"}
        ]
        return {str(i+1): emotion for i, emotion in enumerate(emotions)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the emotional state of {t['emotion']} ({t['description']}) into a musical composition, then create a data visualization representing the musical elements and their emotional correlates. Your response should include:

1. Musical Composition (200-250 words):
   a) Describe a short musical piece that expresses the given emotion.
   b) Specify the key, time signature, tempo, and primary instruments.
   c) Explain how each musical element (melody, harmony, rhythm) contributes to conveying the emotion.
   d) Include at least one musical technique or theory concept (e.g., leitmotif, counterpoint) in your composition.

2. Emotional-Musical Mapping (150-200 words):
   a) Create a table mapping at least 5 specific musical elements to their emotional correlates.
   b) Explain the psychological basis for each mapping, citing relevant research or theories.

3. Data Visualization (200-250 words):
   a) Design a data visualization that represents your musical composition and its emotional elements.
   b) Describe the visualization in detail, including its type (e.g., circular plot, network graph), color scheme, and layout.
   c) Explain how different aspects of the visualization correspond to musical elements and emotional qualities.
   d) Discuss how your visualization enhances understanding of the emotion-music relationship.

4. Technical Implementation (150-200 words):
   a) Propose a method for generating this visualization programmatically.
   b) Specify which programming language and libraries you would use.
   c) Outline the key steps in your implementation process.

5. Cross-Cultural Consideration (100-150 words):
   a) Discuss how your musical composition and visualization might be perceived differently in another culture.
   b) Suggest one modification to make your representation more culturally universal.

Ensure your response demonstrates a deep understanding of music theory, emotional psychology, and data visualization techniques. Be creative in your approach while maintaining scientific validity and technical feasibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The musical composition should clearly convey the emotion of {t['emotion']}.",
            "The response must include a detailed mapping of musical elements to emotional correlates.",
            "The data visualization description should be innovative and coherently represent both musical and emotional elements.",
            "The technical implementation proposal should be feasible and well-explained.",
            "The cross-cultural consideration should demonstrate awareness of cultural differences in music and emotion perception.",
            "The overall response should show a deep understanding of music theory, psychology, and data visualization techniques."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
