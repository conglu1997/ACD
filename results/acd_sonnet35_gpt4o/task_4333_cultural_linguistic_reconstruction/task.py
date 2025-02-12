import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                'name': 'Ainu',
                'status': 'Critically endangered',
                'region': 'Japan',
                'features': 'Polysynthetic, subject-object-verb order'
            },
            {
                'name': 'Yagan',
                'status': 'Extinct',
                'region': 'Tierra del Fuego',
                'features': 'Agglutinative, rich system of suffixes'
            }
        ]
        artifacts = [
            {
                'name': 'Oral folklore',
                'type': 'Narrative',
                'description': 'Traditional stories passed down through generations'
            },
            {
                'name': 'Ritual chants',
                'type': 'Performance',
                'description': 'Sacred vocalizations used in ceremonies'
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'language': random.choice(languages),
                'artifact': random.choice(artifacts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to reconstruct and preserve the {t['language']['name']} language, which is {t['language']['status']} and originates from {t['language']['region']}. Then, apply your system to interpret a {t['artifact']['name']} artifact from this culture. Your response should include:

1. Language Reconstruction System (300-350 words):
   a) Describe the architecture of your AI system for reconstructing {t['language']['name']}.
   b) Explain how your system incorporates the known linguistic features: {t['language']['features']}.
   c) Detail the computational linguistics techniques and cultural inference methods your system employs.
   d) Discuss how your system handles uncertainties and makes educated guesses about unknown linguistic elements.

2. Cultural Context Integration (250-300 words):
   a) Explain how your AI system incorporates cultural and historical context in the language reconstruction process.
   b) Describe the types of cultural data your system uses and how it processes this information.
   c) Discuss how your system ensures cultural sensitivity and accuracy in its reconstructions.

3. Artifact Interpretation (250-300 words):
   a) Apply your AI system to interpret a {t['artifact']['type']} artifact: {t['artifact']['description']}.
   b) Provide a step-by-step explanation of how your system analyzes and interprets the artifact.
   c) Discuss any challenges in interpreting this type of artifact and how your system addresses them.

4. Linguistic and Cultural Insights (200-250 words):
   a) Based on your system's analysis, propose at least two novel insights about the {t['language']['name']} language or culture.
   b) Explain how these insights were derived and their potential significance for linguistic or anthropological research.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss the ethical implications of using AI to reconstruct and interpret endangered or extinct languages and cultural artifacts.
   b) Address potential biases in your AI system and how you mitigate them.
   c) Explain the limitations of your approach and areas where human expertise is still crucial.

6. Future Developments (150-200 words):
   a) Propose two potential enhancements to your AI system for future iterations.
   b) Suggest a novel application of your system beyond language reconstruction and artifact interpretation.

Ensure your response demonstrates a deep understanding of computational linguistics, cultural anthropology, and AI technologies. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section and use subheadings (a, b, c) where applicable. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['language']['name']} language and its cultural context.",
            "The AI system design is innovative and plausibly incorporates computational linguistics and cultural anthropology principles.",
            f"The artifact interpretation convincingly applies the AI system to analyze the {t['artifact']['name']}.",
            "The proposed linguistic and cultural insights are novel and well-reasoned.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
