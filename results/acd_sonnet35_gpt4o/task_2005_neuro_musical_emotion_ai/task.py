import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {
                'emotion': 'Joy',
                'musical_feature': 'Major key, fast tempo',
                'brain_region': 'Nucleus accumbens'
            },
            {
                'emotion': 'Sadness',
                'musical_feature': 'Minor key, slow tempo',
                'brain_region': 'Amygdala'
            },
            {
                'emotion': 'Fear',
                'musical_feature': 'Dissonant harmonies, irregular rhythm',
                'brain_region': 'Hippocampus'
            }
        ]
        return {str(i+1): emotion for i, emotion in enumerate(random.sample(emotions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand and generate emotionally impactful music based on neuroscientific principles of music perception and emotion. Focus on the emotion of {t['emotion']}, typically associated with {t['musical_feature']} in music and the {t['brain_region']} in the brain. Your response should include:

1. Neuroscientific Framework (200-250 words):
   a) Explain the neural mechanisms involved in perceiving and processing {t['emotion']} in music.
   b) Describe how {t['musical_feature']} relates to the activation of the {t['brain_region']}.
   c) Discuss any relevant neurotransmitters or hormones involved in this emotional response.

2. AI System Architecture (250-300 words):
   a) Propose an AI architecture that can analyze and generate music to evoke {t['emotion']}.
   b) Explain how your system incorporates the neuroscientific principles discussed above.
   c) Describe the key components of your AI, including any novel neural network structures or algorithms.
   d) Discuss how your system would be trained on existing music data and neuroscientific findings.

3. Music Generation Process (200-250 words):
   a) Explain how your AI would generate new music to evoke {t['emotion']}.
   b) Describe how it would manipulate {t['musical_feature']} and other relevant musical elements.
   c) Discuss how the system ensures both musical coherence and emotional impact.

4. Evaluation Method (200-250 words):
   a) Propose a method to evaluate the emotional impact of the AI-generated music.
   b) Describe how you would use neuroimaging techniques to validate the activation of the {t['brain_region']}.
   c) Discuss potential challenges in measuring subjective emotional responses to AI-generated music.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to manipulate human emotions through music.
   b) Consider potential misuse of this technology and propose safeguards.
   c) Explore the impact on human creativity and the music industry.

6. Future Applications (150-200 words):
   a) Propose two potential applications of your AI system beyond music composition.
   b) Discuss how this technology could advance our understanding of emotion, music, and the brain.
   c) Speculate on potential long-term impacts on society and human-AI interaction.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            "The AI system design is innovative, well-explained, and grounded in neuroscientific principles.",
            "The music generation process is clearly described and accounts for both musical coherence and emotional impact.",
            "The evaluation method is comprehensive, incorporating both subjective and objective measures.",
            "Ethical considerations are thoroughly discussed with thoughtful safeguards proposed.",
            "Future applications and impacts are insightful and well-reasoned.",
            "The response includes all required sections with appropriate detail and word count.",
            "Technical terminology is used appropriately and explanations are provided where necessary.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
