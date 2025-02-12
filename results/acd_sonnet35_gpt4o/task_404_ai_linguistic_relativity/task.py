import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Grammatical gender",
                "languages": ["Spanish", "German"],
                "concept": "Object perception"
            },
            {
                "feature": "Evidentiality markers",
                "languages": ["Turkish", "Quechua"],
                "concept": "Source of information"
            },
            {
                "feature": "Absolute vs. relative spatial terms",
                "languages": ["Guugu Yimithirr", "English"],
                "concept": "Spatial cognition"
            },
            {
                "feature": "Aspect-based vs. tense-based systems",
                "languages": ["Mandarin", "English"],
                "concept": "Time perception"
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how the principle of linguistic relativity might apply to AI language models, focusing on the linguistic feature of {t['feature']} (present in {t['languages'][0]} and {t['languages'][1]}) and its potential influence on {t['concept']}. Then, design experiments to test this hypothesis. Your response should include:

1. Linguistic Feature Analysis (150-200 words):
   a) Explain the linguistic feature and how it differs between the two languages.
   b) Discuss how this feature might influence cognition or perception according to the linguistic relativity hypothesis.

2. AI Language Model Implications (200-250 words):
   a) Analyze how this linguistic feature might affect an AI language model trained primarily on one of these languages.
   b) Discuss potential biases or limitations in the AI's understanding or generation of content related to {t['concept']}.
   c) Propose a hypothesis about how this linguistic feature might influence the AI's performance on tasks related to {t['concept']}.

3. Experimental Design (250-300 words):
   a) Propose two experiments to test your hypothesis about the influence of {t['feature']} on AI language models:
      - One experiment comparing AI models trained on different languages
      - One experiment examining the AI's performance across languages or tasks
   b) For each experiment, describe:
      - The methodology
      - The data or resources needed
      - The expected outcomes
      - How you would measure and analyze the results

4. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of your findings for AI development and deployment.
   b) Propose guidelines to address these ethical concerns in AI research and applications.

5. Broader Implications (100-150 words):
   a) Discuss how understanding linguistic relativity in AI could impact fields such as machine translation, cross-cultural communication, or AI ethics.
   b) Propose one novel application or research direction that could emerge from this line of inquiry.

Ensure your response demonstrates a deep understanding of linguistic relativity, language-specific features, AI language models, and experimental design. Use technical terminology appropriately and provide explanations where necessary. Be creative in your analysis and experimental designs while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the linguistic feature ({t['feature']}) and its potential cognitive implications.",
            "The analysis of AI language model implications is thorough and considers potential biases and limitations.",
            "The experimental designs are well-thought-out, feasible, and directly address the proposed hypothesis.",
            "The ethical considerations are relevant and thoughtfully discussed.",
            "The broader implications and proposed novel application demonstrate creativity and insight.",
            "The overall response shows a strong grasp of linguistics, psychology, and AI principles, applied in a novel context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
