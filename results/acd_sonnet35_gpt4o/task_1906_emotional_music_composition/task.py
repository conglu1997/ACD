import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "joy", "musical_elements": "major key, upbeat tempo, bright timbre"},
            {"emotion": "sadness", "musical_elements": "minor key, slow tempo, mellow timbre"},
            {"emotion": "anger", "musical_elements": "dissonant harmonies, intense rhythm, harsh timbre"},
            {"emotion": "fear", "musical_elements": "unstable tonality, irregular rhythm, dark timbre"},
            {"emotion": "serenity", "musical_elements": "consonant harmonies, gentle rhythm, soft timbre"}
        ]
        return {
            "1": random.choice(emotions),
            "2": random.choice(emotions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an algorithm to compose music that expresses the emotion of {t['emotion']}. Your task has four parts:\n\n1. Algorithm Design (250-300 words):\n   a) Describe your algorithm's approach to generating music that expresses {t['emotion']}.\n   b) Explain how your algorithm incorporates the following musical elements: {t['musical_elements']}.\n   c) Discuss any additional musical techniques or structures your algorithm uses to convey the emotion.\n\n2. Implementation Details (200-250 words):\n   a) Provide pseudocode for the core components of your algorithm.\n   b) Explain any key data structures or musical representations used.\n   c) Describe how your algorithm handles musical coherence and structure.\n\n3. Emotional Expression Analysis (200-250 words):\n   a) Analyze how specific musical choices in your algorithm contribute to expressing {t['emotion']}.\n   b) Discuss potential challenges in algorithmically generating emotionally expressive music.\n   c) Propose a method to evaluate the emotional effectiveness of the composed music.\n\n4. Computational Creativity and Artistic Implications (200-250 words):\n   a) Discuss the role of AI in music composition and its potential impact on human creativity.\n   b) Explore the question: Can AI-generated music be considered truly emotionally expressive?\n   c) Propose an approach for effective human-AI collaboration in emotional music composition.\n\nEnsure your response demonstrates a deep understanding of music theory, algorithmic composition, and the relationship between music and emotions. Be creative in your approach while maintaining technical feasibility. Use appropriate musical and technical terminology, providing explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 850-1050 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm design effectively incorporates the specified musical elements for expressing {t['emotion']}.",
            "The implementation details are technically sound and demonstrate a clear understanding of algorithmic music composition.",
            f"The emotional expression analysis provides insightful connections between musical choices and the emotion of {t['emotion']}.",
            "The discussion on computational creativity and artistic implications shows depth of thought and consideration of multiple perspectives.",
            "The response demonstrates a strong grasp of music theory, emotional interpretation, and algorithmic thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
