import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = [
            "Flow state",
            "Cognitive dissonance",
            "Mindfulness meditation",
            "Decision fatigue"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody",
            "Timbre"
        ]
        tasks = [
            {
                "cognitive_state": state,
                "musical_focus": element
            } for state in cognitive_states for element in musical_elements
        ]
        selected_tasks = random.sample(tasks, 2)
        return {"1": selected_tasks[0], "2": selected_tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can compose music based on cognitive and emotional states, integrating theories from cognitive science, music theory, and affective computing. Your system should focus on the cognitive state of {t['cognitive_state']} and primarily utilize the musical element of {t['musical_focus']}.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles from cognitive science related to {t['cognitive_state']}.
   b) Describe how {t['musical_focus']} in music theory can be used to express or induce this cognitive state.
   c) Discuss relevant theories from affective computing that your system will incorporate.

2. System Architecture (300-350 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system processes cognitive state information and translates it into musical parameters.
   c) Describe any novel algorithms or techniques your system uses for music generation.
   d) Discuss how your system ensures coherence and emotional relevance in the composed music.

3. Cognitive-Musical Mapping (200-250 words):
   a) Provide a detailed explanation of how your system maps {t['cognitive_state']} to specific aspects of {t['musical_focus']}.
   b) Include at least one concrete example of a musical pattern or structure your system might generate, using musical notation or a clear textual description.
   c) Explain the rationale behind this mapping, citing relevant research in music psychology or neuroscience.

4. Learning and Adaptation (150-200 words):
   a) Describe how your system learns and improves its compositions over time.
   b) Explain how it might adapt to individual preferences or cultural differences in music perception.
   c) Discuss any challenges in creating a system that can generalize across different cognitive states and musical elements.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system in expressing {t['cognitive_state']} through {t['musical_focus']}.
   b) Describe how you would measure both the musical quality and the cognitive-emotional impact of the compositions.
   c) Discuss the challenges in evaluating such a system and how you'd address them.

6. Ethical Considerations and Applications (150-200 words):
   a) Identify potential ethical concerns related to an AI system that composes emotionally impactful music.
   b) Propose guidelines for responsible development and use of such a system.
   c) Suggest two potential applications of your system in fields such as therapy, education, or entertainment.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the cognitive state of {t['cognitive_state']} and focus on the musical element of {t['musical_focus']}",
            "The theoretical framework should demonstrate a strong understanding of cognitive science, music theory, and affective computing",
            "The system architecture should be well-designed and clearly explained, with novel approaches to translating cognitive states into music",
            "The cognitive-musical mapping should be detailed and scientifically grounded, including a concrete example with musical notation or clear description",
            "The learning and adaptation section should propose plausible mechanisms for improvement and personalization",
            "The evaluation and validation methods should be comprehensive and address both musical and cognitive-emotional aspects",
            "Ethical considerations should be thoughtfully addressed with practical guidelines and applications proposed",
            "The response should demonstrate interdisciplinary thinking by effectively connecting concepts from cognitive science, music theory, and AI",
            "The proposed system should be innovative while maintaining scientific and technological plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
