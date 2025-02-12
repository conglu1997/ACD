import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        planetary_conditions = [
            {
                "gravity": "1.5 times Earth's gravity",
                "atmosphere": "Nitrogen-rich with trace amounts of methane",
                "temperature_range": "Average temperature of -10°C to 20°C"
            },
            {
                "gravity": "0.8 times Earth's gravity",
                "atmosphere": "Dense carbon dioxide atmosphere with high humidity",
                "temperature_range": "Average temperature of 25°C to 40°C"
            }
        ]
        return {
            "1": random.choice(planetary_conditions),
            "2": random.choice(planetary_conditions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and simulating a complex, self-sustaining ecosystem on a hypothetical exoplanet with the following conditions:

- Gravity: {t['gravity']}
- Atmosphere: {t['atmosphere']}
- Temperature Range: {t['temperature_range']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI ecosystem architect system.
   b) Explain how your system integrates knowledge from ecology, climatology, and evolutionary biology.
   c) Detail the algorithms or techniques used for generating and evaluating ecosystem components.
   d) Discuss how your system handles the complex interactions between different parts of the ecosystem.

2. Ecosystem Design Principles (250-300 words):
   a) Outline the core principles guiding the ecosystem creation process.
   b) Explain how these principles address the given planetary conditions.
   c) Describe any novel or unique features your system might develop to ensure ecosystem stability.
   d) Discuss potential challenges or limitations in simulating the given planetary conditions.

3. Ecosystem Generation Process (250-300 words):
   a) Detail the steps involved in creating the ecosystem, from basic organisms to complex food webs.
   b) Explain how the system balances biodiversity with ecosystem stability.
   c) Discuss how the system handles evolutionary processes and adaptations over time.

4. Simulation and Monitoring (200-250 words):
   a) Describe how your AI system simulates the ecosystem over extended periods.
   b) Explain the key metrics and indicators used to monitor ecosystem health and stability.
   c) Discuss how the system detects and responds to potential ecosystem collapse scenarios.

5. Specific Ecosystem Example (250-300 words):
   a) Provide a detailed example of a specific ecosystem your AI might generate for the given planetary conditions.
   b) Describe at least three unique organisms, their roles in the ecosystem, and their adaptations.
   c) Explain a complex interaction or food web within this ecosystem.

6. Scientific Implications and Applications (200-250 words):
   a) Analyze the potential scientific insights that could be gained from your AI ecosystem architect.
   b) Discuss possible applications in fields such as astrobiology, climate science, and conservation biology.
   c) Consider how this system could contribute to our understanding of Earth's ecosystems and biodiversity.

7. Ethical Considerations and Limitations (200-250 words):
   a) Discuss ethical implications of using AI to design and simulate ecosystems.
   b) Address potential limitations or biases in your AI system's approach.
   c) Propose guidelines for the responsible use of AI-generated ecosystem models in scientific research.

8. Comparison with Existing Models (200-250 words):
   a) Compare your AI ecosystem architect to an existing ecosystem simulation model (e.g., Madingley Model or EcoSim).
   b) Discuss the similarities and differences in approach and capabilities.
   c) Explain how your system improves upon or complements existing models.

Ensure your response demonstrates a deep understanding of ecology, climatology, evolutionary biology, and AI systems. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) for each point within a section. Your total response should be between 1850-2250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of ecology, climatology, and evolutionary biology, and their integration in AI systems.",
            "The AI system architecture is well-designed and incorporates appropriate algorithms and techniques for ecosystem simulation.",
            "The ecosystem design principles and generation process are scientifically plausible and address the given planetary conditions.",
            "The specific ecosystem example is detailed, creative, and consistent with the planetary conditions.",
            "The response adequately addresses scientific implications, applications, and ethical considerations of the AI ecosystem architect.",
            "The comparison with existing models is thorough and highlights the unique aspects of the proposed system.",
            "The writing is clear, well-organized, and uses appropriate technical terminology.",
            "The response follows the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
