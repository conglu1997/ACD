import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_styles = [
            {
                "style": "Geometric Abstraction",
                "cognitive_process": "Spatial reasoning",
                "emotion": "Serenity"
            },
            {
                "style": "Lyrical Abstraction",
                "cognitive_process": "Emotional processing",
                "emotion": "Joy"
            },
            {
                "style": "Abstract Expressionism",
                "cognitive_process": "Intuitive thinking",
                "emotion": "Anger"
            },
            {
                "style": "Minimalism",
                "cognitive_process": "Conceptual thinking",
                "emotion": "Contemplation"
            }
        ]
        return {
            "1": random.choice(art_styles),
            "2": random.choice(art_styles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the cognitive processes involved in creating abstract art, focusing on the style of {t['style']}, the cognitive process of {t['cognitive_process']}, and the emotion of {t['emotion']}. Then use this system to generate and analyze a novel artwork. Your response should include the following sections:

1. Cognitive Model (250-300 words):
   a) Describe the key components of your AI system's cognitive model for abstract art creation.
   b) Explain how it incorporates the specified cognitive process and emotion.
   c) Discuss how your model simulates the creative decision-making involved in {t['style']}.
   d) Include a diagram or flowchart illustrating the cognitive processes in your model.

2. AI System Architecture (300-350 words):
   a) Outline the overall architecture of your AI system for abstract art creation.
   b) Explain how it integrates the cognitive model with machine learning techniques.
   c) Describe the main components and their interactions within your system.
   d) Discuss any novel algorithms or approaches used in your design.
   e) Explain how your system would be trained or learn to create abstract art.

3. Artwork Generation (200-250 words):
   a) Describe the process your AI system would follow to generate a new abstract artwork in the style of {t['style']}.
   b) Explain how the cognitive process of {t['cognitive_process']} and the emotion of {t['emotion']} influence the generation process.
   c) Provide a detailed description or ASCII art representation of the generated artwork.
   d) Analyze the key features of the generated artwork and how they relate to the specified style, cognitive process, and emotion.

4. Artistic Analysis (200-250 words):
   a) Explain how your AI system would analyze and interpret its own or other abstract artworks.
   b) Describe the criteria or methods your system would use to evaluate the artistic merit of an abstract piece.
   c) Discuss how your system might identify influences or similarities to existing artists or art movements.
   d) Provide an example analysis of a famous abstract artwork using your AI system's approach.

5. Philosophical Implications (150-200 words):
   a) Discuss the implications of your AI system for our understanding of human creativity and artistic expression.
   b) Explore the question of whether AI-generated art can be considered truly creative or emotionally expressive.
   c) Consider how your system might challenge or support existing theories of aesthetics or art appreciation.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical concerns related to AI-generated art and its impact on human artists.
   b) Propose guidelines for the responsible development and use of AI in artistic creation.
   c) Suggest future research directions or potential applications of your system in fields such as art therapy, education, or human-AI collaboration.

Ensure your response demonstrates a deep understanding of cognitive science, art theory, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, art theory, and AI system design.",
            "The cognitive model and AI system architecture are well-explained and scientifically plausible.",
            "The artwork generation process clearly incorporates the specified style, cognitive process, and emotion.",
            "The artistic analysis approach is well-reasoned and grounded in art theory.",
            "The discussion of philosophical implications and ethical considerations is insightful and thought-provoking.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "Technical terminology is used appropriately and complex concepts are explained clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
