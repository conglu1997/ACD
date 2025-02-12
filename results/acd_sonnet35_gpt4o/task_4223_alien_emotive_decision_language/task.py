import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "alien_trait": "Hive mind",
                "emotion_base": "Electromagnetic fluctuations",
                "ethical_dilemma": "Resource allocation during interstellar migration"
            },
            {
                "alien_trait": "Non-linear time perception",
                "emotion_base": "Quantum entanglement states",
                "ethical_dilemma": "First contact protocol with a less advanced civilization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a language system for a hypothetical alien species with the trait of {t['alien_trait']}, where emotions are based on {t['emotion_base']}. Then, use this language to approach the ethical dilemma of {t['ethical_dilemma']}. Your response should include:\n\n1. Alien Species and Language Design (300-350 words):\n   a) Describe the key characteristics of your alien species, focusing on their cognitive processes.\n   b) Explain how their language system integrates emotion and decision-making.\n   c) Provide examples of how {t['emotion_base']} form the basis for emotional expression in their language.\n   d) Discuss how {t['alien_trait']} influences their language structure and use.\n   e) Ensure your language design includes at least one feature that is not present in any known human language.\n\n2. Linguistic Features (250-300 words):\n   a) Detail the unique features of your alien language (e.g., syntax, morphology, phonology).\n   b) Explain how emotion and decision-making are grammatically encoded.\n   c) Provide a small lexicon (5-10 words/phrases) with translations and explanations.\n   d) Describe any non-verbal components of the language, if applicable.\n\n3. Decision-Making Process (200-250 words):\n   a) Describe how your aliens use their language in their decision-making process.\n   b) Explain the role of emotions in their logical reasoning.\n   c) Compare this process to human decision-making models.\n   d) Discuss any potential biases or limitations in their decision-making process.\n\n4. Ethical Dilemma Analysis (250-300 words):\n   a) Present the ethical dilemma of {t['ethical_dilemma']} in terms understandable to your alien species.\n   b) Demonstrate how they would discuss and analyze this dilemma using their language.\n   c) Provide a sample dialogue or monologue (3-5 sentences) in your alien language with translation and explanation of the emotional-decisional components.\n\n5. Problem-Solving Approach (200-250 words):\n   a) Explain how your aliens would approach solving the ethical dilemma.\n   b) Discuss how their language and emotion-based decision-making influence their solution.\n   c) Compare their approach to potential human approaches to the same dilemma.\n   d) Address any potential challenges or limitations in applying their language system to this ethical problem.\n\n6. Implications and Reflections (150-200 words):\n   a) Discuss what this alien language reveals about the nature of language, emotion, and ethics.\n   b) Reflect on how this exercise could inform human understanding of cognitive processes and decision-making.\n   c) Propose potential applications or insights for AI development or cognitive science research.\n   d) Discuss the limitations of your proposed alien language system and areas for future exploration.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and ethics.",
            "The alien language system is innovative, coherent, and plausibly integrates emotion and decision-making.",
            "The language design includes at least one feature not present in any known human language.",
            "The ethical dilemma is analyzed thoughtfully using the alien language and cognitive framework.",
            "The sample dialogue/monologue effectively demonstrates the alien language in use.",
            "The implications and reflections show insightful connections to human cognition and AI development.",
            "The response addresses limitations and challenges of the proposed alien language system.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
