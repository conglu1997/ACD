import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'initial_alphabet': 'Binary (0, 1)',
                'cognitive_constraint': 'Working memory capacity',
                'communication_goal': 'Describing spatial relationships'
            },
            {
                'initial_alphabet': 'Quaternary (A, C, G, T)',
                'cognitive_constraint': 'Pattern recognition ability',
                'communication_goal': 'Expressing emotional states'
            },
            {
                'initial_alphabet': 'Octal (0-7)',
                'cognitive_constraint': 'Attention span',
                'communication_goal': 'Conveying abstract concepts'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and simulate an evolving language system based on information-theoretic principles, then analyze its development and implications for cognitive linguistics. Use the following specifications:

Initial Alphabet: {t['initial_alphabet']}
Cognitive Constraint: {t['cognitive_constraint']}
Communication Goal: {t['communication_goal']}

Your response should include the following sections:

1. Language System Design (300-350 words):
   a) Describe the initial state of your language system, including its alphabet and basic rules.
   b) Explain how you incorporate information-theoretic principles (e.g., entropy, mutual information) into the language's evolution.
   c) Detail how the specified cognitive constraint influences the language's development.
   d) Discuss how the communication goal shapes the language's features.

2. Evolution Simulation (250-300 words):
   a) Outline the algorithm or process you would use to simulate the language's evolution.
   b) Describe key stages or milestones in the language's development over time.
   c) Explain how you would measure and optimize the language's efficiency in terms of information theory.
   d) Provide a simple pseudocode snippet (10-15 lines) illustrating a crucial part of your simulation process.

3. Linguistic Analysis (250-300 words):
   a) Analyze the evolved language's structure, comparing it to natural human languages.
   b) Discuss any emergent properties or unexpected features in the evolved language.
   c) Explain how the language balances efficiency (in terms of information theory) with expressiveness.
   d) Provide 2-3 example 'sentences' or expressions in the evolved language, with explanations.

4. Cognitive Implications (200-250 words):
   a) Discuss how the evolved language reflects or challenges current theories in cognitive linguistics.
   b) Analyze the potential cognitive load of using this language, considering the specified constraint.
   c) Hypothesize how using this language might affect thought processes or problem-solving approaches.

5. Practical Applications and Future Directions (200-250 words):
   a) Propose two potential real-world applications of your evolving language system or the insights gained from it.
   b) Discuss how this approach could be extended to study other aspects of language or cognition.
   c) Suggest an experiment to test a hypothesis derived from your language system.

Ensure your response demonstrates a deep understanding of information theory, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of information theory, linguistics, and cognitive science.",
            "The language system design effectively incorporates information-theoretic principles, the specified cognitive constraint, and communication goal.",
            "The evolution simulation is clearly explained and includes a relevant pseudocode snippet.",
            "The linguistic analysis provides insightful comparisons to natural languages and includes example 'sentences' from the evolved language.",
            "The cognitive implications section offers thoughtful connections to cognitive linguistics theories.",
            "Practical applications and future directions are innovative and well-reasoned.",
            "The response is well-structured, using appropriate technical terminology and clear explanations.",
            "The proposed language system and analysis are creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
