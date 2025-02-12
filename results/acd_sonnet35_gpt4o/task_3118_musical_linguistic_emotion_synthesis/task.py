import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_input": "A heartfelt apology",
                "target_emotion": "Remorse and hope",
                "musical_style": "Classical",
                "application_domain": "Conflict resolution therapy"
            },
            {
                "linguistic_input": "A declaration of love",
                "target_emotion": "Joy and excitement",
                "musical_style": "Jazz",
                "application_domain": "Cross-cultural wedding ceremonies"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can synthesize original music based on linguistic input and target emotional states, then analyze its potential applications in therapy and cross-cultural communication. Your system should focus on the following specifications:

Linguistic Input: {t['linguistic_input']}
Target Emotion: {t['target_emotion']}
Musical Style: {t['musical_style']}
Application Domain: {t['application_domain']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for musical-linguistic-emotional synthesis.
   b) Explain how your system processes linguistic input and translates it into musical elements.
   c) Detail how the system incorporates the target emotional state into the music generation process.
   d) Discuss how your system ensures the generated music adheres to the specified musical style.
   e) Include a brief description of a flowchart or diagram representing your system's architecture.

2. Linguistic-Musical Mapping (250-300 words):
   a) Explain your approach to mapping linguistic features (e.g., syntax, semantics, prosody) to musical elements (e.g., melody, harmony, rhythm).
   b) Describe how your system handles the challenge of maintaining semantic coherence between the linguistic input and the generated music.
   c) Provide an example of how a specific phrase from the given linguistic input might be translated into musical elements.

3. Emotion Integration (250-300 words):
   a) Describe the model or framework your system uses to represent and manipulate emotions in music.
   b) Explain how your system ensures the generated music evokes the target emotional state.
   c) Discuss any challenges in balancing emotional expression with linguistic meaning and musical style.

4. Style Adaptation (200-250 words):
   a) Explain how your system adapts to different musical styles.
   b) Describe any techniques used to ensure authenticity and coherence within the specified style.
   c) Discuss how your system might handle potential conflicts between the target emotion, linguistic input, and musical style.

5. Application Analysis (250-300 words):
   a) Analyze the potential benefits and challenges of applying your system in the specified domain.
   b) Propose a specific use case within this domain and explain how your system would be employed.
   c) Discuss any ethical considerations or potential risks associated with using AI-generated emotional music in this context.

6. Cross-cultural Considerations (200-250 words):
   a) Explore how your system might need to be adapted for use across different cultures.
   b) Discuss potential challenges in emotional and musical interpretation across cultural boundaries.
   c) Propose methods for making your system more culturally adaptive and inclusive.

7. Evaluation and Future Directions (200-250 words):
   a) Suggest methods for evaluating the effectiveness of your system in generating emotionally appropriate music.
   b) Propose an experiment to test your system's impact in the specified application domain.
   c) Discuss potential future improvements or extensions to your system.

Ensure your response demonstrates a deep understanding of musicology, linguistics, affective computing, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of musicology, linguistics, affective computing, and artificial intelligence.",
            "The system design is innovative, coherent, and scientifically plausible.",
            "The linguistic-musical mapping and emotion integration approaches are well-explained and logical.",
            "The application analysis and cross-cultural considerations are thorough and insightful.",
            "The response addresses all required sections and adheres to the specified word count.",
            f"The system effectively incorporates the given linguistic input '{t['linguistic_input']}', target emotion '{t['target_emotion']}', and musical style '{t['musical_style']}'.",
            f"The application analysis is relevant to the specified domain of {t['application_domain']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
