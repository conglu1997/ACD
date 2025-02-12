import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "semantic_feature": "polysemy",
                "language_task": "word sense disambiguation",
                "cognitive_constraint": "limited working memory"
            },
            {
                "semantic_feature": "metaphor comprehension",
                "language_task": "figurative language interpretation",
                "cognitive_constraint": "attention bottleneck"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models human semantic networks based on neurolinguistic principles, focusing on the semantic feature of {t['semantic_feature']}. Then, apply your system to the language processing task of {t['language_task']}, while accounting for the cognitive constraint of {t['cognitive_constraint']}. Your response should include:\n\n" + \
               "1. Neurolinguistic Foundation (250-300 words):\n" + \
               "   a) Explain the neurolinguistic principles underlying semantic networks in the human brain.\n" + \
               "   b) Describe how {t['semantic_feature']} is represented and processed in the brain.\n" + \
               "   c) Discuss how {t['cognitive_constraint']} affects semantic processing in humans.\n\n" + \
               "2. AI System Architecture (300-350 words):\n" + \
               "   a) Design an AI architecture that models semantic networks based on your neurolinguistic foundation.\n" + \
               "   b) Explain how your system represents and processes {t['semantic_feature']}.\n" + \
               "   c) Describe how you've implemented the {t['cognitive_constraint']} in your AI system.\n" + \
               "   d) Provide a diagram or detailed description of your system's structure.\n\n" + \
               "3. Application to Language Task (250-300 words):\n" + \
               "   a) Explain how your AI system approaches the task of {t['language_task']}.\n" + \
               "   b) Provide a step-by-step description of how your system processes input and generates output for this task.\n" + \
               "   c) Discuss how the {t['cognitive_constraint']} affects your system's performance on this task.\n\n" + \
               "4. Comparative Analysis (200-250 words):\n" + \
               "   a) Compare your neuro-semantic AI system to traditional NLP approaches for {t['language_task']}.\n" + \
               "   b) Discuss potential advantages and limitations of your approach.\n" + \
               "   c) Propose an experiment to evaluate your system against both human performance and traditional AI methods.\n\n" + \
               "5. Ethical and Societal Implications (150-200 words):\n" + \
               "   a) Discuss ethical considerations in developing AI systems that closely mimic human cognitive processes.\n" + \
               "   b) Explore potential societal impacts of AI systems with advanced semantic processing capabilities.\n" + \
               "   c) Propose guidelines for responsible development and use of neuro-semantic AI systems.\n\n" + \
               "Ensure your response demonstrates a deep understanding of neurolinguistics, semantic processing, and AI system design. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neurolinguistics, semantic processing, and AI system design.",
            f"The AI system effectively models semantic networks and addresses {t['semantic_feature']}.",
            f"The design appropriately tackles the {t['language_task']} task.",
            f"The {t['cognitive_constraint']} is clearly implemented and its effects are well-explained.",
            "The comparative analysis is thorough and insightful.",
            "The ethical and societal implications are thoughtfully considered.",
            "The response is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
