import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'application': 'memory enhancement',
                'target_emotion': 'nostalgia',
                'olfactory_challenge': 'complex natural scents',
                'creative_element': 'incorporate a bio-inspired sensor design'
            },
            {
                'application': 'emotional regulation',
                'target_emotion': 'anxiety reduction',
                'olfactory_challenge': 'synthetic aroma compounds',
                'creative_element': 'integrate with a virtual reality interface'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can digitally encode and recreate olfactory experiences for {t['application']}, focusing on the emotion of {t['target_emotion']} and addressing the challenge of {t['olfactory_challenge']}. Additionally, {t['creative_element']} in your design. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including its main components and their functions.
   b) Explain how the system captures, processes, and recreates olfactory information.
   c) Detail the AI techniques or algorithms used in your system (e.g., neural networks, machine learning approaches).

2. Olfactory-Digital Mapping (200-250 words):
   a) Create a framework for mapping olfactory stimuli to digital representations.
   b) Explain the neuroscientific and chemical principles that inform your mapping choices.
   c) Provide an example of how a specific scent would be digitally encoded and recreated.

3. Emotion and Memory Integration (200-250 words):
   a) Describe how your system links olfactory experiences to emotions and memories.
   b) Explain the mechanisms for triggering {t['target_emotion']} through olfactory recreation.
   c) Discuss how the system adapts to individual differences in olfactory perception and emotional responses.

4. Addressing Olfactory Challenges (150-200 words):
   a) Explain how your system handles the complexities of {t['olfactory_challenge']}.
   b) Discuss potential limitations in recreating certain types of scents and proposed solutions.

5. Applications and Ethical Considerations (200-250 words):
   a) Describe potential applications of your system in {t['application']}.
   b) Discuss ethical implications of manipulating olfactory experiences and emotions.
   c) Propose guidelines for responsible use of this technology.

6. Creative Element Integration (100-150 words):
   a) Explain how you have incorporated {t['creative_element']} into your system design.
   b) Discuss the benefits and potential challenges of this integration.

Ensure your response demonstrates a deep understanding of olfactory neuroscience, chemistry, artificial intelligence, and their practical applications. Be creative in your system design while maintaining scientific plausibility. Use clear headings for each section of your response.

Format your response as follows:
[Section Name]
[Your response for this section]

Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of an AI system for encoding and recreating olfactory experiences.",
            f"The system architecture addresses the application of {t['application']}.",
            f"The design incorporates mechanisms for triggering the emotion of {t['target_emotion']}.",
            f"The response adequately addresses the challenge of {t['olfactory_challenge']}.",
            f"The design creatively integrates {t['creative_element']}.",
            "The response shows a deep understanding of olfactory neuroscience, chemistry, and AI principles.",
            "The response follows the specified format and word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
