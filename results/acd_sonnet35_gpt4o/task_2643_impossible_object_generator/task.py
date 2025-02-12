import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        impossible_objects = [
            {
                "name": "Penrose Triangle",
                "description": "A triangle that appears to be a solid object, but is actually impossible in three-dimensional space"
            },
            {
                "name": "Escher Waterfall",
                "description": "A perpetual motion machine where water appears to flow uphill"
            },
            {
                "name": "Impossible Cube",
                "description": "A cube with contradictory perspective, where edges that should be parallel appear to intersect"
            }
        ]
        return {str(i+1): obj for i, obj in enumerate(random.sample(impossible_objects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze 'impossible objects' - visual paradoxes that challenge human perception and understanding of physical reality. Focus on the {t['name']} as an example.

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and analyzing impossible objects.
   b) Explain how your system incorporates principles of visual perception and cognitive science.
   c) Detail any novel algorithms or techniques used in your design.
   d) Include a simple diagram of your system architecture (describe it textually).

2. Object Generation (250-300 words):
   a) Explain how your AI system would generate a new variation of the {t['name']}.
   b) Describe the steps involved in creating a 2D or 3D representation of this impossible object.
   c) Discuss how your system ensures the object maintains its 'impossible' nature while being visually coherent.

3. Perceptual Analysis (250-300 words):
   a) Detail how your AI system analyzes the perceptual properties of the generated impossible object.
   b) Explain how it identifies and quantifies the specific visual paradoxes present in the object.
   c) Describe how your system predicts human cognitive responses to the impossible object.

4. Cognitive Implications (200-250 words):
   a) Discuss how studying impossible objects like the {t['name']} can inform our understanding of human visual processing and cognition.
   b) Explain how your AI system's approach to generating and analyzing impossible objects might contribute to theories of perception and mental representation.

5. Practical Applications (150-200 words):
   a) Propose three potential applications of your impossible object generator in fields such as art, design, cognitive science, or AI research.
   b) Discuss how these applications might lead to new insights or capabilities in their respective fields.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to creating AI systems that can manipulate human perception.
   b) Discuss the implications of using such technology in areas like advertising, entertainment, or psychological research.
   c) Propose guidelines for the responsible development and use of impossible object generation technology.

Ensure your response demonstrates a deep understanding of visual perception, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must focus on the {t['name']} as the primary example",
            "The system architecture should be clearly described and incorporate relevant cognitive science principles",
            "The object generation process should be logically explained and maintain the 'impossible' nature of the object",
            "The perceptual analysis should demonstrate understanding of visual paradoxes and human cognition",
            "The response should discuss cognitive implications and practical applications of the technology",
            "Ethical considerations should be thoughtfully addressed",
            "The response should be well-organized, creative, and scientifically plausible",
            "The total response should be between 1300-1600 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
