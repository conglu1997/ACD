import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'culture': 'Nomadic desert dwellers',
                'environment': 'Harsh desert with occasional oases',
                'social_structure': 'Tribal, with emphasis on resource sharing',
                'technology_level': 'Pre-industrial, but with advanced water management'
            },
            {
                'culture': 'Advanced underwater civilization',
                'environment': 'Deep ocean with bioluminescent life forms',
                'social_structure': 'Hive-mind like, with individual specializations',
                'technology_level': 'Post-singularity, with bio-tech integration'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes hypothetical languages based on specific cultural and environmental factors. Then, use your system to create and analyze a language for the following scenario:

Culture: {t['culture']}
Environment: {t['environment']}
Social Structure: {t['social_structure']}
Technology Level: {t['technology_level']}

Your task has the following parts:

1. AI System Design (250-300 words):
   a) Describe the architecture of your AI system for language generation and analysis.
   b) Explain how it incorporates cultural, environmental, social, and technological factors.
   c) Detail the key algorithms or models used in your system.

2. Language Generation (250-300 words):
   Use your AI system to generate a hypothetical language for the given scenario. Provide:
   a) Key phonological features (e.g., sound inventory, syllable structure)
   b) Morphological characteristics (e.g., word formation rules)
   c) Syntactic structures (e.g., word order, clause structure)
   d) Semantic peculiarities (e.g., unique conceptual distinctions)
   e) Explain how these features reflect the cultural and environmental factors.

3. Sample Texts (150-200 words):
   Provide two short sample texts in the generated language:
   a) A common greeting or social interaction
   b) A description of an important cultural practice or environmental feature
   Include translations and explain how these texts demonstrate the language's unique features.

4. Linguistic Analysis (200-250 words):
   Analyze the generated language using your AI system:
   a) Identify unique linguistic features that reflect the given scenario.
   b) Explain how the language might influence or be influenced by thought patterns and worldview.
   c) Predict how this language might evolve over time given the cultural and environmental factors.

5. Comparative Analysis (150-200 words):
   Compare the generated language to existing human languages:
   a) Identify any similarities with real-world languages and explain possible reasons for these similarities.
   b) Discuss how this language differs from known human languages and why.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential applications of your AI system in fields like linguistics, anthropology, or science fiction.
   b) Address ethical considerations in using AI to model language and culture.
   c) Propose guidelines for responsible use of such technology.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and AI. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity. Your total response should be between 1150-1450 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cultural anthropology, and AI.",
            "The AI system design is well-explained and incorporates cultural, environmental, social, and technological factors.",
            "The generated language features are creative, plausible, and clearly reflect the given scenario.",
            "The sample texts effectively demonstrate the unique features of the generated language.",
            "The linguistic analysis shows insight into the relationship between language, culture, and environment.",
            "The comparative analysis with existing human languages is thoughtful and well-reasoned.",
            "The discussion of ethical and practical implications is comprehensive and demonstrates foresight."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
