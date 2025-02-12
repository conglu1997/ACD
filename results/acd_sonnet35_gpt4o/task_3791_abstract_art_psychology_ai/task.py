import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        psychological_concepts = [
            {
                "concept": "Cognitive Dissonance",
                "description": "The mental discomfort experienced when holding contradictory beliefs or values"
            },
            {
                "concept": "Flow State",
                "description": "A mental state of complete absorption and focus in an activity"
            },
            {
                "concept": "Collective Unconscious",
                "description": "A part of the unconscious mind shared by a society, a people, or all humanity"
            },
            {
                "concept": "Emotional Intelligence",
                "description": "The capacity to be aware of, control, and express one's emotions, and to handle interpersonal relationships"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(psychological_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and analyzing abstract art that represents the psychological concept of {t['concept']}. Then, use this system to explore the intersection of art therapy and artificial intelligence. Your response should include the following sections:

1. AI Art Generation System (300-350 words):
   a) Describe the architecture and key components of your AI system for creating abstract art.
   b) Explain how your system interprets and represents the concept of {t['concept']} in visual form.
   c) Detail the algorithms or techniques used to ensure the art is truly abstract yet meaningful.
   d) Discuss how your system balances creativity and adherence to the psychological concept.

2. Art Analysis Capabilities (250-300 words):
   a) Explain how your AI system analyzes and interprets abstract art, both its own creations and human-made art.
   b) Describe the features or elements the system looks for when identifying representations of {t['concept']}.
   c) Discuss any novel approaches your system uses to connect visual elements to psychological meanings.

3. Psychological Representation (200-250 words):
   a) Provide a detailed text-based description of an abstract artwork your AI system would generate to represent {t['concept']}.
   b) Explain the key visual elements and how they relate to aspects of the psychological concept.
   c) Analyze how effectively this artwork conveys the concept and potential viewer interpretations.

4. Art Therapy Application (250-300 words):
   a) Propose a specific application of your AI system in art therapy practices.
   b) Explain how the system could assist therapists and patients in exploring {t['concept']}.
   c) Discuss potential benefits and limitations of using AI-generated abstract art in therapy.
   d) Address any ethical considerations in using AI for this purpose.

5. Comparative Analysis (200-250 words):
   a) Compare your AI system's approach to representing {t['concept']} with how human artists might approach the same task.
   b) Discuss any insights about human creativity or psychology that emerge from this comparison.
   c) Explore how AI and human artists could potentially collaborate in representing complex psychological concepts.

6. Future Implications (150-200 words):
   a) Speculate on future developments in AI-generated art and its role in psychology and therapy.
   b) Discuss potential impacts on our understanding of creativity, emotion, and mental health.
   c) Propose an innovative future application of your system beyond art therapy.

Ensure your response demonstrates a deep understanding of artificial intelligence, psychology, and art theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for an AI system that creates and analyzes abstract art representing {t['concept']}",
            "The AI system's architecture and methods for art generation and analysis are clearly explained",
            "The application in art therapy is well-thought-out and addresses potential benefits and limitations",
            "The comparative analysis between AI and human approaches is insightful",
            "The response demonstrates deep understanding of AI, psychology, and art theory",
            "The ideas presented are creative and innovative while maintaining plausibility",
            f"The response adequately addresses the specific psychological concept of {t['concept']}",
            "The response follows the specified format and is within the 1350-1650 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
