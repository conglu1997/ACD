import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem": "Coral Reef",
                "climate_threat": "Ocean Acidification",
                "biological_mechanism": "Symbiosis"
            },
            {
                "ecosystem": "Boreal Forest",
                "climate_threat": "Increasing Wildfires",
                "biological_mechanism": "Genetic Diversity"
            }
        ]
        return {
            "1": ecosystems[0],
            "2": ecosystems[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by the biological adaptation mechanism of {t['biological_mechanism']} to model and propose solutions for climate change adaptation in {t['ecosystem']} ecosystems facing the threat of {t['climate_threat']}. Your response should include:

1. Biological Inspiration (250-300 words):
   a) Explain the biological mechanism of {t['biological_mechanism']} and how it contributes to adaptation in natural systems.
   b) Discuss how this mechanism could be applied to AI systems for modeling complex adaptive systems.
   c) Describe how this bioinspired approach could offer unique insights into climate change adaptation.

2. AI System Architecture (300-350 words):
   a) Design the main components of your bioinspired AI system for modeling {t['ecosystem']} adaptation to {t['climate_threat']}.
   b) Explain how each component corresponds to aspects of {t['biological_mechanism']}.
   c) Describe how these components interact to model ecosystem adaptation.
   d) Include a simple diagram illustrating your system's architecture (use ASCII art).

3. Adaptation Modeling Algorithm (250-300 words):
   a) Outline the key steps in your algorithm for modeling ecosystem adaptation.
   b) Explain how your algorithm incorporates principles of {t['biological_mechanism']}.
   c) Provide a brief pseudocode (10-15 lines) for a critical part of your algorithm.
   d) Include a mathematical formula that represents a key aspect of your model (e.g., adaptation rate, system dynamics).

4. Climate Change Adaptation Application (300-350 words):
   a) Describe how your AI system models the adaptation of {t['ecosystem']} to {t['climate_threat']}.
   b) Explain the potential advantages of your bioinspired approach compared to traditional climate modeling methods.
   c) Discuss any challenges in implementing your system and how you would address them.
   d) Provide a specific example of how your system could inform climate change adaptation strategies, including a hypothetical quantitative prediction or insight.

5. Comparative Analysis (200-250 words):
   a) Compare your bioinspired approach to existing methods for modeling ecosystem adaptation to climate change.
   b) Discuss the strengths and limitations of your approach.
   c) Explain how your system might be combined with other AI or modeling techniques for optimal performance.

6. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss potential ethical implications of using bioinspired AI systems for climate change adaptation modeling.
   b) Propose guidelines for responsible development and use of such systems in climate science.
   c) Suggest future research directions or potential applications of your system beyond the current scope.

Ensure your response demonstrates a deep understanding of biology, ecology, climate science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_mechanism']} and how it can be applied to AI systems for modeling adaptation.",
            f"The AI system architecture is well-designed and clearly inspired by {t['biological_mechanism']}.",
            f"The adaptation modeling algorithm effectively incorporates principles of {t['biological_mechanism']} and is suitable for modeling {t['ecosystem']} adaptation to {t['climate_threat']}.",
            "The application to climate change adaptation is well-explained and provides meaningful insights.",
            "The comparative analysis shows a good understanding of existing methods and the strengths/limitations of the proposed approach.",
            "Ethical considerations are thoughtfully discussed and future research directions are proposed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
