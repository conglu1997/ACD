import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'extinct_language': 'Linear A',
                'historical_period': 'Minoan civilization (2000-1450 BCE)',
                'modern_puzzle': 'Decipher an encrypted message in a contemporary language'
            },
            {
                'extinct_language': 'Etruscan',
                'historical_period': 'Ancient Italy (800-100 BCE)',
                'modern_puzzle': 'Develop a new constructed language for interspecies communication'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical texts to reconstruct the extinct {t['extinct_language']} language from the {t['historical_period']}, then use insights from this process to {t['modern_puzzle']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for language reconstruction and analysis.
   b) Explain how your system processes historical texts and linguistic data.
   c) Detail any novel machine learning approaches or algorithms used in your design.
   d) Include a simple diagram of your system architecture using ASCII art or Unicode characters (max 20 lines by 80 characters).

2. Historical Language Reconstruction (250-300 words):
   a) Explain your AI's approach to reconstructing {t['extinct_language']}.
   b) Discuss how your system accounts for the historical and cultural context of {t['historical_period']}.
   c) Describe any challenges specific to this language and how your AI addresses them.
   d) Provide an example of how your system might reconstruct a simple phrase or grammatical rule.

3. Modern Application (250-300 words):
   a) Detail how your AI system applies insights from reconstructing {t['extinct_language']} to {t['modern_puzzle']}.
   b) Explain any adaptations or extensions to your AI necessary for this modern application.
   c) Provide a specific example of how a feature of {t['extinct_language']} contributes to solving the modern puzzle.

4. Linguistic Analysis (200-250 words):
   a) Analyze potential similarities and differences between {t['extinct_language']} and modern languages.
   b) Discuss how your AI's understanding of language evolution contributes to its problem-solving capabilities.
   c) Explain how your system distinguishes between linguistic universals and language-specific features.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of reconstructing extinct languages and cultures.
   b) Address concerns about AI-driven linguistic and historical analysis.
   c) Propose guidelines for responsible use of AI in linguistic and historical research.

6. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose a research question that could further explore the intersection of AI, linguistics, and historical analysis.

Ensure your response demonstrates a deep understanding of linguistics, historical analysis, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, historical analysis, and artificial intelligence as applied to {t['extinct_language']} reconstruction and {t['modern_puzzle']}",
            "The AI system design is innovative and plausible, with clear explanations of its components and functioning",
            "The approach to reconstructing the extinct language and applying insights to the modern puzzle is creative and well-reasoned",
            "Ethical considerations are thoroughly addressed",
            "The response is well-structured, coherent, and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
