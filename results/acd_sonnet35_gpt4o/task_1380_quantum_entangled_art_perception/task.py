import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "wave function collapse",
            "quantum tunneling"
        ]
        visual_elements = [
            "color",
            "shape",
            "texture",
            "composition"
        ]
        art_styles = [
            "abstract expressionism",
            "surrealism",
            "cubism",
            "minimalism"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "visual_element": random.choice(visual_elements),
                "art_style": random.choice(art_styles)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "visual_element": random.choice(visual_elements),
                "art_style": random.choice(art_styles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates and analyzes visual art based on quantum entanglement principles, focusing on the quantum principle of {t['quantum_principle']}, the visual element of {t['visual_element']}, and the art style of {t['art_style']}. Then, use this system to explore the relationship between quantum phenomena and human visual perception. Your response should include the following sections:

1. Quantum Art Generation System (250-300 words):
   a) Describe the key components of your quantum-inspired art generation system.
   b) Explain how it incorporates the quantum principle of {t['quantum_principle']}.
   c) Detail how the system manipulates the visual element of {t['visual_element']}.
   d) Discuss how the system emulates the art style of {t['art_style']}.

2. Quantum-Visual Mapping (200-250 words):
   a) Explain how your system maps quantum states or processes to visual elements.
   b) Describe any novel algorithms or techniques used in this mapping process.
   c) Discuss how this mapping might reveal new insights about quantum phenomena or visual perception.

3. Artwork Analysis (250-300 words):
   a) Generate a hypothetical artwork using your system and describe it in detail.
   b) Analyze how the quantum principle of {t['quantum_principle']} is manifested in the artwork.
   c) Explain how the visual element of {t['visual_element']} is manipulated to reflect quantum properties.
   d) Discuss how the art style of {t['art_style']} interacts with the quantum-inspired elements.

4. Perceptual Experiment Design (200-250 words):
   a) Propose an experiment to test how humans perceive and interpret the quantum-inspired artwork.
   b) Describe the methodology, including participant selection, stimuli presentation, and data collection.
   c) Explain how this experiment might reveal connections between quantum phenomena and visual perception.

5. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your system for understanding quantum mechanics, visual perception, or artistic expression.
   b) Propose at least two ways to extend or improve your system.
   c) Suggest how this approach might contribute to other fields of study or practical applications.

Ensure your response demonstrates a deep understanding of quantum mechanics, visual arts, and cognitive science. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1300 words. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system clearly incorporates the quantum principle of {t['quantum_principle']} and manipulates the visual element of {t['visual_element']}",
            f"The artwork generation and analysis convincingly emulates the art style of {t['art_style']}",
            "The quantum-visual mapping process is innovative and well-explained",
            "The hypothetical artwork is described in detail and analyzed thoroughly",
            "The proposed perceptual experiment is well-designed and relevant to the task",
            "The response demonstrates a deep understanding of quantum mechanics, visual arts, and cognitive science",
            "The implications and future directions are thoughtfully discussed",
            "The proposed system is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
