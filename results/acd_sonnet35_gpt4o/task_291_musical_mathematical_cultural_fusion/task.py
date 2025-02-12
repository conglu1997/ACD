import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "mathematical_sequence": "Fibonacci sequence",
                "cultural_rhythm": "West African polyrhythms",
                "historical_narrative": "The Trans-Atlantic slave trade"
            },
            "2": {
                "mathematical_sequence": "Prime number sequence",
                "cultural_rhythm": "Indian tala system",
                "historical_narrative": "The Silk Road trade routes"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical composition system that combines the {t['mathematical_sequence']} with {t['cultural_rhythm']}, and use it to encode a historical narrative about {t['historical_narrative']}. Your task has the following parts:

1. Musical System Design (200-250 words):
   a) Explain how you integrate the mathematical sequence into a musical structure.
   b) Describe how you incorporate the cultural rhythm into your system.
   c) Provide a notation or representation method for your musical system.

2. Historical Narrative Encoding (200-250 words):
   a) Outline key events or aspects of the historical narrative you will encode.
   b) Explain how these elements are represented in your musical system.
   c) Describe how the mathematical and cultural elements contribute to storytelling.

3. Composition Example (150-200 words):
   a) Provide a short excerpt (4-8 measures) of a composition using your system.
   b) Explain what this excerpt represents in the historical narrative.
   c) Describe how the mathematical and cultural elements are evident in this excerpt.

4. Cultural and Mathematical Analysis (200-250 words):
   a) Analyze how your system reflects or preserves elements of the cultural rhythm.
   b) Explain how the mathematical sequence influences the musical structure and narrative.
   c) Discuss any challenges in balancing mathematical, cultural, and narrative elements.

5. Potential Applications (150-200 words):
   a) Suggest how this system could be used in music education or composition.
   b) Discuss its potential for preserving or transmitting cultural and historical knowledge.
   c) Propose an interdisciplinary research question that this system could help explore.

Ensure your response demonstrates a deep understanding of music theory, mathematical sequences, and the chosen cultural rhythm and historical narrative. Be creative in your approach while maintaining musical and cultural authenticity. Your total response should be between 900-1150 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and integration of the specified mathematical sequence, cultural rhythm, and historical narrative.",
            "The musical system design is creative, well-explained, and effectively combines mathematical and cultural elements.",
            "The historical narrative encoding is logical and demonstrates how the musical system can represent complex narratives.",
            "The composition example is provided and clearly explained in terms of its narrative representation and musical elements.",
            "The cultural and mathematical analysis shows depth of understanding and critical thinking about the integration of these elements.",
            "The potential applications are innovative and demonstrate an understanding of the interdisciplinary nature of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
