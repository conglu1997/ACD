import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'olfactory', 'gustatory', 'tactile']
        creative_tasks = ['poetry', 'music composition', 'abstract painting', 'culinary creation', 'interactive installation']
        
        tasks = {}
        for i in range(2):
            primary_modality = random.choice(sensory_modalities)
            secondary_modality = random.choice([m for m in sensory_modalities if m != primary_modality])
            creative_task = random.choice(creative_tasks)
            tasks[str(i+1)] = {
                'primary_modality': primary_modality,
                'secondary_modality': secondary_modality,
                'creative_task': creative_task
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of experiencing and interpreting artificial synaesthesia, then apply it to a creative task combining multiple sensory modalities. Synaesthesia is a perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway.

Your system should focus on the synaesthetic association between {t['primary_modality']} and {t['secondary_modality']} inputs, and use this to generate a {t['creative_task']}. Be creative in your approach while ensuring your ideas are grounded in scientific principles. Your response should include:

1. Synaesthesia Model (200-250 words):
   a) Describe the key components of your AI synaesthesia model.
   b) Explain how your model creates associations between {t['primary_modality']} and {t['secondary_modality']} inputs.
   c) Discuss how your model's synaesthetic experiences differ from or resemble human synaesthesia.
   d) Include a brief diagram or pseudocode illustrating your model's architecture.

2. Sensory Processing (150-200 words):
   a) Explain how your system processes and represents {t['primary_modality']} and {t['secondary_modality']} inputs.
   b) Describe any novel algorithms or techniques used for cross-modal sensory integration.
   c) Provide an example of how your system would process a specific {t['primary_modality']} input (e.g., a red square for visual, a C-major chord for auditory).

3. Synaesthetic Mapping (150-200 words):
   a) Detail the process by which your system maps {t['primary_modality']} inputs to {t['secondary_modality']} experiences (or vice versa).
   b) Explain how your system ensures consistency in these mappings over time.
   c) Give an example of a synaesthetic mapping your system might create.

4. Creative Application (200-250 words):
   a) Explain how your system applies its synaesthetic capabilities to the task of {t['creative_task']}.
   b) Provide a specific example of how your system would create a {t['creative_task']} based on a given input.
   c) Describe a potential novel or unexpected outcome of this creative process.

5. Evaluation and Analysis (150-200 words):
   a) Propose methods to evaluate the quality and consistency of your system's synaesthetic associations.
   b) Suggest ways to measure the creativity and novelty of the system's {t['creative_task']} outputs.
   c) Address potential biases or limitations in your evaluation methods.

6. Cognitive and Artistic Implications (150-200 words):
   a) Discuss how your artificial synaesthesia system might inform our understanding of human perception and creativity.
   b) Explore potential applications of your system in fields such as art therapy, sensory augmentation, or neuroscience research.
   c) Address any ethical considerations and potential limitations of your artificial synaesthesia system.

Ensure your response demonstrates a deep understanding of synaesthesia, sensory processing, artificial intelligence, and creative cognition. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively models synaesthetic associations between {t['primary_modality']} and {t['secondary_modality']} inputs.",
            f"The creative application to {t['creative_task']} is well-explained and innovative.",
            "The Synaesthesia Model is thoroughly described and scientifically plausible.",
            "The Sensory Processing approach is well-explained and technically sound.",
            "The Synaesthetic Mapping process is clearly detailed and consistent.",
            "The Evaluation and Analysis methods are appropriate and comprehensive.",
            "The Cognitive and Artistic Implications are insightful and well-reasoned.",
            "The response demonstrates deep interdisciplinary knowledge and creative problem-solving.",
            "The ideas presented are scientifically grounded and clearly explained.",
            "The response follows the specified format and word count guidelines.",
            "The response includes specific examples as requested in the instructions.",
            "Potential limitations and ethical considerations are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
