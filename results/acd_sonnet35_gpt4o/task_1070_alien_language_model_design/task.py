import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                'species': 'Quantum Resonators',
                'sensory_system': 'Quantum entanglement detection',
                'cognitive_feature': 'Collective consciousness',
                'communication_medium': 'Manipulated quantum fields'
            },
            {
                'species': 'Chrono-Shifters',
                'sensory_system': 'Temporal flux perception',
                'cognitive_feature': 'Non-linear time processing',
                'communication_medium': 'Temporal wave modulation'
            },
            {
                'species': 'Biophotonic Symbiotes',
                'sensory_system': 'Full-spectrum light sensing',
                'cognitive_feature': 'Distributed neural network',
                'communication_medium': 'Bioluminescent patterns'
            },
            {
                'species': 'Gravitational Weavers',
                'sensory_system': 'Gravity field manipulation',
                'cognitive_feature': 'Spatial-temporal reasoning',
                'communication_medium': 'Gravitational wave pulses'
            }
        ]
        return {str(i+1): species for i, species in enumerate(random.sample(alien_species, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model for the hypothetical alien species '{t['species']}' with the following characteristics:

- Sensory System: {t['sensory_system']}
- Key Cognitive Feature: {t['cognitive_feature']}
- Communication Medium: {t['communication_medium']}

Your task has five parts:

1. Conceptual Framework (250-300 words):
   a) Describe the fundamental principles of the alien language based on their unique characteristics.
   b) Explain how their sensory system and cognitive feature influence the structure and complexity of the language.
   c) Discuss how the communication medium shapes the 'phonology' or basic units of the language.

2. Language Model Architecture (200-250 words):
   a) Propose a novel neural architecture for modeling this alien language.
   b) Explain how your architecture accommodates the unique aspects of the alien communication system.
   c) Describe how your model would handle input and output given the alien's sensory system and communication medium.

3. Training and Data Generation (200-250 words):
   a) Describe how you would generate a synthetic dataset to train your language model.
   b) Explain any unique challenges in creating training data for this alien language.
   c) Propose a method for evaluating the model's performance in understanding and generating alien communications.

4. Comparative Analysis (150-200 words):
   a) Compare your alien language model to traditional human language models.
   b) Discuss potential insights about language and cognition that could be gained from this comparison.
   c) Explain how this model might enhance our understanding of universal principles of communication.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of this alien language model in scientific research or technological development.
   b) Discuss any ethical considerations in developing and using such a model.
   c) Speculate on how this work might contribute to the search for extraterrestrial intelligence (SETI) or preparation for potential future alien contact.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and machine learning. Be creative in your approach while maintaining scientific plausibility and internal coherence. Use clear headings for each section of your response.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creativity and originality in designing the alien language model.",
            "The conceptual framework and model architecture are well-explained and logically consistent with the given alien characteristics.",
            "The training and evaluation methods proposed are innovative and appropriate for the unique challenges of the alien language.",
            "The comparative analysis provides insightful reflections on the nature of language and cognition.",
            "The potential applications and ethical considerations are thoughtfully discussed and scientifically plausible.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        # The eval_with_llm_judge function takes the instructions, submission, and criteria as inputs
        # and returns a boolean indicating whether the submission meets the criteria.
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
