import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        aesthetic_domains = [
            {
                "domain": "Visual Art",
                "cognitive_principle": "Gestalt principles of perception",
                "challenge": "Create an AI system that can generate and evaluate abstract art based on Gestalt principles"
            },
            {
                "domain": "Music",
                "cognitive_principle": "Auditory scene analysis",
                "challenge": "Design an AI system that can compose and critique music based on principles of auditory scene analysis"
            },
            {
                "domain": "Literature",
                "cognitive_principle": "Conceptual blending",
                "challenge": "Develop an AI system that can create and analyze metaphors using the theory of conceptual blending"
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(aesthetic_domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and evaluate aesthetic experiences in the domain of {t['domain']}, based on the cognitive principle of {t['cognitive_principle']}. Your specific challenge is to {t['challenge']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key aspects of {t['cognitive_principle']} and how they relate to aesthetic experiences in {t['domain']}.
   b) Discuss how these principles could be computationally modeled.
   c) Propose a novel approach for integrating these cognitive principles into an AI system for aesthetic generation and evaluation.

2. AI System Design (300-350 words):
   a) Describe the architecture of your AI system, including its main components and their functions.
   b) Explain how your system incorporates the cognitive principle of {t['cognitive_principle']}.
   c) Detail the algorithms or techniques your system would use for both generation and evaluation of aesthetic experiences.
   d) Discuss how your system would handle the subjective nature of aesthetics.

3. Implementation and Training (200-250 words):
   a) Outline the data requirements for training your AI system.
   b) Describe the training process, including any novel approaches you would use.
   c) Explain how you would validate the system's understanding of the cognitive principles and aesthetic qualities.

4. Evaluation Metrics (150-200 words):
   a) Propose at least three quantitative metrics to assess the performance of your AI system.
   b) Explain how these metrics relate to human aesthetic judgments and the underlying cognitive principles.
   c) Describe a method for gathering human feedback to refine these metrics.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of an AI system that can generate and evaluate aesthetic experiences.
   b) Consider issues of creativity, authorship, and the role of AI in art and culture.
   c) Propose guidelines for the responsible development and use of such AI systems.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how this research could contribute to our understanding of human cognition and aesthetics.

Ensure your response demonstrates a deep understanding of cognitive science, aesthetics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of {t['cognitive_principle']} and its application to {t['domain']}",
            "The AI system design should be innovative yet plausible",
            "The proposed implementation and evaluation methods should be well-thought-out and scientifically grounded",
            "Ethical considerations should be thoroughly addressed",
            "The response should show interdisciplinary knowledge synthesis and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
