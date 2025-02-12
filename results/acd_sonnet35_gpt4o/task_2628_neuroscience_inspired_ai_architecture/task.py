import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'neuroscience_principle': 'Predictive coding in the visual cortex',
                'ai_application': 'Computer vision and image recognition'
            },
            {
                'neuroscience_principle': 'Hippocampal pattern separation and completion',
                'ai_application': 'Continual learning and memory consolidation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI architecture inspired by the neuroscience principle of {t['neuroscience_principle']} and analyze its potential impact on {t['ai_application']}. Your response should include:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the key aspects of the given neuroscience principle.
   b) Discuss how this principle contributes to brain function and cognition.
   c) Identify specific neural mechanisms or structures involved.

2. AI Architecture Design (300-350 words):
   a) Propose an AI architecture that incorporates the given neuroscience principle.
   b) Describe the key components of your architecture and their functions.
   c) Explain how your design mimics or adapts the neural mechanisms involved.
   d) Discuss how this architecture could be implemented using current AI technologies.

3. Application Analysis (250-300 words):
   a) Explain how your AI architecture could improve or revolutionize the given AI application.
   b) Provide a specific example or use case demonstrating the potential advantages of your approach.
   c) Discuss any challenges or limitations in applying your architecture to this domain.

4. Comparative Analysis (200-250 words):
   a) Compare your neuroscience-inspired architecture to current approaches in the given AI application.
   b) Analyze potential advantages and limitations of your approach.
   c) Discuss how your architecture might handle tasks or challenges that are difficult for current systems.

5. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical implications or risks associated with your proposed AI architecture.
   b) Discuss how this approach might impact our understanding of artificial intelligence and its relationship to human cognition.
   c) Suggest guidelines or safeguards for responsible development and deployment of such systems.

6. Future Research Directions (150-200 words):
   a) Propose two specific research questions or experiments to further explore the potential of your architecture.
   b) Suggest potential collaborations between neuroscientists and AI researchers that could advance this field.

Ensure your response demonstrates a deep understanding of both neuroscience and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words, excluding section headings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given neuroscience principle and its relevance to brain function.",
            "The AI architecture design is innovative, plausible, and clearly incorporates the neuroscience principle.",
            "The application analysis provides insightful examples and addresses both advantages and challenges.",
            "The comparative analysis offers a thoughtful evaluation of the proposed architecture against current approaches.",
            "Ethical and societal implications are thoroughly considered, with relevant guidelines proposed.",
            "Future research directions are specific, relevant, and demonstrate foresight in the field.",
            "The response maintains scientific accuracy while showcasing creativity and interdisciplinary knowledge integration.",
            "The response follows the specified format with clear section headings and appropriate word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
