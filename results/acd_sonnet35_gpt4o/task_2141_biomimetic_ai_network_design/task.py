import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        animals = [
            {
                "animal": "octopus",
                "brain_feature": "distributed neural network",
                "cognitive_ability": "problem-solving and adaptability"
            },
            {
                "animal": "elephant",
                "brain_feature": "large, highly developed hippocampus",
                "cognitive_ability": "social cognition and memory"
            },
            {
                "animal": "bird (corvid family)",
                "brain_feature": "high neuronal density",
                "cognitive_ability": "tool use and causal reasoning"
            },
            {
                "animal": "dolphin",
                "brain_feature": "paralimbic lobe",
                "cognitive_ability": "echolocation processing and social intelligence"
            }
        ]
        return {
            "1": random.choice(animals),
            "2": random.choice(animals)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI network architecture inspired by the neural structure of a {t['animal']}'s brain, focusing on its {t['brain_feature']}. Then, analyze the potential applications and ethical implications of this biomimetic AI system, particularly in relation to {t['cognitive_ability']}. Your response should include:\n\n1. Biomimetic AI Architecture (250-300 words):\n   a) Describe the key components of your AI network architecture.\n   b) Explain how your design mimics the {t['brain_feature']} of the {t['animal']}'s brain.\n   c) Discuss any novel features or algorithms in your architecture.\n   d) Provide a high-level diagram or detailed description of your network structure.\n\n2. Implementation and Training (200-250 words):\n   a) Outline the data requirements and preprocessing steps for your AI system.\n   b) Describe the training process, including any specialized algorithms or techniques.\n   c) Discuss potential challenges in implementing this biomimetic approach and how you would address them.\n\n3. Performance Analysis (150-200 words):\n   a) Hypothesize how your biomimetic AI might perform in tasks related to {t['cognitive_ability']}.\n   b) Compare your system's potential advantages and limitations to traditional AI architectures.\n   c) Propose a specific experiment or benchmark to evaluate your biomimetic AI's performance.\n\n4. Applications and Implications (200-250 words):\n   a) Suggest two potential real-world applications for your biomimetic AI system.\n   b) Analyze how these applications might impact relevant industries or scientific fields.\n   c) Discuss any insights your system might provide into biological neural processing or cognition.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues or concerns raised by your biomimetic AI system.\n   b) Discuss how these ethical considerations might be addressed or mitigated.\n   c) Propose guidelines for the responsible development and use of biomimetic AI systems.\n\n6. Future Research Directions (100-150 words):\n   a) Suggest areas for future research in biomimetic AI, building on your proposed architecture.\n   b) Discuss potential interdisciplinary collaborations that could advance this field.\n\nEnsure your response demonstrates understanding of neuroscience, artificial intelligence, and ethical reasoning. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.\n\nFormat your response using clear headings for each section. Your total response should be between 1050-1350 words. Include a word count at the end of your response.\n\nExample: For a bird-inspired AI, you might discuss how the high neuronal density could be mimicked using densely connected layers or advanced pruning techniques in neural networks to achieve efficient information processing in a compact architecture."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response proposes a biomimetic AI architecture inspired by the {t['brain_feature']} of a {t['animal']}'s brain.",
            "The architecture design is explained and shows understanding of both AI and neuroscience principles.",
            f"The response analyzes potential applications related to {t['cognitive_ability']}.",
            "The implementation, training, and performance analysis sections demonstrate understanding of AI systems.",
            "Ethical considerations are explored and guidelines are proposed.",
            "The response adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
