import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {
                'target_language': 'Mandarin Chinese',
                'cognitive_focus': 'working memory',
                'learning_style': 'visual-spatial',
                'vr_activity': 'Character-building puzzle in a virtual Chinese street'
            },
            {
                'target_language': 'Arabic',
                'cognitive_focus': 'attention control',
                'learning_style': 'kinesthetic',
                'vr_activity': 'Virtual calligraphy practice in a simulated Arabic marketplace'
            }
        ]
        return {str(i+1): pair for i, pair in enumerate(random.sample(language_pairs, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system for language learning that adapts to users' cognitive processes and learning styles, then analyze its effectiveness and potential impact on language acquisition theories. Your system should focus on teaching {t['target_language']}, with a particular emphasis on enhancing {t['cognitive_focus']} and catering to {t['learning_style']} learners. One of the key VR activities in your system should be: {t['vr_activity']}.

        Your response should include the following sections:

        1. System Architecture (300-350 words):
           a) Describe the key components of your VR language learning system.
           b) Explain how the system adapts to the user's cognitive processes, particularly {t['cognitive_focus']}.
           c) Detail how the system caters to {t['learning_style']} learners.
           d) Discuss any novel features that enhance language acquisition in the VR environment.

        2. Cognitive-Linguistic Interface (250-300 words):
           a) Explain how your system integrates principles of cognitive science and linguistics.
           b) Describe specific VR activities or exercises designed to enhance {t['cognitive_focus']}.
           c) Discuss how the system assesses and adapts to the user's cognitive load during learning.

        3. Language Acquisition Methodology (250-300 words):
           a) Outline the pedagogical approach your system uses for teaching {t['target_language']}.
           b) Explain how VR technology enhances this approach compared to traditional methods.
           c) Describe how the system provides feedback and tracks user progress.
           d) Provide a detailed example of how {t['vr_activity']} is implemented in your system.

        4. User Experience and Interaction (200-250 words):
           a) Describe the user interface and interaction methods in your VR system.
           b) Explain how the system creates an immersive language learning experience.
           c) Discuss how the system maintains user engagement and motivation.

        5. Effectiveness Analysis (200-250 words):
           a) Propose a method for evaluating the effectiveness of your VR language learning system.
           b) Discuss potential impacts on language acquisition theories.
           c) Compare the expected outcomes of your system to traditional language learning methods.

        6. Ethical Considerations and Limitations (150-200 words):
           a) Discuss potential ethical implications of using VR for cognitive-linguistic training.
           b) Address concerns about privacy and data collection in your system.
           c) Identify potential limitations or challenges in implementing your system.

        7. Future Developments and Applications (150-200 words):
           a) Suggest potential improvements or extensions to your VR language learning system.
           b) Discuss how this technology could be applied to other areas of education or cognitive enhancement.
           c) Propose a novel research question that arises from the intersection of VR, cognitive science, and linguistics.

        Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and virtual reality technology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

        Important: Your response should focus on high-level design principles, theoretical foundations, and analysis. Do not provide specific code implementations or technical details of the VR system. Instead, concentrate on the conceptual design and its potential impacts.

        Format your response with clear headings for each section and use subheadings where appropriate. Adhere strictly to the word count guidelines provided for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of language acquisition, cognitive science, and VR technology, with a clear focus on {t['target_language']}, {t['cognitive_focus']}, and {t['learning_style']} learning.",
            "The VR system design is innovative, scientifically plausible, and thoroughly explained with clear architectural components, without providing specific technical implementations.",
            f"The cognitive-linguistic interface and language acquisition methodology are well-developed, grounded in current theories, and effectively incorporate the specified VR activity: {t['vr_activity']}.",
            "The effectiveness analysis provides insightful comparisons to traditional methods and proposes a valid, detailed evaluation approach.",
            "Ethical considerations and future developments are thoughtfully addressed, with consideration of privacy concerns and potential applications beyond language learning.",
            "The response adheres to the specified word count guidelines for each section and overall formatting requirements.",
            "The response focuses on high-level design and analysis without providing direct solutions or technical implementations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
