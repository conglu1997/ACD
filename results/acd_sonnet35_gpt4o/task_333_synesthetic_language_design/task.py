import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            {
                "type": "Grapheme-color synesthesia",
                "description": "Letters or numbers are perceived as inherently colored",
                "primary_sense": "vision",
                "secondary_sense": "color"
            },
            {
                "type": "Chromesthesia",
                "description": "Sounds evoke an experience of color",
                "primary_sense": "hearing",
                "secondary_sense": "color"
            },
            {
                "type": "Lexical-gustatory synesthesia",
                "description": "Certain words and phonemes evoke tastes",
                "primary_sense": "language",
                "secondary_sense": "taste"
            },
            {
                "type": "Spatial-sequence synesthesia",
                "description": "Numerical sequences are perceived as points in space",
                "primary_sense": "numbers",
                "secondary_sense": "spatial perception"
            },
            {
                "type": "Auditory-tactile synesthesia",
                "description": "Sounds evoke tactile sensations",
                "primary_sense": "hearing",
                "secondary_sense": "touch"
            }
        ]
        concepts = [
            "democracy",
            "quantum entanglement",
            "climate change",
            "artificial intelligence",
            "economic inequality",
            "biodiversity",
            "cultural relativism",
            "dark matter"
        ]
        tasks = {}
        for i in range(2):
            synesthesia = random.choice(synesthesia_types)
            concept = random.choice(concepts)
            tasks[str(i+1)] = {
                "synesthesia": synesthesia,
                "concept": concept
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Synesthesia is a neurological phenomenon where stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway. Your task is to design a language system based on {t['synesthesia']['type']} and use it to explain the concept of {t['concept']}.

1. Language System Design (200-250 words):
   a) Explain how your language system works, incorporating the principles of {t['synesthesia']['type']}.
   b) Describe how information is encoded and decoded in your system.
   c) Provide at least 5 examples of basic elements in your language (e.g., words, symbols) and their meanings.

2. Concept Translation (150-200 words):
   Translate the concept of "{t['concept']}" into your synesthetic language system. Explain the translation process and how the concept is represented in your system.

3. Advantages and Limitations (100-150 words):
   Discuss potential advantages and limitations of your synesthetic language system, particularly in relation to explaining complex concepts like {t['concept']}.

4. Cross-modal Applications (100-150 words):
   Propose an application of your synesthetic language system in a field unrelated to {t['synesthesia']['primary_sense']} or {t['synesthesia']['secondary_sense']}. Explain how it could provide unique insights or solutions.

Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of both synesthesia and linguistic principles. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed explanation of a language system based on {t['synesthesia']['type']}",
            f"The language system should be used to explain the concept of {t['concept']}",
            "The response should provide at least 5 examples of basic elements in the designed language",
            "The response should discuss advantages and limitations of the synesthetic language system",
            "The response should propose a cross-modal application of the synesthetic language system",
            "The response should demonstrate creativity and scientific grounding in both synesthesia and linguistic principles",
            "The response should be well-organized with clear headings for each section",
            "The language system should be logically consistent and demonstrate a clear connection to the principles of synesthesia"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
