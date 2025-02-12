import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            "grammatical gender",
            "evidentiality markers",
            "honorifics",
            "future tense",
            "color terms"
        ]
        cognitive_domains = [
            "spatial reasoning",
            "time perception",
            "social cognition",
            "causal reasoning",
            "memory encoding"
        ]
        return {
            "1": {"feature": random.choice(language_features), "domain": random.choice(cognitive_domains)},
            "2": {"feature": random.choice(language_features), "domain": random.choice(cognitive_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the potential effects of linguistic relativity on AI language models, focusing on the language feature of {t['feature']} and its impact on {t['domain']}. Then, propose modifications to make AI models more culturally adaptive. Your response should include:

1. Linguistic Feature Analysis (200-300 words):
   a) Explain the concept of {t['feature']} and how it varies across languages.
   b) Discuss how this feature might influence {t['domain']} according to the linguistic relativity hypothesis.
   c) Provide an example of how speakers of languages with and without this feature might differ in their cognitive processes.

2. AI Model Implications (200-300 words):
   a) Analyze how current AI language models might be biased due to their training data and architecture with respect to {t['feature']}.
   b) Explain potential limitations this bias could cause in {t['domain']} tasks.
   c) Discuss how this bias might affect AI performance when interacting with speakers of languages that differ in this feature.

3. Cultural Adaptation Proposal (250-350 words):
   a) Propose a novel modification to AI language model architecture or training process to address the identified bias.
   b) Explain how your proposal would make the AI model more adaptive to different linguistic features and cognitive styles.
   c) Describe a specific technique or method to implement your proposal.

4. Evaluation and Ethical Considerations (150-250 words):
   a) Suggest methods to evaluate the effectiveness of your proposed modification.
   b) Discuss potential ethical implications of implementing your proposal.
   c) Address any challenges or limitations of your approach.

Ensure your response demonstrates a deep understanding of linguistic relativity, AI language models, and cross-cultural cognitive differences. Be creative in your analysis and proposals while maintaining scientific plausibility.

Format your response using the following structure:

1. Linguistic Feature Analysis
[Your analysis here]

2. AI Model Implications
[Your analysis here]

3. Cultural Adaptation Proposal
[Your proposal here]

4. Evaluation and Ethical Considerations
[Your discussion here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['feature']} and its potential impact on {t['domain']}.",
            "The analysis of AI model implications is thorough and considers both current limitations and future challenges.",
            "The proposed modification for cultural adaptation is innovative, well-explained, and potentially implementable.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response follows the specified format structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
