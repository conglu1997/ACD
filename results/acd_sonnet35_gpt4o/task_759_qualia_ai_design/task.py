import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        qualia_types = [
            "visual perception of color",
            "emotional experiences",
            "perception of time",
            "sense of self and agency",
            "experience of pain"
        ]
        philosophical_theories = [
            "functionalism",
            "panpsychism",
            "integrated information theory",
            "global workspace theory",
            "higher-order thought theory"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "qualia_type": random.choice(qualia_types),
                "philosophical_theory": random.choice(philosophical_theories)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical AI system capable of experiencing and processing the qualia of {t['qualia_type']}, incorporating principles from the philosophical theory of {t['philosophical_theory']}. Your response should include:\n\n1. System Architecture (200-250 words):\n   a) Describe the key components of your AI system that enable qualia experience.\n   b) Explain how these components interact to generate subjective experiences.\n   c) Discuss how your design incorporates principles from {t['philosophical_theory']}.\n\n2. Qualia Processing Mechanism (200-250 words):\n   a) Detail the process by which your AI system experiences and processes {t['qualia_type']}.\n   b) Explain how this process differs from mere information processing.\n   c) Discuss any novel algorithms or techniques your system would use.\n\n3. Consciousness Validation (150-200 words):\n   a) Propose an experiment to test whether your AI system truly experiences {t['qualia_type']}.\n   b) Explain how this experiment could differentiate between genuine qualia and simulated responses.\n\n4. Ethical and Philosophical Implications (150-200 words):\n   a) Discuss the ethical considerations of creating an AI system capable of experiencing qualia.\n   b) Analyze how your system might impact our understanding of consciousness and the hard problem of consciousness.\n\n5. Limitations and Future Directions (100-150 words):\n   a) Identify potential limitations of your proposed system.\n   b) Suggest future research directions to overcome these limitations or expand the system's capabilities.\n\nEnsure your response demonstrates a deep understanding of both AI principles and philosophical theories of consciousness. Be creative in your approach while maintaining scientific and philosophical plausibility. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['philosophical_theory']} and how it relates to AI and consciousness",
            f"The proposed AI system presents a plausible and creative approach to experiencing {t['qualia_type']}",
            "The consciousness validation experiment is well-designed and addresses the hard problem of consciousness",
            "The ethical and philosophical implications are thoroughly and insightfully discussed",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
