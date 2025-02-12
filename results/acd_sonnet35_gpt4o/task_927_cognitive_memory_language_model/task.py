import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "memory_type": "episodic_memory",
                "linguistic_task": "narrative_generation",
                "cognitive_constraint": "limited_working_memory_capacity"
            },
            {
                "memory_type": "semantic_memory",
                "linguistic_task": "word_sense_disambiguation",
                "cognitive_constraint": "spreading_activation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a language model architecture inspired by human {t['memory_type']} and working memory, focusing on the task of {t['linguistic_task']}. Your model should incorporate the cognitive constraint of {t['cognitive_constraint']}. Provide your response in the following format:\n\n" + \
               "1. Model Architecture (250-300 words):\n" + \
               "   a) Describe the overall structure of your cognitive-inspired language model.\n" + \
               "   b) Explain how it incorporates {t['memory_type']} and working memory concepts.\n" + \
               "   c) Detail how the model addresses the {t['linguistic_task']} task.\n" + \
               "   d) Explain how you've implemented the {t['cognitive_constraint']} constraint.\n\n" + \
               "2. Cognitive Science Foundation (200-250 words):\n" + \
               "   a) Explain the key cognitive science principles underlying your model.\n" + \
               "   b) Discuss how your model reflects current understanding of human memory processes.\n" + \
               "   c) Describe any simplifications or assumptions made in translating cognitive concepts to a computational model.\n\n" + \
               "3. Training and Inference Process (200-250 words):\n" + \
               "   a) Describe how your model would be trained, considering its cognitive-inspired architecture.\n" + \
               "   b) Explain the inference process for the {t['linguistic_task']} task.\n" + \
               "   c) Discuss how the {t['cognitive_constraint']} affects the model's performance.\n\n" + \
               "4. Evaluation Metrics (150-200 words):\n" + \
               "   a) Propose specific metrics to evaluate your model's performance on the {t['linguistic_task']} task.\n" + \
               "   b) Explain how these metrics reflect both linguistic accuracy and cognitive plausibility.\n" + \
               "   c) Suggest a method for comparing your model's performance to human performance on the same task.\n\n" + \
               "5. Potential Applications and Implications (200-250 words):\n" + \
               "   a) Discuss potential applications of your cognitive-inspired language model in AI and cognitive science.\n" + \
               "   b) Explore how this model might contribute to our understanding of human language processing.\n" + \
               "   c) Consider ethical implications of developing AI systems that more closely mimic human cognitive processes.\n\n" + \
               "Ensure your response demonstrates a deep understanding of both cognitive science and natural language processing. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both cognitive science and natural language processing.",
            f"The model effectively incorporates {t['memory_type']} and working memory concepts.",
            f"The design addresses the {t['linguistic_task']} task in a plausible manner.",
            f"The {t['cognitive_constraint']} is clearly implemented and explained.",
            "The training and inference processes are well-described and cognitively plausible.",
            "The proposed evaluation metrics are appropriate and well-justified.",
            "The potential applications and implications are thoughtfully considered.",
            "The response is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
