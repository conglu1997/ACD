import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                "name": "Broca's area",
                "function": "speech production and language processing",
                "key_feature": "hierarchical structure processing"
            },
            {
                "name": "Wernicke's area",
                "function": "language comprehension",
                "key_feature": "semantic processing"
            }
        ]
        return {
            "1": random.choice(brain_regions),
            "2": random.choice(brain_regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language model architecture inspired by the neurobiological principles of human language processing, focusing on the functions of {t['name']} ({t['function']}). Your task is to create an AI system that mimics the key features of this brain region, particularly its role in {t['key_feature']}. Your response should include the following sections:

1. Neurobiological Basis (200-250 words):
   a) Explain the key functions and characteristics of {t['name']} in human language processing.
   b) Describe how {t['key_feature']} contributes to language comprehension or production.
   c) Discuss any relevant neuronal architectures or processes that could inspire AI design.

2. Model Architecture (250-300 words):
   a) Propose a novel architecture for a language model inspired by {t['name']}.
   b) Explain how your model incorporates the principle of {t['key_feature']}.
   c) Describe the key components of your model and their interactions.
   d) Include a simple diagram or flowchart of your model architecture (use ASCII art).

3. Training and Data Considerations (200-250 words):
   a) Describe the type of data and training approach needed for your model.
   b) Explain how your training method reflects neurobiological learning processes.
   c) Discuss any potential challenges in training this model and propose solutions.

4. Comparative Analysis (200-250 words):
   a) Compare your neurobiologically inspired model to current state-of-the-art language models.
   b) Discuss potential advantages and limitations of your approach.
   c) Explain how your model might perform differently on specific language tasks.

5. Ethical Implications (150-200 words):
   a) Discuss potential ethical concerns related to developing AI systems that closely mimic human brain functions.
   b) Propose guidelines for responsible development and use of neurobiologically inspired AI models.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your model.
   b) Propose a research question that could further the development of neurobiologically inspired language models.

Ensure your response demonstrates a deep understanding of both neurobiology and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Your total response should be between 1100-1400 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically accurate explanation of {t['name']} and its role in {t['key_feature']}.",
            "The proposed model architecture is novel, well-described, and clearly inspired by the specified brain region.",
            "The training and data considerations are thoughtfully discussed and reflect neurobiological principles.",
            "The comparative analysis provides insightful comparisons between the proposed model and current language models.",
            "Ethical implications are thoroughly considered with reasonable guidelines proposed.",
            "The future research directions are relevant and demonstrate forward-thinking in the field.",
            "The overall response demonstrates a strong grasp of neurobiology, linguistics, and artificial intelligence, creatively applied to language model design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
