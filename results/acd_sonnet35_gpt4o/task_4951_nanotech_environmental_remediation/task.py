import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        pollutants = [
            "Microplastics in marine environments",
            "Heavy metals in soil",
            "Persistent organic pollutants in freshwater",
            "Atmospheric particulate matter",
            "Oil spills in aquatic ecosystems"
        ]
        nano_approaches = [
            "Self-assembling nanostructures",
            "Catalytic nanoparticles",
            "Nanoscale filtration systems",
            "Bioengineered nanoorganisms",
            "Nanorobotic swarms"
        ]
        return {
            "1": {
                "pollutant": random.choice(pollutants),
                "nano_approach": random.choice(nano_approaches)
            },
            "2": {
                "pollutant": random.choice(pollutants),
                "nano_approach": random.choice(nano_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a nanotechnology-based system for environmental remediation of {t['pollutant']}, using {t['nano_approach']} as the primary approach. Your response should include the following sections:

1. System Design (300-350 words):
   a) Describe the key components and mechanisms of your nanotechnology-based remediation system.
   b) Explain how your system specifically targets and removes or neutralizes the given pollutant.
   c) Detail how the chosen nano-approach is implemented in your design.
   d) Include a diagram or schematic representation of your system (described textually).

2. Scientific Principles (250-300 words):
   a) Explain the underlying scientific principles that make your system effective.
   b) Discuss any novel applications of nanoscience or materials engineering in your design.
   c) Address how your system interacts with the pollutant at the molecular or atomic level.

3. Environmental Impact Analysis (250-300 words):
   a) Analyze the potential positive and negative environmental impacts of your system.
   b) Discuss any potential unintended consequences and how they might be mitigated.
   c) Compare the environmental footprint of your system to traditional remediation methods.

4. Scalability and Implementation (200-250 words):
   a) Describe how your system could be scaled up for large-scale environmental remediation.
   b) Discuss any technical or logistical challenges in implementing your system in real-world conditions.
   c) Propose solutions to overcome these challenges.

5. Performance Metrics and Evaluation (200-250 words):
   a) Define specific metrics to evaluate the effectiveness of your remediation system.
   b) Propose a method for monitoring and measuring these metrics in a real-world deployment.
   c) Discuss how you would conduct a long-term assessment of your system's impact on ecosystem health.

6. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical concerns related to the use of nanotechnology for environmental remediation.
   b) Discuss the societal implications of successful implementation of your system.
   c) Propose guidelines for responsible development and deployment of nanotech remediation systems.

7. Future Developments and Research Directions (150-200 words):
   a) Suggest potential improvements or extensions to your system for future versions.
   b) Identify areas where further research is needed to enhance the effectiveness or safety of your approach.
   c) Discuss how your system might be adapted to address other environmental challenges.

Ensure your response demonstrates a deep understanding of nanotechnology, environmental science, and materials engineering. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            f"The system design effectively incorporates {t['nano_approach']} for remediating {t['pollutant']}.",
            "The response demonstrates a deep understanding of nanotechnology, environmental science, and materials engineering.",
            "The proposed system is innovative and scientifically plausible.",
            "The response shows a strong interdisciplinary integration of knowledge from multiple scientific fields.",
            "The environmental impact analysis and ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
