import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'proprioceptive', 'vestibular']
        linguistic_aspects = ['semantic representation', 'syntactic processing', 'pragmatic understanding', 'metaphor comprehension', 'language acquisition']
        
        task1 = {
            'sensory_modality': random.choice(sensory_modalities),
            'linguistic_aspect': random.choice(linguistic_aspects)
        }
        
        task2 = {
            'sensory_modality': random.choice(sensory_modalities),
            'linguistic_aspect': random.choice(linguistic_aspects)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model architecture that incorporates principles of embodied cognition, focusing on the integration of {t['sensory_modality']} sensory-motor experiences in {t['linguistic_aspect']}. Your response should include:

1. Theoretical Foundation (150-200 words):
   Explain the key principles of embodied cognition and how they relate to language processing, particularly in the context of {t['sensory_modality']} experiences and {t['linguistic_aspect']}.

2. Model Architecture (250-300 words):
   Describe your proposed language model architecture, including:
   - How it incorporates {t['sensory_modality']} sensory-motor information
   - How it integrates this information with traditional language processing for {t['linguistic_aspect']}
   - The main components and their interactions
   - How the model processes and generates language
   Provide a high-level diagram or pseudocode to illustrate your architecture.

3. Training and Data Requirements (150-200 words):
   Explain how your model would be trained, addressing:
   - The types of data required (linguistic and sensory-motor)
   - Any novel training approaches or techniques
   - How the model might simulate aspects of human language acquisition

4. Potential Advantages and Challenges (200-250 words):
   Discuss the potential advantages of your model over traditional language models, particularly in {t['linguistic_aspect']}. Address any challenges or limitations in implementing this architecture.

5. Implications and Applications (200-250 words):
   Explore the broader implications of your model for:
   - Natural language processing and AI
   - Our understanding of human language and cognition
   - Potential applications in fields like education, human-computer interaction, or cognitive assistance
   Propose at least two specific use cases or experiments to demonstrate the unique capabilities of your model.

Ensure your response demonstrates a deep understanding of embodied cognition, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition and its relevance to language processing.",
            f"The model architecture effectively incorporates {t['sensory_modality']} sensory-motor experiences in {t['linguistic_aspect']}.",
            "The proposed training approach and data requirements are well-explained and feasible.",
            "The discussion of advantages and challenges is insightful and comprehensive.",
            "The implications and applications are thoughtfully explored with creative and plausible use cases.",
            "The response maintains a high level of interdisciplinary integration throughout.",
            "The answer is well-structured, clear, and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
