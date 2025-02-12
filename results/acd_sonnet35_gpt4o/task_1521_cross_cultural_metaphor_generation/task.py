class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "abstract_concept": "resilience",
                "context": "economic hardship"
            },
            "2": {
                "source_culture": "Maasai",
                "target_culture": "Nordic",
                "abstract_concept": "harmony",
                "context": "environmental conservation"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model capable of generating and interpreting metaphors across different cultures and languages, then use it to analyze the abstract concept of {t['abstract_concept']} in the context of {t['context']}. Your task has the following parts:

1. Model Architecture (250-300 words):
   a) Describe the key components of your cross-cultural metaphor generation model.
   b) Explain how your model incorporates cultural knowledge and linguistic structures.
   c) Discuss any novel techniques or approaches used in your model design.

2. Training Process (200-250 words):
   a) Outline the data sources and types you would use to train your model.
   b) Describe the training process, including any specific techniques for cross-cultural learning.
   c) Explain how you would evaluate and refine your model during training.

3. Metaphor Generation (250-300 words):
   a) Use your model to generate a metaphor for '{t['abstract_concept']}' in the context of {t['context']}, originating from {t['source_culture']} culture.
   b) Explain the cultural and linguistic elements of the generated metaphor.
   c) Describe how your model would adapt this metaphor for {t['target_culture']} culture.
   d) Analyze the similarities and differences between the original and adapted metaphors.

4. Interpretation and Analysis (200-250 words):
   a) Explain how your model would interpret and analyze the generated metaphors.
   b) Discuss any insights about {t['abstract_concept']} revealed through this cross-cultural metaphor analysis.
   c) Describe how your model handles ambiguity or cultural-specific connotations.

5. Model Evaluation (150-200 words):
   a) Propose metrics to evaluate your model's performance in cross-cultural metaphor generation and interpretation.
   b) Discuss potential biases or limitations in your model and how you might address them.
   c) Compare your model's approach to human cognitive processes in cross-cultural metaphor understanding.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI for cross-cultural metaphor generation and interpretation.
   b) Propose guidelines for responsible use of your model in real-world applications.
   c) Explore potential misuse scenarios and suggest safeguards against them.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response using the following structure:

1. Model Architecture
   [Your response here]

2. Training Process
   [Your response here]

3. Metaphor Generation
   [Your response here]

4. Interpretation and Analysis
   [Your response here]

5. Model Evaluation
   [Your response here]

6. Ethical Considerations
   [Your response here]

Your entire response should not exceed 1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and AI principles.",
            "The proposed model architecture and training process are well-explained and scientifically plausible.",
            "The generated metaphors show cultural sensitivity and creativity while accurately representing the abstract concept.",
            "The analysis of cross-cultural metaphor adaptation is insightful and demonstrates understanding of cultural nuances.",
            "The model evaluation section proposes relevant metrics and addresses potential biases and limitations.",
            "Ethical considerations are thoroughly explored with practical guidelines and safeguards proposed.",
            "The response is well-structured, adhering to the specified sections and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
