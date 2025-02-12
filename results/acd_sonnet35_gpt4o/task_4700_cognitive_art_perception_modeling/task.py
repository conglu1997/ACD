import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_styles = [
            "Abstract Expressionism",
            "Surrealism",
            "Cubism",
            "Impressionism",
            "Pop Art"
        ]
        cognitive_processes = [
            "Visual attention",
            "Pattern recognition",
            "Emotional response",
            "Semantic interpretation",
            "Aesthetic judgment"
        ]
        return {
            "1": {
                "art_style": random.choice(art_styles),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "art_style": random.choice(art_styles),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human cognitive processes in art perception and analysis, then apply it to interpret and generate novel artworks. Your system should focus on the art style of {t['art_style']} and the cognitive process of {t['cognitive_process']}. Your response should include:

1. Cognitive Model Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling human art perception and analysis.
   b) Explain how your system integrates knowledge from cognitive science, computer vision, and art history.
   c) Detail how your model simulates the specific cognitive process of {t['cognitive_process']} in relation to art perception.
   d) Discuss any novel algorithms or approaches used in your design.

2. Art Style Analysis (250-300 words):
   a) Explain how your system represents and analyzes the characteristics of {t['art_style']}.
   b) Describe the features or elements your model focuses on when processing artworks in this style.
   c) Discuss how your system's approach to {t['art_style']} relates to human perception and appreciation of this style.

3. Artwork Interpretation Process (250-300 words):
   a) Detail the step-by-step process your system uses to interpret an artwork in the {t['art_style']} style.
   b) Explain how the {t['cognitive_process']} is simulated during this interpretation process.
   c) Provide an example of how your system might interpret a specific artwork, highlighting the role of {t['cognitive_process']}.

4. Novel Artwork Generation (200-250 words):
   a) Describe how your system generates new artworks in the {t['art_style']} style.
   b) Explain how the {t['cognitive_process']} influences the generation process.
   c) Discuss the balance between mimicking existing artworks and creating truly novel pieces.

5. Evaluation and Comparison (200-250 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system's art interpretation and generation.
   b) Compare your system's performance to human art perception and creation in the context of {t['art_style']}.
   c) Discuss potential biases or limitations in your approach and how they might be addressed.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for our understanding of human art perception and creativity.
   b) Propose two novel applications of your system in fields such as art education, therapy, or creative industries.
   c) Suggest how your system could be extended to incorporate other cognitive processes or art styles.

Ensure your response demonstrates a deep understanding of cognitive science, computer vision, and art history. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, computer vision, and art history.",
            f"The proposed AI system effectively models the cognitive process of {t['cognitive_process']} in art perception.",
            f"The system's approach to analyzing and generating artworks in the {t['art_style']} style is well-explained and plausible.",
            "The response includes creative and innovative ideas while maintaining scientific rigor.",
            "The implications and potential applications of the system are thoughtfully discussed.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
