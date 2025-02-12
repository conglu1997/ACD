import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "abstract_concept": "time",
                "concrete_domain": "nature",
                "emotional_tone": "melancholic"
            },
            {
                "abstract_concept": "freedom",
                "concrete_domain": "architecture",
                "emotional_tone": "hopeful"
            },
            {
                "abstract_concept": "knowledge",
                "concrete_domain": "ocean",
                "emotional_tone": "curious"
            },
            {
                "abstract_concept": "power",
                "concrete_domain": "weather",
                "emotional_tone": "intimidating"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets visual metaphors based on linguistic input, then analyze its cognitive processes and potential applications. Focus on creating a visual metaphor for the abstract concept of {t['abstract_concept']}, using elements from the concrete domain of {t['concrete_domain']}, while conveying an {t['emotional_tone']} emotional tone.

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and interpreting visual metaphors.
   b) Explain how your system integrates natural language processing, visual cognition, and creative problem-solving.
   c) Detail how the system maps abstract linguistic concepts to concrete visual elements.
   d) Discuss any novel algorithms or approaches used in your system.

2. Visual Metaphor Generation (250-300 words):
   a) Explain how your system would generate a visual metaphor for {t['abstract_concept']} using elements from {t['concrete_domain']}.
   b) Describe the process of incorporating the {t['emotional_tone']} emotional tone into the visual metaphor.
   c) Provide a detailed textual description of the visual metaphor your system would generate.
   d) Discuss how your system ensures the metaphor is both creative and comprehensible.

3. Cognitive Process Analysis (250-300 words):
   a) Analyze the cognitive processes involved in your AI's generation of visual metaphors.
   b) Compare these processes to human cognitive processes in metaphor creation and interpretation.
   c) Discuss any insights your system might provide about the nature of human creativity and cognition.
   d) Explain how your system handles potential ambiguities or cultural differences in metaphor interpretation.

4. Interpretation and Evaluation (200-250 words):
   a) Describe how your AI system would interpret and evaluate the effectiveness of its own generated visual metaphors.
   b) Propose metrics for assessing the quality, creativity, and communicative power of the generated metaphors.
   c) Explain how your system could learn and improve its metaphor generation based on feedback or evaluation.

5. Potential Applications and Ethical Considerations (200-250 words):
   a) Suggest two potential applications of your visual metaphor AI system in fields such as education, art, or cross-cultural communication.
   b) Discuss ethical considerations in using AI for creative tasks traditionally performed by humans.
   c) Address potential biases in your system and how you would mitigate them.
   d) Propose guidelines for responsible development and use of AI in generating visual metaphors.

6. Future Research Directions (150-200 words):
   a) Identify areas where your system could be expanded or improved.
   b) Propose a specific experiment to further explore the relationship between linguistic input and visual metaphor generation.
   c) Discuss potential implications of this technology for our understanding of language, cognition, and creativity.

Ensure your response demonstrates a deep understanding of linguistics, visual cognition, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering ethical implications.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, visual cognition, and artificial intelligence.",
            "The proposed system effectively integrates natural language processing, visual cognition, and creative problem-solving.",
            "The visual metaphor generation process is well-explained and incorporates the given abstract concept, concrete domain, and emotional tone.",
            "The analysis of cognitive processes is insightful and compares AI processes to human cognition.",
            "The submission addresses ethical considerations and potential biases in AI-generated visual metaphors.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The proposed applications and future research directions are innovative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
