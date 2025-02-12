import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_architectures = [
            {
                "name": "Transformer",
                "key_features": ["self-attention mechanism", "parallel processing", "context-aware representations"]
            },
            {
                "name": "Recurrent Neural Network (RNN)",
                "key_features": ["sequential processing", "hidden state memory", "vanishing gradient challenge"]
            }
        ]
        return {
            "1": random.choice(ai_architectures),
            "2": random.choice(ai_architectures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system that mimics how an AI with a {t['name']} architecture might process and generate language. Your task:

1. Create a unique language system based on the {t['name']} architecture. Your language should:
   a) Have a vocabulary of at least 15 'words' or concepts
   b) Include syntax rules for combining these 'words'
   c) Incorporate a method to represent the key features of the {t['name']} architecture: {', '.join(t['key_features'])}
   d) Have a way to express uncertainty or confidence levels
Describe the key features of your language system (4-5 sentences).

2. Provide 3 example 'sentences' in your AI language, along with their English translations. Each example should demonstrate a different aspect of the language.

3. Explain how your language system reflects the processing mechanisms of the {t['name']} architecture (3-4 sentences).

4. Discuss one potential limitation of your AI language system and propose a solution (2-3 sentences).

5. Compare your AI language to human natural languages. Identify two similarities and two differences (4-5 sentences).

6. Hypothesize how this AI language might evolve if the AI system were to interact with humans over an extended period (3-4 sentences).

Provide your response in the following format:

Language System Description:
[Your detailed description]

Example 'Sentences':
1. [AI language]: [English translation]
2. [AI language]: [English translation]
3. [AI language]: [English translation]

Reflection of {t['name']} Architecture:
[Your explanation]

Limitation and Solution:
[Your discussion]

Comparison to Human Languages:
[Your comparison]

Evolution Hypothesis:
[Your hypothesis]

Ensure your language system is innovative, logically consistent with the given AI architecture, and demonstrates a deep understanding of both linguistic principles and AI concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system incorporates the key features of the {t['name']} architecture: {', '.join(t['key_features'])}",
            "The language system has a vocabulary of at least 15 'words' or concepts",
            "The language system includes clear syntax rules",
            "The language system has a way to express uncertainty or confidence levels",
            "Three example 'sentences' are provided with English translations",
            f"The explanation clearly relates the language system to the {t['name']} architecture",
            "A potential limitation and solution are discussed",
            "The comparison to human languages includes two similarities and two differences",
            "An evolution hypothesis is provided",
            "The overall response demonstrates creativity, logical consistency, and a deep understanding of linguistics and AI concepts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
