import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_areas = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Supramarginal gyrus"
        ]
        linguistic_features = [
            "Syntax",
            "Semantics",
            "Phonology",
            "Pragmatics"
        ]
        ai_techniques = [
            "Transformer architecture",
            "Recurrent Neural Networks",
            "Attention mechanisms",
            "Neuro-symbolic AI"
        ]
        cognitive_constraints = [
            "Working memory limitations",
            "Cognitive load theory",
            "Dual-process theory",
            "Predictive coding"
        ]
        return {
            "1": {
                "brain_area": random.choice(language_areas),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques),
                "cognitive_constraint": random.choice(cognitive_constraints)
            },
            "2": {
                "brain_area": random.choice(language_areas),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques),
                "cognitive_constraint": random.choice(cognitive_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for a universal language model based on neural patterns, integrating neuroscience, linguistics, and artificial intelligence. Your model should focus on the brain area {t['brain_area']}, the linguistic feature of {t['linguistic_feature']}, incorporate the AI technique of {t['ai_technique']}, and account for the cognitive constraint of {t['cognitive_constraint']}. Your response should include:

1. Conceptual Framework (300-350 words):
   a) Describe the key components of your neural universal language model.
   b) Explain how it integrates insights from neuroscience, linguistics, and AI.
   c) Detail how your model incorporates the specified brain area, linguistic feature, AI technique, and cognitive constraint.
   d) Propose a novel mechanism for translating neural patterns into a universal language representation.

2. Neural-Linguistic Interface (250-300 words):
   a) Explain how your model maps neural activity in {t['brain_area']} to linguistic structures.
   b) Describe how the model accounts for the specified linguistic feature of {t['linguistic_feature']}.
   c) Discuss how your model might handle cross-linguistic variations and universals.
   d) Explain how the model incorporates the cognitive constraint of {t['cognitive_constraint']}.

3. AI Implementation (250-300 words):
   a) Detail how the {t['ai_technique']} is used in your model.
   b) Explain how this AI technique enhances the model's ability to process and generate language.
   c) Describe any novel algorithms or architectures you propose for your neural universal language model.
   d) Discuss how the AI implementation accounts for the specified cognitive constraint.

4. Potential Applications (200-250 words):
   a) Propose three potential applications of your neural universal language model.
   b) Explain how each application could advance fields such as machine translation, brain-computer interfaces, or language acquisition.
   c) Discuss the ethical implications and potential risks associated with these applications.

5. Theoretical Implications (200-250 words):
   a) Discuss how your model might inform our understanding of language processing in the brain.
   b) Explore potential insights into the nature of language and cognition that could be derived from your model.
   c) Propose a testable hypothesis about language universals based on your neural universal language model.
   d) Explain how your model's incorporation of {t['cognitive_constraint']} contributes to our understanding of language processing.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your model.
   b) Suggest ways to overcome these challenges or improve the model.
   c) Propose future research directions that could further develop the concept of a neural universal language model.

7. Comparative Analysis (200-250 words):
   a) Compare your proposed model to existing language models and theories in linguistics.
   b) Discuss how your model addresses limitations of current approaches.
   c) Analyze potential advantages and disadvantages of your model compared to traditional NLP techniques.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all seven required sections comprehensively.",
            f"The model effectively incorporates {t['brain_area']}, {t['linguistic_feature']}, {t['ai_technique']}, and {t['cognitive_constraint']}.",
            "The proposed framework is innovative and demonstrates interdisciplinary integration.",
            "The response shows a deep understanding of neuroscience, linguistics, and AI.",
            "The theoretical implications and potential applications are well-reasoned and insightful.",
            "The response is scientifically plausible while being creative and speculative.",
            "The comparative analysis demonstrates a critical evaluation of the proposed model against existing approaches."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
