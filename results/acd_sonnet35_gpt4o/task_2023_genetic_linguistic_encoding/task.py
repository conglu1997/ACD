import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genetic_elements = [
            "protein-coding genes",
            "regulatory sequences",
            "non-coding RNAs",
            "transposable elements",
            "epigenetic markers"
        ]
        linguistic_features = [
            "syntax",
            "morphology",
            "phonology",
            "semantics",
            "pragmatics"
        ]
        
        return {
            "1": {
                "genetic_element": random.choice(genetic_elements),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "genetic_element": random.choice(genetic_elements),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system that encodes genetic information using linguistic principles, focusing on representing {t['genetic_element']} using concepts from {t['linguistic_feature']}. Your response should include:\n\n" \
               f"1. Encoding System Design (300-350 words):\n" \
               f"   a) Describe the key components of your genetic-linguistic encoding system.\n" \
               f"   b) Explain how your system incorporates principles from {t['linguistic_feature']}.\n" \
               f"   c) Discuss how your encoding system represents {t['genetic_element']}.\n" \
               f"   d) Provide a simple example of how a specific genetic sequence would be encoded in your system.\n\n" \
               f"2. Information Theory Analysis (200-250 words):\n" \
               f"   a) Analyze the efficiency of your encoding system using information theory principles.\n" \
               f"   b) Compare the information density of your system to that of natural DNA.\n" \
               f"   c) Discuss any trade-offs between complexity and information content in your system.\n\n" \
               f"3. Biological Implications (200-250 words):\n" \
               f"   a) Explain how your encoding system might reveal new insights about the structure or function of {t['genetic_element']}.\n" \
               f"   b) Discuss potential applications of your system in genetic research or synthetic biology.\n" \
               f"   c) Analyze how your system might handle genetic mutations or variations.\n\n" \
               f"4. Computational Implementation (150-200 words):\n" \
               f"   a) Outline an algorithm for translating between standard genetic notation and your linguistic encoding.\n" \
               f"   b) Discuss potential challenges in implementing this system computationally and propose solutions.\n\n" \
               f"5. Ethical Considerations and Limitations (100-150 words):\n" \
               f"   a) Identify potential ethical issues or limitations in using linguistic principles to encode genetic information.\n" \
               f"   b) Propose guidelines for the responsible development and use of such encoding systems.\n\n" \
               f"Ensure your response demonstrates a deep understanding of genetics, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['genetic_element']} and {t['linguistic_feature']}.",
            "The proposed encoding system creatively and feasibly incorporates linguistic principles into genetic representation.",
            "The information theory analysis is sound and provides meaningful insights.",
            "The biological implications and potential applications are thoughtfully explored.",
            "The computational implementation is logically outlined and challenges are realistically addressed.",
            "Ethical considerations are appropriately discussed and guidelines are proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
