import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            {
                "principle": "Working Memory Limitations",
                "description": "The cognitive constraint that humans can only hold a limited amount of information in their working memory at once.",
                "nlp_task": "Text Summarization"
            },
            {
                "principle": "Predictive Processing",
                "description": "The brain's tendency to constantly generate predictions about future inputs and events based on prior knowledge and context.",
                "nlp_task": "Next Word Prediction"
            }
        ]
        return {
            "1": random.choice(cognitive_principles),
            "2": random.choice(cognitive_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language model architecture based on the cognitive science principle of {t['principle']}. Then, apply your model to the NLP task of {t['nlp_task']}. Your response should include the following sections:

1. Cognitive Principle Overview (100-150 words):
   Explain the given cognitive principle and its relevance to language processing.

2. Model Architecture (200-250 words):
   a) Describe the key components of your language model architecture.
   b) Explain how it incorporates the given cognitive principle.
   c) Discuss how your model differs from traditional language models.
   d) Include a simple diagram or pseudocode representation of your model's architecture.

3. Training and Data Requirements (150-200 words):
   a) Describe the type of data needed to train your model.
   b) Explain any unique training procedures or techniques required.
   c) Discuss potential challenges in training your model and how to address them.

4. Application to NLP Task (200-250 words):
   a) Explain how your model would approach the given NLP task.
   b) Describe the expected advantages of your model for this task.
   c) Discuss potential limitations or challenges in applying your model to this task.
   d) Provide a specific example of how your model would process a given input for this task.

5. Evaluation and Comparison (150-200 words):
   a) Propose metrics to evaluate your model's performance on the given NLP task.
   b) Compare your model's expected performance to traditional approaches.
   c) Suggest an experiment to test your model against existing models.

6. Ethical Considerations and Cognitive Implications (100-150 words):
   a) Discuss potential ethical issues or biases that could arise from your model.
   b) Explain how your model might contribute to our understanding of human cognition.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all six required sections as outlined in the instructions.",
            f"The language model architecture must clearly incorporate the cognitive principle of {t['principle']}.",
            f"The application to the NLP task of {t['nlp_task']} must be clearly explained and relevant.",
            "The response must demonstrate a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The proposed model must be creative and novel while remaining scientifically plausible.",
            "The response must include appropriate technical terminology and clear explanations for complex concepts.",
            "The response must adhere to the specified word count range (900-1200 words) and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
