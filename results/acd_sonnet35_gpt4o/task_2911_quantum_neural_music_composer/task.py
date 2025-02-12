import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "Superposition",
                "neural_structure": "Tonotopic organization",
                "music_genre": "Jazz",
                "cultural_context": "West African"
            },
            "2": {
                "quantum_principle": "Entanglement",
                "neural_structure": "Hierarchical predictive processing",
                "music_genre": "Classical",
                "cultural_context": "East Asian"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses the quantum computing principle of {t['quantum_principle']} and neural network architectures inspired by the {t['neural_structure']} of the human auditory cortex to compose and analyze {t['music_genre']} music in the {t['cultural_context']} context. Your response should include the following sections:

1. Quantum-Neural Music Model (300-350 words):
   a) Explain how {t['quantum_principle']} can be applied to music composition and analysis. Provide a specific example of how this principle could represent musical elements (e.g., pitch, rhythm, or harmony).
   b) Describe how you would model the {t['neural_structure']} using quantum-inspired neural networks. Include a brief comparison with classical neural network approaches.
   c) Discuss how this integration can capture unique aspects of {t['music_genre']} in the {t['cultural_context']} context. Give an example of a specific musical feature that your model could represent more effectively than traditional approaches.
   d) Provide a high-level diagram or pseudocode representing your model's architecture. Ensure you explain each component and its role in the system.

2. Composition Process (250-300 words):
   a) Explain how your AI system would generate new musical compositions. Describe the step-by-step process, from initialization to final output.
   b) Describe how {t['quantum_principle']} influences the creative process. Provide a concrete example of how this principle enables a unique compositional technique.
   c) Discuss how the {t['neural_structure']} inspiration affects the musical structure and complexity. Relate this to known cognitive processes in human music perception.
   d) Provide an example of how a specific {t['cultural_context']} musical element (e.g., a particular scale, rhythm pattern, or instrumental technique) would be incorporated into the composition process.

3. Music Analysis Capabilities (250-300 words):
   a) Describe how your system would analyze existing {t['music_genre']} pieces. Outline the key features or patterns it would identify.
   b) Explain how {t['quantum_principle']} enhances the analysis process. Provide an example of an analytical task that becomes more efficient or accurate using this quantum approach.
   c) Discuss how the system's understanding of {t['neural_structure']} contributes to identifying musical patterns and structures. Relate this to theories of human music cognition.
   d) Provide an example of a unique insight your system might uncover about {t['music_genre']} in the {t['cultural_context']} context, which might be challenging for traditional music analysis methods.

4. Cross-Cultural Applications (200-250 words):
   a) Explain how your system could be adapted to other musical genres and cultural contexts. Provide a specific example of how it might be applied to a contrasting genre/culture pair.
   b) Discuss potential insights into universal musical features that your approach might reveal. Propose a hypothesis about music cognition that your system could help test.
   c) Describe a hypothetical experiment using your system to explore cross-cultural musical influences. Include the experimental design, data collection method, and expected outcomes.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues in using AI for music composition and cultural analysis. Address concerns of cultural appropriation and the impact on human musicians.
   b) Address limitations of your quantum-neural approach in capturing human creativity and cultural nuances. Provide an example of a musical aspect your system might struggle to represent or generate.
   c) Propose guidelines for responsible development and use of such AI systems in music and cultural studies. Include considerations for transparency, bias mitigation, and stakeholder involvement.

6. Future Directions and Implications (150-200 words):
   a) Suggest potential expansions or modifications to your system for other applications in music or cognitive science. Provide a specific example of how it could be adapted for a different domain.
   b) Discuss how this technology might impact the music industry and our understanding of human creativity. Consider both positive and negative potential outcomes.
   c) Speculate on the long-term implications of quantum-neural AI systems for the arts and cultural preservation. Propose a potential scenario for how music creation and appreciation might evolve with such technology.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and music theory. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section (e.g., '1. Quantum-Neural Music Model', '2. Composition Process', etc.). Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding and integration of {t['quantum_principle']}, {t['neural_structure']}, {t['music_genre']}, and {t['cultural_context']} context.",
            "The quantum-neural music model is well-explained with specific examples of how quantum principles are applied to music composition and analysis.",
            "The composition process and analysis capabilities show creative and well-reasoned applications of quantum and neural elements to music creation and understanding.",
            "The cross-cultural applications section includes a concrete example of adapting the system to a different genre/culture and a well-designed hypothetical experiment.",
            "Ethical considerations and limitations are thoughtfully addressed with specific examples and proposed guidelines.",
            "The response is well-structured with clear headings, within the specified word limit, and includes a word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
