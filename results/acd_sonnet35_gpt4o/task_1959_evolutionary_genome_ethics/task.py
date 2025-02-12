import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_targets = [
            {
                "trait": "Longevity",
                "gene_complex": "Telomere maintenance",
                "ethical_concern": "Overpopulation"
            },
            {
                "trait": "Intelligence",
                "gene_complex": "Synaptic plasticity",
                "ethical_concern": "Cognitive inequality"
            },
            {
                "trait": "Disease resistance",
                "gene_complex": "Immune system efficiency",
                "ethical_concern": "Unintended ecological effects"
            },
            {
                "trait": "Physical endurance",
                "gene_complex": "Mitochondrial efficiency",
                "ethical_concern": "Unfair athletic advantage"
            }
        ]
        return {
            "1": random.choice(optimization_targets),
            "2": random.choice(optimization_targets)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolutionary algorithm for genome optimization targeting {t['trait']} through the {t['gene_complex']} gene complex, then evaluate its ethical implications and propose safeguards. Your response should include:

1. Algorithm Design (250-300 words):
   a) Describe the key components of your evolutionary algorithm for genome optimization.
   b) Explain how it specifically targets the {t['gene_complex']} gene complex to enhance {t['trait']}.
   c) Detail the fitness function, selection method, and genetic operators used.
   d) Discuss how your algorithm handles potential genetic interactions and pleiotropy.

2. Bioinformatics Integration (200-250 words):
   a) Explain how your algorithm incorporates real genomic data and bioinformatics tools.
   b) Describe any novel approaches to handling the complexity of genetic information.
   c) Discuss how your system accounts for epigenetic factors and gene expression regulation.

3. Simulation and Analysis (200-250 words):
   a) Propose a method to simulate the long-term effects of your genome optimization.
   b) Describe key metrics to evaluate the success and stability of the optimized genomes.
   c) Analyze potential unintended consequences or side effects of the optimization.

4. Ethical Implications (250-300 words):
   a) Discuss the ethical concerns related to optimizing {t['trait']}, particularly {t['ethical_concern']}.
   b) Analyze the potential societal impacts of widespread genome optimization.
   c) Explore the philosophical implications of directed human evolution.

5. Safeguards and Regulations (200-250 words):
   a) Propose a comprehensive framework for ethical oversight of genome optimization.
   b) Describe specific technical safeguards built into your algorithm to prevent misuse.
   c) Suggest policy recommendations for the responsible development and application of this technology.

6. Future Directions and Challenges (150-200 words):
   a) Identify key challenges in implementing and scaling your genome optimization system.
   b) Propose potential improvements or expansions to your algorithm.
   c) Discuss how advancements in genetics or AI might further impact this field.

Ensure your response demonstrates a deep understanding of genetics, evolutionary algorithms, and bioethics. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical responsibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of evolutionary algorithms, genetics, and bioethics.",
            f"The algorithm design effectively targets the {t['gene_complex']} gene complex for enhancing {t['trait']}.",
            "The bioinformatics integration is well-explained and scientifically plausible.",
            "The simulation and analysis approach is thorough and considers long-term effects.",
            f"Ethical implications, particularly {t['ethical_concern']}, are thoroughly discussed.",
            "Proposed safeguards and regulations are comprehensive and well-reasoned.",
            "Future challenges and directions are insightfully explored.",
            "The response maintains scientific rigor while showcasing creativity in algorithm design and ethical analysis.",
            "The response is well-structured and addresses all required points comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
