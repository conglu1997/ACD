import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_types = [
            "embodied",
            "orientational",
            "structural",
            "ontological"
        ]
        brain_regions = [
            "prefrontal cortex",
            "Broca's area",
            "Wernicke's area",
            "angular gyrus"
        ]
        cultures = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African"
        ]
        return {
            "1": {
                "metaphor_type": random.choice(metaphor_types),
                "brain_region": random.choice(brain_regions),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != "source_culture"])
            },
            "2": {
                "metaphor_type": random.choice(metaphor_types),
                "brain_region": random.choice(brain_regions),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != "source_culture"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates metaphorical expressions between languages based on neural activity patterns, then apply it to analyze and generate culturally-specific metaphors. Focus on {t['metaphor_type']} metaphors, the {t['brain_region']}, and translation between {t['source_culture']} and {t['target_culture']} cultures. Your response should include:

1. Neural-Linguistic Framework (300-350 words):
   a) Explain how neural activity in the {t['brain_region']} relates to metaphor processing.
   b) Describe how cultural differences might influence this neural activity for {t['metaphor_type']} metaphors.
   c) Propose a model that integrates neural data with linguistic analysis for metaphor translation.

2. System Architecture (250-300 words):
   a) Design the architecture of your neural metaphor translation system.
   b) Explain how your system processes neural data to identify and translate metaphors.
   c) Describe how your system accounts for cultural differences in metaphor use and interpretation.
   d) Provide a diagram or flowchart of your system's key components and processes.

3. Cross-Cultural Application (200-250 words):
   a) Apply your system to translate the following complex {t['metaphor_type']} metaphor from {t['source_culture']} to {t['target_culture']} culture:
      - For embodied metaphors: "The seeds of her rage blossomed into a garden of vengeance"
      - For orientational metaphors: "As his power grew, he ascended the corporate ladder while his ethics sank into an abyss"
      - For structural metaphors: "Their relationship was a delicate dance on the edge of a volcano"
      - For ontological metaphors: "The invisible hand of the market strangled the dreams of the working class"
   b) Explain how your system handles the cultural nuances and potential mistranslations.
   c) Discuss how this translation might differ from traditional language translation methods.

4. Metaphor Generation (200-250 words):
   a) Describe how your system could be used to generate novel, culturally-appropriate metaphors.
   b) Provide an example of a generated metaphor for each culture, explaining its cultural significance.
   c) Discuss the creative and cultural implications of AI-generated metaphors.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of using neural data for language processing and generation.
   b) Explore the philosophical implications of mechanizing metaphorical thinking.
   c) Address potential concerns about cultural appropriation or misrepresentation.

6. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the accuracy and cultural authenticity of your system's translations and generations, including at least one quantitative metric.
   b) Suggest two potential extensions or applications of your system in fields such as education, therapy, or intercultural communication.
   c) Discuss how advancements in neuroscience or AI might impact your system in the future.

Ensure your response demonstrates a deep understanding of neurolinguistics, cultural studies, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) within each section as outlined. Your total response should be between 1250-1550 words, with each section adhering to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Neural-Linguistic Framework demonstrates a comprehensive understanding of how the {t['brain_region']} processes {t['metaphor_type']} metaphors and provides a detailed analysis of how cultural differences influence this processing.",
            "The System Architecture provides a sophisticated and plausible design for a neural metaphor translation system, including a clear and detailed diagram or flowchart.",
            f"The Cross-Cultural Application section includes a specific and nuanced translation of the given complex {t['metaphor_type']} metaphor from {t['source_culture']} to {t['target_culture']} culture, with a thorough analysis of cultural nuances and potential mistranslations.",
            f"The Metaphor Generation section provides highly creative and culturally-appropriate metaphor examples for both {t['source_culture']} and {t['target_culture']} cultures, with in-depth explanations of their significance.",
            "The Ethical and Philosophical Implications section addresses a wide range of relevant concerns about using neural data and potential cultural misrepresentation, demonstrating a nuanced understanding of the issues.",
            "The Evaluation and Future Directions section proposes feasible and innovative methods for system evaluation, including at least one quantitative metric, and suggests relevant and creative applications in other fields.",
            "The response adheres strictly to the specified format and word count requirements, demonstrating excellent organization and concision."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
