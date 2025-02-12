import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        concepts = ['time', 'emotion', 'power', 'knowledge', 'life']
        tasks = {
            "1": {
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities),
                "abstract_concept": random.choice(concepts)
            },
            "2": {
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities),
                "abstract_concept": random.choice(concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting metaphors across different sensory modalities, applying cognitive linguistics theories to enhance machine learning models. Your task focuses on creating a metaphor that expresses the abstract concept of {t['abstract_concept']} using a mapping from the {t['source_modality']} modality to the {t['target_modality']} modality.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of cognitive linguistics and conceptual metaphor theory relevant to cross-modal metaphor generation.
   b) Describe how your AI system incorporates these principles in its design.
   c) Discuss the challenges and opportunities of mapping between {t['source_modality']} and {t['target_modality']} modalities.
   d) Explain how your system handles the abstract concept of {t['abstract_concept']} in this context.

2. System Architecture (300-350 words):
   a) Provide a detailed description of your AI system's architecture for cross-modal metaphor synthesis.
   b) Explain how each component contributes to the metaphor generation and interpretation process.
   c) Describe the data sources and preprocessing techniques your system would use.
   d) Include a diagram or flowchart of your system architecture (use ASCII art or a clear textual description).

3. Metaphor Generation Process (250-300 words):
   a) Describe the step-by-step process of how your system generates a metaphor for {t['abstract_concept']} using {t['source_modality']} and {t['target_modality']} modalities.
   b) Explain how your system ensures the metaphor is coherent and meaningful.
   c) Provide an example of a metaphor your system might generate, and explain its components.

4. Interpretation and Evaluation (200-250 words):
   a) Explain how your system would interpret and evaluate the quality of the generated metaphors.
   b) Describe metrics or criteria you would use to assess metaphor effectiveness.
   c) Discuss how your system might handle ambiguity or multiple interpretations.

5. Cognitive Science Integration (200-250 words):
   a) Analyze how your system's approach aligns with human cognitive processes in metaphor comprehension.
   b) Discuss any insights your system might provide about human cognition and linguistic creativity.
   c) Propose an experiment to compare your system's metaphor processing with human performance.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical implications or misuses of advanced metaphor generation AI.
   b) Discuss limitations of your approach and areas for future improvement.
   c) Propose guidelines for responsible development and use of cross-modal metaphor AI systems.

Ensure your response demonstrates a deep understanding of cognitive linguistics, machine learning, and sensory processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive linguistics and conceptual metaphor theory.",
            "The proposed AI system architecture is well-designed and incorporates relevant principles for cross-modal metaphor generation.",
            "The metaphor generation process is clearly explained and plausible.",
            "The interpretation and evaluation methods are well-thought-out and grounded in linguistic theory.",
            "The response shows a deep understanding of the integration between AI and cognitive science.",
            "Ethical considerations and limitations are thoroughly addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
