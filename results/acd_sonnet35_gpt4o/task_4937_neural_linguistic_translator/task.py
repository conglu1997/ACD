import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        thought_categories = [
            'Visual Imagery',
            'Abstract Reasoning',
            'Emotional Processing',
            'Spatial Navigation',
            'Memory Recall'
        ]
        brain_regions = [
            'Prefrontal Cortex',
            'Hippocampus',
            'Amygdala',
            'Visual Cortex',
            'Broca\'s Area'
        ]
        linguistic_features = [
            'Metaphorical Expression',
            'Syntactic Complexity',
            'Semantic Ambiguity',
            'Prosodic Features',
            'Pragmatic Context'
        ]
        tasks = [
            {
                'thought_category': random.choice(thought_categories),
                'brain_region': random.choice(brain_regions),
                'linguistic_feature': random.choice(linguistic_features)
            },
            {
                'thought_category': random.choice(thought_categories),
                'brain_region': random.choice(brain_regions),
                'linguistic_feature': random.choice(linguistic_features)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate neural activity patterns directly into natural language, focusing on the thought category of {t['thought_category']}, the brain region {t['brain_region']}, and the linguistic feature of {t['linguistic_feature']}. Then, use your system to interpret and express a complex abstract thought. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neural-linguistic translation.
   b) Explain how your system integrates neuroscientific principles, particularly related to {t['brain_region']}.
   c) Detail how your system processes and generates language, with emphasis on {t['linguistic_feature']}.
   d) Include a diagram or flowchart of your system architecture (describe it textually).

2. Neural Decoding Mechanism (250-300 words):
   a) Explain the specific techniques your system uses to decode neural activity patterns.
   b) Describe how it handles the particular challenges of {t['thought_category']}.
   c) Discuss how your system accounts for individual variability in neural patterns.

3. Linguistic Encoding Process (250-300 words):
   a) Detail how your system translates decoded neural patterns into language.
   b) Explain how it incorporates {t['linguistic_feature']} in the generated output.
   c) Describe any novel approaches to natural language generation in your system.

4. Abstract Thought Interpretation (200-250 words):
   a) Present a complex abstract thought related to {t['thought_category']}.
   b) Provide a step-by-step explanation of how your system would interpret this thought.
   c) Show the resulting linguistic output, highlighting the use of {t['linguistic_feature']}.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and coherence of your system's translations.
   b) Discuss potential biases or limitations in your approach.
   c) Suggest an experiment to validate your AI system's performance with human participants.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of direct thought-to-language translation technology.
   b) Address potential misuse or privacy concerns.
   c) Propose guidelines for responsible development and use of such systems.

7. Future Directions (150-200 words):
   a) Suggest potential improvements or expansions to your system.
   b) Discuss how it could be adapted to other thought categories or linguistic features.
   c) Propose a novel research question arising from your design.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence, particularly in relation to {t['thought_category']}, {t['brain_region']}, and {t['linguistic_feature']}.",
            "The AI system design is innovative, scientifically plausible, and effectively integrates neural decoding with linguistic encoding.",
            "The abstract thought interpretation demonstration is coherent and showcases the system's capabilities.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response shows strong integration of knowledge from multiple disciplines.",
            "The response adheres to the specified word limits for each section and overall length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
