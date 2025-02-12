import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "Working Memory Limitations",
                "ai_concept": "Attention Mechanisms",
                "interaction_context": "Emergency Response Coordination"
            },
            {
                "cognitive_principle": "Chunking and Pattern Recognition",
                "ai_concept": "Hierarchical Learning",
                "interaction_context": "Educational Tutoring"
            },
            {
                "cognitive_principle": "Dual-Process Theory",
                "ai_concept": "Multi-Agent Systems",
                "interaction_context": "Collaborative Problem Solving"
            },
            {
                "cognitive_principle": "Embodied Cognition",
                "ai_concept": "Sensorimotor Integration in Robotics",
                "interaction_context": "Human-Robot Physical Collaboration"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an artificial language (conlang) optimized for AI-human interaction that incorporates the cognitive science principle of {t['cognitive_principle']} and the AI concept of {t['ai_concept']}. The language should be tailored for the interaction context of {t['interaction_context']}. Your response should include:\n\n1. Language Overview (100-150 words):\n   a) Briefly describe the key features and structure of your conlang.\n   b) Explain how it incorporates the specified cognitive principle and AI concept.\n   c) Discuss how it is optimized for the given interaction context.\n   d) Provide a brief rationale for your design choices.\n\n2. Phonology and Orthography (100-150 words):\n   a) Describe the sound system of your language.\n   b) Explain the writing system or symbolic representation.\n   c) Justify your choices in relation to the cognitive principle, AI concept, and interaction context.\n   d) Provide a brief rationale for your design choices.\n\n3. Grammar and Syntax (150-200 words):\n   a) Outline the basic grammatical structures of your conlang.\n   b) Explain how these structures reflect the cognitive principle and AI concept.\n   c) Provide examples of how the grammar facilitates efficient AI-human interaction in the given context.\n   d) Provide a brief rationale for your design choices.\n\n4. Lexicon and Semantics (100-150 words):\n   a) Describe the principles guiding vocabulary creation in your conlang.\n   b) Explain how word formation and meaning are influenced by the cognitive principle and AI concept.\n   c) Provide 3-5 example words or phrases with their meanings, relevant to the interaction context.\n   d) Provide a brief rationale for your design choices.\n\n5. Pragmatics and Discourse (100-150 words):\n   a) Explain how your conlang handles contextual information and pragmatic aspects of communication.\n   b) Describe any special discourse features that enhance AI-human interaction.\n   c) Provide an example dialogue snippet in your conlang with translation and explanation.\n   d) Provide a brief rationale for your design choices.\n\n6. Cognitive Load and Processing (100-150 words):\n   a) Analyze how your conlang minimizes cognitive load for human users.\n   b) Explain how it optimizes for AI processing and understanding.\n   c) Discuss any potential challenges or trade-offs in your design.\n   d) Provide a brief rationale for your design choices.\n\n7. Practical Application (100-150 words):\n   a) Describe how your conlang could be implemented in real-world AI systems for the given interaction context.\n   b) Discuss potential benefits and limitations of using your conlang in practice.\n   c) Suggest a method for teaching or onboarding humans to use this language efficiently.\n   d) Provide a brief rationale for your design choices.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative and innovative in your language design while maintaining scientific plausibility and practical applicability. Your total response should be between 750-1100 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design clearly incorporates the specified cognitive principle and AI concept",
            "The language features are well-suited for the given interaction context",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and AI",
            "The conlang design is creative, innovative, and scientifically plausible",
            "All required sections are present and adequately addressed",
            "The language design effectively balances human usability and AI optimization",
            "The response provides clear rationales for design choices in each section",
            "The conlang design shows originality and is not derivative of existing languages or systems",
            "The total word count falls within the specified range of 750-1100 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
