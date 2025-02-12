import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        developmental_stages = [
            "babbling",
            "one-word utterances",
            "two-word phrases",
            "telegraphic speech",
            "complex sentences"
        ]
        linguistic_features = [
            "phonological rules",
            "morphological patterns",
            "syntactic structures",
            "semantic relationships",
            "pragmatic conventions"
        ]
        cognitive_constraints = [
            "limited working memory",
            "attentional biases",
            "overgeneralization tendencies",
            "social learning preferences",
            "critical period effects"
        ]
        
        tasks = {
            "1": {
                "stage": random.choice(developmental_stages),
                "feature": random.choice(linguistic_features),
                "constraint": random.choice(cognitive_constraints)
            },
            "2": {
                "stage": random.choice(developmental_stages),
                "feature": random.choice(linguistic_features),
                "constraint": random.choice(cognitive_constraints)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a simulated language acquisition process for an AI agent, mimicking key stages of human language development, then analyze the resulting 'child language'. Your task involves the following steps:

1. Acquisition Model Design (250-300 words):
   a) Describe a model for simulating language acquisition in an AI agent, focusing on the {t['stage']} stage.
   b) Explain how your model incorporates the {t['feature']} as a key linguistic feature to be acquired.
   c) Detail how your model accounts for the cognitive constraint of {t['constraint']}.
   d) Outline the key parameters and variables you would use in your simulation.

2. Implementation Process (200-250 words):
   a) Describe the step-by-step process of implementing your language acquisition model.
   b) Explain how you would represent and process input data (e.g., simulated caregiver speech).
   c) Detail how your model would generate and evaluate language outputs at different stages.

3. Simulated Outputs (200-250 words):
   a) Provide examples of the 'child language' your model would produce at three different points in the acquisition process.
   b) Explain any patterns, errors, or unique features in these outputs.
   c) Compare these outputs to typical patterns observed in human language acquisition.

4. Analysis (200-250 words):
   a) Analyze the strengths and limitations of your simulated acquisition model.
   b) Discuss how well this simulation might represent real-world language acquisition processes.
   c) Explain how this model could be improved or expanded to better capture language development.

5. Implications and Applications (150-200 words):
   a) Discuss the potential insights this simulation could provide into human language acquisition.
   b) Propose two potential applications of your model in language education or AI development.
   c) Consider any ethical implications of using such simulations to inform educational or AI policies.

Ensure your response demonstrates a deep understanding of language acquisition theories, developmental psychology, and AI learning processes. Be creative in your approach while maintaining scientific plausibility and accuracy. Strive to balance innovative ideas with established theories in the field. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of a language acquisition model focusing on the {t['stage']} stage",
            f"The model incorporates {t['feature']} as a key linguistic feature to be acquired",
            f"The model accounts for the cognitive constraint of {t['constraint']}",
            "A step-by-step implementation process for the language acquisition model is provided",
            "Examples of 'child language' outputs at three different acquisition points are included",
            "The response includes an analysis of the model's strengths and limitations",
            "Two potential applications of the model are proposed",
            "The response demonstrates understanding of language acquisition theories and AI learning processes",
            "The ideas presented are creative while maintaining scientific plausibility",
            "The response is well-structured with clear headings and numbered paragraphs",
            "The total response falls within the specified word count range of 1000-1250 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
