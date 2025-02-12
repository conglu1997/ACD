import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sorrow', 'anger', 'fear', 'love', 'disgust', 'surprise']
        poetic_forms = ['sonnet', 'haiku', 'free verse', 'villanelle', 'limerick']
        literary_devices = ['metaphor', 'alliteration', 'personification', 'imagery', 'symbolism']
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "poetic_form": random.choice(poetic_forms),
                "literary_device": random.choice(literary_devices)
            },
            "2": {
                "emotion": random.choice(emotions),
                "poetic_form": random.choice(poetic_forms),
                "literary_device": random.choice(literary_devices)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing poetry that evokes the emotion of {t['emotion']}, focusing on the poetic form of {t['poetic_form']} and emphasizing the use of {t['literary_device']}. Your system should incorporate principles from affective computing and literary theory. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates natural language processing, emotion modeling, and poetic generation.
   c) Discuss any novel features that make your system particularly suited for emotive poetry generation and analysis.

2. Emotion Modeling (200-250 words):
   a) Explain how your system models and represents the emotion of {t['emotion']}.
   b) Describe the psychological or neuroscientific theories of emotion that inform your model.
   c) Discuss how your system translates emotional representations into poetic elements.

3. Poetic Generation (250-300 words):
   a) Detail the process by which your system generates {t['poetic_form']} poetry.
   b) Explain how your system incorporates {t['literary_device']} to enhance emotional evocation.
   c) Provide an example of a short poem (50-100 words) your system might generate, along with an explanation of its emotional elements.

4. Poetry Analysis (200-250 words):
   a) Describe how your system analyzes poetry for emotional content.
   b) Explain the metrics or methods used to evaluate the emotional impact of generated poems.
   c) Discuss how your system might provide feedback or suggestions for improving emotional resonance.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI-generated emotive poetry.
   b) Discuss how your system addresses concerns about authenticity and the nature of machine-generated art.
   c) Propose guidelines for the responsible development and use of emotive poetry AI.

6. Evaluation and Future Work (150-200 words):
   a) Propose methods for evaluating the effectiveness of your system in generating emotionally resonant poetry.
   b) Suggest areas for future research or improvement in AI-driven creative writing.
   c) Discuss potential applications of your system beyond poetry generation.

Ensure your response demonstrates a deep understanding of natural language processing, emotion theory, poetics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Include at least 5 relevant citations or references to support your system design and theoretical foundations.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of emotion modeling, particularly for the emotion of {t['emotion']}.",
            f"The proposed AI system effectively integrates natural language processing, emotion modeling, and {t['poetic_form']} generation.",
            f"The system's use of {t['literary_device']} in poetry generation is well-explained and appropriate for emotional evocation.",
            "The poetry analysis component is well-designed and considers both technical and artistic aspects.",
            "Ethical considerations are thoroughly addressed, including concerns about AI-generated art.",
            "The evaluation methods and future work suggestions are insightful and relevant to the field of AI-driven creative writing.",
            "The response includes a concrete example of a generated poem (50-100 words) that demonstrates the system's capabilities.",
            "At least 5 relevant citations or references are provided to support the system design and theoretical foundations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
