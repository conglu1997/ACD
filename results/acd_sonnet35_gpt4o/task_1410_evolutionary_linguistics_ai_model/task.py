import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_family": "Indo-European",
                "time_span": "3000 years",
                "environmental_factor": "technological advancement",
                "cultural_shift": "globalization"
            },
            {
                "language_family": "Sino-Tibetan",
                "time_span": "2000 years",
                "environmental_factor": "climate change",
                "cultural_shift": "rapid urbanization"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models language evolution within the {t['language_family']} language family over a {t['time_span']} period, considering the environmental factor of {t['environmental_factor']} and the cultural shift of {t['cultural_shift']}. Then, apply the principles derived from this model to develop more robust and adaptable AI language models. Your response should include the following sections:

1. Evolutionary Linguistics Model (300-350 words):
   a) Describe the key components of your AI system for modeling language evolution.
   b) Explain how your model incorporates historical linguistics principles and computational methods.
   c) Detail how your system accounts for the given environmental factor and cultural shift in the language evolution process.
   d) Discuss any novel approaches or algorithms you've incorporated to handle the complexity of language change.

2. Simulated Language Changes (250-300 words):
   a) Provide specific examples of potential language changes your model predicts over the given time span.
   b) Explain the linguistic reasoning behind these changes, considering phonological, morphological, syntactic, and semantic aspects.
   c) Discuss how these changes reflect the influence of the environmental factor and cultural shift.

3. Application to AI Language Models (300-350 words):
   a) Describe how insights from your evolutionary linguistics model can be applied to improve AI language models.
   b) Explain specific techniques or modifications you would implement in AI language model architecture based on your findings.
   c) Discuss how these improvements could enhance the robustness and adaptability of AI language models.

4. Comparative Analysis (200-250 words):
   a) Compare your evolutionary AI model's predictions with known historical changes in the given language family.
   b) Analyze any discrepancies and discuss possible reasons for these differences.
   c) Propose how this comparative analysis could further refine your model and its applications.

5. Ethical and Practical Implications (200-250 words):
   a) Discuss potential ethical considerations in using AI to model language evolution and apply it to language model development.
   b) Explore practical applications of your system in fields such as historical linguistics, language preservation, or machine translation.
   c) Propose a method to validate the accuracy and cultural sensitivity of your system's predictions and applications.

6. Future Directions (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how emerging technologies in AI or linguistics could enhance your system's capabilities.
   c) Propose a related linguistic challenge that could be addressed using a similar approach.

Ensure your response demonstrates a deep understanding of linguistics, language evolution, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and linguistic accuracy.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics and computational methods for modeling language evolution.",
            f"The model effectively incorporates the environmental factor of {t['environmental_factor']} and the cultural shift of {t['cultural_shift']} in its predictions.",
            "The simulated language changes are linguistically plausible and well-explained across multiple aspects of language (phonology, morphology, syntax, semantics).",
            "The application of evolutionary insights to AI language models is innovative and well-reasoned.",
            "The comparative analysis shows critical thinking in evaluating the model's predictions against known historical changes.",
            "Ethical considerations and practical applications are thoughtfully discussed.",
            "The proposed future directions are creative and relevant to advancing the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
