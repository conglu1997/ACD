import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_domain": "journey",
                "target_domain": "life",
                "cognitive_process": "analogical reasoning"
            },
            {
                "source_domain": "war",
                "target_domain": "argument",
                "cognitive_process": "conceptual blending"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an artificial cognitive architecture capable of generating and understanding conceptual metaphors, focusing on the metaphorical mapping from the source domain of {t['source_domain']} to the target domain of {t['target_domain']}. Your architecture should incorporate the cognitive process of {t['cognitive_process']}. Provide your response in the following format:\n\n1. Cognitive Architecture Overview (250-300 words):\nDescribe the key components and mechanisms of your artificial cognitive architecture for metaphor generation and understanding. Explain how it incorporates the specified cognitive process.\n\n2. Metaphor Generation Process (200-250 words):\nDetail how your system generates conceptual metaphors, specifically for the given source and target domains. Provide at least two example metaphors your system might generate.\n\n3. Metaphor Understanding Mechanism (200-250 words):\nExplain how your system interprets and derives meaning from conceptual metaphors. Describe the algorithms or methods used for metaphor comprehension.\n\n4. Neural-Symbolic Integration (150-200 words):\nDiscuss how your architecture integrates neural network approaches with symbolic reasoning to handle metaphorical thinking.\n\n5. Evaluation and Validation (150-200 words):\nPropose a method to evaluate the effectiveness and cognitive plausibility of your system in generating and understanding metaphors.\n\n6. Implications for AI and Cognitive Science (150-200 words):\nAnalyze the potential implications of your architecture for advancing AI language understanding and our knowledge of human cognition.\n\n7. Ethical Considerations and Limitations (100-150 words):\nDiscuss potential ethical implications or challenges arising from the development or application of your metaphor-capable AI system.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cognitive architecture effectively addresses the generation and understanding of metaphors from {t['source_domain']} to {t['target_domain']}.",
            f"The system incorporates the cognitive process of {t['cognitive_process']} in a plausible and well-explained manner.",
            "The response demonstrates a nuanced understanding of conceptual metaphor theory and cognitive science principles.",
            "The proposed architecture is innovative and theoretically sound.",
            "The metaphor generation and understanding processes are well-explained and cognitively plausible.",
            "The neural-symbolic integration is thoughtfully addressed.",
            "The evaluation method is appropriate and well-designed.",
            "Implications for AI and cognitive science are insightfully analyzed.",
            "Ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
