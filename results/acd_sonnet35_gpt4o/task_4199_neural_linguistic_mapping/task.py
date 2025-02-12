import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Syntactic complexity",
                "brain_region": "Broca's area",
                "language_sample": "The cat that the dog chased climbed the tree."
            },
            {
                "feature": "Semantic processing",
                "brain_region": "Wernicke's area",
                "language_sample": "The colorless green ideas sleep furiously."
            },
            {
                "feature": "Phonological processing",
                "brain_region": "Superior temporal gyrus",
                "language_sample": "She sells seashells by the seashore."
            },
            {
                "feature": "Morphological processing",
                "brain_region": "Left fusiform gyrus",
                "language_sample": "The unlockable door was unlocked by an unlocking device."
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that maps linguistic features to simulated neural activity patterns, focusing on the linguistic feature of {t['feature']} associated with the {t['brain_region']}. Then, use your system to analyze and generate language samples. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for mapping linguistic features to neural activity patterns.
   b) Explain how your system models the neural processes in the {t['brain_region']}.
   c) Discuss any novel techniques or approaches used in your design.

2. Neural-Linguistic Mapping (200-250 words):
   a) Explain how your system maps {t['feature']} to specific neural activity patterns.
   b) Describe the data sources or models your system uses to establish this mapping.
   c) Discuss any challenges in this mapping process and how your system addresses them.

3. Analysis of Sample (200-250 words):
   a) Use your system to analyze the following language sample: "{t['language_sample']}"
   b) Describe the simulated neural activity patterns your system generates for this sample.
   c) Explain how these patterns reflect the linguistic feature and the associated brain region.

4. Language Generation (200-250 words):
   a) Use your system to generate a new language sample that would produce similar neural activity patterns.
   b) Explain the generation process and how it incorporates the mapped neural patterns.
   c) Compare and contrast your generated sample with the original in terms of linguistic features and potential neural activity.

5. Comparative Analysis (150-200 words):
   a) Compare your AI system's approach to language processing with current understanding of human language processing.
   b) Discuss potential insights your system might provide into human language cognition.
   c) Identify any limitations in your system's ability to model human neural language processing.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss the potential applications of your system in fields such as neurolinguistics, language therapy, or brain-computer interfaces.
   b) Address ethical considerations in developing AI systems that model brain activity.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['feature']} and its relation to {t['brain_region']}.",
            "The system architecture is well-designed and plausibly integrates neuroscience and AI concepts.",
            "The analysis of the provided language sample is thorough and consistent with the system's design.",
            "The generated language sample is coherent and plausibly related to the original in terms of neural activity patterns.",
            "The comparative analysis shows insight into both AI and human language processing.",
            "The discussion of ethical and practical implications is thoughtful and comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
