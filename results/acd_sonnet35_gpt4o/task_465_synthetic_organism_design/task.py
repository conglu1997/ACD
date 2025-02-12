import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "environment": "Deep ocean",
                "primary_function": "Plastic waste decomposition",
                "ethical_constraint": "Minimal impact on existing ecosystems"
            },
            {
                "environment": "Arid desert",
                "primary_function": "Water harvesting and purification",
                "ethical_constraint": "No competition with native species for resources"
            },
            {
                "environment": "Urban air",
                "primary_function": "Air pollution filtration",
                "ethical_constraint": "No unintended effects on human health"
            },
            {
                "environment": "Agricultural soil",
                "primary_function": "Nitrogen fixation and pest control",
                "ethical_constraint": "No gene transfer to wild organisms"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an artificial organism for the following scenario:\n\n" \
               f"Environment: {t['environment']}\n" \
               f"Primary Function: {t['primary_function']}\n" \
               f"Ethical Constraint: {t['ethical_constraint']}\n\n" \
               f"Your response should include the following sections:\n\n" \
               f"1. Organism Design (200-250 words):\n" \
               f"   a) Describe the key biological features of your artificial organism.\n" \
               f"   b) Explain how these features enable it to perform its primary function.\n" \
               f"   c) Discuss how the organism is adapted to its specified environment.\n\n" \
               f"2. Synthetic Biology Approach (150-200 words):\n" \
               f"   a) Outline the key genetic modifications or synthetic biological techniques used to create your organism.\n" \
               f"   b) Explain any novel biological pathways or systems you've incorporated.\n\n" \
               f"3. Ethical Considerations (200-250 words):\n" \
               f"   a) Address how your design meets the specified ethical constraint.\n" \
               f"   b) Discuss any potential unintended consequences and how they might be mitigated.\n" \
               f"   c) Consider broader ethical implications of releasing this organism into the environment.\n\n" \
               f"4. Potential Applications and Limitations (150-200 words):\n" \
               f"   a) Describe potential real-world applications of your artificial organism beyond its primary function.\n" \
               f"   b) Discuss any limitations or challenges in implementing your design.\n\n" \
               f"5. Interdisciplinary Connections (50-75 words):\n" \
               f"   Briefly explain how your design integrates principles from biology, engineering, and environmental science.\n\n" \
               f"Ensure your organism design is scientifically plausible, creative, and demonstrates a deep understanding of biological principles and synthetic biology techniques. Use appropriate scientific terminology throughout your response.\n\n" \
               f"Format your answer with clear headings for each section. Your total response should be between 750-975 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The artificial organism is well-designed for the {t['environment']} environment.",
            f"The organism effectively performs its primary function of {t['primary_function']}.",
            f"The design clearly addresses the ethical constraint: {t['ethical_constraint']}.",
            "The response includes all required sections (1-5) as specified, adhering to the given word limits.",
            "The organism design is scientifically plausible and demonstrates a deep understanding of biological principles and synthetic biology techniques.",
            "The synthetic biology approach is well-explained and incorporates novel biological pathways or systems.",
            "Ethical considerations are thoroughly addressed, including potential unintended consequences and broader implications.",
            "Potential applications and limitations of the organism are thoughtfully discussed.",
            "The response demonstrates clear interdisciplinary connections between biology, engineering, and environmental science.",
            "Appropriate scientific terminology is used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
