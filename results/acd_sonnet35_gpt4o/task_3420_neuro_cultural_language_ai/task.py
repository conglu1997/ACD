import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "neural_pattern": "increased activity in the anterior cingulate cortex",
                "cultural_context": "a society with a circular concept of time",
                "communication_challenge": "expressing complex emotional states"
            },
            {
                "neural_pattern": "heightened connectivity between Broca's and Wernicke's areas",
                "cultural_context": "a culture that primarily communicates through color and light",
                "communication_challenge": "describing abstract scientific concepts"
            },
            {
                "neural_pattern": "enhanced activation in the fusiform gyrus",
                "cultural_context": "a civilization living in complete darkness",
                "communication_challenge": "navigating and describing spatial relationships"
            },
            {
                "neural_pattern": "increased synchronization between the prefrontal cortex and hippocampus",
                "cultural_context": "a society with collective consciousness",
                "communication_challenge": "expressing individual thoughts and experiences"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can learn and generate new languages based on neural patterns and cultural contexts, then use it to create a hypothetical language for the following scenario:

Neural Pattern: {t['neural_pattern']}
Cultural Context: {t['cultural_context']}
Communication Challenge: {t['communication_challenge']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for language generation.
   b) Explain how your system integrates neurolinguistic principles, cultural anthropology, and machine learning.
   c) Detail how the system processes neural data and cultural information to generate language structures.
   d) Propose a novel algorithm for mapping neural patterns to linguistic features.

2. Language Learning Mechanism (250-300 words):
   a) Explain how your AI system learns from existing languages and neural patterns.
   b) Describe the process of extracting cultural context and incorporating it into language generation.
   c) Discuss how your system ensures the generated languages are both neurologically plausible and culturally appropriate.

3. Hypothetical Language Design (300-350 words):
   a) Present the key features of the language you've generated for the given scenario.
   b) Explain how this language reflects the specified neural pattern and cultural context.
   c) Describe how the language addresses the given communication challenge.
   d) Provide examples of unique linguistic structures or elements in your generated language.

4. Linguistic Analysis (200-250 words):
   a) Analyze the phonology, morphology, syntax, and semantics of your generated language.
   b) Compare and contrast your language with existing human languages.
   c) Discuss how your language might influence or be influenced by cognitive processes.

5. Practical Applications and Implications (200-250 words):
   a) Explore potential applications of your AI system in fields such as linguistics, anthropology, or cognitive science.
   b) Discuss how this technology might enhance our understanding of the relationship between brain, culture, and language.
   c) Consider potential impacts on language preservation, evolution, and cross-cultural communication.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to AI-generated languages and their use.
   b) Discuss the implications for linguistic diversity and cultural preservation.
   c) Propose guidelines for the responsible development and use of neurocultural language AI systems.

Ensure your response demonstrates a deep understanding of neurolinguistics, cultural anthropology, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system architecture effectively integrates neurolinguistics, cultural anthropology, and machine learning, with a focus on {t['neural_pattern']} and {t['cultural_context']}.",
            "The language learning mechanism is well-explained and scientifically plausible.",
            f"The hypothetical language design convincingly addresses the communication challenge of {t['communication_challenge']} while reflecting the given neural pattern and cultural context.",
            "The linguistic analysis demonstrates a deep understanding of language structures and their relationship to cognitive processes.",
            "Practical applications and ethical considerations are thoroughly addressed.",
            "The response includes all required sections and adheres to the specified word count.",
            "The proposed novel algorithm for mapping neural patterns to linguistic features is innovative and well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
