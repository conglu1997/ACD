import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_periods = [
            "Renaissance",
            "Impressionism",
            "Cubism",
            "Surrealism",
            "Abstract Expressionism"
        ]
        cognitive_processes = [
            "Visual perception",
            "Emotional processing",
            "Symbolic reasoning",
            "Spatial cognition",
            "Metaphorical thinking"
        ]
        return {
            "1": {
                "art_period": random.choice(art_periods),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "art_period": random.choice(art_periods),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the cognitive processes involved in artistic creation and appreciation, focusing on the {t['art_period']} period and emphasizing the role of {t['cognitive_process']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system models the specified cognitive process in the context of art creation and appreciation.
   c) Detail how your system represents and processes artistic knowledge specific to the given art period.
   d) Propose a novel algorithm or technique that enables your system to generate art in the style of the specified period.
   e) Include a diagram or flowchart of your system's architecture (described textually).

2. Artistic Analysis Capabilities (250-300 words):
   a) Explain how your system analyzes existing artworks from the specified period.
   b) Describe the features and patterns your system would identify as characteristic of the given art period.
   c) Discuss how your system integrates historical and cultural context into its analysis.
   d) Provide an example of how your system might analyze a specific artwork from the given period.

3. Art Generation Process (250-300 words):
   a) Describe the step-by-step process your system uses to generate new artworks in the style of the specified period.
   b) Explain how the specified cognitive process influences the art generation.
   c) Discuss how your system ensures originality while maintaining period-appropriate style.
   d) Provide an example of a hypothetical artwork your system might generate, including a description of its features and how they relate to the art period.

4. Cognitive Simulation (200-250 words):
   a) Explain how your system simulates the specified cognitive process in both art analysis and generation.
   b) Discuss how this simulation contributes to the system's understanding and creation of art.
   c) Compare your system's cognitive simulation to current theories about human artistic cognition.
   d) Propose a method for evaluating the fidelity of your system's cognitive simulation.

5. Interdisciplinary Implications (200-250 words):
   a) Discuss how your system could contribute to our understanding of human creativity and artistic cognition.
   b) Propose two novel research questions in cognitive science or art history that could be explored using your system.
   c) Explain how your system could be adapted to study other aspects of human cognition or cultural production.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to AI-generated art and simulated artistic cognition.
   b) Discuss any limitations or potential biases in your approach to modeling artistic creation and appreciation.
   c) Propose guidelines for the responsible development and use of AI systems in art creation and analysis.

7. Future Developments (150-200 words):
   a) Suggest potential improvements or extensions to your system for future versions.
   b) Discuss how emerging technologies in AI or neuroscience might enhance your system's capabilities.
   c) Speculate on the potential long-term impact of such systems on the art world and our understanding of creativity.

Ensure your response demonstrates a deep understanding of cognitive science, art history, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            f"The system design effectively incorporates the cognitive process of {t['cognitive_process']}.",
            f"The system demonstrates a deep understanding of the {t['art_period']} art period.",
            "The proposed AI system is innovative and scientifically plausible.",
            "The response shows a strong interdisciplinary integration of cognitive science, art history, and AI.",
            "The ethical considerations and limitations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
