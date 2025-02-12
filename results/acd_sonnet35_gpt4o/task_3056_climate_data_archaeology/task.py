import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        unconventional_sources = [
            "Quantum-preserved microfossils",
            "Chronoparticle emissions from ancient materials",
            "Bioengineered retroviruses carrying climate information",
            "Crystallized atmospheric memory structures",
            "Time-echoing geological formations"
        ]
        climate_patterns = [
            "Cyclical extreme weather events",
            "Long-term atmospheric composition shifts",
            "Global temperature oscillations",
            "Sea level fluctuations",
            "Biodiversity and ecosystem changes"
        ]
        return {
            "1": {"source": random.choice(unconventional_sources), "pattern": random.choice(climate_patterns)},
            "2": {"source": random.choice(unconventional_sources), "pattern": random.choice(climate_patterns)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative future system for reconstructing historical climate data from {t['source']}, then use it to analyze potential {t['pattern']}. Your response should include the following sections:

1. Data Source Description (150-200 words):
   a) Describe the nature and properties of {t['source']} as a climate data repository.
   b) Explain the theoretical basis for how climate information is preserved in this source.
   c) Discuss any limitations or unique characteristics of this data source.

2. Reconstruction System Design (250-300 words):
   a) Outline the key components and processes of your climate data reconstruction system.
   b) Explain how your system extracts and interprets climate information from {t['source']}.
   c) Describe any novel technologies or scientific principles your system employs.
   d) Discuss how your system addresses potential challenges in data reliability and interpretation.

3. Data Analysis Methodology (200-250 words):
   a) Describe your approach to analyzing the reconstructed climate data.
   b) Explain how you identify and characterize {t['pattern']}.
   c) Outline any statistical or computational methods used in your analysis.
   d) Discuss how you account for uncertainties and potential biases in the reconstructed data.

4. Pattern Analysis and Implications (250-300 words):
   a) Present your findings on {t['pattern']} based on the reconstructed data.
   b) Describe any significant trends, cycles, or anomalies you've identified.
   c) Discuss the potential implications of these patterns for future climate scenarios.
   d) Compare your findings with current climate models and historical data.

5. Ethical and Societal Considerations (150-200 words):
   a) Discuss potential ethical implications of using {t['source']} for climate data reconstruction.
   b) Explore how your findings on {t['pattern']} might impact climate policy and public perception.
   c) Propose guidelines for the responsible use and communication of speculative climate data.

6. Future Research Directions (100-150 words):
   a) Suggest two areas for further research or improvement in your reconstruction system.
   b) Propose a potential experiment to validate your system's accuracy and reliability.

Ensure your response demonstrates a deep understanding of climate science, data analysis, and speculative scientific concepts. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed description of {t['source']} as a climate data repository",
            "The climate data reconstruction system design should be innovative yet scientifically plausible",
            f"The data analysis methodology should clearly explain how {t['pattern']} is identified and characterized",
            f"The pattern analysis should present findings on {t['pattern']} and discuss their implications",
            "Ethical and societal considerations of the speculative climate data reconstruction should be addressed",
            "Future research directions should be proposed to improve the system or validate its accuracy",
            "The response should demonstrate interdisciplinary knowledge synthesis and creative problem-solving",
            "Appropriate technical terminology should be used throughout the response"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
