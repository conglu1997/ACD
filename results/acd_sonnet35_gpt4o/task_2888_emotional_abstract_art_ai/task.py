class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "emotional_state": "Ambivalence",
                "art_style": "Abstract Expressionism",
                "cultural_context": "Contemporary Western"
            },
            "2": {
                "emotional_state": "Nostalgia",
                "art_style": "Surrealism",
                "cultural_context": "East Asian"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract conceptual art based on complex emotional states, then analyze its potential impact on human creativity and emotional intelligence. Focus on the emotional state of {t['emotional_state']}, the art style of {t['art_style']}, and the {t['cultural_context']} cultural context.

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and interpreting abstract conceptual art.
   b) Explain how your system processes and represents complex emotional states.
   c) Detail how the system incorporates cultural context and art style information.
   d) Discuss any novel algorithms or approaches used in your design.
   e) Provide a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Emotional State Analysis (200-250 words):
   a) Analyze the complex emotional state of {t['emotional_state']}.
   b) Explain how your AI system would represent and process this emotional state.
   c) Discuss how cultural context influences the understanding and expression of this emotion.

3. Art Generation Process (250-300 words):
   a) Describe the step-by-step process your AI system would use to generate abstract conceptual art based on the given emotional state.
   b) Explain how the system incorporates the specified art style ({t['art_style']}) in its generation process.
   c) Provide a detailed description of an example artwork your system might generate, highlighting how it reflects the emotional state and cultural context.

4. Art Interpretation Process (200-250 words):
   a) Explain how your AI system would interpret abstract conceptual art representing the given emotional state.
   b) Describe the features or elements the system would analyze to understand the artwork's emotional content.
   c) Discuss how the system accounts for cultural context and art style in its interpretation.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your AI system in generating and interpreting emotionally-charged abstract art.
   b) Describe experiments or studies to validate the system's performance and its alignment with human perception.
   c) Discuss potential limitations of your approach and how they might be addressed.

6. Impact on Human Creativity and Emotional Intelligence (200-250 words):
   a) Analyze how your AI system might influence or enhance human creativity in abstract art.
   b) Discuss the potential impact on human emotional intelligence and empathy.
   c) Explore how this technology could be used in art therapy or emotional education.
   d) Consider any potential negative effects on human artistic expression or emotional processing.

7. Ethical Considerations and Future Developments (150-200 words):
   a) Discuss ethical implications of using AI systems to generate and interpret emotionally-charged art.
   b) Propose guidelines for responsible development and use of such systems in artistic and therapeutic contexts.
   c) Suggest potential future enhancements or research directions for your AI system.

Ensure your response demonstrates a deep understanding of artificial intelligence, emotional psychology, art theory, and cultural studies. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI systems, emotional psychology, art theory, and cultural studies.",
            "The AI system architecture is well-designed and addresses the complexities of generating and interpreting abstract conceptual art based on emotions.",
            "The analysis of the emotional state is thorough and considers cultural context.",
            "The art generation and interpretation processes are clearly explained and incorporate the specified art style and cultural context.",
            "The proposed evaluation methods and experiments are appropriate and well-reasoned.",
            "The discussion of the impact on human creativity and emotional intelligence is insightful and considers both positive and negative effects.",
            "Ethical considerations are thoughtfully addressed, and future research directions are proposed.",
            "The response is creative and innovative while maintaining scientific and technological plausibility.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
