import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Spanish', 'Arabic', 'Russian']
        idiom_types = ['weather-related', 'animal-based', 'body part metaphors', 'food-related', 'color idioms']
        cognitive_aspects = ['conceptual metaphor theory', 'mental simulation', 'embodied cognition', 'cultural schema activation', 'cognitive linguistic frameworks']
        
        tasks = {
            "1": {
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "idiom_type": random.choice(idiom_types),
                "cognitive_aspect": random.choice(cognitive_aspects)
            },
            "2": {
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "idiom_type": random.choice(idiom_types),
                "cognitive_aspect": random.choice(cognitive_aspects)
            }
        }
        
        # Ensure source and target languages are different
        while tasks["2"]["source_language"] == tasks["2"]["target_language"]:
            tasks["2"]["target_language"] = random.choice(languages)
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating, interpreting, and translating idiomatic expressions across multiple languages, while analyzing the cognitive processes involved in understanding figurative language. Focus on {t['idiom_type']} idioms, translating from {t['source_language']} to {t['target_language']}, and incorporate {t['cognitive_aspect']} in your analysis. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for idiom processing and generation.
   b) Explain how your system incorporates linguistic and cognitive models for understanding figurative language.
   c) Detail how the system handles cross-linguistic and cross-cultural variations in idiomatic expressions.
   d) Discuss any novel approaches or algorithms used in your design.

2. Idiom Generation and Translation Process (250-300 words):
   a) Explain how your system generates new idiomatic expressions in the source language.
   b) Describe the process of translating idioms from the source to the target language.
   c) Discuss how your system ensures cultural appropriateness and maintains the original meaning.
   d) Provide an example of a generated idiom in the source language and its translation to the target language.

3. Cognitive Analysis (250-300 words):
   a) Analyze how your system models the cognitive processes involved in understanding the generated idioms.
   b) Explain how {t['cognitive_aspect']} is incorporated into your system's processing and analysis.
   c) Discuss potential insights your system could provide about human cognition and language processing.

4. Cross-cultural Implications (200-250 words):
   a) Explore how cultural differences between {t['source_language']} and {t['target_language']} speakers might affect idiom interpretation.
   b) Discuss strategies your system employs to bridge cultural gaps in idiomatic understanding.
   c) Propose a method for evaluating the cultural authenticity and effectiveness of translated idioms.

5. Evaluation and Testing (200-250 words):
   a) Describe methods for evaluating the performance of your multilingual idiom AI system.
   b) Propose experiments to test both the generation and interpretation capabilities of your system.
   c) Discuss how you would measure the system's understanding of cultural nuances and cognitive processes.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in using AI for cross-cultural idiomatic communication.
   b) Discuss limitations of your approach and areas for future improvement.
   c) Propose guidelines for responsible development and use of multilingual idiom AI systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all six required sections as outlined in the instructions.",
            f"The system design must incorporate {t['cognitive_aspect']} in its analysis of idiom processing.",
            f"The response must demonstrate a clear understanding of idiomatic expressions and their cultural significance in both {t['source_language']} and {t['target_language']}.",
            f"The proposed AI system must be capable of generating and translating {t['idiom_type']} idioms between {t['source_language']} and {t['target_language']}.",
            "The response must show innovative approaches to cross-linguistic and cross-cultural challenges in idiom processing.",
            "The ethical considerations and limitations section must provide thoughtful insights into the responsible development of multilingual idiom AI systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
