import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_processes = [
            {
                "process": "Syntax acquisition",
                "brain_region": "Broca's area",
                "linguistic_phenomenon": "Subject-Verb-Object order"
            },
            {
                "process": "Semantic processing",
                "brain_region": "Wernicke's area",
                "linguistic_phenomenon": "Polysemy resolution"
            },
            {
                "process": "Phonological processing",
                "brain_region": "Superior temporal gyrus",
                "linguistic_phenomenon": "Phoneme discrimination"
            },
            {
                "process": "Pragmatic inference",
                "brain_region": "Right hemisphere",
                "linguistic_phenomenon": "Metaphor comprehension"
            }
        ]
        return {
            "1": random.choice(language_processes),
            "2": random.choice(language_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the brain's language processing regions, focusing on {t['process']} in the {t['brain_region']}. Then, use your model to simulate the acquisition and processing of {t['linguistic_phenomenon']} in both humans and AI systems. Your response should include:

1. Neural Architecture Design (250-300 words):
   a) Describe the key components of your neural network architecture.
   b) Explain how your design is inspired by the structure and function of the {t['brain_region']}.
   c) Detail how your architecture models the specific process of {t['process']}.
   d) Include a diagram or schematic representation of your neural network (describe it textually).

2. Language Acquisition Simulation (200-250 words):
   a) Explain how your model simulates the acquisition of {t['linguistic_phenomenon']} in human language learners.
   b) Describe the training process and data requirements for your model.
   c) Discuss how your model accounts for developmental stages in language acquisition.

3. AI Language Processing (200-250 words):
   a) Describe how your model can be applied to improve {t['process']} in AI language models.
   b) Compare and contrast your approach with current methods in natural language processing.
   c) Propose a specific application or task where your model could outperform traditional NLP approaches.

4. Comparative Analysis (150-200 words):
   a) Analyze the similarities and differences between human and AI performance in {t['process']} based on your model.
   b) Discuss any insights your model provides about the nature of human language processing.
   c) Identify limitations in current AI systems that your model helps to address.

5. Experimental Validation (150-200 words):
   a) Propose an experiment to test the predictions of your model in human subjects.
   b) Describe how you would validate your model's performance against human behavioral data.
   c) Discuss potential challenges in comparing AI and human performance in {t['process']}.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss ethical considerations in developing AI systems that closely mimic human language processing.
   b) Explore potential societal impacts of AI systems with more human-like language capabilities.
   c) Propose guidelines for responsible development and use of neurolinguistically-inspired AI.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words. Begin each section with the heading (e.g., '1. Neural Architecture Design:') followed by your response for that section.

IMPORTANT: Strive for scientific plausibility and innovation in your design. Your response should demonstrate a strong integration of knowledge across neuroscience, linguistics, and artificial intelligence fields."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The neural architecture design effectively models {t['process']} and is clearly inspired by the {t['brain_region']}.",
            f"The language acquisition simulation for {t['linguistic_phenomenon']} is well-explained and plausible.",
            f"The application to AI language processing demonstrates a clear improvement in {t['process']}.",
            "The comparative analysis provides insightful distinctions between human and AI language processing.",
            "The proposed experimental validation is well-designed and addresses potential challenges.",
            "The response demonstrates a deep understanding and integration of neuroscience, linguistics, and artificial intelligence concepts.",
            "The ethical and societal implications are thoughtfully considered and discussed.",
            "The response shows innovation while maintaining scientific plausibility across all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
