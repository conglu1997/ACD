import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Chinese', 'Russian', 'Arabic', 'Spanish']
        tasks = [
            {
                'culture1': random.choice(cultures),
                'culture2': random.choice([c for c in cultures if c != cultures[0]])
            },
            {
                'culture1': random.choice(cultures),
                'culture2': random.choice([c for c in cultures if c != cultures[2]])
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a poem that incorporates idioms from {t['culture1']} and {t['culture2']} cultures, and then analyze its cultural significance. Follow these steps:

1. Research and select two idioms from {t['culture1']} culture and two idioms from {t['culture2']} culture. Briefly explain the meaning and origin of each idiom (30-40 words per idiom).

2. Write a poem (12-16 lines) that creatively incorporates all four idioms. The poem should have a coherent theme or narrative that connects the idioms in a meaningful way.

3. Analyze your poem (200-250 words):
   a) Explain how you integrated the idioms into the poem's structure and theme.
   b) Discuss any challenges you faced in combining idioms from different cultures.
   c) Explore how the juxtaposition of these idioms creates new meanings or perspectives.

4. Cultural reflection (150-200 words):
   a) Discuss how your poem reflects or comments on the cultural values or worldviews of the two chosen cultures.
   b) Consider any potential misunderstandings or misinterpretations that might arise from combining idioms across cultures.
   c) Reflect on how this exercise in cross-cultural poetry might contribute to intercultural understanding.

Ensure your response demonstrates creativity, cultural sensitivity, and a deep understanding of idiomatic expressions and their cultural contexts.

Please format your response as follows:

1. Idiom Explanations
[Your explanations here]

2. Poem
[Your poem here]

3. Analysis
[Your analysis here]

4. Cultural Reflection
[Your reflection here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes explanations of four idioms (two from each specified culture) with their meanings and origins.",
            "The poem creatively incorporates all four idioms while maintaining a coherent theme or narrative.",
            "The analysis effectively explains the integration of idioms, discusses challenges, and explores new meanings created by their juxtaposition.",
            "The cultural reflection demonstrates insight into the cultural values of the chosen cultures and considers potential misunderstandings.",
            "The overall response shows creativity, cultural sensitivity, and a deep understanding of idiomatic expressions and their cultural contexts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
