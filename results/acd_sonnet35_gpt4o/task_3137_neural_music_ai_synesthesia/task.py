import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        sensory_modalities = ['visual', 'tactile', 'olfactory', 'gustatory']
        synesthetic_phenomena = ['chromesthesia', 'tactile-auditory synesthesia', 'lexical-gustatory synesthesia']
        
        tasks = {
            "1": {
                "musical_element": random.choice(musical_elements),
                "target_modality": random.choice(sensory_modalities),
                "synesthetic_phenomenon": random.choice(synesthetic_phenomena)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "target_modality": random.choice(sensory_modalities),
                "synesthetic_phenomenon": random.choice(synesthetic_phenomena)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and manipulates neural responses to music, simulating and enhancing synesthetic experiences across sensory modalities. Focus on the musical element of {t['musical_element']}, targeting the {t['target_modality']} sensory modality, and incorporate aspects of {t['synesthetic_phenomenon']}. Your response should include:

1. Neural-Music Interface (300-350 words):
   a) Describe the key components of your AI system for modeling neural responses to music.
   b) Explain how your system processes and represents the specified musical element.
   c) Detail how your model simulates the neural pathways involved in music perception and synesthesia.
   d) Discuss any novel techniques or algorithms used in your neural-music interface.

2. Synesthetic Mapping (250-300 words):
   a) Explain how your system maps musical features to the target sensory modality.
   b) Describe the specific mechanisms used to generate synesthetic experiences.
   c) Discuss how your model incorporates known aspects of {t['synesthetic_phenomenon']}.
   d) Provide an example of how your system would translate a musical passage into a synesthetic experience.

3. AI-Enhanced Synesthesia (200-250 words):
   a) Explain how your AI system could enhance or modify natural synesthetic experiences.
   b) Describe potential applications of your system in fields such as music therapy, artistic creation, or cognitive enhancement.
   c) Discuss ethical considerations related to artificially inducing or modifying synesthetic experiences.

4. Experimental Design (250-300 words):
   Propose an experiment using your AI system to investigate a specific aspect of music perception or synesthesia. Include:
   a) A clear research question related to neural responses to music or synesthetic experiences.
   b) The methodology for using your AI system to explore this question.
   c) Expected results and their potential implications for our understanding of music cognition or synesthesia.
   d) Potential limitations of using an AI model for this type of research.

5. Comparative Analysis (200-250 words):
   a) Compare your AI synesthesia model to natural synesthetic experiences in humans.
   b) Discuss similarities and differences between your model's output and documented synesthetic phenomena.
   c) Analyze what these comparisons might reveal about both human cognition and AI capabilities in modeling complex perceptual experiences.

6. Future Directions and Implications (150-200 words):
   a) Propose two future research directions that could build upon your neural music AI synesthesia model.
   b) Discuss the potential long-term implications of this technology for our understanding of consciousness, perception, and creativity.
   c) Explore how this type of AI system might influence the future of music composition and appreciation.

Ensure your response demonstrates a deep understanding of neuroscience, musicology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, musicology, and artificial intelligence, particularly in relation to {t['musical_element']}, {t['target_modality']} sensory modality, and {t['synesthetic_phenomenon']}.",
            "The AI system design is innovative, scientifically plausible, and effectively integrates neural modeling with music processing and synesthetic experience simulation.",
            "The explanation of synesthetic mapping and AI-enhanced synesthesia is clear, detailed, and grounded in current scientific understanding.",
            "The proposed experiment is well-designed, relevant, and demonstrates a thoughtful approach to investigating music perception or synesthesia.",
            "The comparative analysis shows insightful reflection on the similarities and differences between the AI model and natural synesthetic experiences.",
            "The response addresses ethical considerations and future implications of the technology in a nuanced and thought-provoking manner.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
