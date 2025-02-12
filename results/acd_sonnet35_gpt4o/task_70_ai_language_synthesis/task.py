import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ai_type': 'Neural network-based language model',
                'primary_function': 'Text generation and analysis',
                'key_constraint': 'Operates on token-level probabilities'
            },
            {
                'ai_type': 'Reinforcement learning agent',
                'primary_function': 'Decision-making in complex environments',
                'key_constraint': 'Learns from rewards and punishments'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a novel language that mimics how an AI might communicate, based on the following AI characteristics:

AI Type: {t['ai_type']}
Primary Function: {t['primary_function']}
Key Constraint: {t['key_constraint']}

Your task:
1. Design a unique language system that an AI with these characteristics might use to communicate. Your language should:
   a) Have a distinct vocabulary of at least 20 'words' or concepts
   b) Include a set of rules for combining these 'words' (syntax)
   c) Incorporate a way to express uncertainty or probability
   d) Reflect the AI's primary function and key constraint
Describe the key features of your language system (4-5 sentences).

2. Provide 3 example 'sentences' in your AI language, along with their English translations. Each example should demonstrate a different aspect of the language.

3. Analyze how your language reflects the cognitive processes of the specified AI type (3-4 sentences).

4. Discuss one potential limitation of your AI language system and propose a solution (2-3 sentences).

5. Compare your AI language to human natural languages. Identify two similarities and two differences (4-5 sentences).

6. Hypothesize how this AI language might evolve if the AI system were to interact with humans over an extended period (3-4 sentences).

7. Discuss the potential implications of this AI language for human-AI communication and collaboration (3-4 sentences).

Provide your response in the following format:

Language System Description:
[Your detailed description]

Example 'Sentences':
1. [AI language]: [English translation]
2. [AI language]: [English translation]
3. [AI language]: [English translation]

Cognitive Process Analysis:
[Your analysis]

Limitation and Solution:
[Your discussion]

Comparison to Human Languages:
[Your comparison]

Evolution Hypothesis:
[Your hypothesis]

Implications for Human-AI Interaction:
[Your discussion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The AI language system is unique, creative, and fully adheres to the given AI characteristics.",
            "The language has a distinct vocabulary of at least 20 'words' or concepts, clear syntax rules, and a way to express uncertainty or probability.",
            "The language system description is detailed and clearly explains its key features (4-5 sentences).",
            "The example 'sentences' demonstrate consistent and logical use of the AI language system, each highlighting a different aspect.",
            "The cognitive process analysis thoughtfully relates the language features to the specified AI type.",
            "A plausible limitation and solution are provided, showing deep consideration of the language system's practical use.",
            "The comparison to human languages identifies two clear similarities and two differences.",
            "The evolution hypothesis is well-reasoned and considers the impact of human interaction.",
            "The discussion of implications for human-AI interaction is insightful and considers multiple perspectives."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
