import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neurolinguistic_principles = [
            "Phonological processing",
            "Semantic networks",
            "Syntactic structures",
            "Pragmatic context"
        ]
        emotional_states = [
            "Ambivalence",
            "Catharsis",
            "Nostalgia",
            "Sublime awe"
        ]
        return {
            "1": {"principle": random.choice(neurolinguistic_principles), "emotion": random.choice(emotional_states)},
            "2": {"principle": random.choice(neurolinguistic_principles), "emotion": random.choice(emotional_states)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that synthesizes a new form of musical language based on the neurolinguistic principle of {t['principle']}, then use it to compose and analyze a piece that expresses the complex emotional state of {t['emotion']}. Your response should include:\n\n1. Neuro-Musical Language Design (300-350 words):\n   a) Explain how you translate {t['principle']} into musical parameters.\n   b) Describe the core elements of your musical language (e.g., tonal system, rhythmic structures, timbral palette).\n   c) Discuss how your language incorporates neurolinguistic features to enhance emotional expression.\n   d) Provide an example of how a specific neurolinguistic concept maps to a musical element in your system.\n\n2. AI System Architecture (250-300 words):\n   a) Outline the key components of your AI system for generating and analyzing this musical language.\n   b) Explain how your system integrates neurolinguistic principles, music theory, and emotional intelligence.\n   c) Describe any novel algorithms or approaches used in your AI design.\n\n3. Composition Process (200-250 words):\n   a) Detail how your AI system composes a piece to express {t['emotion']}.\n   b) Explain how the composition process reflects both the neurolinguistic principle and the target emotional state.\n   c) Discuss any challenges in mapping complex emotions to your musical language.\n\n4. Musical Analysis (200-250 words):\n   a) Provide a detailed analysis of the composed piece.\n   b) Explain how specific elements of the composition reflect {t['emotion']}.\n   c) Discuss how the neurolinguistic basis of the language enhances emotional expression.\n\n5. Cognitive and Emotional Impact (150-200 words):\n   a) Hypothesize about the potential cognitive and emotional effects of your musical language on listeners.\n   b) Discuss how this system might contribute to our understanding of music perception and emotional processing.\n\n6. Ethical Considerations and Future Applications (150-200 words):\n   a) Identify potential ethical concerns in developing AI systems for emotional musical expression.\n   b) Propose guidelines for responsible use of neuro-musical AI technologies.\n   c) Suggest potential applications in fields such as music therapy, cognitive science, or human-computer interaction.\n\nEnsure your response demonstrates a deep understanding of neurolinguistics, music theory, artificial intelligence, and emotional psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nYour total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the specified neurolinguistic principle ({t['principle']}) and its application to music.",
            f"The musical language system effectively translates neurolinguistic concepts into musical parameters.",
            f"The AI system architecture is well-designed and integrates neurolinguistics, music theory, and emotional intelligence.",
            f"The composed piece successfully expresses the complex emotional state of {t['emotion']}.",
            "The analysis shows a deep understanding of the connections between neurolinguistics, music, and emotion.",
            "The response addresses ethical considerations and proposes plausible future applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
