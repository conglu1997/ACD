import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = ['Baroque', 'Classical', 'Romantic', 'Jazz', 'Electronic']
        cognitive_principles = ['Working Memory', 'Attention', 'Pattern Recognition', 'Expectation']
        emotional_targets = ['Joy', 'Sadness', 'Tension', 'Nostalgia', 'Awe']
        
        return {
            "1": {
                "style": random.choice(musical_styles),
                "cognitive_principle": random.choice(cognitive_principles),
                "emotion": random.choice(emotional_targets)
            },
            "2": {
                "style": random.choice(musical_styles),
                "cognitive_principle": random.choice(cognitive_principles),
                "emotion": random.choice(emotional_targets)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing, generating, and manipulating complex musical structures based on cognitive and emotional principles, then use it to compose a piece that elicits specific emotional responses. This task requires a deep understanding and integration of music theory, cognitive science, artificial intelligence, and emotional psychology.

Your system should focus on the musical style of {t['style']}, incorporate the cognitive principle of {t['cognitive_principle']}, and aim to evoke the emotion of {t['emotion']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI music cognition system.
   b) Explain how your system integrates music theory, cognitive science, and emotional psychology.
   c) Detail how your system incorporates the specified cognitive principle in its music processing.
   d) Discuss any novel AI techniques or algorithms used in your system.

2. Musical Analysis and Generation (250-300 words):
   a) Explain how your system analyzes and represents musical structures in the specified style.
   b) Describe the process by which your AI generates new musical ideas.
   c) Discuss how your system ensures coherence and adherence to the chosen musical style.

3. Cognitive-Emotional Mapping (250-300 words):
   a) Describe how your system maps musical elements to cognitive processes and emotional responses.
   b) Explain the theoretical basis for these mappings, citing relevant research in music psychology.
   c) Discuss how the system uses these mappings to guide its composition process.

4. Composition Process (300-350 words):
   a) Provide a step-by-step description of how your AI system would compose a piece to evoke the specified emotion.
   b) Explain how the system incorporates the chosen cognitive principle throughout the composition process.
   c) Describe specific musical techniques or structures the AI would use to elicit the target emotion.
   d) Include a short excerpt (8-12 measures) of the composed piece in musical notation or a detailed verbal description. If using notation, provide it in a text-based format (e.g., ABC notation or a detailed textual description of the notes, rhythms, and other musical elements).

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your AI's composition in evoking the target emotion.
   b) Describe an experiment to test whether the composed piece activates the specified cognitive principle in listeners.
   c) Discuss potential challenges in validating the AI's output and how you would address them.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI to compose emotionally evocative music.
   b) Address potential concerns about AI-generated music in the context of human creativity and artistry.
   c) Propose future research directions or extensions of your AI music cognition system.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, artificial intelligence, and emotional psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['style']} musical style and provides specific examples of how the AI system generates music in this style.",
            f"The AI system effectively incorporates the cognitive principle of {t['cognitive_principle']} in its music processing and composition, with clear explanations of how this principle influences the system's operations.",
            f"The composition process and output are clearly aimed at evoking the emotion of {t['emotion']}, with specific musical techniques or structures described to achieve this goal.",
            "The AI system architecture integrates music theory, cognitive science, and emotional psychology in a novel and plausible way, with clear explanations of how these disciplines interact within the system.",
            "The response includes a detailed description or notation of a musical excerpt (8-12 measures) composed by the AI system, which aligns with the specified style, cognitive principle, and emotional target.",
            "The proposed evaluation methods are scientifically sound, appropriate for validating the AI's output, and include specific experimental designs.",
            "Ethical considerations regarding AI-generated music are thoughtfully addressed, with consideration of multiple perspectives and potential societal impacts.",
            "The response is well-structured, following the specified format, and falls within the 1450-1750 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
