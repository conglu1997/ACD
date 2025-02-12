import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "music composition",
            "architectural design",
            "scientific hypothesis generation",
            "product innovation",
            "literary metaphor creation",
            "visual art conceptualization"
        ]
        blend_types = [
            "cross-domain integration",
            "conceptual opposition",
            "analogy-based fusion",
            "emergent structure elaboration"
        ]
        return {
            "1": {"domain": random.choice(domains), "blend_type": random.choice(blend_types)},
            "2": {"domain": random.choice(domains), "blend_type": random.choice(blend_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that implements conceptual blending theory to generate novel ideas in the domain of {t['domain']}, focusing on the blend type of {t['blend_type']}. Then, analyze its potential impact on human creativity and problem-solving. Your response should include the following sections:\n\n1. Conceptual Blending AI System Design (300-350 words):\n   a) Describe the architecture of your AI system, including its key components and how they interact.\n   b) Explain how your system implements conceptual blending theory, particularly for {t['blend_type']}.\n   c) Detail how your system would generate novel ideas in the domain of {t['domain']}.\n   d) Provide a high-level pseudocode or flowchart illustrating a key process in your system.\n\n2. Cognitive Model Integration (250-300 words):\n   a) Analyze how conceptual blending theory influences the AI's approach to idea generation.\n   b) Discuss how this integration might lead to more 'human-like' creativity or problem-solving.\n   c) Explain any challenges in implementing conceptual blending in an AI system and how you addressed them.\n\n3. Creative Output Analysis (250-300 words):\n   a) Describe a sample novel idea that your AI system might generate in {t['domain']}, highlighting its unique features.\n   b) Analyze how the AI's output might differ from human-generated ideas in the same domain.\n   c) Discuss how the system's handling of {t['blend_type']} contributes to the idea's novelty or usefulness.\n\n4. Human-AI Collaboration (200-250 words):\n   a) Propose a method for humans to collaborate with your AI system in {t['domain']}.\n   b) Discuss potential benefits and challenges of this collaboration.\n   c) Explain how this collaboration might enhance human creativity and problem-solving abilities.\n\n5. Ethical Implications (200-250 words):\n   a) Analyze the potential impact of your AI system on human creativity and traditional approaches in {t['domain']}.\n   b) Discuss any ethical concerns related to AI-generated ideas and how they might be addressed.\n   c) Consider the long-term implications of widespread use of conceptual blending AI in creative and problem-solving tasks.\n\n6. Evaluation and Future Directions (200-250 words):\n   a) Propose a method to evaluate the creativity and usefulness of your AI system's outputs.\n   b) Suggest two potential improvements or extensions to your system for future development.\n   c) Discuss how your system might adapt to or incorporate other cognitive theories of creativity.\n\nEnsure your response demonstrates a deep understanding of conceptual blending theory, cognitive science, artificial intelligence, and the specific domain of application. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your system design while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section and use numbered or bulleted lists where appropriate. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of conceptual blending theory and its application in AI for {t['domain']}.",
            f"The AI system design effectively incorporates {t['blend_type']} and addresses idea generation in {t['domain']}.",
            "The design is innovative and scientifically plausible.",
            "A high-level pseudocode or flowchart illustrating a key process in the system is included.",
            "The creative output analysis and human-AI collaboration sections are insightful and well-reasoned.",
            "Ethical implications and future directions are thoughtfully addressed.",
            "The response follows the specified format with clearly labeled sections and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
