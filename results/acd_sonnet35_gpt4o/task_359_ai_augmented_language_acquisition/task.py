import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "target_language": "Mandarin Chinese",
                "learner_profile": "Adult native English speaker with no prior experience in tonal languages",
                "learning_focus": "Tonal perception and production",
                "example_challenge": "Distinguishing between mā (mother), má (hemp), mǎ (horse), and mà (scold)"
            },
            "2": {
                "target_language": "Arabic",
                "learner_profile": "Teenage Spanish speaker with intermediate proficiency in English",
                "learning_focus": "Script recognition and writing",
                "example_challenge": "Differentiating between similar Arabic letters like ب (bā'), ت (tā'), and ث (thā')"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI-augmented language acquisition system for learning {t['target_language']}, tailored to the following learner profile: {t['learner_profile']}. The system should focus primarily on {t['learning_focus']}.

Your task is to:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI-augmented language acquisition system.
   b) Explain how it integrates principles from natural language processing, cognitive science, and educational psychology.
   c) Discuss how the system adapts to the specific learner profile and learning focus.
   d) Provide a simple diagram or flowchart of your system architecture.

2. AI-Human Interaction (150-200 words):
   a) Detail how the AI system interacts with the learner during the language acquisition process.
   b) Explain any novel interface or communication methods used.
   c) Describe how the system provides feedback and adapts to the learner's progress.

3. Cognitive Model (200-250 words):
   a) Explain the cognitive model underlying your system's approach to language acquisition.
   b) Discuss how this model accounts for the specific challenges of the target language and learning focus.
   c) Propose a hypothesis about how your system might affect the learner's cognitive processes related to language learning.

4. Learning Algorithms (150-200 words):
   a) Describe the key machine learning algorithms or AI techniques used in your system.
   b) Explain how these algorithms are specifically tailored to language acquisition.
   c) Discuss any novel approaches or combinations of existing techniques in your system.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI-augmented systems for language learning.
   b) Address issues such as data privacy, cultural sensitivity, and potential cognitive effects.
   c) Propose guidelines for the responsible development and use of such systems.

6. Comparative Analysis (150-200 words):
   a) Compare your AI-augmented system to traditional language learning methods.
   b) Discuss potential advantages and limitations of your approach.
   c) Speculate on how this technology might impact the field of language education.

7. Future Research Directions (100-150 words):
   a) Suggest two potential research projects that could further explore or validate your system.
   b) Briefly describe the methodology and expected outcomes of these projects.

8. Specific Challenge (100-150 words):
   Explain how your system would address the following specific challenge: {t['example_challenge']}

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section, adhering to the word limits provided. Your total response should be between 1250-1550 words, not including the diagram. Include the diagram as a text-based representation (e.g., ASCII art or a structured text description) within your response.

Your response will be evaluated based on:
1. Adherence to the specified format and word limits.
2. Depth and accuracy of linguistic, cognitive science, and AI knowledge demonstrated.
3. Creativity and innovation in system design while maintaining scientific plausibility.
4. Appropriateness of the system design for the given target language, learner profile, and learning focus.
5. Quality and relevance of the system architecture diagram.
6. Thoroughness in addressing ethical considerations and future research directions.
7. Effectiveness of the proposed solution for the specific challenge provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response adheres to the specified format and word limits for each section.",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence, using technical terminology appropriately.",
            "The proposed system is creative and innovative while maintaining scientific plausibility.",
            "The system design is appropriately tailored to the specific target language, learner profile, and learning focus provided.",
            "The response includes a clear, relevant diagram or flowchart of the system architecture.",
            "Ethical considerations and future research directions are thoughtfully and thoroughly addressed.",
            "The response effectively addresses the specific challenge provided, demonstrating how the system would handle it.",
            "The cognitive model and learning algorithms are well-explained and relevant to language acquisition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
