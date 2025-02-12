import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "Broca's area",
                "language_pair": "Mandarin Chinese and Arabic",
                "communication_context": "diplomatic negotiations"
            },
            {
                "brain_region": "Wernicke's area",
                "language_pair": "Spanish and Japanese",
                "communication_context": "emergency medical situations"
            },
            {
                "brain_region": "arcuate fasciculus",
                "language_pair": "English and Swahili",
                "communication_context": "cultural exchange programs"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural-inspired AI system for real-time multilingual communication between {t['language_pair']}, drawing inspiration from the {t['brain_region']} and incorporating principles of neurolinguistics. Your system should be optimized for {t['communication_context']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, explaining how it mimics the function of the {t['brain_region']}.
   b) Detail the key components and their interactions within your system.
   c) Explain how your architecture handles the specific challenges of translating between {t['language_pair']}.
   d) Include a high-level diagram or pseudocode snippet illustrating a crucial part of your architecture.

2. Neurolinguistic Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in human language processing.
   b) Describe how your AI system incorporates neurolinguistic principles in its design.
   c) Discuss any limitations or challenges in translating biological neural processes to artificial systems.
   d) Cite at least one relevant scientific paper or study to support your analysis.

3. Real-time Processing Techniques (200-250 words):
   a) Describe the methods your system uses to achieve real-time translation.
   b) Explain how these methods are optimized for {t['communication_context']}.
   c) Discuss any trade-offs between speed and accuracy in your system.

4. Cross-cultural Adaptation (200-250 words):
   a) Explain how your system handles cultural nuances and context-specific language use in {t['language_pair']}.
   b) Describe any mechanisms for adapting to different communication styles or cultural norms.
   c) Discuss how your system maintains cultural sensitivity in {t['communication_context']}.

5. Performance Evaluation (150-200 words):
   a) Propose metrics for evaluating the performance of your system.
   b) Describe a hypothetical experiment to test your system's effectiveness in {t['communication_context']}.
   c) Discuss potential challenges in evaluating real-time multilingual communication systems.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues arising from the use of your system in {t['communication_context']}.
   b) Propose guidelines for responsible development and deployment of neural-inspired AI translators.
   c) Suggest areas for future research or improvement in your approach.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI principles. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['brain_region']} and its role in language processing, with at least one relevant scientific citation",
            f"The AI system architecture clearly draws inspiration from the {t['brain_region']} and is well-suited for translating between {t['language_pair']}",
            f"The system design effectively addresses the challenges of real-time processing in {t['communication_context']}",
            "The approach to cross-cultural adaptation is well-thought-out and culturally sensitive",
            "The proposed performance evaluation metrics and experiment are appropriate and well-designed",
            "The ethical considerations are thorough and the proposed guidelines are relevant and practical",
            "The response shows creativity and interdisciplinary knowledge integration throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
