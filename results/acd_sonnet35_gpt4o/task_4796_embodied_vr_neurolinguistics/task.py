import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'vr_environment': 'ancient marketplace',
                'target_language': 'Classical Greek',
                'embodied_aspect': 'gestures and spatial metaphors'
            },
            {
                'vr_environment': 'futuristic space station',
                'target_language': 'Mandarin Chinese',
                'embodied_aspect': 'tonal production and perception'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that simulates embodied language learning experiences in a {t['vr_environment']} for {t['target_language']}, focusing on {t['embodied_aspect']}. Then, analyze its effects on neural language processing using an AI-driven neuroimaging interpreter. Your response should include the following sections:

1. Virtual Reality System Design (300-350 words):
   a) Describe the key components of your VR system for embodied language learning.
   b) Explain how the {t['vr_environment']} environment is designed to facilitate learning of {t['target_language']}.
   c) Detail how your system incorporates {t['embodied_aspect']} into the language learning experience.
   d) Discuss any novel VR technologies or techniques used in your design.

2. Embodied Cognition and Language Learning (250-300 words):
   a) Explain the theoretical basis for using embodied cognition in language learning.
   b) Describe how your VR system leverages embodied cognition principles for {t['target_language']}.
   c) Discuss potential advantages of this approach over traditional language learning methods.

3. AI-Driven Neuroimaging Interpreter (250-300 words):
   a) Describe the architecture of your AI system for interpreting neuroimaging data.
   b) Explain how it processes and analyzes neural activity related to language learning.
   c) Detail any novel algorithms or techniques used in your AI interpreter.

4. Experimental Design and Analysis (200-250 words):
   a) Propose an experiment to test the effectiveness of your VR language learning system.
   b) Describe how you would use the AI neuroimaging interpreter to analyze the results.
   c) Discuss expected outcomes and how they might differ from traditional language learning methods.

5. Neurolinguistic Implications (200-250 words):
   a) Analyze potential impacts of embodied VR language learning on neural language processing.
   b) Discuss how this approach might change our understanding of language acquisition.
   c) Propose a hypothesis about long-term neural plasticity resulting from this method.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to using VR and AI in language learning and neural analysis.
   b) Discuss limitations of your system and how they might be addressed in future iterations.
   c) Propose guidelines for responsible use of this technology in educational and research settings.

7. Future Directions and Applications (150-200 words):
   a) Suggest two potential extensions or improvements to your embodied VR neurolinguistics system.
   b) Discuss how this technology might be applied to other areas of cognitive science or education.
   c) Speculate on the long-term implications of this approach for language learning and cognitive enhancement.

Ensure your response demonstrates a deep understanding of virtual reality technology, embodied cognition, neurolinguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a VR system for embodied language learning in a {t['vr_environment']} for {t['target_language']}, focusing on {t['embodied_aspect']}.",
            "The design demonstrates a deep understanding of virtual reality technology, embodied cognition, neurolinguistics, and artificial intelligence.",
            "The AI-driven neuroimaging interpreter is thoroughly explained and its application is well-described.",
            "The experimental design and analysis section is well-thought-out and scientifically plausible.",
            "The response addresses neurolinguistic implications, ethical considerations, and future directions comprehensively.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
