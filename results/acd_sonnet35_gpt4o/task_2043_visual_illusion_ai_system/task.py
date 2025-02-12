import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        illusion_types = [
            {
                'type': 'Geometrical-optical illusions',
                'example': 'Müller-Lyer illusion',
                'key_principle': 'misperception of length due to arrow configurations'
            },
            {
                'type': 'Cognitive illusions',
                'example': 'Rubin\'s vase',
                'key_principle': 'figure-ground organization in visual perception'
            },
            {
                'type': 'Physiological illusions',
                'example': 'Afterimages',
                'key_principle': 'adaptation of photoreceptors or neurons in the visual system'
            },
            {
                'type': 'Motion illusions',
                'example': 'Rotating snakes illusion',
                'key_principle': 'peripheral drift and contrast patterns'
            }
        ]
        return {str(i+1): illusion for i, illusion in enumerate(random.sample(illusion_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing, generating, and manipulating visual illusions, with a focus on {t['type']} (e.g., {t['example']}). Your system should incorporate principles of human visual perception and cognitive psychology, particularly considering the key principle of {t['key_principle']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for visual illusion processing.
   b) Explain how your system integrates knowledge from cognitive psychology and computer vision.
   c) Detail how the system models and applies the key principle of {t['key_principle']}.

2. Illusion Analysis (200-250 words):
   a) Explain how your AI system would analyze and quantify the strength of a given {t['type']} illusion.
   b) Describe the features or parameters your system would extract from the illusion.
   c) Discuss how your system accounts for individual differences in illusion perception.

3. Illusion Generation (200-250 words):
   a) Outline the process your AI system would use to generate novel {t['type']} illusions.
   b) Explain how your system ensures the generated illusions adhere to the key principle of {t['key_principle']}.
   c) Describe any techniques used for optimizing the strength or effectiveness of generated illusions.

4. Illusion Manipulation (200-250 words):
   a) Describe how your system could modify existing illusions to enhance or reduce their effects.
   b) Explain the algorithms or methods used for illusion manipulation.
   c) Discuss how your system predicts the perceptual impact of these manipulations.

5. Cognitive Modeling (150-200 words):
   a) Explain how your AI system models human cognitive processes related to {t['type']} illusion perception.
   b) Discuss any insights your system might provide into human visual processing.
   c) Describe how your system's performance compares to human perception of these illusions.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss potential ethical concerns related to AI-generated or manipulated visual illusions.
   b) Propose guidelines for the responsible use of your system.
   c) Suggest two novel applications of your AI system beyond basic research (e.g., in art, design, or therapy).

7. Future Developments (100-150 words):
   a) Identify key areas for improvement in your current system design.
   b) Propose a potential extension of your system to handle a different type of visual illusion.
   c) Discuss how advances in neuroscience might inform future versions of your AI system.

Ensure your response demonstrates a deep understanding of visual perception, cognitive psychology, and artificial intelligence. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively integrates concepts from cognitive psychology and computer vision, with a focus on {t['type']} illusions.",
            f"The illusion analysis and generation processes adequately capture the key principle: {t['key_principle']}.",
            "The response demonstrates creativity and innovation in the AI system design while maintaining scientific plausibility.",
            "The cognitive modeling and ethical considerations are thoughtfully addressed and well-reasoned.",
            "The response shows a high level of understanding in visual perception, cognitive psychology, and AI concepts, using appropriate terminology from these fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
