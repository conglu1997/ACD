import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_problems = [
            "urban heat islands",
            "coastal erosion",
            "agricultural water scarcity",
            "air pollution in cities",
            "loss of biodiversity"
        ]
        biological_systems = [
            "termite mounds",
            "mangrove forests",
            "desert plants",
            "blue mussels",
            "coral reefs"
        ]
        return {
            "1": {
                "climate_problem": random.choice(climate_problems),
                "biological_system": random.choice(biological_systems)
            },
            "2": {
                "climate_problem": random.choice(climate_problems),
                "biological_system": random.choice(biological_systems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution to the climate change problem of {t['climate_problem']}, inspired by the biological system of {t['biological_system']}. Your response should include the following sections:

1. Biological System Analysis (200-250 words):
   a) Describe the key characteristics and functions of {t['biological_system']}.
   b) Explain how these characteristics help the organism adapt to its environment.
   c) Identify specific features or processes that could be relevant to addressing {t['climate_problem']}.
   d) Cite at least one relevant scientific study or principle related to this biological system.

2. Biomimetic Solution Design (250-300 words):
   a) Propose a detailed solution to {t['climate_problem']} inspired by {t['biological_system']}.
   b) Explain how your solution mimics or adapts the biological system's features.
   c) Describe the key components and functioning of your proposed solution.
   d) Include a simple diagram or schematic representation of your design using ASCII characters or Unicode box-drawing symbols.
   e) Use at least three specific scientific terms related to biomimicry or climate science in your explanation.

3. Implementation and Scalability (200-250 words):
   a) Discuss how your solution could be implemented in real-world settings.
   b) Analyze potential challenges in scaling up the solution.
   c) Propose strategies to overcome these challenges.
   d) Cite a relevant scientific principle or study related to implementation or scalability.

4. Environmental Impact Assessment (200-250 words):
   a) Evaluate the potential positive and negative environmental impacts of your solution.
   b) Compare the environmental footprint of your solution to existing non-biomimetic approaches.
   c) Suggest ways to minimize any potential negative impacts.
   d) Use at least two specific environmental science terms in your assessment.

5. Ethical and Social Considerations (150-200 words):
   a) Discuss ethical implications of implementing your biomimetic solution.
   b) Analyze potential social and economic impacts on different stakeholders.
   c) Propose guidelines for responsible development and implementation of your solution.

6. Future Research Directions (150-200 words):
   a) Identify areas where further research is needed to refine or validate your solution.
   b) Propose two specific research projects or experiments to address these areas.
   c) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of both the biological system and the climate problem. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include in-text citations for any scientific studies or principles mentioned, using a consistent citation style."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the specified biological system and climate problem, including relevant scientific citations.",
            "The proposed biomimetic solution is innovative, well-explained, and plausibly addresses the climate issue, using appropriate scientific terminology.",
            "The implementation, scalability, and environmental impact are thoroughly analyzed, with relevant scientific principles cited.",
            "Ethical and social considerations are thoughtfully discussed.",
            "The response shows strong interdisciplinary knowledge application and creative problem-solving.",
            "The response includes a clear diagram or schematic representation using ASCII or Unicode characters.",
            "The word count for each section falls within the specified ranges, and the overall response is between 1150-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
