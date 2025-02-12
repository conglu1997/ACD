class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "musical_tradition": "Indian classical music",
                "cognitive_principle": "auditory scene analysis",
                "composition_task": "Create a new raga",
                "sample_phrase": "Sa Re Ga Ma Pa Dha Ni Sa"
            },
            "2": {
                "musical_tradition": "West African polyrhythms",
                "cognitive_principle": "entrainment theory",
                "composition_task": "Compose a piece for talking drum ensemble",
                "rhythm_pattern": "1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of composing and analyzing complex musical pieces in {t['musical_tradition']}, incorporating the cognitive principle of {t['cognitive_principle']}. Your system should {t['composition_task']}.

Provide your response in the following format, with word counts as specified:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI music composition and analysis system.
   b) Explain how your system integrates knowledge from music theory, cognitive science, and cultural musicology.
   c) Detail how the system incorporates {t['cognitive_principle']} in its music processing.

2. Musical Tradition Integration (200-250 words):
   a) Explain how your system models and incorporates the principles of {t['musical_tradition']}.
   b) Describe how your system ensures cultural authenticity in its compositions and analyses.

3. Composition Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to {t['composition_task']}.
   b) Explain how the system balances creativity with adherence to traditional forms and structures.
   c) Demonstrate how your system would use or transform the given sample phrase or rhythm pattern: {t['sample_phrase'] if 'sample_phrase' in t else t['rhythm_pattern']}

4. Cognitive Principle Application (150-200 words):
   a) Explain how {t['cognitive_principle']} is specifically applied in the context of {t['musical_tradition']}.
   b) Provide an example of how this application enhances the composition or analysis process.

5. Analysis Capabilities (200-250 words):
   a) Describe how your AI system analyzes existing musical pieces within {t['musical_tradition']}.
   b) Explain what insights your system can provide about the structure, emotional content, and cultural significance of analyzed pieces.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI for composing and analyzing culturally significant music.
   b) Propose guidelines for responsible development and use of AI in music composition and analysis.

7. Sample Composition:
   Provide a brief musical notation or textual representation (50-100 words) of a sample composition created by your AI system, demonstrating its understanding of {t['musical_tradition']}.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and the specific musical tradition. Use appropriate technical terminology and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['musical_tradition']} and {t['cognitive_principle']}.",
            "The AI system architecture integrates music theory, cognitive science, and cultural musicology.",
            f"The composition process explains how the system uses or transforms the given sample phrase or rhythm pattern: {t['sample_phrase'] if 'sample_phrase' in t else t['rhythm_pattern']}",
            f"The application of {t['cognitive_principle']} in the context of {t['musical_tradition']} is clearly explained with an example.",
            "Ethical considerations are thoughtfully addressed with proposed guidelines.",
            f"A sample composition demonstrating understanding of {t['musical_tradition']} is provided.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
