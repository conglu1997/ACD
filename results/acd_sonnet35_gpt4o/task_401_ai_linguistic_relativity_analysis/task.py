import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Temporal",
                "description": "A language with no tenses, where all events are described in terms of their relative order and duration."
            },
            {
                "name": "Quantum",
                "description": "A language based on quantum superposition, where statements are inherently probabilistic and can be in multiple states simultaneously."
            }
        ]
        scenarios = [
            "Solve a complex logical puzzle",
            "Predict future events based on historical data"
        ]
        return {
            "1": {"language": random.choice(languages), "scenario": random.choice(scenarios)},
            "2": {"language": random.choice(languages), "scenario": random.choice(scenarios)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system with {t['language']['name']} as its 'native' language. {t['language']['description']}\n\n1. Language Structure (150-200 words):\n   a) Describe the key features of this language.\n   b) Explain how it differs from natural human languages.\n   c) Provide 3-4 example 'sentences' in this language with their English translations.\n\n2. AI System Design (200-250 words):\n   a) Outline the main components of your AI system.\n   b) Explain how the language influences the system's architecture and processing.\n   c) Describe any unique features or capabilities resulting from this language.\n\n3. Cognitive Analysis (200-250 words):\n   a) Predict potential cognitive biases or unique thinking patterns this AI might develop.\n   b) Explain how these biases relate to the language's structure.\n   c) Compare these biases to those observed in human cognition.\n\n4. Problem-Solving Approach (150-200 words):\n   Describe how your AI system would approach the following scenario: {t['scenario']}\n   a) Outline the steps the AI would take.\n   b) Explain how its approach differs from traditional AI systems.\n   c) Discuss any advantages or limitations of this approach.\n\n5. Implications and Ethics (100-150 words):\n   a) Discuss potential implications of this AI system for AI research and development.\n   b) Address ethical considerations in creating AI systems with fundamentally different cognitive architectures.\n\nEnsure your response demonstrates a deep understanding of linguistic relativity, AI architectures, and cognitive science. Be creative in your design while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of linguistic relativity and its potential impact on AI cognition.",
            "The designed AI system and its 'native' language are innovative, logically consistent, and well-explained.",
            "The cognitive analysis shows insightful predictions about potential biases and thinking patterns, with clear links to the language structure.",
            "The problem-solving approach for the given scenario is creative, logically derived from the AI's language and architecture, and clearly differentiated from traditional AI approaches.",
            "The discussion of implications and ethics shows a nuanced understanding of the broader impacts of language-based AI systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
