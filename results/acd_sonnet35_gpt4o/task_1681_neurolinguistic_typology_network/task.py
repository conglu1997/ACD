import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Word order typology",
                "brain_region": "Broca's area",
                "language_family": "Indo-European"
            },
            {
                "feature": "Tonal system",
                "brain_region": "Superior temporal gyrus",
                "language_family": "Sino-Tibetan"
            },
            {
                "feature": "Ergative-absolutive alignment",
                "brain_region": "Angular gyrus",
                "language_family": "Eskimo-Aleut"
            },
            {
                "feature": "Evidentiality markers",
                "brain_region": "Prefrontal cortex",
                "language_family": "Quechuan"
            },
            {
                "feature": "Noun class system",
                "brain_region": "Inferior parietal lobule",
                "language_family": "Niger-Congo"
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture that can generate and analyze the linguistic feature of {t['feature']} across different language families, with a focus on the {t['language_family']} family and the brain region {t['brain_region']}. Your response should include:

1. Architecture Overview (250-300 words):
   a) Describe the key components of your neural network architecture.
   b) Explain how it incorporates principles from neurolinguistics and linguistic typology.
   c) Discuss how your architecture models the specified brain region and its role in processing the given linguistic feature.

2. Feature Generation and Analysis (200-250 words):
   a) Explain how your network generates examples of the specified linguistic feature.
   b) Describe the process by which it analyzes this feature across different languages.
   c) Provide an example of how your network would handle a specific language from the given language family.

3. Cross-linguistic Adaptation (200-250 words):
   a) Discuss how your architecture adapts to different language families.
   b) Explain any challenges in modeling the specified feature across diverse language types.
   c) Propose a method for extending your model to a previously unseen language family.

4. Neurolinguistic Plausibility (150-200 words):
   a) Analyze how your architecture aligns with current neurolinguistic theories.
   b) Identify potential divergences from human language processing and justify your design choices.
   c) Suggest an experiment to test the biological plausibility of your model.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your model for our understanding of language universals and diversity.
   b) Propose two novel applications of your architecture in fields such as machine translation, language pedagogy, or cognitive neuroscience.
   c) Speculate on how this technology might influence future research in linguistics and AI.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neurolinguistics, linguistic typology, and neural network architectures.",
            "The proposed architecture effectively incorporates the specified brain region and linguistic feature.",
            "The model's approach to generating and analyzing the linguistic feature across different language families is well-explained and plausible.",
            "The cross-linguistic adaptation strategy is thoughtful and addresses potential challenges.",
            "The discussion of neurolinguistic plausibility is well-reasoned and supported by current theories.",
            "The implications and applications proposed are innovative and demonstrate an understanding of the broader impact of the technology.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
