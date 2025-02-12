import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Hypergravity planet (5x Earth's gravity)",
            "Tidally locked planet (one side always faces its star)",
            "Underwater volcanic vent system",
            "Methane-based atmosphere",
            "Extreme temperature fluctuations (from -100°C to +100°C daily)"
        ]
        return {
            "1": {"environment": random.choice(environments)},
            "2": {"environment": random.choice(environments)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You have 15 minutes to complete this task. Design a fictional ecosystem for the following extreme environment: {t['environment']}\n\n1. Describe three unique species that have evolved to thrive in this environment. For each species, include:\n   a) Its role in the ecosystem (producer, consumer, decomposer)\n   b) Two specific adaptations that allow it to survive in the extreme conditions\n   c) How it interacts with at least one other species in the ecosystem\n\n2. Explain how energy flows through this ecosystem, considering the extreme conditions.\n\n3. Describe one potential threat to the ecosystem's balance and propose a mechanism that could help maintain stability.\n\n4. Hypothesize how this ecosystem might evolve over the next million years if the environmental conditions gradually become less extreme.\n\nProvide your response in the following format:\n\nSpecies 1:\n[Name]\nRole: [Producer/Consumer/Decomposer]\nAdaptations: [Adaptation 1], [Adaptation 2]\nInteraction: [Description of interaction with another species]\n\n[Repeat for Species 2 and 3]\n\nEnergy Flow:\n[Your explanation]\n\nEcosystem Threat and Stability:\nThreat: [Description of threat]\nStability Mechanism: [Description of mechanism]\n\nFuture Evolution:\n[Your hypothesis]\n\nEnsure that your ecosystem is logically consistent and takes into account the specific challenges posed by the extreme environment. Use scientific terminology where appropriate."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes three unique species with clear roles, specific adaptations relevant to the extreme environment, and logical interactions.",
            "The energy flow explanation is scientifically sound and consistent with the extreme environment.",
            "A plausible threat to the ecosystem's balance is identified, along with a reasonable and creative stabilizing mechanism.",
            "The evolutionary hypothesis is scientifically grounded, consistent with the gradual change in conditions, and demonstrates an understanding of long-term ecological processes.",
            "The overall ecosystem design is creative, logically consistent, and properly considers the challenges of the extreme environment, using appropriate scientific terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
