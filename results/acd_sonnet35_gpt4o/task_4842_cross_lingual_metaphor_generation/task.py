import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {"concept": "time", "source_language": "English", "target_language": "Mandarin Chinese"},
            {"concept": "love", "source_language": "Spanish", "target_language": "Japanese"},
            {"concept": "power", "source_language": "Arabic", "target_language": "Russian"},
            {"concept": "knowledge", "source_language": "French", "target_language": "Swahili"}
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating metaphors across multiple languages, then apply it to create culturally appropriate metaphors for abstract concepts. For this task, focus on the following parameters:

Abstract Concept: {t['concept']}
Source Language: {t['source_language']}
Target Language: {t['target_language']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-lingual metaphor generation and understanding.
   b) Explain how your system integrates linguistic knowledge, cultural understanding, and metaphor theory.
   c) Discuss any novel techniques or approaches used in your system design.
   d) Include a high-level diagram or flowchart of your AI system's architecture (describe it textually).

2. Metaphor Analysis and Generation Process (250-300 words):
   a) Explain how your system analyzes and understands metaphors in the source language.
   b) Describe the process of generating culturally appropriate metaphors in the target language.
   c) Discuss how your system maintains the conceptual mapping and emotional impact across languages.

3. Cultural and Linguistic Adaptation (200-250 words):
   a) Describe how your system accounts for cultural differences in metaphor usage and interpretation.
   b) Explain any challenges in adapting metaphors between the given language pair and how your system addresses them.
   c) Discuss how your system ensures the generated metaphors are culturally sensitive and appropriate.

4. Example Output (200-250 words):
   a) Provide three examples of metaphors for the given abstract concept in the source language.
   b) Show how your system would translate or adapt these metaphors into the target language.
   c) Explain the cultural and linguistic considerations for each example.

5. Evaluation Methodology (150-200 words):
   a) Propose metrics for evaluating the quality, creativity, and cultural appropriateness of the generated metaphors.
   b) Describe an experiment to validate your system's performance across different concepts and language pairs.
   c) Discuss how you would compare your system's output to human-generated metaphors.

6. Ethical Considerations and Potential Applications (150-200 words):
   a) Discuss the ethical implications of using AI for cross-cultural metaphor generation and understanding.
   b) Propose two potential applications of your system in fields such as education, international relations, or creative writing.
   c) Address any potential risks or misuses of this technology and suggest safeguards.

7. Limitations and Future Directions (100-150 words):
   a) Identify the main limitations or challenges of your proposed system.
   b) Suggest approaches to address these limitations.
   c) Propose two directions for future research that could extend or improve your system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe an AI system capable of understanding and generating metaphors across {t['source_language']} and {t['target_language']}.",
            f"The system should demonstrate an ability to create culturally appropriate metaphors for the concept of {t['concept']}.",
            "The response should show a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The proposed system and its applications should be innovative while maintaining scientific plausibility.",
            "The response should address all required sections with appropriate depth and clarity.",
            "The ethical considerations and limitations should be thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
