import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "memory_process": "long-term potentiation",
                "info_theory_concept": "Shannon entropy",
                "data_type": "text documents"
            },
            {
                "memory_process": "pattern separation",
                "info_theory_concept": "Huffman coding",
                "data_type": "digital images"
            },
            {
                "memory_process": "memory reconsolidation",
                "info_theory_concept": "Kolmogorov complexity",
                "data_type": "audio files"
            },
            {
                "memory_process": "synaptic pruning",
                "info_theory_concept": "data compression ratio",
                "data_type": "genetic sequences"
            },
            {
                "memory_process": "episodic memory formation",
                "info_theory_concept": "minimum description length",
                "data_type": "time series data"
            },
            {
                "memory_process": "working memory capacity",
                "info_theory_concept": "lossy compression",
                "data_type": "sensor network data"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical brain-inspired data compression system for {t['data_type']}, based on the neuroscientific principle of {t['memory_process']} and the information theory concept of {t['info_theory_concept']}. Your response should include the following sections:\n\n1. System Overview (200-250 words):\n   a) Briefly explain the chosen memory process and information theory concept.\n   b) Describe your proposed compression system, focusing on how it incorporates both neuroscientific and information theory principles.\n   c) Outline the key components of the system and how they interact.\n\n2. Compression Algorithm (250-300 words):\n   a) Provide a detailed explanation of how your algorithm compresses {t['data_type']}.\n   b) Describe how the algorithm mimics or incorporates the chosen memory process.\n   c) Explain how the chosen information theory concept is applied in the compression process.\n   d) Include a high-level pseudocode or flow diagram of your algorithm.\n\n3. Performance Analysis (200-250 words):\n   a) Discuss the potential advantages of your brain-inspired system over traditional compression methods.\n   b) Analyze any trade-offs or limitations in your approach.\n   c) Propose metrics to evaluate the performance of your system.\n\n4. Neuroscientific Implications (150-200 words):\n   a) Discuss how your system might provide insights into human memory processes.\n   b) Explore potential applications of your system in neuroscience research.\n\n5. Ethical Considerations and Future Directions (150-200 words):\n   a) Address any ethical concerns related to mimicking brain processes in data compression.\n   b) Suggest two potential research directions to further develop or expand upon your system.\n\nEnsure your response demonstrates a deep understanding of both neuroscience and information theory principles. Be creative in your design while maintaining scientific plausibility. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively incorporates the neuroscientific principle of {t['memory_process']} and the information theory concept of {t['info_theory_concept']}.",
            f"The compression algorithm is well-explained and logically applies to {t['data_type']}.",
            "The response demonstrates a deep understanding of both neuroscience and information theory principles.",
            "The performance analysis and neuroscientific implications are insightful and well-reasoned.",
            "The ethical considerations and future directions are thoughtfully addressed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format with clearly labeled sections and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
