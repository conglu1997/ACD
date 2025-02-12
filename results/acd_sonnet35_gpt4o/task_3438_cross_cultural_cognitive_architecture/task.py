import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Evidentiality markers",
                "description": "Grammatical elements that indicate the source of information in a statement",
                "example_languages": ["Turkish", "Quechua", "Tibetan"]
            },
            {
                "feature": "Honorifics",
                "description": "Linguistic forms that convey levels of politeness or social status",
                "example_languages": ["Japanese", "Korean", "Javanese"]
            },
            {
                "feature": "Grammatical gender",
                "description": "Categorization of nouns and associated agreement in the grammar",
                "example_languages": ["Spanish", "German", "Arabic"]
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture capable of modeling and analyzing linguistic phenomena across different cultures, then use it to investigate the cross-cultural linguistic feature of {t['feature']}. Your response should include the following sections:

1. Cognitive Architecture Design (300-350 words):
   a) Describe the key components of your cognitive architecture, explaining how they model various aspects of language processing and cultural cognition.
   b) Detail how your architecture incorporates theories from cognitive science, linguistics, and cultural psychology.
   c) Explain how your model accounts for the interaction between language, thought, and culture.
   d) Provide a high-level diagram or pseudocode representing a crucial part of your architecture.

2. Cross-Cultural Analysis Framework (250-300 words):
   a) Explain how your cognitive architecture would analyze {t['feature']} across different cultures.
   b) Describe the data inputs required for your model and how they would be processed.
   c) Detail the output format of your analysis and what insights it would provide.

3. Case Study: {t['feature']} (250-300 words):
   a) Apply your cognitive architecture to analyze {t['feature']} in at least two of the example languages provided: {', '.join(t['example_languages'])}.
   b) Compare and contrast how this feature manifests in these languages and cultures.
   c) Discuss any challenges your model faces in accurately representing this linguistic phenomenon.

4. Cognitive Implications (200-250 words):
   a) Based on your model's analysis, discuss the potential cognitive implications of {t['feature']} for speakers of languages that have this feature versus those that don't.
   b) Explore how this feature might influence thought patterns, memory, or other cognitive processes.
   c) Propose a hypothesis about the relationship between this linguistic feature and cultural cognition.

5. Model Validation and Improvement (150-200 words):
   a) Suggest methods to validate your cognitive architecture's predictions about {t['feature']}.
   b) Propose an experiment that could test your model's accuracy in representing this linguistic phenomenon.
   c) Discuss potential improvements or extensions to your architecture based on this case study.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss ethical implications of modeling cultural cognition and linguistic features.
   b) Address potential biases in your model and how they might be mitigated.
   c) Explore the broader implications of this research for cross-cultural understanding and communication.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and cultural psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, linguistics, and cultural psychology.",
            "The cognitive architecture design is well-explained, innovative, and plausibly integrates multiple disciplines.",
            "The cross-cultural analysis framework is clearly described and appropriate for the given linguistic feature.",
            "The case study effectively applies the cognitive architecture to analyze the specified linguistic feature across different languages.",
            "The discussion of cognitive implications is insightful and well-reasoned.",
            "The proposed validation methods and improvements are scientifically sound and relevant.",
            "Ethical considerations are thoughtfully addressed.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
