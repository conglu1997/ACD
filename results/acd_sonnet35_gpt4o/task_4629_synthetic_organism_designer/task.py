import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organism_types = [
            "bacteria",
            "algae",
            "fungus",
            "protozoa"
        ]
        desired_traits = [
            "bioremediation",
            "biofuel production",
            "pharmaceutical synthesis",
            "extreme environment survival"
        ]
        environmental_constraints = [
            "high temperature",
            "high salinity",
            "low pH",
            "low oxygen"
        ]
        return {
            "1": {
                "organism_type": random.choice(organism_types),
                "desired_trait": random.choice(desired_traits),
                "environmental_constraint": random.choice(environmental_constraints)
            },
            "2": {
                "organism_type": random.choice(organism_types),
                "desired_trait": random.choice(desired_traits),
                "environmental_constraint": random.choice(environmental_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a genetic algorithm to create an artificial {t['organism_type']} with the capability for {t['desired_trait']}, optimized for survival in {t['environmental_constraint']} conditions. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the key components of your genetic algorithm.
   b) Explain how your algorithm represents and manipulates genetic information.
   c) Detail how your algorithm evaluates fitness for the desired trait and environmental constraint.
   d) Provide a high-level pseudocode of your algorithm.

2. Genetic Engineering Approach (250-300 words):
   a) Identify key genes or genetic pathways you would target to achieve the desired trait.
   b) Explain how you would modify these genes to enhance the organism's capabilities.
   c) Describe any synthetic genetic circuits or novel genes you would introduce.
   d) Discuss potential challenges in engineering the desired traits and how you would address them.

3. Environmental Adaptation (200-250 words):
   a) Explain how your algorithm ensures the organism's survival in the specified environment.
   b) Describe any trade-offs between trait optimization and environmental adaptation.
   c) Discuss potential unintended consequences of optimizing for this environment.

4. Biosafety and Containment (200-250 words):
   a) Propose methods to ensure the engineered organism cannot survive outside its intended environment.
   b) Discuss potential ecological impacts if the organism were to escape containment.
   c) Suggest failsafe mechanisms to control or eliminate the engineered organism if necessary.

5. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of creating this artificial organism.
   b) Discuss potential benefits and risks to society and the environment.
   c) Propose guidelines for responsible development and use of this technology.

6. Practical Applications and Future Directions (150-200 words):
   a) Suggest potential real-world applications for your engineered organism.
   b) Discuss how this technology could impact the field of synthetic biology.
   c) Propose a future research direction building on this work.

Ensure your response demonstrates a deep understanding of genetics, computational biology, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world concerns.

Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of genetic algorithms and how they can be applied to design an artificial {t['organism_type']}.",
            f"The genetic engineering approach should be scientifically plausible for achieving {t['desired_trait']}.",
            f"The algorithm should effectively address adaptation to {t['environmental_constraint']} conditions.",
            "The biosafety and containment measures should be comprehensive and well-reasoned.",
            "The ethical analysis should be thoughtful and consider multiple perspectives.",
            "The practical applications and future directions should be innovative and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
