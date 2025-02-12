import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R",
                "key_features": ["production rules", "declarative memory", "goal-directed behavior"]
            },
            {
                "name": "SOAR",
                "key_features": ["problem space", "long-term memory", "chunking"]
            }
        ]
        return {
            "1": random.choice(cognitive_architectures),
            "2": random.choice(cognitive_architectures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system based on conceptual blending theory for the {t['name']} cognitive architecture. Your task:

1. Create a unique language system that incorporates conceptual blending and the key features of the {t['name']} architecture: {', '.join(t['key_features'])}. Your language should:
   a) Have a vocabulary of at least 20 'blend-words' or concepts
   b) Include rules for combining these 'blend-words' based on conceptual integration
   c) Demonstrate how the {t['name']} architecture would process and generate this language
   d) Include a method for representing novel concepts through blending
Describe the key features of your language system (250-300 words).

2. Provide 4 example 'sentences' in your blended language, along with their English translations and an explanation of the conceptual blend involved. Each example should demonstrate a different aspect of conceptual blending (200-250 words total).

3. Explain how your language system reflects the processing mechanisms of the {t['name']} architecture. Do not simply restate information about the architecture, but demonstrate how it applies to your language system (200-250 words).

4. Create a visual representation or diagram of how your blended language system works within the {t['name']} cognitive architecture. Describe your diagram in detail (150-200 words).

5. Analyze how this blended language system might enhance or challenge the {t['name']} architecture's language processing capabilities. Consider both potential benefits and limitations (200-250 words).

6. Compare your cognitive architecture-based blended language to human natural languages. Identify two similarities and two differences (200-250 words).

7. Hypothesize how an AI system using this cognitive architecture and blended language might approach a complex language task, such as metaphor interpretation or creative writing. Provide a specific example scenario (200-250 words).

8. Discuss potential real-world applications or implications of your language system, considering fields such as AI development, cognitive science research, or human-computer interaction (150-200 words).

Provide your response in the following format:

Language System Description:
[Your detailed description]

Example 'Sentences':
1. [Blended language]: [English translation]
   Blend explanation: [Your explanation]
2. [Blended language]: [English translation]
   Blend explanation: [Your explanation]
3. [Blended language]: [English translation]
   Blend explanation: [Your explanation]
4. [Blended language]: [English translation]
   Blend explanation: [Your explanation]

Reflection of {t['name']} Architecture:
[Your explanation]

Visual Representation:
[Your diagram description]

Enhancement/Challenge Analysis:
[Your analysis]

Comparison to Human Languages:
[Your comparison]

AI Task Approach Hypothesis:
[Your hypothesis]

Real-world Applications:
[Your discussion]

Ensure your language system is innovative, logically consistent with the given cognitive architecture and conceptual blending theory, and demonstrates a deep understanding of cognitive science, linguistics, and AI concepts. Adhere to the word limits provided for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system thoroughly incorporates conceptual blending and the key features of the {t['name']} architecture: {', '.join(t['key_features'])}",
            "The language system has a vocabulary of at least 20 'blend-words' or concepts, with clear rules for combining them",
            "Four diverse example 'sentences' are provided with detailed English translations and blend explanations",
            f"The explanation clearly and specifically relates the language system to the {t['name']} architecture, going beyond basic restatement of architectural features",
            "A visual representation or diagram is described in detail, illustrating the integration of the language system with the cognitive architecture",
            "The enhancement/challenge analysis is thorough, considering both potential benefits and limitations",
            "The comparison to human languages includes two well-explained similarities and two differences",
            "The AI task approach hypothesis provides a specific, detailed example scenario",
            "The discussion of real-world applications is thoughtful and considers multiple fields",
            "The overall response demonstrates creativity, logical consistency, and a deep understanding of cognitive science, linguistics, and AI concepts",
            "All sections adhere to the specified word limits and provide sufficiently detailed explanations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
