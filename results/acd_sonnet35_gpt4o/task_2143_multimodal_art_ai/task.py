import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_movements = [
            "Surrealism",
            "Cubism",
            "Impressionism",
            "Abstract Expressionism",
            "Pop Art"
        ]
        primary_modalities = [
            "visual",
            "auditory",
            "textual"
        ]
        return {
            "1": {
                "art_movement": random.choice(art_movements),
                "primary_modality": random.choice(primary_modalities)
            },
            "2": {
                "art_movement": random.choice(art_movements),
                "primary_modality": random.choice(primary_modalities)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating multimodal art pieces, incorporating visual, auditory, and textual elements. Then, use your system to create and analyze a piece inspired by {t['art_movement']}, with {t['primary_modality']} as the primary modality. Your response should include:

1. Multimodal Art AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for multimodal art analysis and generation.
   b) Explain how your system integrates and processes visual, auditory, and textual data.
   c) Detail any novel elements in your design that enable cross-modal translation and synthesis.
   d) Discuss how your system incorporates art historical knowledge and cultural context.

2. Art Movement Analysis (200-250 words):
   a) Provide a brief overview of the key characteristics of {t['art_movement']}.
   b) Explain how your AI system would identify and analyze these characteristics across different modalities.
   c) Describe how your system accounts for the historical and cultural context of the art movement.

3. Multimodal Art Piece Generation (250-300 words):
   a) Describe the process your AI system would follow to generate a multimodal art piece inspired by {t['art_movement']}.
   b) Explain how your system ensures the {t['primary_modality']} modality is primary while incorporating other modalities.
   c) Provide a detailed description of the generated art piece, including its visual, auditory, and textual elements.
   d) Discuss how the generated piece reflects the characteristics of {t['art_movement']}.

4. Art Piece Analysis (200-250 words):
   a) Explain how your AI system would analyze the generated multimodal art piece.
   b) Describe the key features or elements your system would identify in each modality.
   c) Discuss how your system would interpret the relationships between different modalities in the piece.

5. Evaluation and Interpretation (200-250 words):
   a) Propose a method to evaluate the artistic quality and movement-adherence of the generated piece.
   b) Discuss how your AI system's interpretation of the piece might differ from human art critics.
   c) Address potential biases or limitations in your AI system's artistic understanding.

6. Ethical and Cultural Considerations (150-200 words):
   a) Discuss the ethical implications of using AI for art creation and analysis.
   b) Address concerns about AI potentially replacing human artists or misinterpreting cultural artifacts.
   c) Propose guidelines for responsible development and use of AI in the arts.

Ensure your response demonstrates a deep understanding of art history, multimodal AI systems, and the chosen art movement. Use appropriate technical and artistic terminology, providing explanations where necessary. Be creative in your approach while maintaining plausibility and addressing potential limitations.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a sophisticated understanding of {t['art_movement']} and its characteristics.",
            "The proposed AI system architecture is innovative and plausibly capable of multimodal art analysis and generation.",
            f"The generated art piece description reflects the characteristics of {t['art_movement']} and effectively incorporates multiple modalities, with {t['primary_modality']} as the primary one.",
            "The analysis and evaluation methods show depth in understanding both AI and art criticism.",
            "Ethical considerations are thoroughly addressed, showing awareness of potential issues in AI art creation and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
