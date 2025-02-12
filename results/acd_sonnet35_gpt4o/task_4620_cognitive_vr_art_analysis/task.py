import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_movements = [
            {
                "movement": "Impressionism",
                "cognitive_principle": "Color perception",
                "vr_technique": "Dynamic lighting simulation"
            },
            {
                "movement": "Cubism",
                "cognitive_principle": "Object recognition",
                "vr_technique": "3D spatial manipulation"
            },
            {
                "movement": "Surrealism",
                "cognitive_principle": "Memory and association",
                "vr_technique": "Dream-like environment generation"
            },
            {
                "movement": "Abstract Expressionism",
                "cognitive_principle": "Emotional response to visual stimuli",
                "vr_technique": "Biofeedback-driven visual effects"
            }
        ]
        return {
            "1": random.choice(art_movements),
            "2": random.choice(art_movements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that uses cognitive science principles to enhance the perception and analysis of historical artworks, focusing on the art movement of {t['movement']}. Your system should incorporate the cognitive principle of {t['cognitive_principle']} and utilize the VR technique of {t['vr_technique']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your VR art analysis system.
   b) Explain how it integrates cognitive science principles, particularly {t['cognitive_principle']}.
   c) Detail how your system implements the VR technique of {t['vr_technique']}.
   d) Discuss any novel features that make your system particularly suited for analyzing {t['movement']} artworks.
   e) Include a high-level diagram of your system architecture (describe this textually).

2. Cognitive Science Integration (250-300 words):
   a) Explain how your system leverages the cognitive principle of {t['cognitive_principle']} to enhance art perception and analysis.
   b) Describe how this cognitive principle relates to the characteristics of {t['movement']}.
   c) Discuss how your system might affect the viewer's cognitive processes during art analysis.

3. VR Implementation (250-300 words):
   a) Detail how you implement the VR technique of {t['vr_technique']} in your system.
   b) Explain how this technique enhances the viewer's ability to perceive and analyze {t['movement']} artworks.
   c) Describe any challenges in implementing this technique and how you address them.

4. Art Analysis Methodology (250-300 words):
   a) Outline the step-by-step process a user would go through to analyze an artwork using your system.
   b) Explain how your system guides the user's attention to key elements of {t['movement']} artworks.
   c) Describe how your system facilitates a deeper understanding of the artist's techniques and intentions.

5. Case Study (200-250 words):
   a) Apply your system to a specific, well-known artwork from the {t['movement']} movement.
   b) Describe the enhanced perceptual experience a viewer would have using your system.
   c) Explain how your system reveals new insights about the artwork that might not be apparent through traditional viewing methods.

6. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in enhancing art perception and analysis.
   b) Describe an experiment to test whether your system improves understanding and appreciation of {t['movement']} artworks.
   c) Discuss potential biases or limitations in your system and how you might address them.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using VR and cognitive science principles to alter art perception.
   b) Address concerns about authenticity and the artist's original intent.
   c) Propose future enhancements or applications of your system beyond {t['movement']} artworks.

Ensure your response demonstrates a deep understanding of cognitive science, virtual reality technology, and art history, particularly {t['movement']}. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implementation and user experience.

Format your response with clear headings for each section. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses all seven sections as specified in the instructions.",
            f"The system design incorporates the cognitive principle of {t['cognitive_principle']} and the VR technique of {t['vr_technique']}.",
            f"The response demonstrates a deep understanding of the {t['movement']} art movement and how it relates to the specified cognitive principle and VR technique.",
            "The case study application is detailed and plausible.",
            "The response includes a thoughtful discussion of ethical implications and future directions.",
            "The response uses appropriate terminology from cognitive science, virtual reality technology, and art history.",
            "The total response is between 1600-1950 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
