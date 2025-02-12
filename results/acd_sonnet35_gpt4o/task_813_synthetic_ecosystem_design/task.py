import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Mars-like planet",
            "Ocean-covered moon",
            "Asteroid belt habitat",
            "Venus-like planet",
            "Subterranean colony"
        ]
        primary_functions = [
            "Oxygen generation",
            "Water purification",
            "Soil formation",
            "Temperature regulation",
            "Radiation protection"
        ]
        constraints = [
            "Limited genetic diversity",
            "Extreme temperature fluctuations",
            "High radiation levels",
            "Low gravity",
            "Scarce water resources"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "primary_function": random.choice(primary_functions),
                "constraint": random.choice(constraints)
            },
            "2": {
                "environment": random.choice(environments),
                "primary_function": random.choice(primary_functions),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel synthetic ecosystem for terraforming a {t['environment']}, with a primary function of {t['primary_function']}, while addressing the constraint of {t['constraint']}. Your response should include the following sections:

1. Ecosystem Overview (200-250 words):
   a) Describe the overall structure and components of your synthetic ecosystem.
   b) Explain how it addresses the primary function and environmental constraints.
   c) Discuss the key synthetic organisms or biological systems involved.

2. Synthetic Biology Design (250-300 words):
   a) Detail the genetic engineering techniques used to create your synthetic organisms.
   b) Explain any novel metabolic pathways or biological processes you've designed.
   c) Describe how these engineered organisms interact with each other and the environment.
   d) Discuss how your design ensures ecosystem stability and prevents uncontrolled proliferation.

3. Ecological Engineering (200-250 words):
   a) Explain how your ecosystem is designed to evolve and adapt over time.
   b) Describe any abiotic components or systems that support the biological elements.
   c) Discuss how you've addressed potential ecological cascades or unintended consequences.

4. Performance Analysis (150-200 words):
   a) Provide quantitative estimates of your ecosystem's effectiveness in fulfilling its primary function.
   b) Compare your synthetic ecosystem's performance to natural systems or alternative terraforming methods.
   c) Identify potential failure modes and describe built-in safeguards or redundancies.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of deploying your synthetic ecosystem.
   b) Address concerns about potential long-term impacts on the target environment.
   c) Propose guidelines for responsible development and use of synthetic ecosystems.

6. Future Developments (100-150 words):
   a) Suggest two potential improvements or expansions to your synthetic ecosystem.
   b) Discuss how this technology could be adapted for other environments or applications.

Ensure your response demonstrates a deep understanding of synthetic biology, ecological engineering, and terraforming principles. Be creative in your approach while maintaining scientific plausibility and addressing ethical concerns. It's crucial to balance innovative ideas with realistic scientific foundations. Use clear headings for each section and adhere to the specified word counts.

Your total response should be between 1050-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The synthetic ecosystem must be designed for a {t['environment']}.",
            f"The primary function of {t['primary_function']} must be addressed comprehensively.",
            f"The design must account for and provide solutions to the constraint of {t['constraint']}.",
            "The response must include all six required sections with appropriate content and depth.",
            "The ecosystem design must demonstrate scientific plausibility while also showing creativity and innovation.",
            "The response must show a deep understanding of synthetic biology and ecological engineering principles, including specific examples of genetic engineering techniques and ecological interactions.",
            "Ethical considerations and guidelines for responsible use must be discussed in detail, addressing both short-term and long-term impacts.",
            "The performance analysis must include quantitative estimates and comparisons to existing systems or methods.",
            "The response must propose realistic future developments and adaptations of the technology.",
            "The response must adhere to the specified word count range and use clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
