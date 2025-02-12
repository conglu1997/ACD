import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Coral Reef",
            "Rainforest",
            "Arctic Tundra",
            "Grassland"
        ]
        biotech_approaches = [
            "CRISPR Gene Editing",
            "Synthetic Biology",
            "Bioremediation",
            "Artificial Seed Dispersal"
        ]
        ai_techniques = [
            "Deep Reinforcement Learning",
            "Generative Adversarial Networks",
            "Federated Learning",
            "Evolutionary Algorithms"
        ]
        endangered_species = [
            "Hawksbill Turtle",
            "Sumatran Orangutan",
            "Polar Bear",
            "Black-Footed Ferret"
        ]
        constraints = [
            "Limited genetic diversity in the target species",
            "Strict regulations on introducing genetically modified organisms",
            "Rapidly changing climate conditions in the ecosystem",
            "Limited funding and resources for implementation"
        ]
        return {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "biotech_approach": random.choice(biotech_approaches),
                "ai_technique": random.choice(ai_techniques),
                "endangered_species": random.choice(endangered_species),
                "constraint": random.choice(constraints)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "biotech_approach": random.choice(biotech_approaches),
                "ai_technique": random.choice(ai_techniques),
                "endangered_species": random.choice(endangered_species),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven biotechnology system for ecosystem restoration and biodiversity preservation, focusing on the {t['ecosystem']} ecosystem. Your system should incorporate {t['biotech_approach']} as the primary biotechnology approach and utilize {t['ai_technique']} as the key AI component. Then, analyze its potential impacts and propose experiments to validate its effectiveness. 

Consider the following baseline data and constraint for your chosen ecosystem:
- Biodiversity index: 0.65 (on a scale of 0 to 1)
- Carbon sequestration rate: 2.5 tons per hectare per year
- Endangered species population: {t['endangered_species']}, with only 500 individuals remaining
- Constraint: {t['constraint']}

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven biotechnology system for ecosystem restoration.
   b) Explain how your system integrates the specified biotechnology approach with the AI technique.
   c) Detail how your system is tailored to address the unique challenges of the given ecosystem and the specified constraint.
   d) Include a high-level diagram or pseudocode to illustrate your architecture (describe it textually).
   e) Provide a specific example of how your system would address a challenge related to the {t['endangered_species']}.

2. Biotechnology-AI Integration (250-300 words):
   a) Explain how the specified AI technique enhances or optimizes the biotechnology approach.
   b) Describe any novel algorithms or techniques used in your system.
   c) Discuss the theoretical advantages of your integrated approach over traditional conservation methods.
   d) Provide a concrete example of how this integration would work in practice.

3. Ecosystem Restoration Process (250-300 words):
   a) Provide a step-by-step explanation of how your system would approach ecosystem restoration.
   b) Describe how your system monitors and adapts to changes in the ecosystem.
   c) Analyze the potential risks and safeguards in your approach.
   d) Explain how your system aims to improve the given biodiversity index and carbon sequestration rate.
   e) Address how your system works within the specified constraint.

4. Biodiversity Preservation Strategies (200-250 words):
   a) Explain how your system addresses biodiversity preservation in the given ecosystem.
   b) Discuss specific techniques for protecting the {t['endangered_species']} and promoting genetic diversity.
   c) Describe how your system balances restoration goals with maintaining existing biodiversity.
   d) Discuss any potential negative consequences or trade-offs of your approach.

5. Performance Evaluation (200-250 words):
   a) Propose metrics to evaluate the effectiveness of your system in ecosystem restoration and biodiversity preservation.
   b) Discuss how you would benchmark your system against current conservation practices.
   c) Address any potential limitations or challenges in implementing your system.
   d) Explain how you would measure success given the specified constraint.

6. Ethical Implications (200-250 words):
   a) Identify potential ethical issues arising from the use of AI and biotechnology in ecosystem intervention.
   b) Discuss the potential long-term consequences of your approach on natural evolution and ecosystem dynamics.
   c) Propose guidelines for responsible development and use of AI-driven biotechnology in conservation.
   d) Address any ethical considerations specific to the given constraint.

7. Experimental Validation (150-200 words):
   a) Design an experiment to test the effectiveness and safety of your system in a controlled environment.
   b) Describe the methodology, including how you would measure ecosystem health and biodiversity.
   c) Discuss potential challenges in scaling up from experimental trials to full ecosystem implementation.
   d) Explain how your experimental design accounts for the specified constraint.

Ensure your response demonstrates a deep understanding of biotechnology, artificial intelligence, and ecology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and ecological responsibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count ranges provided for each section. Your total response should be between 1550-1900 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly address the {t['ecosystem']} ecosystem, incorporate {t['biotech_approach']} as the biotechnology approach, and utilize {t['ai_technique']} as the AI technique.",
            f"The system should specifically address the conservation of the {t['endangered_species']} and provide concrete examples of how it would be implemented.",
            f"The proposed solution should adequately address the given constraint: {t['constraint']}.",
            "The response should demonstrate a novel and plausible approach to ecosystem restoration and biodiversity preservation, with clear strategies for improving the given biodiversity index and carbon sequestration rate.",
            "The submission should show a deep understanding of the complexities and challenges in integrating biotechnology, AI, and ecological principles.",
            "The ethical implications, potential risks, and negative consequences or trade-offs should be thoroughly considered and addressed.",
            "The response should include all seven requested sections with appropriate detail and scientific rigor, adhering to the specified word count ranges.",
            "The proposed experimental validation should be well-designed, appropriate for testing the system's effectiveness and safety, and account for the specified constraint."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
