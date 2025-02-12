import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_worldviews = [
            {
                "name": "Cyclical Time Perception",
                "description": "A culture that perceives time as cyclical rather than linear"
            },
            {
                "name": "Collective Consciousness Priority",
                "description": "A society that prioritizes collective consciousness over individual identity"
            },
            {
                "name": "Quantum Interconnectedness",
                "description": "A civilization that views reality as fundamentally interconnected at a quantum level"
            },
            {
                "name": "Spiritual Materialism",
                "description": "A culture that sees all physical objects as imbued with spiritual significance"
            }
        ]
        return {
            "1": random.choice(cultural_worldviews),
            "2": random.choice(cultural_worldviews)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language feature based on the cultural worldview of {t['name']}: {t['description']}. Then analyze its potential impact on cognition and behavior. Your response should include:

1. Language Feature Design (200-250 words):
   a) Describe a unique grammatical, lexical, or phonological feature that reflects the given cultural worldview.
   b) Explain how this feature embodies or expresses the cultural perspective.
   c) Provide examples of how this feature would be used in the language.

2. Cognitive Impact Analysis (200-250 words):
   a) Discuss how this language feature might influence thought processes and perception.
   b) Analyze potential effects on memory, decision-making, or problem-solving.
   c) Consider how this feature might shape the speakers' worldview or cultural values.

3. Behavioral Implications (150-200 words):
   a) Predict how this language feature could affect social interactions or individual behaviors.
   b) Discuss potential implications for cultural practices or societal structures.
   c) Consider any adaptive advantages or challenges this feature might present.

4. Comparative Linguistics (100-150 words):
   a) Compare your designed feature to similar elements in existing human languages.
   b) Discuss how your feature is unique or goes beyond known linguistic phenomena.

5. Experimental Proposal (150-200 words):
   a) Design a hypothetical experiment to test the cognitive or behavioral effects of your language feature.
   b) Describe the methodology, including control groups and measurable outcomes.
   c) Discuss potential challenges in isolating the effects of the language feature.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and cultural anthropology. Be creative in your language design while maintaining scientific plausibility and logical consistency. Use appropriate terminology from relevant fields throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of linguistics, cognitive science, and cultural anthropology concepts.",
            "The designed language feature is creative, unique, and plausibly reflects the given cultural worldview.",
            "The cognitive impact analysis is well-reasoned and considers multiple aspects of cognition.",
            "The behavioral implications are logically derived and consider both individual and societal levels.",
            "The comparative linguistics section shows knowledge of existing language phenomena and highlights the uniqueness of the designed feature.",
            "The experimental proposal is well-designed and addresses potential challenges.",
            "The response uses appropriate terminology from linguistics, cognitive science, and cultural anthropology.",
            "The overall analysis is coherent, demonstrating the ability to connect language, thought, and culture.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
