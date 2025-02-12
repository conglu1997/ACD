import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language_area': 'Broca\'s area',
                'linguistic_feature': 'syntax processing',
                'developmental_stage': 'early childhood (2-4 years)'
            },
            {
                'language_area': 'Wernicke\'s area',
                'linguistic_feature': 'semantic processing',
                'developmental_stage': 'adolescence (12-16 years)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by {t['language_area']} to model {t['linguistic_feature']} during {t['developmental_stage']}. Your task has five parts:

1. Architectural Design (300-350 words):
   a) Describe the overall structure of your neural network, explaining how it mirrors the functionality of {t['language_area']}.
   b) Detail the types of layers, connections, and activation functions used, justifying your choices based on neuroscientific evidence.
   c) Explain how your architecture specifically addresses {t['linguistic_feature']}.
   d) Discuss how your model accounts for the developmental aspects of {t['developmental_stage']}.

2. Input and Output Representation (200-250 words):
   a) Describe how linguistic input would be encoded for your network.
   b) Explain the format of the network's output and how it represents {t['linguistic_feature']}.
   c) Discuss any preprocessing or postprocessing steps necessary for your model.

3. Learning Algorithm and Training Process (250-300 words):
   a) Propose a learning algorithm suitable for your architecture and the task of {t['linguistic_feature']}.
   b) Describe the training process, including the type of data needed and how it would be presented to the network.
   c) Explain how your training process mimics language acquisition during {t['developmental_stage']}.
   d) Discuss potential challenges in training your model and how you would address them.

4. Performance Evaluation (200-250 words):
   a) Propose methods to evaluate your model's performance in {t['linguistic_feature']}.
   b) Describe specific metrics or tests you would use, explaining their relevance to both linguistic theory and neuroscience.
   c) Discuss how you would compare your model's performance to human performance, considering the {t['developmental_stage']}.

5. Implications and Future Directions (200-250 words):
   a) Analyze the potential insights your model could provide about human language processing and acquisition.
   b) Discuss the limitations of your approach and how it might be extended or improved.
   c) Propose two novel experiments or applications that could build upon your model.
   d) Reflect on the ethical implications of using such models to study or replicate human language abilities.

Ensure your response demonstrates a deep understanding of neurolinguistics, developmental psychology, and machine learning. Use appropriate technical terminology and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed neural network architecture inspired by {t['language_area']} for modeling {t['linguistic_feature']}.",
            f"The design demonstrates a deep understanding of neuroscience, particularly related to {t['language_area']} and its role in language processing.",
            f"The model appropriately addresses the developmental aspects of {t['developmental_stage']}.",
            "The submission includes a well-reasoned approach to input/output representation, learning algorithms, and training processes.",
            "The response proposes valid methods for performance evaluation and comparison to human performance.",
            "The implications and future directions section demonstrates critical thinking about the model's potential impact and limitations.",
            "The overall response shows creativity and plausibility in integrating concepts from neuroscience, linguistics, and machine learning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
