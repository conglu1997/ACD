import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "psychological_theory": "Freudian psychoanalysis",
                "dream_scenario": "You're walking through a house where each room represents a different period of your life. As you move from room to room, the doors keep getting smaller."
            },
            {
                "psychological_theory": "Jungian analytical psychology",
                "dream_scenario": "You find yourself in a vast library. As you pull books from the shelves, they transform into various animals that begin to speak to you in riddles."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and interprets dreams based on linguistic patterns and psychological theories, with a focus on {t['psychological_theory']}. Then, use your system to interpret the following dream scenario:

"{t['dream_scenario']}"

Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI dream interpretation system.
   b) Explain how the system incorporates principles from {t['psychological_theory']}.
   c) Detail how the system analyzes linguistic patterns in dream narratives.

2. Linguistic Analysis Approach (200-250 words):
   a) Explain how your system identifies and categorizes key linguistic features in dream narratives.
   b) Describe any natural language processing techniques your system employs.
   c) Discuss how the system handles metaphors, symbols, and ambiguities in dream descriptions.

3. Psychological Theory Integration (200-250 words):
   a) Explain how your system applies concepts from {t['psychological_theory']} to dream interpretation.
   b) Describe how the system balances psychological theory with linguistic analysis.
   c) Discuss any challenges in translating psychological concepts into computational processes.

4. Dream Interpretation (250-300 words):
   a) Apply your AI system to interpret the given dream scenario.
   b) Provide a detailed analysis, explaining how your system arrived at its interpretation.
   c) Highlight specific linguistic patterns and psychological concepts identified by your system.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical concerns related to AI-based dream interpretation.
   b) Explain limitations of your system and areas for future improvement.
   c) Compare your AI approach to human-conducted dream analysis.

Ensure your response demonstrates a deep understanding of linguistics, psychology, and artificial intelligence. Be creative in your system design while maintaining scientific plausibility and addressing real-world constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The AI system architecture effectively incorporates linguistic analysis and psychological theory.",
            "The linguistic analysis approach is well-explained and scientifically grounded.",
            "The integration of the specified psychological theory is thorough and appropriate.",
            "The dream interpretation demonstrates creative application of the AI system.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The overall response shows strong interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
