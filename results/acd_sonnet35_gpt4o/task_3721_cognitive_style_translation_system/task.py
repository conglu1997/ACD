import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_styles = [
            {
                "style": "Analytical-Systematic",
                "characteristics": ["linear thinking", "logical reasoning", "step-by-step processing"],
                "domain": "Scientific method"
            },
            {
                "style": "Holistic-Intuitive",
                "characteristics": ["pattern recognition", "gestalt perception", "intuitive leaps"],
                "domain": "Creative problem-solving"
            },
            {
                "style": "Visual-Spatial",
                "characteristics": ["mental imagery", "spatial relationships", "visual metaphors"],
                "domain": "Architectural design"
            },
            {
                "style": "Verbal-Linguistic",
                "characteristics": ["word-based reasoning", "narrative thinking", "semantic networks"],
                "domain": "Literary analysis"
            }
        ]
        
        abstract_concepts = [
            "Causality",
            "Emergence",
            "Complexity",
            "Consciousness",
            "Justice",
            "Free will"
        ]
        
        source_style = random.choice(cognitive_styles)
        target_style = random.choice([s for s in cognitive_styles if s != source_style])
        
        return {
            "1": {
                "source_style": source_style,
                "target_style": target_style,
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "source_style": random.choice(cognitive_styles),
                "target_style": random.choice([s for s in cognitive_styles if s != source_style]),
                "concept": random.choice(abstract_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a cognitive style translation system that can translate the concept of {t['concept']} from the {t['source_style']['style']} cognitive style to the {t['target_style']['style']} cognitive style. A cognitive style refers to the preferred way an individual processes information and approaches problems.\n\nYour response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the overall structure and key components of your cognitive style translation system.\n   b) Explain how your system represents and processes abstract concepts in different cognitive styles.\n   c) Detail how your system handles the translation process between cognitive styles.\n   d) Include a high-level diagram or pseudocode illustrating your system's architecture.\n\n2. Cognitive Style Modeling (200-250 words):\n   a) Explain how your system models the {t['source_style']['style']} cognitive style, focusing on its characteristics: {', '.join(t['source_style']['characteristics'])}.\n   b) Describe how your system models the {t['target_style']['style']} cognitive style, focusing on its characteristics: {', '.join(t['target_style']['characteristics'])}.\n   c) Discuss how your system accounts for the differences and similarities between these cognitive styles.\n\n3. Concept Translation Process (200-250 words):\n   a) Detail the step-by-step process of how your system would translate the concept of {t['concept']} from the {t['source_style']['style']} style to the {t['target_style']['style']} style.\n   b) Explain how your system preserves the essential meaning of the concept while adapting it to the target cognitive style.\n   c) Provide an example of how the concept might be represented in each cognitive style.\n\n4. Application in {t['source_style']['domain']} (150-200 words):\n   a) Describe how your system could be applied to translate concepts in the domain of {t['source_style']['domain']}.\n   b) Provide a specific example of how this translation could enhance understanding or problem-solving in this domain.\n\n5. Evaluation and Validation (150-200 words):\n   a) Propose a method for evaluating the accuracy and effectiveness of your cognitive style translation system.\n   b) Discuss potential challenges in validating translations between cognitive styles and how you would address them.\n\n6. Ethical Considerations and Limitations (100-150 words):\n   a) Discuss any ethical implications of translating between cognitive styles.\n   b) Address potential limitations of your approach and suggest areas for future improvement.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be innovative in your approach while maintaining scientific plausibility and accuracy. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the translation of {t['concept']} between the {t['source_style']['style']} and {t['target_style']['style']} cognitive styles, demonstrating a clear understanding of both styles.",
            "The system architecture is well-described, includes all required components, and demonstrates feasibility.",
            f"The modeling of both {t['source_style']['style']} and {t['target_style']['style']} cognitive styles is thorough, accurate, and reflects the given characteristics.",
            "The concept translation process is clearly explained, logically sound, and demonstrates a deep understanding of cognitive style differences.",
            f"The application in {t['source_style']['domain']} is relevant, well-explained, and illustrates a practical use case.",
            "The evaluation and validation methods are appropriate, well-reasoned, and address the unique challenges of cognitive style translation.",
            "Ethical considerations and limitations are thoughtfully addressed, showing awareness of potential issues.",
            "The response shows creativity and innovation while maintaining scientific accuracy and plausibility.",
            "The response demonstrates interdisciplinary knowledge integration and technical proficiency throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
