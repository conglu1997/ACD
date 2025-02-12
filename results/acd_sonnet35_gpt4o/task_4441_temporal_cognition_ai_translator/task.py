import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_culture': 'Aymara',
                'target_culture': 'Western',
                'narrative_theme': 'personal growth'
            },
            {
                'source_culture': 'Hopi',
                'target_culture': 'Chinese',
                'narrative_theme': 'technological progress'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating temporal expressions between languages with fundamentally different concepts of time, then use it to analyze and generate culturally-specific narratives. Focus on translating between the {t['source_culture']} and {t['target_culture']} concepts of time, and apply it to a narrative about {t['narrative_theme']}.

Note: The Aymara culture conceptualizes the future as behind and the past as ahead, while the Hopi language lacks tense markers and views time as a continuous cycle rather than a linear progression.

Your response should include:

1. Temporal Cognition Framework (250-300 words):
   a) Explain how your AI system represents and processes different cultural concepts of time.
   b) Describe how it integrates linguistic, psychological, and cultural knowledge about temporal cognition.
   c) Discuss how it handles the specific temporal concepts of the {t['source_culture']} and {t['target_culture']} cultures.
   d) Explain how the system accounts for context-dependent temporal expressions.
   e) Compare and contrast your AI system's approach with how humans process and translate temporal expressions.

2. Translation System Architecture (200-250 words):
   a) Provide an overview of your AI system's architecture for temporal translation.
   b) Explain how different components interact to process and generate temporally nuanced language.
   c) Describe any novel techniques or algorithms used in your design.
   d) Discuss how your system handles ambiguity and cultural specificity in temporal expressions.

3. Cross-cultural Temporal Analysis (250-300 words):
   a) Analyze how time is typically conceptualized and expressed in {t['source_culture']} and {t['target_culture']} cultures.
   b) Identify potential misunderstandings or conflicts that could arise due to these differences.
   c) Explain how your AI system would recognize and navigate these cultural nuances.
   d) Provide examples of how the system would translate specific temporal expressions between the two cultures.
   e) Give one example of a temporal expression that is particularly challenging to translate between these cultures and explain why.

4. Narrative Generation (200-250 words):
   a) Generate a short narrative (3-4 sentences, 50-75 words) about {t['narrative_theme']} using the temporal concepts of the {t['source_culture']} culture.
   b) Translate this narrative into the temporal framework of the {t['target_culture']} culture.
   c) Explain the key differences in how time is represented in each version.
   d) Discuss how these differences might affect the interpretation of the narrative's meaning.

5. Evaluation and Ethical Considerations (150-200 words):
   a) Propose methods to evaluate the accuracy and cultural sensitivity of your system's translations.
   b) Discuss potential biases in your system and how you would address them.
   c) Analyze ethical implications of using AI for cross-cultural temporal translations.
   d) Suggest guidelines for responsible development and use of temporally-aware AI systems.

6. Cognitive Implications and Future Directions (200-250 words):
   a) Explore the potential implications of your system for our understanding of human temporal cognition.
   b) Discuss how this technology might impact fields such as cognitive science, linguistics, and artificial intelligence.
   c) Propose two potential applications of your system outside of pure language translation.
   d) Identify three major challenges or limitations of your proposed system and suggest avenues for future research.
   e) Describe how your AI system might adapt to encounter with a completely new culture with an unfamiliar concept of time.
   f) Briefly discuss how the AI system's temporal cognition capabilities might be applied to improve other AI tasks, such as long-term planning or causal reasoning.

Ensure your response demonstrates a deep understanding of temporal cognition, linguistics, cultural studies, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural accuracy.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed temporal cognition framework that addresses the {t['source_culture']} and {t['target_culture']} concepts of time, and compares the AI system's approach with human cognition.",
            "The translation system architecture is clearly explained and incorporates novel techniques for handling temporal expressions.",
            f"The cross-cultural temporal analysis provides specific examples of translating temporal expressions between {t['source_culture']} and {t['target_culture']} cultures, including one particularly challenging example.",
            f"A short narrative (50-75 words) about {t['narrative_theme']} is generated and translated, with a clear explanation of the differences in temporal representation.",
            "The response includes a thoughtful discussion of evaluation methods, ethical considerations, and potential biases in the AI system.",
            "The cognitive implications and future directions section explores the impact on related fields, proposes applications beyond language translation, and discusses adaptation to new cultural concepts of time and application to other AI tasks."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
