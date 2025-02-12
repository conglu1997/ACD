import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise', 'trust', 'anticipation']
        sensory_modalities = ['visual', 'auditory', 'olfactory', 'gustatory', 'tactile']
        creative_forms = ['poetry', 'music', 'painting', 'sculpture', 'dance', 'perfume', 'culinary dish']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'emotion': random.choice(emotions),
                'primary_modality': random.choice(sensory_modalities),
                'secondary_modality': random.choice(sensory_modalities),
                'creative_form': random.choice(creative_forms)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates emotional synesthesia, focusing on the emotion of {t['emotion']}. Then, use this system to analyze and generate an emotionally-charged {t['creative_form']} that translates the {t['primary_modality']} experience of {t['emotion']} into a {t['secondary_modality']} representation. Your response should include:

1. Emotional Synesthesia Model (250-300 words):
   a) Describe the key components of your AI system for simulating emotional synesthesia.
   b) Explain how it models the relationship between {t['emotion']} and sensory experiences.
   c) Detail how the system translates between {t['primary_modality']} and {t['secondary_modality']} modalities.

2. Cognitive Science Foundation (200-250 words):
   a) Discuss the cognitive science principles underlying your model.
   b) Explain how your model incorporates theories of emotion and cross-modal sensory processing.
   c) Describe any novel approaches in your model that extend current understanding of emotional synesthesia.

3. Creative Work Generation (200-250 words):
   a) Use your AI system to generate a {t['creative_form']} that expresses {t['emotion']} by translating a {t['primary_modality']} experience into a {t['secondary_modality']} representation.
   b) Provide a detailed description or representation of the generated work.
   c) Explain how specific elements of the work reflect the emotional synesthesia process.

4. Analysis and Interpretation (200-250 words):
   a) Analyze the generated {t['creative_form']} in terms of its emotional impact and sensory associations.
   b) Discuss how effectively it translates the {t['primary_modality']} experience of {t['emotion']} into the {t['secondary_modality']} modality.
   c) Interpret the work in the context of emotional synesthesia and creative expression.

5. Artistic and Therapeutic Applications (150-200 words):
   a) Propose potential applications of your emotional synesthesia AI in artistic creation.
   b) Discuss how this technology could be used in therapeutic contexts for emotional processing or communication.
   c) Address any ethical considerations in using AI for emotional-creative tasks.

Ensure your response demonstrates a deep understanding of cognitive science, emotional processing, and creative expression. Use appropriate terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed description of an AI system that simulates emotional synesthesia for the emotion {t['emotion']}.",
            f"The system must demonstrate the ability to translate between {t['primary_modality']} and {t['secondary_modality']} sensory modalities.",
            f"The generated {t['creative_form']} should effectively express {t['emotion']} through a {t['secondary_modality']} representation.",
            "The response should show a deep understanding of cognitive science principles related to emotion and cross-modal sensory processing.",
            "The analysis should provide insightful interpretation of the generated creative work in the context of emotional synesthesia.",
            "The response must discuss potential artistic and therapeutic applications of the emotional synesthesia AI.",
            "The overall response should demonstrate creativity, scientific plausibility, and interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
