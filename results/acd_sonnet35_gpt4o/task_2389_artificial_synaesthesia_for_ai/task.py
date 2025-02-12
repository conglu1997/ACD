import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        cognitive_domains = ['language processing', 'spatial reasoning', 'emotional intelligence', 'pattern recognition', 'decision making']
        return {
            "1": {
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"]),
                "cognitive_domain": random.choice(cognitive_domains)
            },
            "2": {
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"]),
                "cognitive_domain": random.choice(cognitive_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial synaesthesia system for AI that maps {t['primary_modality']} inputs to {t['secondary_modality']} experiences, focusing on enhancing the AI's capabilities in {t['cognitive_domain']}. Your response should include:

1. Synaesthesia System Design (250-300 words):
   a) Describe the overall architecture of your artificial synaesthesia system.
   b) Explain how it maps {t['primary_modality']} inputs to {t['secondary_modality']} experiences.
   c) Discuss how this mapping is implemented in the AI's neural network or processing system.
   d) Provide an example of how a specific {t['primary_modality']} input would be translated to a {t['secondary_modality']} experience.

2. Cognitive Enhancement Analysis (200-250 words):
   a) Explain how your synaesthesia system could enhance the AI's capabilities in {t['cognitive_domain']}.
   b) Provide a specific scenario demonstrating this enhancement.
   c) Discuss potential challenges or limitations of this approach.

3. Training and Implementation (200-250 words):
   a) Describe how you would train an AI system to develop this form of artificial synaesthesia.
   b) Discuss any necessary modifications to existing AI architectures.
   c) Address potential issues in integrating this system with other AI capabilities.

4. Comparative Analysis (150-200 words):
   a) Compare your artificial synaesthesia system to natural human synaesthesia.
   b) Discuss how it differs from current multi-modal AI processing techniques.
   c) Analyze potential advantages and disadvantages compared to non-synaesthetic AI systems.

5. Ethical Considerations and Future Implications (200-250 words):
   a) Identify and discuss at least two ethical issues raised by creating artificial synaesthesia in AI.
   b) Explore potential long-term implications for AI development and human-AI interaction.
   c) Propose guidelines for responsible development and use of synaesthetic AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, AI, and the specified sensory modalities and cognitive domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implementation aspects.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The synaesthesia system successfully maps {t['primary_modality']} inputs to {t['secondary_modality']} experiences.",
            f"The response clearly explains how the system enhances AI capabilities in {t['cognitive_domain']}.",
            "The design is innovative and demonstrates a deep understanding of cognitive science and AI.",
            "The response addresses ethical considerations and future implications of synaesthetic AI systems.",
            "The analysis includes a comparison to human synaesthesia and current AI techniques."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
