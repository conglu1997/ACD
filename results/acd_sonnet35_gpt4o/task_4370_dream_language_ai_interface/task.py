import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dream_features = [
            {
                'feature': 'Non-linear narrative',
                'brain_region': 'Prefrontal cortex',
                'linguistic_aspect': 'Temporal coherence'
            },
            {
                'feature': 'Emotional intensity',
                'brain_region': 'Amygdala',
                'linguistic_aspect': 'Affective language'
            },
            {
                'feature': 'Bizarre imagery',
                'brain_region': 'Visual cortex',
                'linguistic_aspect': 'Metaphorical language'
            },
            {
                'feature': 'Memory integration',
                'brain_region': 'Hippocampus',
                'linguistic_aspect': 'Autobiographical references'
            }
        ]
        return {str(i+1): random.choice(dream_features) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret and generate dream narratives based on neurolinguistic principles, focusing on the dream feature of {t['feature']}, associated with the {t['brain_region']} and the linguistic aspect of {t['linguistic_aspect']}. Then, explore its potential applications and ethical implications. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for dream interpretation and generation.
   b) Explain how it incorporates neuroscientific understanding of {t['brain_region']} function.
   c) Detail how your system models the linguistic aspect of {t['linguistic_aspect']}.
   d) Propose a novel feature that enhances the system's ability to capture {t['feature']} in dreams.
   e) Include a simple diagram or flowchart of your system's architecture (describe it textually).

2. Dream Interpretation Mechanism (250-300 words):
   a) Explain how your system would interpret dream narratives, focusing on {t['feature']}.
   b) Describe the AI techniques or algorithms used for this interpretation.
   c) Discuss how your system differentiates between literal and symbolic content in dreams.
   d) Address potential challenges in accurately interpreting subjective dream experiences.

3. Dream Generation Process (250-300 words):
   a) Detail how your AI would generate dream-like narratives incorporating {t['feature']}.
   b) Explain how the system ensures the generated dreams reflect realistic cognitive processes.
   c) Describe how {t['linguistic_aspect']} is incorporated into the generated narratives.
   d) Propose a method for validating the authenticity of AI-generated dreams.

4. Potential Applications (200-250 words):
   a) Suggest three innovative applications for your dream interpretation and generation AI.
   b) Explain how each application leverages the system's understanding of {t['feature']}.
   c) Discuss the potential impact of these applications on fields such as psychology, neuroscience, or art.

5. Ethical Implications (250-300 words):
   a) Identify and analyze at least three ethical concerns raised by your system.
   b) Discuss the implications of AI interpreting or generating highly personal and subjective experiences.
   c) Explore the potential psychological impacts of using AI-generated dreams.
   d) Propose guidelines or safeguards to address these ethical issues.

6. Future Directions (150-200 words):
   a) Suggest potential advancements or iterations for your system.
   b) Discuss how this technology might evolve alongside other emerging neurotechnologies.
   c) Propose a research agenda to further develop the field of AI-assisted dream analysis and generation.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical considerations.

Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['feature']} in dreams and provides a detailed explanation of how it is incorporated into the AI system.",
            f"The system design effectively integrates knowledge from neuroscience (particularly regarding the {t['brain_region']}) and linguistics (focusing on {t['linguistic_aspect']}).",
            "The dream interpretation and generation processes are well-explained and scientifically plausible.",
            "The proposed applications are innovative and leverage the unique aspects of the system.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The response adheres to the specified format and word count, and demonstrates appropriate use of technical terminology from neuroscience, linguistics, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
