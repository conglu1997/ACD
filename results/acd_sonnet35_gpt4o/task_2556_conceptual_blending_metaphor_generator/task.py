import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "technology",
            "nature",
            "emotions",
            "politics",
            "economics",
            "art"
        ]
        languages = [
            "English",
            "Mandarin",
            "Spanish",
            "Arabic",
            "Hindi",
            "Swahili"
        ]
        return {
            "1": {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "language1": random.choice(languages),
                "language2": random.choice(languages)
            },
            "2": {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "language1": random.choice(languages),
                "language2": random.choice(languages)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that performs conceptual blending across domains and languages to generate and analyze novel metaphors, then use it to explore cross-cultural communication. Focus on the following domains: {t['domain1']} and {t['domain2']}, and the following languages: {t['language1']} and {t['language2']}.

Your response should include:

1. Conceptual Blending System Design (300-350 words):
   a) Describe the architecture of your AI system for conceptual blending and metaphor generation.
   b) Explain how your system integrates knowledge from different domains and languages.
   c) Detail the process of generating novel metaphors through conceptual blending.
   d) Provide a high-level diagram or pseudocode snippet illustrating a key component of your system.
   e) Discuss potential biases in your AI system and propose methods to mitigate them.

2. Cross-linguistic Blending (250-300 words):
   a) Explain how your system handles conceptual blending across {t['language1']} and {t['language2']}.
   b) Discuss challenges in preserving meaning and cultural nuances during cross-linguistic blending.
   c) Provide an example of a metaphor your system might generate by blending concepts from {t['domain1']} in {t['language1']} with {t['domain2']} in {t['language2']}.
   d) Explain the conceptual mappings and blending process for your example metaphor.

3. Metaphor Analysis (250-300 words):
   a) Describe how your AI system would analyze and interpret metaphors.
   b) Explain the criteria your system uses to evaluate the novelty and effectiveness of generated metaphors.
   c) Propose a quantitative metric for evaluating metaphor effectiveness and explain its components.
   d) Discuss how your system could identify culturally specific elements in metaphors.
   e) Provide an example analysis of a complex metaphor, demonstrating your system's capabilities.

4. Cross-cultural Communication Application (200-250 words):
   a) Propose an application of your system to improve cross-cultural communication.
   b) Explain how metaphor generation and analysis could bridge cultural gaps.
   c) Provide a specific scenario demonstrating your system's potential impact on international relations or business communication.
   d) Include a sample dialogue or exchange that your system might facilitate or analyze.

5. Cognitive Science Foundation (200-250 words):
   a) Discuss the cognitive science theories and principles underlying your AI system.
   b) Compare your system's approach to human conceptual blending and metaphor creation.
   c) Suggest an experiment to test whether your AI system's outputs align with human cognitive processes.
   d) Provide a hypothesis and brief experimental design for this comparison.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in using AI for cross-cultural metaphor generation and interpretation.
   b) Discuss limitations of your approach and potential unintended consequences.
   c) Propose guidelines for responsible development and use of conceptual blending AI in cross-cultural contexts.
   d) Suggest a method for ongoing evaluation and improvement of your system's cultural sensitivity.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and cross-cultural communication. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use numbered lists where appropriate. Your total response should be between 1400-1700 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively blends concepts from {t['domain1']} and {t['domain2']} across {t['language1']} and {t['language2']}",
            "The response demonstrates a deep understanding of conceptual blending, cognitive linguistics, and artificial intelligence",
            "The proposed AI system architecture is well-described, innovative, and includes a clear diagram or pseudocode snippet",
            "The cross-linguistic blending approach is thoughtfully explained and addresses cultural nuances, with a concrete example provided",
            "The metaphor analysis section includes a detailed example demonstrating the system's capabilities and a proposed quantitative metric for evaluating metaphor effectiveness",
            "The application to cross-cultural communication is practical, impactful, and includes a sample dialogue or exchange",
            "The cognitive science foundation is well-explained and includes a testable hypothesis and experimental design",
            "Ethical considerations and limitations are thoroughly addressed, including guidelines for responsible development and methods to mitigate biases",
            "The response is well-formatted, within the specified word count, and addresses all required components"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
