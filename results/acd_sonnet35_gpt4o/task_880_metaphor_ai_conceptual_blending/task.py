import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            ("Politics", "Weather"),
            ("Technology", "Biology"),
            ("Economics", "Ecology"),
            ("Art", "Mathematics")
        ]
        return {
            "1": {"domains": random.choice(domains)},
            "2": {"domains": random.choice(domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating metaphors based on conceptual blending theory, focusing on the domains of {t['domains'][0]} and {t['domains'][1]}. Your response should include:

1. Conceptual Blending Framework (250-300 words):
   a) Explain how your AI system would implement conceptual blending theory for metaphor processing.
   b) Describe the key components of your system and how they interact.
   c) Discuss how your system would identify and map conceptual correspondences between the two given domains.

2. Metaphor Analysis (200-250 words):
   a) Provide an example of a complex metaphor that blends concepts from {t['domains'][0]} and {t['domains'][1]}.
   b) Explain step-by-step how your AI system would analyze and interpret this metaphor.
   c) Discuss how your system would identify the source domain, target domain, and the conceptual mappings between them.

3. Metaphor Generation (200-250 words):
   a) Describe how your AI system would generate novel metaphors blending concepts from {t['domains'][0]} and {t['domains'][1]}.
   b) Provide an example of a metaphor your system might generate, explaining the conceptual integration process.
   c) Discuss how your system would ensure the generated metaphors are both coherent and creative.

4. Cognitive Implications (150-200 words):
   a) Analyze how your AI system's approach to metaphor processing compares to human cognitive processes.
   b) Discuss potential insights your system could provide into human conceptual blending and metaphor comprehension.

5. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or challenges in implementing your system.
   b) Discuss ethical implications of AI systems capable of advanced metaphor processing and generation.
   c) Propose guidelines for responsible development and use of such systems.

6. Future Directions (100-150 words):
   a) Suggest potential applications of your metaphor processing AI system in fields such as natural language understanding, creative writing, or cognitive science research.
   b) Propose ideas for expanding your system to handle more complex forms of figurative language or multi-domain conceptual blending.

Ensure your response demonstrates a deep understanding of conceptual blending theory, cognitive linguistics, and AI systems. Be innovative in your approach while maintaining scientific plausibility. Format your response with clear headings for each section.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-defined AI system design that implements conceptual blending theory for metaphor processing, focusing on the domains of {t['domains'][0]} and {t['domains'][1]}.",
            "The metaphor analysis section should provide a clear example and a step-by-step explanation of how the AI system would interpret it.",
            "The metaphor generation section should describe the process and provide an example of a novel metaphor blending the given domains.",
            "The response should discuss cognitive implications, comparing the AI system's approach to human cognitive processes.",
            "Limitations, ethical considerations, and future directions must be addressed.",
            "The overall response should demonstrate creativity, interdisciplinary knowledge integration, and a deep understanding of conceptual blending theory and AI principles.",
            "The response should follow the provided structure and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
