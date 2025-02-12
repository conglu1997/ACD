import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre', 'dynamics']
        cultural_contexts = ['Western classical', 'Jazz', 'Indian classical', 'Chinese traditional', 'African tribal']
        
        tasks = [
            {
                'emotion': random.choice(emotions),
                'musical_element': random.choice(musical_elements),
                'cultural_context': random.choice(cultural_contexts)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of composing emotionally expressive music by integrating music theory, emotional intelligence, and cultural context awareness. Your system should focus on expressing the emotion of {t['emotion']} through the musical element of {t['musical_element']}, within the cultural context of {t['cultural_context']} music. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music composition system.
   b) Explain how your system integrates music theory, emotional intelligence, and cultural awareness.
   c) Detail how the system processes and generates music focusing on the specified musical element.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Emotional-Musical Mapping (250-300 words):
   a) Explain how your system maps the specified emotion to musical characteristics.
   b) Describe any novel algorithms or methods used for emotional expression in music.
   c) Discuss how cultural context influences this emotional-musical mapping.

3. Composition Process (250-300 words):
   a) Detail the step-by-step process your AI system would use to compose a piece expressing the given emotion.
   b) Explain how the system ensures cultural authenticity and emotional effectiveness in its composition.
   c) Describe how the system focuses on and manipulates the specified musical element to convey emotion.

4. Evaluation Mechanism (200-250 words):
   a) Propose methods to evaluate the emotional expressiveness and cultural authenticity of the AI-composed music.
   b) Describe experiments or studies to validate the system's performance against human composers and listeners.
   c) Discuss potential challenges in evaluating emotional expression in music across cultures.

5. Ethical Considerations (200-250 words):
   a) Discuss ethical implications of using AI systems to compose emotionally expressive music.
   b) Address concerns about cultural appropriation and the authenticity of AI-generated cultural expressions.
   c) Propose guidelines for responsible development and use of emotion-aware music composition AI.

6. Potential Applications (150-200 words):
   a) Suggest potential applications of your AI system in fields such as therapy, entertainment, or cross-cultural communication.
   b) Discuss how this technology might impact the music industry and human composers.
   c) Propose an innovative use case that combines emotional music composition with another field or technology.

7. Future Research Directions (150-200 words):
   a) Propose two novel research questions that arise from your system design.
   b) Suggest potential improvements or expansions to your system for future development.
   c) Discuss how advancements in this field might contribute to our understanding of music, emotions, and cultural expression.

Ensure your response demonstrates a deep understanding of music theory, emotional intelligence, cultural studies, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific emotion of {t['emotion']}, musical element of {t['musical_element']}, and cultural context of {t['cultural_context']}",
            "The design should clearly integrate principles from music theory, emotional intelligence, and cultural studies",
            "The response should include all required sections: System Architecture, Emotional-Musical Mapping, Composition Process, Evaluation Mechanism, Ethical Considerations, Potential Applications, and Future Research Directions",
            "The proposed system should be innovative while maintaining scientific and technological plausibility",
            "The response should demonstrate a deep understanding of music theory, emotional intelligence, cultural studies, and artificial intelligence",
            "The discussion should be creative while addressing potential challenges and limitations in emotionally expressive AI music composition"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
