import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'sequence': 'Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34',
                'musical_scale': 'C major scale'
            },
            '2': {
                'sequence': 'Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29',
                'musical_scale': 'A minor scale'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates mathematical sequences into musical compositions and then generates natural language descriptions of the emotional content of these compositions. Your task has three parts:

1. Mathematical to Musical Translation (200-250 words):
   a) Describe a method to translate the given mathematical sequence ({t['sequence']}) into a musical composition using the {t['musical_scale']}.
   b) Explain how your system maps mathematical properties to musical elements (e.g., pitch, rhythm, harmony).
   c) Discuss how your method preserves the mathematical relationships in the musical output.

2. Musical Analysis and Emotion Extraction (200-250 words):
   a) Describe how your system analyzes the generated musical composition.
   b) Explain the process of extracting emotional content from the musical features.
   c) Discuss any machine learning or AI techniques used in this analysis.

3. Natural Language Description (150-200 words):
   a) Provide a sample natural language description of the emotional content of the composition generated from the given sequence.
   b) Explain how your system generates this description, including any NLP techniques used.
   c) Discuss how the mathematical properties of the original sequence might influence the emotional content and resulting description.

4. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the accuracy and meaningfulness of your system's outputs.
   b) Discuss potential limitations or biases in your approach.
   c) Suggest areas for future improvement or expansion of the system.

Ensure your response demonstrates a deep understanding of mathematics, music theory, and natural language processing. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 700-900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of mathematics, music theory, and natural language processing.",
            "The proposed system provides a clear and plausible method for translating mathematical sequences into musical compositions.",
            "The response includes a detailed explanation of how emotional content is extracted from the musical composition.",
            "The sample natural language description of emotional content is coherent and relates to both the mathematical sequence and the musical composition.",
            "The response addresses potential limitations and future improvements of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0