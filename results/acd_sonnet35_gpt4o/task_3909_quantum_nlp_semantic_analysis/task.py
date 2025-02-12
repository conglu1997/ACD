import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "Superposition",
                "linguistic_feature": "Polysemy",
                "literary_work": "Ulysses by James Joyce",
                "analysis_focus": "Stream of consciousness passages",
                "sample_passage": "riverrun, past Eve and Adam's, from swerve of shore to bend of bay, brings us by a commodius vicus of recirculation back to Howth Castle and Environs."
            },
            {
                "quantum_concept": "Entanglement",
                "linguistic_feature": "Semantic coherence",
                "literary_work": "One Hundred Years of Solitude by Gabriel García Márquez",
                "analysis_focus": "Intergenerational narrative connections",
                "sample_passage": "Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system for advanced semantic analysis, incorporating the quantum concept of {t['quantum_concept']} to analyze the linguistic feature of {t['linguistic_feature']}. Then, apply your system to analyze {t['analysis_focus']} in the literary work "{t['literary_work']}". Your response should include:

1. Quantum NLP System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired NLP system.
   b) Explain how you incorporate {t['quantum_concept']} into your NLP algorithms.
   c) Detail how your system analyzes {t['linguistic_feature']} using quantum-inspired methods.
   d) Provide a mathematical formulation of your core algorithm, using appropriate quantum notation.

2. Linguistic Analysis Framework (250-300 words):
   a) Explain how your system identifies and analyzes {t['linguistic_feature']} in text.
   b) Describe how quantum principles enhance this analysis compared to classical NLP approaches.
   c) Discuss any challenges in applying quantum concepts to linguistic analysis and how you address them.

3. Literary Analysis Application (300-350 words):
   a) Apply your quantum NLP system to analyze {t['analysis_focus']} in "{t['literary_work']}".
   b) Provide specific examples from the text and explain your system's analysis.
   c) Discuss how your quantum-inspired approach reveals new insights into the literary work.
   d) Analyze the following sample passage using your system: "{t['sample_passage']}"
      Explain step-by-step how your quantum NLP system processes and interprets this passage.

4. Comparative Evaluation (200-250 words):
   a) Compare your quantum NLP system's performance to traditional NLP methods for this analysis.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose a method to quantify the 'quantum advantage' in NLP analysis, if any.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of quantum-inspired NLP for literary analysis and linguistics.
   b) Propose potential applications in other domains (e.g., machine translation, sentiment analysis).
   c) Suggest future research directions to extend or refine your quantum NLP system.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and literary analysis. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1500 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum-inspired NLP system incorporating {t['quantum_concept']} to analyze {t['linguistic_feature']}",
            f"The system is applied to analyze {t['analysis_focus']} in \"{t['literary_work']}\"",
            f"The response includes a step-by-step analysis of the sample passage: \"{t['sample_passage']}\"",
            "The response demonstrates deep understanding of quantum computing, linguistics, and literary analysis",
            "The proposed system and analysis are innovative while maintaining scientific plausibility",
            "The comparative evaluation and future directions are thoughtfully addressed",
            "The response follows the specified format and word count",
            "The submission does not contain direct copies of the instructions or trivial responses"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
