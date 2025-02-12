import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "Working Memory Capacity",
                "ai_algorithm": "Recurrent Neural Networks",
                "musical_element": "Melody"
            },
            {
                "cognitive_principle": "Attentional Blink",
                "ai_algorithm": "Generative Adversarial Networks",
                "musical_element": "Rhythm"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical composition system that integrates the cognitive principle of {t['cognitive_principle']}, the AI algorithm {t['ai_algorithm']}, and focuses on the musical element of {t['musical_element']}. Then, analyze the potential impact of compositions created by this system on human cognition and emotion.

Your response should include the following sections:

1. System Design (300-350 words):
   a) Explain how your system incorporates {t['cognitive_principle']} into the composition process.
   b) Describe the implementation of {t['ai_algorithm']} in your system.
   c) Detail how the system generates or manipulates {t['musical_element']}.
   d) Discuss any novel features or innovations in your design.

2. Cognitive-AI-Music Integration (250-300 words):
   a) Analyze how {t['cognitive_principle']} influences the musical output.
   b) Explain the role of {t['ai_algorithm']} in enhancing or complementing this cognitive principle.
   c) Describe how this integration affects the generation or perception of {t['musical_element']}.

3. Composition Example (200-250 words):
   a) Provide a detailed description of a hypothetical composition created by your system.
   b) Explain how this composition reflects the integration of cognitive science, AI, and music theory.
   c) Use musical terminology to describe the structure and characteristics of the composition.

4. Cognitive and Emotional Impact Analysis (250-300 words):
   a) Predict potential effects of listening to compositions from your system on human cognition.
   b) Analyze possible emotional responses to these compositions.
   c) Discuss how the unique integration in your system might influence music perception and processing.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the cognitive or emotional effects of your system's compositions.
   b) Describe the methodology, including participant selection, stimuli, and measurements.
   c) Explain how you would control for confounding variables.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns related to your system and its applications.
   b) Discuss possible societal impacts of widespread use of cognitive-AI music composition systems.
   c) Propose guidelines for responsible development and use of such technologies.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and music theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section and address all subpoints. Your total response should be between 1350-1650 words. Include a word count at the end of your submission.

Reminder: Carefully structure your response, ensuring that you address all subpoints in each section. The integration of cognitive science, AI, and music theory should be evident throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design effectively integrates {t['cognitive_principle']}, {t['ai_algorithm']}, and {t['musical_element']}, showing clear connections between all three domains.",
            "The response demonstrates a deep understanding of cognitive science, AI, and music theory, with appropriate use of technical terminology from each field.",
            "The composition example is well-described and clearly reflects the integration of cognitive science, AI, and music theory principles.",
            "The cognitive and emotional impact analysis is thorough, scientifically plausible, and considers multiple perspectives.",
            "The proposed experiment is well-designed, appropriate for testing the system's effects, and considers potential confounding variables.",
            "Ethical considerations and societal impacts are thoughtfully discussed, with specific examples and proposed guidelines.",
            "The overall response is creative, scientifically grounded, well-structured, and within the specified word count (1350-1650 words).",
            "All required sections and subpoints are addressed in the response, with clear headings and logical flow between sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
