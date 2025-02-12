import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        thought_categories = [
            "abstract concepts",
            "spatial reasoning",
            "emotional experiences",
            "decision-making processes"
        ]
        language_families = [
            "Indo-European",
            "Sino-Tibetan",
            "Afroasiatic",
            "Austronesian"
        ]
        brain_regions = [
            "prefrontal cortex",
            "Broca's area",
            "Wernicke's area",
            "hippocampus"
        ]
        return {
            "1": {
                "thought_category": random.choice(thought_categories),
                "language_family": random.choice(language_families),
                "brain_region": random.choice(brain_regions)
            },
            "2": {
                "thought_category": random.choice(thought_categories),
                "language_family": random.choice(language_families),
                "brain_region": random.choice(brain_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate human thoughts directly into multiple languages simultaneously, focusing on the thought category of {t['thought_category']}, the {t['language_family']} language family, and the {t['brain_region']} of the brain. Then, analyze its potential implications for neurolinguistics and AI development. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for thought-to-language translation.
   b) Explain how your system interfaces with and interprets neural activity from the {t['brain_region']}.
   c) Detail how the system translates thoughts into multiple languages within the {t['language_family']} family.
   d) Discuss any novel AI techniques or algorithms used in your system's design.
   e) Include a high-level diagram or flowchart of your system architecture (describe it textually).

2. Thought-to-Language Mapping (250-300 words):
   a) Explain the theoretical basis for mapping neural activity related to {t['thought_category']} to linguistic outputs.
   b) Describe any novel algorithms or techniques you've developed for this mapping process.
   c) Discuss how your system handles the complexities and nuances of translating {t['thought_category']} across multiple languages.
   d) Address potential challenges in maintaining semantic and cultural accuracy in the translations.

3. Neurolinguistic Implications (200-250 words):
   a) Analyze how your system's approach to thought translation might inform our understanding of language processing in the {t['brain_region']}.
   b) Discuss potential insights your system could provide about the relationship between {t['thought_category']} and language formation.
   c) Propose a hypothesis about multilingual cognition that could be tested using your system.

4. AI Development Implications (200-250 words):
   a) Explain how your system pushes the boundaries of current AI capabilities in language processing and translation.
   b) Discuss potential applications of your technology in AI research and development.
   c) Analyze how the principles used in your system might be applied to other areas of AI, such as multimodal learning or artificial general intelligence.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in directly translating thoughts into multiple languages.
   b) Discuss privacy concerns and propose safeguards for protecting individuals' inner thoughts.
   c) Analyze potential societal impacts of this technology, both positive and negative.

6. Future Research Directions (150-200 words):
   a) Propose two specific areas for future research to enhance your thought translation system.
   b) Explain how these research directions could address current limitations or expand the system's capabilities.
   c) Discuss potential collaborations between neuroscientists, linguists, and AI researchers to further develop this technology.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs an AI system for translating thoughts into multiple languages, focusing on {t['thought_category']}, the {t['language_family']} language family, and the {t['brain_region']}.",
            "The system architecture and thought-to-language mapping process are well-explained and scientifically plausible.",
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence, using appropriate technical terminology.",
            "The implications for neurolinguistics and AI development are thoroughly analyzed and include novel insights or hypotheses.",
            "Ethical considerations are thoughtfully addressed, including privacy concerns and potential societal impacts.",
            "The proposed future research directions are innovative and relevant to advancing the field.",
            "The response follows the specified format and word limit, with clear and well-structured sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
