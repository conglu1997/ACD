import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_frameworks = [
            "Western analytical",
            "Eastern holistic",
            "Indigenous ecological",
            "Quantum mechanical"
        ]
        abstract_concepts = [
            "Time",
            "Causality",
            "Consciousness",
            "Knowledge"
        ]
        disciplines = [
            "Philosophy",
            "Physics",
            "Neuroscience",
            "Anthropology"
        ]
        return {
            "1": {
                "source_framework": random.choice(cognitive_frameworks),
                "target_framework": random.choice(cognitive_frameworks),
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "discipline": random.choice(disciplines)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "source_framework" in t:
            return f"Design a system to translate the abstract concept of {t['concept']} from a {t['source_framework']} cognitive framework to a {t['target_framework']} cognitive framework. Your response should include:\n\n1. System Design (250-300 words):\n   a) Describe the key components of your translation system.\n   b) Explain how your system accounts for differences in cognitive frameworks.\n   c) Discuss any novel techniques or algorithms used in your system.\n\n2. Concept Analysis (200-250 words):\n   a) Analyze how {t['concept']} is understood within the {t['source_framework']} framework.\n   b) Identify key aspects of {t['concept']} that might be challenging to translate.\n\n3. Translation Process (250-300 words):\n   a) Provide a step-by-step explanation of how your system would translate {t['concept']}.\n   b) Discuss how your system preserves or adapts meaning across frameworks.\n   c) Address any potential loss or gain of information in the translation process.\n\n4. Output and Validation (200-250 words):\n   a) Present the translated concept of {t['concept']} in the {t['target_framework']}.\n   b) Explain how you would validate the accuracy and effectiveness of the translation.\n   c) Discuss potential applications or implications of this translation.\n\nEnsure your response demonstrates a deep understanding of both cognitive frameworks and the abstract concept. Use appropriate terminology and provide clear explanations for complex ideas. Include relevant citations or references when discussing specific cognitive frameworks or theories.\n\nYour total response should be between 900-1100 words."
        else:
            return f"Use your cognitive framework translation system to analyze and reframe the concept of {t['concept']} within the discipline of {t['discipline']}. Your response should include:\n\n1. Concept Analysis (200-250 words):\n   a) Analyze how {t['concept']} is currently understood within {t['discipline']}.\n   b) Identify key aspects of this understanding that might benefit from reframing.\n\n2. Framework Selection (150-200 words):\n   a) Choose two distinct cognitive frameworks for your analysis.\n   b) Justify your choice of frameworks for this particular concept and discipline.\n\n3. Translation and Reframing (300-350 words):\n   a) Apply your translation system to reframe {t['concept']} using the chosen frameworks.\n   b) Discuss how each framework offers a different perspective on {t['concept']}.\n   c) Explain how these translations might lead to new insights or approaches in {t['discipline']}.\n\n4. Synthesis and Implications (250-300 words):\n   a) Synthesize the insights gained from the different framework translations.\n   b) Discuss how this reframing might impact research or practice in {t['discipline']}.\n   c) Propose a novel research question or approach that emerges from this analysis.\n\nEnsure your response demonstrates a deep understanding of the chosen cognitive frameworks, the abstract concept, and the relevant discipline. Be creative in your approach while maintaining scientific plausibility. Emphasize cross-disciplinary thinking and the potential for new insights at the intersection of different fields.\n\nInclude relevant citations or references when discussing specific cognitive frameworks or theories.\n\nYour total response should be between 900-1100 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the cognitive frameworks and abstract concepts involved.",
            "The proposed system or analysis is creative, coherent, and scientifically plausible.",
            "The response shows strong interdisciplinary reasoning and knowledge integration.",
            "The analysis offers novel insights or approaches to the given concept or discipline.",
            "The writing is clear, well-structured, and effectively communicates complex ideas.",
            "The response includes relevant citations or references when discussing specific cognitive frameworks or theories.",
            "The total word count is between 900-1100 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
