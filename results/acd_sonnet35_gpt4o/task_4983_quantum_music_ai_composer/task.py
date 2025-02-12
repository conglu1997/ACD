class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_concept": "superposition",
                "musical_element": "harmony",
                "musical_style": "classical"
            },
            "2": {
                "quantum_concept": "entanglement",
                "musical_element": "rhythm",
                "musical_style": "jazz"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual model that integrates the quantum concept of {t['quantum_concept']} with the musical element of {t['musical_element']}. Then, use your model to analyze a short musical phrase in the {t['musical_style']} style. Your response should include:

        1. Conceptual Model (200-250 words):
           a) Explain how you conceptually link {t['quantum_concept']} with {t['musical_element']}.
           b) Describe the key components of your quantum-inspired musical model.
           c) Discuss any novel insights this integration might bring to music analysis or composition.

        2. Model Application (200-250 words):
           a) Provide a short (4-8 bars) musical phrase in the {t['musical_style']} style, using standard notation, lead sheet, or clear textual description.
           b) Analyze this phrase using your quantum-inspired model, focusing on the {t['musical_element']} aspect.
           c) Explain how the {t['quantum_concept']} principle manifests in your analysis.

        3. Implications and Potential (150-200 words):
           a) Discuss how this quantum-inspired approach might offer new perspectives on {t['musical_style']} music.
           b) Propose one potential application of your model in music theory or composition.
           c) Briefly address any limitations or ethical considerations of applying quantum concepts to music.

        Ensure your response demonstrates an understanding of both {t['quantum_concept']} and {t['musical_element']}. Use appropriate terminology from quantum physics and music theory, providing clear explanations for complex concepts. Be creative in your approach while maintaining scientific and musical plausibility.

        Format your response with clear headings for each section. Your total response should be between 550-700 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response presents a plausible conceptual link between {t['quantum_concept']} and {t['musical_element']}.",
            f"A musical phrase in the {t['musical_style']} style is provided and analyzed using the quantum-inspired model.",
            f"The analysis demonstrates an attempt to apply {t['quantum_concept']} principles to {t['musical_element']}.",
            "The response discusses potential implications or applications of the quantum-inspired approach to music.",
            "The overall response is coherent and demonstrates an attempt at interdisciplinary knowledge integration."
        ]
        word_count = len(submission.split())
        if word_count < 500 or word_count > 750:  # Allow a 50-word margin on either side
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
