import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_development_stages = [
            "Babbling stage (0-6 months)",
            "One-word stage (6-18 months)",
            "Two-word stage (18-24 months)",
            "Telegraphic stage (24-30 months)",
            "Multi-word stage (30+ months)"
        ]
        cognitive_aspects = [
            "Phonological awareness",
            "Semantic development",
            "Syntactic development",
            "Pragmatic development",
            "Metalinguistic awareness"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "language_stage": random.choice(language_development_stages),
                "cognitive_aspect": random.choice(cognitive_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language model that mimics human language acquisition and development, focusing on the {t['language_stage']} and the cognitive aspect of {t['cognitive_aspect']}. Your response should include the following sections:

1. Model Architecture (250-300 words):
   a) Describe the key components of your AI model and how they correspond to human cognitive processes.
   b) Explain how your model simulates the specified language development stage.
   c) Detail how your model addresses the given cognitive aspect of language acquisition.
   d) Provide a diagram or flowchart illustrating your model's architecture.

2. Training Approach (200-250 words):
   a) Outline the data types and sources you would use to train your model.
   b) Describe the training process, including any novel techniques or algorithms.
   c) Explain how your training approach reflects human language learning processes.

3. Evaluation Metrics (150-200 words):
   a) Propose specific metrics to assess your model's performance in mimicking human language acquisition.
   b) Explain how these metrics relate to the specified language stage and cognitive aspect.
   c) Discuss any challenges in evaluating the model's cognitive similarity to humans.

4. Experiment Design (200-250 words):
   a) Propose an experiment to test how closely your model's language processing matches that of humans at the specified developmental stage.
   b) Describe the experimental setup, including control groups and variables.
   c) Explain how you would analyze and interpret the results.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of developing AI systems that closely mimic human cognitive processes.
   b) Propose guidelines for responsible development and use of such models.

6. Future Research Directions (100-150 words):
   a) Suggest two potential areas for future research based on your model.
   b) Explain how these research directions could contribute to our understanding of human language acquisition or AI development.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts",
            "The model architecture demonstrates a clear understanding of both AI and human cognitive processes",
            "The training approach reflects human language learning processes",
            "The evaluation metrics and experiment design are appropriate for assessing cognitive similarity",
            "The response shows creativity and innovation while maintaining scientific plausibility",
            "The ethical considerations and future research directions are thoughtful and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
