import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language': 'Mandarin Chinese',
                'cognitive_style': 'Visual-spatial learner',
                'vr_feature': 'Gesture recognition'
            },
            {
                'language': 'Arabic',
                'cognitive_style': 'Auditory-sequential learner',
                'vr_feature': '3D sound localization'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality-based language learning environment for {t['language']} that adapts to the cognitive style of a {t['cognitive_style']}, with a focus on utilizing {t['vr_feature']}. Your design should integrate principles from linguistics, cognitive science, and VR technology to create an effective and immersive language learning experience.

Provide your response in the following format:

1. Cognitive Style Analysis (200-250 words):
   a) Explain the key characteristics of a {t['cognitive_style']}.
   b) Discuss how this cognitive style influences language learning processes.
   c) Identify specific challenges and opportunities for learning {t['language']} with this cognitive style.

2. VR Environment Design (250-300 words):
   a) Describe the overall structure and key components of your VR language learning environment.
   b) Explain how you integrate {t['vr_feature']} into the learning experience.
   c) Detail how the VR environment adapts to the {t['cognitive_style']}.

3. Linguistic Principles Integration (200-250 words):
   a) Discuss the key linguistic features of {t['language']} that your system focuses on.
   b) Explain how your VR environment addresses these linguistic features.
   c) Describe any novel approaches to teaching grammar, vocabulary, or pronunciation in VR.

4. Adaptive Learning Mechanisms (200-250 words):
   a) Explain how your system assesses and adapts to the learner's progress and preferences.
   b) Describe the AI or algorithmic approaches used for personalization.
   c) Discuss how the system balances adaptation with a structured curriculum.

5. User Interaction and Feedback (150-200 words):
   a) Detail the primary modes of user interaction within the VR environment.
   b) Explain how the system provides feedback and corrections to the learner.
   c) Describe how {t['vr_feature']} enhances the interaction and feedback processes.

6. Challenges and Solutions (150-200 words):
   a) Identify two major challenges in implementing your VR language learning system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any trade-offs or limitations of your proposed solutions.

7. Potential Impact and Future Directions (150-200 words):
   a) Discuss the potential impact of your system on language learning methodologies.
   b) Propose two ways your system could be extended or applied to other areas of education or cognitive training.
   c) Suggest a research study to evaluate the effectiveness of your VR language learning approach.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and virtual reality technology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['cognitive_style']} and its implications for language learning.",
            f"The VR environment design effectively incorporates {t['vr_feature']} and adapts to the specified cognitive style.",
            f"The integration of linguistic principles specific to {t['language']} is well-explained and innovative.",
            "The adaptive learning mechanisms are clearly described and scientifically plausible.",
            "The user interaction and feedback systems are well-designed and utilize VR technology effectively.",
            "The response addresses potential challenges and proposes thoughtful solutions.",
            "The discussion of potential impact and future directions is insightful and demonstrates foresight.",
            "The overall response shows strong integration of knowledge from linguistics, cognitive science, and VR technology.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
