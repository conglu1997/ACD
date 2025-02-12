class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "source_domain": "Journey",
                "target_domain": "Life",
                "emotion": "Hope"
            },
            "2": {
                "source_domain": "War",
                "target_domain": "Argument",
                "emotion": "Frustration"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model for metaphor generation and interpretation, focusing on the metaphor '{t['target_domain']} is a {t['source_domain']}' and the emotion of {t['emotion']}. Your response should include:

        1. Theoretical Framework (250-300 words):
           a) Explain the cognitive linguistics theories underlying your model, particularly regarding metaphor comprehension and generation.
           b) Describe how your model incorporates the theory of conceptual blending.
           c) Discuss how emotional content is integrated into metaphor processing.

        2. Model Architecture (300-350 words):
           a) Design a neural network architecture for your cognitive model of metaphor processing.
           b) Explain how different components of your model correspond to cognitive processes in metaphor comprehension and generation.
           c) Describe how your model represents and manipulates conceptual spaces.
           d) Include a diagram or detailed description of your model's architecture.

        3. Metaphor Generation Process (250-300 words):
           a) Explain step-by-step how your model generates novel metaphors.
           b) Describe how the model ensures the generated metaphors are coherent and meaningful.
           c) Discuss how the specified emotion influences the metaphor generation process.

        4. Interpretation Mechanism (200-250 words):
           a) Detail how your model would interpret given metaphors.
           b) Explain how the model extracts meaning and emotional content from metaphorical expressions.

        5. Training and Data Requirements (200-250 words):
           a) Describe the type of data needed to train your model.
           b) Explain your proposed training process.
           c) Discuss any challenges in obtaining or creating suitable training data.

        6. Evaluation and Testing (200-250 words):
           a) Propose methods to evaluate the quality and creativity of generated metaphors.
           b) Describe how you would test the model's metaphor interpretation capabilities.
           c) Discuss potential benchmarks or comparison points for your model.

        7. Limitations and Ethical Considerations (150-200 words):
           a) Identify potential limitations of your approach.
           b) Discuss ethical implications of modeling and generating metaphorical language.
           c) Propose guidelines for responsible development and use of such models.

        Ensure your response demonstrates a deep understanding of cognitive linguistics, neural network architectures, and metaphor theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1550-1900 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts.",
            "The theoretical framework demonstrates a strong understanding of cognitive linguistics and metaphor theory.",
            "The model architecture is innovative, well-explained, and plausibly connects to cognitive processes.",
            "The metaphor generation process is clearly described and incorporates the specified emotion.",
            "The interpretation mechanism is logically explained and accounts for meaning and emotional content.",
            "Training and data requirements are realistic and well-considered.",
            "Evaluation methods are appropriate and well-justified.",
            "Limitations and ethical considerations are thoughtfully discussed.",
            "The overall response shows creativity, interdisciplinary knowledge integration, and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
