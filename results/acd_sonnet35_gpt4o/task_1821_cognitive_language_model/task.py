import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_aspects = [
            {
                "aspect": "episodic memory",
                "application": "contextual retrieval",
                "scenario": "a virtual assistant for elderly care"
            },
            {
                "aspect": "semantic memory",
                "application": "conceptual integration",
                "scenario": "an AI-powered educational tool for students"
            }
        ]
        return {
            "1": random.choice(cognitive_aspects),
            "2": random.choice(cognitive_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model that incorporates cognitive theories of human memory and language processing, with a specific focus on {t['aspect']} for {t['application']}. Consider the following scenario: {t['scenario']}. Your task has the following components:

1. Cognitive-Linguistic Framework (250-300 words):
   a) Explain how {t['aspect']} functions in human cognition and language processing.
   b) Describe how you would model {t['aspect']} in a language processing system.
   c) Discuss how incorporating {t['aspect']} could enhance {t['application']} in language models, particularly in the context of {t['scenario']}.

2. Model Architecture (250-300 words):
   a) Outline the key components of your cognitive language model.
   b) Explain how your model integrates {t['aspect']} with traditional language processing techniques.
   c) Describe the data structures and algorithms you would use to implement {t['aspect']} in your model.

3. Training and Learning Process (200-250 words):
   a) Propose a method for training your cognitive language model.
   b) Explain how your model would learn and update its {t['aspect']} component.
   c) Discuss any challenges in training a model with integrated cognitive components and how you would address them.

4. Performance Evaluation (200-250 words):
   a) Suggest metrics for evaluating your model's performance in {t['application']}.
   b) Describe an experiment to test how well your model implements {t['aspect']}.
   c) Compare your model's expected performance to traditional language models without cognitive components.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns of developing language models that mimic human cognitive processes.
   b) Explore practical applications of your cognitive language model in {t['scenario']}.

6. Future Directions (150-200 words):
   a) Propose two potential extensions or improvements to your cognitive language model.
   b) Discuss how your model could contribute to our understanding of human cognition and language processing.

7. Use Case Example (100-150 words):
   Provide a brief, specific example of how your cognitive language model would process and respond to a user input in the context of {t['scenario']}. Include both the user input and the model's response.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary. Balance theoretical knowledge with practical applications throughout your response.

Format your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Cognitive-Linguistic Framework:') followed by your response for that section. Adhere strictly to the word limits provided for each section.

Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['aspect']} and its role in human cognition and language processing, with clear application to {t['scenario']}.",
            f"The proposed model architecture effectively integrates {t['aspect']} with traditional language processing techniques, showing innovation and feasibility.",
            f"The training and learning process for the model is well-explained and addresses challenges specific to implementing {t['aspect']}.",
            f"The performance evaluation methods are appropriate for assessing the model's capabilities in {t['application']}, with clear metrics and experimental design.",
            f"The ethical and practical implications of the model are thoughtfully considered, especially in the context of {t['scenario']}.",
            "The proposed future directions are innovative and demonstrate a forward-thinking approach to cognitive language modeling.",
            f"The use case example effectively illustrates the model's application in {t['scenario']}, showing a clear input-output process.",
            "The response balances theoretical knowledge with practical applications throughout.",
            "The response is well-structured with clear headings and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
