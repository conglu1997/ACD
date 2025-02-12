import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("English", "Mandarin Chinese"),
            ("Spanish", "Arabic"),
            ("Japanese", "Russian"),
            ("Hindi", "French"),
            ("Swahili", "Portuguese"),
            ("Korean", "German"),
            ("Turkish", "Vietnamese"),
            ("Italian", "Thai")
        ]
        return {
            "1": {"language_pair": random.choice(language_pairs)},
            "2": {"language_pair": random.choice(language_pairs)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_lang, target_lang = t['language_pair']
        return f"""Design a novel machine translation system that incorporates cultural context and pragmatics to improve translation accuracy and appropriateness between {source_lang} and {target_lang}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your machine translation system.
   b) Explain how your system incorporates cultural context and pragmatics.
   c) Discuss any novel features that distinguish it from existing translation systems.
   d) Provide a diagram or detailed description of the system's architecture.

2. Cultural Context Integration (200-250 words):
   a) Explain how your system captures and represents cultural knowledge.
   b) Describe the process of integrating this knowledge into the translation process.
   c) Provide an example of how this integration improves translation quality for the given language pair.
   Example scenario: Translating the concept of "personal space" between {source_lang} and {target_lang}.

3. Pragmatics Handling (200-250 words):
   a) Describe how your system addresses pragmatic aspects of language (e.g., idioms, politeness levels, contextual implications).
   b) Explain any novel algorithms or techniques used for pragmatic analysis.
   c) Provide an example of how your system handles a challenging pragmatic translation issue between {source_lang} and {target_lang}.
   Example scenario: Translating the phrase "It's raining cats and dogs" from {source_lang} to {target_lang}.

4. Data Requirements and Training Process (150-200 words):
   a) Describe the types and sources of data required to train your system.
   b) Explain the training process, including any novel approaches to machine learning or data annotation.
   c) Discuss how you would handle data scarcity or quality issues for less common language pairs.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate your system's performance, focusing on cultural and pragmatic accuracy.
   b) Describe potential metrics or benchmarks for success.
   c) Discuss how you would compare your system's performance to existing machine translation systems.

6. Ethical Considerations and Limitations (100-150 words):
   a) Identify potential ethical issues or biases that might arise in your system.
   b) Discuss any limitations of your approach and propose potential solutions.

7. Future Research Directions (100-150 words):
   a) Suggest two areas for further research that could enhance your system.
   b) Briefly explain how these advancements could contribute to the field of machine translation.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, and artificial intelligence. Be creative in your approach while maintaining scientific and technical plausibility. Use clear headings for each section and number your paragraphs within each section.

Your response should be formatted as follows:
- Use clear headings for each main section (1-7).
- Number each paragraph within the sections.
- Use bullet points or sub-letters (a, b, c) for lists within sections.
- Include any diagrams or visual representations as text descriptions.

Your entire response should be between 1150-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address machine translation between {t['language_pair'][0]} and {t['language_pair'][1]}.",
            "The system architecture must be clearly described with key components and novel features explained.",
            "The response must explain how cultural context is integrated into the translation process, with a specific example provided.",
            "The handling of pragmatics in translation must be addressed with a specific example, such as translating an idiom.",
            "Data requirements and training process must be described, including handling of data scarcity for less common language pairs.",
            "An evaluation methodology focusing on cultural and pragmatic accuracy must be proposed, with specific metrics or benchmarks.",
            "Ethical considerations and limitations of the system must be discussed, with potential solutions proposed.",
            "Two specific future research directions must be suggested, with explanations of their potential impact.",
            "The response must demonstrate interdisciplinary knowledge of linguistics, cultural studies, and AI.",
            "The response must be creative while maintaining scientific and technical plausibility.",
            "The response must be formatted correctly with clear headings, numbered paragraphs, and be between 1150-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
