import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "target_language": "Mandarin Chinese",
                "learning_focus": "tonal perception and production",
                "cognitive_theory": "Working Memory Model"
            },
            {
                "target_language": "Arabic",
                "learning_focus": "script recognition and writing",
                "cognitive_theory": "Dual Coding Theory"
            },
            {
                "target_language": "Spanish",
                "learning_focus": "verb conjugation and tense system",
                "cognitive_theory": "Cognitive Load Theory"
            },
            {
                "target_language": "Japanese",
                "learning_focus": "honorific system and social context",
                "cognitive_theory": "Social Cognitive Theory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that optimizes second language learning for {t['target_language']}, focusing specifically on {t['learning_focus']}. Your system should incorporate principles from {t['cognitive_theory']} to enhance the learning process. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['cognitive_theory']} and how they relate to language learning.
   b) Discuss the unique challenges in learning {t['learning_focus']} for {t['target_language']}.
   c) Describe how your AI system will apply {t['cognitive_theory']} to address these challenges.

2. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI language learning system.
   b) Explain how your system implements the principles of {t['cognitive_theory']}.
   c) Detail the key components that specifically target {t['learning_focus']} in {t['target_language']}.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

3. Learning Process Simulation (200-250 words):
   a) Describe a typical learning session using your AI system.
   b) Provide a specific example of how it would teach an aspect of {t['learning_focus']} in {t['target_language']}.
   c) Explain how the system adapts to individual learner differences and progress.

4. Evaluation and Optimization (200-250 words):
   a) Propose methods to evaluate the effectiveness of your AI system in teaching {t['learning_focus']}.
   b) Discuss how you would measure learner progress and proficiency.
   c) Explain how your system would use this data to optimize the learning process.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI for language learning.
   b) Address any limitations of your approach, particularly in relation to {t['cognitive_theory']} or {t['target_language']}.
   c) Suggest areas for future research or improvement in AI-assisted language learning.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Your total response should be between 1100-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the target language {t['target_language']} and learning focus {t['learning_focus']}",
            f"The AI system design should incorporate principles from {t['cognitive_theory']}",
            "The response should demonstrate a deep understanding of cognitive science, linguistics, and AI principles",
            "The AI system architecture should be innovative yet scientifically plausible",
            "The response should include all required sections with appropriate depth and detail",
            "The total response should be between 1100-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
