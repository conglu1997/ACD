import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'musical_style': 'jazz improvisation',
                'cognitive_process': 'working memory',
                'neuroscientific_principle': 'neural oscillations'
            },
            {
                'musical_style': 'classical sonata form',
                'cognitive_process': 'pattern recognition',
                'neuroscientific_principle': 'predictive coding'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model of music cognition focusing on {t['musical_style']}, based on the cognitive process of {t['cognitive_process']} and the neuroscientific principle of {t['neuroscientific_principle']}. Then, use your model to analyze an existing piece and generate a new musical excerpt. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the overall structure of your computational model.
   b) Explain how it incorporates the specified cognitive process and neuroscientific principle.
   c) Detail how your model represents and processes musical information.
   d) Provide a diagram or flowchart illustrating the key components and processes of your model.

2. Neuroscientific Basis (250-300 words):
   a) Explain the chosen neuroscientific principle and its relevance to music cognition.
   b) Discuss how your model simulates or incorporates this principle.
   c) Describe how this principle might influence music perception or creation in the human brain.

3. Cognitive Process Implementation (250-300 words):
   a) Elaborate on how the specified cognitive process is implemented in your model.
   b) Explain how this process contributes to the model's understanding or generation of music.
   c) Discuss any simplifications or assumptions made in modeling this cognitive process.

4. Musical Style Analysis (200-250 words):
   a) Briefly describe the key characteristics of the specified musical style.
   b) Explain how your model captures or represents these characteristics.
   c) Discuss any challenges in modeling this particular style and how you addressed them.

5. Existing Piece Analysis (200-250 words):
   a) Choose a well-known piece in the specified style and analyze it using your model.
   b) Describe the insights or patterns your model identifies in the piece.
   c) Explain how these findings relate to human perception of the music.

6. New Musical Excerpt Generation (200-250 words):
   a) Use your model to generate a short musical excerpt (8-16 measures) in the specified style.
   b) Provide a musical score or a detailed description of the generated excerpt.
   c) Explain how the generated music reflects the principles implemented in your model.

7. Model Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your model.
   b) Discuss potential limitations of your approach.
   c) Suggest future improvements or extensions to your model.

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and computational modeling. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed computational model of music cognition focusing on {t['musical_style']}, {t['cognitive_process']}, and {t['neuroscientific_principle']}.",
            "The model architecture is clearly described and illustrated with a diagram or flowchart.",
            "The neuroscientific principle is thoroughly explained and integrated into the model.",
            f"The cognitive process of {t['cognitive_process']} is well-implemented and its role in music cognition is discussed.",
            f"The musical style of {t['musical_style']} is analyzed and represented in the model.",
            "An existing piece is analyzed using the model, with insights provided.",
            "A new musical excerpt is generated and described or notated.",
            "The response demonstrates a deep understanding of music theory, cognitive neuroscience, and computational modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
