import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'environment': 'Desert planet with two moons',
                'cultural_focus': 'Resource management and time-keeping',
                'linguistic_constraint': 'No words longer than five phonemes'
            },
            {
                'environment': 'Subterranean civilization in vast cave network',
                'cultural_focus': 'Echolocation and vibration-based communication',
                'linguistic_constraint': 'Tonal language with no written form'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze the evolution of an artificial language within a simulated culture, considering the following parameters:

Environment: {t['environment']}
Cultural Focus: {t['cultural_focus']}
Linguistic Constraint: {t['linguistic_constraint']}

Your task involves the following steps:

1. Initial Language Design (250-300 words):
   a) Create the basic structure and features of your artificial language.
   b) Explain how the language reflects the given environment and cultural focus.
   c) Describe how you've incorporated the linguistic constraint.
   d) Provide examples of 5-10 core vocabulary items or phrases with their meanings.

2. Cultural Context (200-250 words):
   a) Describe the key aspects of the culture using this language.
   b) Explain how the environment has shaped cultural practices and beliefs.
   c) Discuss how the cultural focus influences daily life and social structures.

3. Language Evolution Simulation (250-300 words):
   a) Propose a 500-year timeline for your language's evolution.
   b) Describe 3-4 major linguistic changes that occur over this period.
   c) Explain the cultural, environmental, or external factors driving these changes.
   d) Provide examples of how specific words or grammatical structures change.

4. Comparative Analysis (200-250 words):
   a) Compare your artificial language's evolution to known patterns in natural language evolution.
   b) Discuss any unique features of your language's evolution due to the specific cultural and environmental factors.
   c) Analyze how the initial linguistic constraint influenced the language's development over time.

5. AI Interaction Scenario (150-200 words):
   a) Describe a hypothetical scenario where an AI system interacts with speakers of your evolved language.
   b) Discuss potential challenges the AI might face in understanding cultural contexts or linguistic nuances.
   c) Propose a method for training an AI to better comprehend and communicate in this language and culture.

Ensure your response demonstrates creativity in language and culture design, a deep understanding of linguistic and cultural evolution, and insightful analysis of the interplay between language, culture, and environment. Use appropriate terminology from linguistics and anthropology, and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creativity and coherence in designing an artificial language and culture.",
            "The language design clearly reflects the given environment, cultural focus, and linguistic constraint.",
            "The cultural context is well-developed and logically connected to the language and environment.",
            "The language evolution simulation is plausible and shows a deep understanding of linguistic change.",
            "The comparative analysis reveals insights into both natural and artificial language evolution.",
            "The AI interaction scenario thoughtfully explores potential challenges and solutions.",
            "The overall response showcases interdisciplinary knowledge in linguistics, anthropology, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
