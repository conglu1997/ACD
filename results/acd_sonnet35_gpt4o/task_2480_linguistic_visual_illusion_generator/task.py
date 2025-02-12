import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        illusion_types = [
            {
                "type": "geometric",
                "perceptual_principle": "size constancy"
            },
            {
                "type": "color",
                "perceptual_principle": "simultaneous contrast"
            },
            {
                "type": "motion",
                "perceptual_principle": "apparent motion"
            },
            {
                "type": "depth",
                "perceptual_principle": "perspective"
            }
        ]
        return {
            "1": random.choice(illusion_types),
            "2": random.choice(illusion_types)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating visual illusions based on linguistic descriptions, focusing on {t['type']} illusions that exploit the perceptual principle of {t['perceptual_principle']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating visual illusions.
   b) Explain how your system processes linguistic input to create visual output.
   c) Detail how your system incorporates principles of cognitive psychology and visual perception.
   d) Discuss any novel approaches in your design that enable the creation of convincing illusions.

2. Linguistic-Visual Translation Process (200-250 words):
   a) Explain how your system translates linguistic descriptions into visual elements.
   b) Describe how it ensures the generated illusions adhere to the specified perceptual principle.
   c) Provide an example of how a simple linguistic input might be processed to create an illusion.

3. Illusion Generation Mechanism (200-250 words):
   a) Detail the step-by-step process your system uses to generate a {t['type']} illusion.
   b) Explain how the system manipulates visual elements to exploit the principle of {t['perceptual_principle']}.
   c) Discuss how your system ensures the generated illusions are novel and not just reproductions of known illusions.

4. Evaluation and Refinement (150-200 words):
   a) Propose a method to evaluate the effectiveness of the generated illusions.
   b) Describe how your system might learn and improve from feedback.
   c) Discuss potential challenges in assessing the quality of AI-generated visual illusions.

5. Cognitive Science Insights (150-200 words):
   a) Explain how this system could contribute to our understanding of human visual perception.
   b) Discuss potential applications of this technology in cognitive science research.
   c) Address any ethical considerations in using AI to manipulate human perception.

6. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations of your proposed system.
   b) Suggest two areas for future research that could enhance the system's capabilities.

Ensure your response demonstrates a deep understanding of cognitive science, visual perception, linguistics, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, visual perception, linguistics, and AI.",
            f"The proposed system effectively generates {t['type']} illusions based on the principle of {t['perceptual_principle']}.",
            "The linguistic-visual translation process is well-explained and plausible.",
            "The system architecture and illusion generation mechanism are innovative and scientifically grounded.",
            "The evaluation method and cognitive science insights are thoughtfully considered.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
