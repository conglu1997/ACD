import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Hypersaline deep-sea hydrothermal vent",
            "Radioactive waste site",
            "Martian subsurface",
            "Sulfuric acid cave system"
        ]
        cellular_processes = [
            "Energy metabolism",
            "Cell membrane adaptation",
            "DNA repair mechanisms",
            "Protein folding under extreme conditions"
        ]
        ai_techniques = [
            "Reinforcement learning",
            "Genetic algorithms",
            "Neural networks",
            "Swarm intelligence"
        ]
        tasks = {
            "1": {
                "environment": random.choice(environments),
                "cellular_process": random.choice(cellular_processes),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "environment": random.choice(environments),
                "cellular_process": random.choice(cellular_processes),
                "ai_technique": random.choice(ai_techniques)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven simulator that models cellular evolution and adaptation in complex biological systems, then use it to predict emergent behaviors in a hypothetical extreme environment. Focus on the environment of a {t['environment']}, the cellular process of {t['cellular_process']}, and utilize the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. Simulator Architecture (300-350 words):
   a) Describe the key components of your AI-driven cellular evolution simulator.
   b) Explain how you integrate {t['ai_technique']} into your simulator design.
   c) Detail how your simulator models {t['cellular_process']} at the cellular level.
   d) Discuss how your system simulates evolutionary processes and adaptation.

2. Environmental Modeling (250-300 words):
   a) Describe how your simulator represents the {t['environment']}.
   b) Explain the key environmental factors and their impact on cellular processes.
   c) Discuss how your model accounts for the dynamic nature of this extreme environment.

3. Cellular Adaptation Mechanisms (250-300 words):
   a) Explain how your simulator models cellular adaptation to the extreme environment.
   b) Describe the specific mechanisms involved in adapting {t['cellular_process']}.
   c) Discuss how your model balances fidelity to biological processes with computational feasibility.

4. Emergent Behavior Predictions (300-350 words):
   a) Use your simulator to predict three emergent behaviors or adaptations in the given environment.
   b) Explain the reasoning behind each prediction, based on your model's processes.
   c) Describe how these adaptations might affect the broader ecosystem or potential applications.

5. Validation and Limitations (200-250 words):
   a) Propose methods to validate your simulator's predictions against real-world data.
   b) Discuss the limitations of your approach and potential sources of error.
   c) Suggest improvements or extensions to enhance the simulator's accuracy and applicability.

6. Ethical Implications and Applications (150-200 words):
   a) Discuss potential ethical considerations in using AI to simulate and predict biological evolution.
   b) Explore possible applications of your simulator in fields such as astrobiology, bioengineering, or environmental science.
   c) Address any potential misuse or dual-use concerns related to your technology.

Ensure your response demonstrates a deep understanding of systems biology, artificial intelligence, and evolutionary processes. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive simulator architecture that integrates {t['ai_technique']}, models {t['cellular_process']}, and simulates evolution and adaptation.",
            f"The environmental modeling section effectively represents the {t['environment']} and its impact on cellular processes.",
            "The cellular adaptation mechanisms are well-explained and balance biological fidelity with computational feasibility.",
            "The emergent behavior predictions are logical, well-reasoned, and derived from the simulator's processes.",
            "The response addresses validation methods, limitations, and potential improvements to the simulator.",
            "The submission demonstrates a deep understanding of systems biology, artificial intelligence, and evolutionary processes, and effectively integrates these fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
