import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_phenomena = [
            {
                "phenomenon": "El Niño-Southern Oscillation (ENSO)",
                "region": "Tropical Pacific",
                "timescale": "Interannual",
                "key_variables": ["Sea Surface Temperature", "Trade Winds", "Thermocline Depth"],
                "data_sources": ["Satellite Observations", "Ocean Buoys", "Climate Models"]
            },
            {
                "phenomenon": "Atlantic Multidecadal Oscillation (AMO)",
                "region": "North Atlantic",
                "timescale": "Multidecadal",
                "key_variables": ["Sea Surface Temperature", "Ocean Heat Content", "Atmospheric Pressure"],
                "data_sources": ["Historical Records", "Proxy Data", "Climate Models"]
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(climate_phenomena, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by the distributed neural network of octopuses to model and predict the {t['phenomenon']} in the {t['region']} on a {t['timescale']} timescale. Your response should include the following sections:

1. Octopus Neural Network Analysis (200-250 words):
   a) Describe the key features of the octopus's distributed neural network.
   b) Explain how these features could be advantageous for modeling complex climate systems.
   c) Discuss any limitations or challenges in adapting this biological system to an AI architecture.

2. AI System Architecture (300-350 words):
   a) Propose a novel AI architecture inspired by the octopus neural network.
   b) Explain how your architecture incorporates key features of the octopus's nervous system.
   c) Describe how your system would process and integrate various climate data inputs.
   d) Include a high-level diagram or flowchart of your AI system's architecture (described in text).

3. Climate Modeling Approach (250-300 words):
   a) Explain how your AI system would model the specified climate phenomenon.
   b) Describe how your system would incorporate the key variables: {', '.join(t['key_variables'])}.
   c) Discuss how your system would integrate data from the following sources: {', '.join(t['data_sources'])}.
   d) Explain any novel approaches to handling the {t['timescale']} timescale of the phenomenon.

4. Prediction and Uncertainty Quantification (200-250 words):
   a) Describe how your system generates predictions for the climate phenomenon.
   b) Explain how it quantifies and communicates uncertainty in its predictions.
   c) Discuss how your system's architecture might improve prediction accuracy or reduce uncertainty compared to traditional methods.

5. Advantages and Limitations (150-200 words):
   a) Analyze the potential advantages of your octopus-inspired AI system for climate modeling.
   b) Discuss any limitations or challenges in implementing or scaling your system.
   c) Propose potential solutions or areas for future research to address these limitations.

6. Broader Implications (150-200 words):
   a) Discuss how your approach could impact the field of climate science and AI development.
   b) Explore potential applications of your system beyond climate modeling.
   c) Consider any ethical implications or societal impacts of using such a system for climate predictions.

Important Notes:
- Ensure your response demonstrates a deep understanding of neurobiology, artificial intelligence architectures, and climate science.
- Use appropriate technical terminology and provide clear explanations for complex concepts.
- Be innovative in your approach while maintaining scientific plausibility.
- Focus on the design and theoretical aspects of the AI system. Do not provide actual climate predictions or solutions.
- Adhere strictly to the word count for each section as specified above.
- Format your response with clear headings for each section, numbered exactly as above.
- Begin each section with the heading (e.g., '1. Octopus Neural Network Analysis:') followed by your response for that section.
- Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the {t['phenomenon']} in the {t['region']} on a {t['timescale']} timescale.",
            "The proposed AI architecture is clearly inspired by the octopus's distributed neural network and incorporates key features of its nervous system.",
            f"The climate modeling approach incorporates the specified key variables ({', '.join(t['key_variables'])}) and data sources ({', '.join(t['data_sources'])}).",
            "The system design demonstrates a deep understanding of neurobiology, AI architectures, and climate science.",
            "The approach to climate modeling and prediction is innovative, scientifically plausible, and addresses uncertainty quantification.",
            "The response adheres to the specified format, including section headings and word count ranges.",
            "The response focuses on the design and theoretical aspects without providing actual climate predictions or solutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
