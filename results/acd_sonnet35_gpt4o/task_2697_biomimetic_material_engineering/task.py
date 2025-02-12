import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_structures = [
            "lotus leaf's water-repellent surface",
            "spider silk's strength and elasticity",
            "gecko's adhesive foot pads",
            "shark skin's drag-reducing properties"
        ]
        ecological_principles = [
            "nutrient cycling",
            "energy flow",
            "biodiversity and ecosystem stability",
            "adaptation to environmental stress"
        ]
        environmental_challenges = [
            "water pollution in urban areas",
            "soil degradation in agriculture",
            "microplastic accumulation in oceans",
            "heat island effect in cities"
        ]
        return {
            "1": {
                "structure": random.choice(biological_structures),
                "principle": random.choice(ecological_principles),
                "challenge": random.choice(environmental_challenges)
            },
            "2": {
                "structure": random.choice(biological_structures),
                "principle": random.choice(ecological_principles),
                "challenge": random.choice(environmental_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel material inspired by the {t['structure']} and the ecological principle of {t['principle']}. Then, analyze its potential applications in addressing the environmental challenge of {t['challenge']}. Your response should include:

1. Biomimetic Material Design (250-300 words):
   a) Describe the key features and properties of your novel material.
   b) Explain how it mimics or is inspired by the given biological structure.
   c) Discuss how the material incorporates or reflects the specified ecological principle.
   d) Provide a molecular or structural diagram of your material (describe it textually).
   e) Specify at least three quantitative properties of your material (e.g., tensile strength, density, thermal conductivity).

2. Material Properties and Fabrication (200-250 words):
   a) Detail the physical and chemical properties of your material.
   b) Propose a method for synthesizing or manufacturing the material.
   c) Discuss any challenges in scaling up production and potential solutions.
   d) Estimate the energy requirements and potential environmental impact of the fabrication process.

3. Application to Environmental Challenge (200-250 words):
   a) Explain how your material could be applied to address the given environmental challenge.
   b) Describe a specific use case or scenario for your material.
   c) Provide quantitative predictions or estimates of the material's effectiveness in addressing the challenge.
   d) Analyze the potential impact of your material on the environment and society.
   e) Discuss any potential drawbacks or unintended consequences of using your material.

4. Comparative Analysis (150-200 words):
   a) Compare your biomimetic material to existing solutions for the environmental challenge.
   b) Discuss the advantages and potential limitations of your approach.
   c) Explain how your material pushes the boundaries of current materials science.
   d) Provide a cost-benefit analysis of your material compared to existing solutions.

5. Future Developments and Ethical Considerations (150-200 words):
   a) Propose two potential future improvements or variations of your material.
   b) Discuss any ethical implications or concerns related to the development and use of your material.
   c) Suggest guidelines for responsible research and application of biomimetic materials.
   d) Speculate on potential misuse or dual-use concerns of your material.

Ensure your response demonstrates a deep understanding of biology, materials science, and environmental engineering. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and creative biomimetic design inspired by {t['structure']} and incorporating {t['principle']}.",
            "The material properties and fabrication process are well-described, including quantitative estimates and scientific plausibility.",
            f"The application to {t['challenge']} is thoughtfully analyzed with quantitative predictions and consideration of potential drawbacks.",
            "The comparative analysis shows a deep understanding of current materials science and environmental solutions, including a cost-benefit analysis.",
            "Ethical considerations, future developments, and potential misuse concerns are insightfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
