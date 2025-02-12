import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "setting": "underwater civilization",
                "resource_constraint": "limited access to surface materials",
                "economic_challenge": "develop a sustainable trade system"
            },
            {
                "setting": "space station network",
                "resource_constraint": "finite energy from distant star",
                "economic_challenge": "optimize resource allocation"
            },
            {
                "setting": "time-locked planet",
                "resource_constraint": "extreme temperature variations between day and night sides",
                "economic_challenge": "balance production and population distribution"
            },
            {
                "setting": "post-scarcity AI society",
                "resource_constraint": "limited human creativity",
                "economic_challenge": "create meaningful economic roles for humans"
            },
            {
                "setting": "subterranean fungal network",
                "resource_constraint": "limited sunlight and water",
                "economic_challenge": "establish an efficient resource sharing system"
            },
            {
                "setting": "nomadic interstellar civilization",
                "resource_constraint": "constantly changing planetary environments",
                "economic_challenge": "maintain economic stability during frequent relocations"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a fictional economic system for a {t['setting']} with the following constraints and challenges:\n\nResource Constraint: {t['resource_constraint']}\nEconomic Challenge: {t['economic_challenge']}\n\nYour response should include the following sections, clearly labeled:\n\n1. System Overview: A brief description of the economic system (2-3 sentences)\n2. Key Principles: Three key economic principles or mechanisms that address the resource constraint and economic challenge (1-2 sentences each)\n3. Unintended Consequence: One potential unintended consequence of your economic system and how it might be mitigated (2-3 sentences)\n4. Unique Currency: A creative idea for a unique currency or medium of exchange in this economy (1-2 sentences)\n5. Societal Impact: An explanation of how this economic system might influence the society's cultural values or social structures (2-3 sentences)\n\nEnsure your economic system is logically consistent, creative, and effectively addresses the given constraints and challenges."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The economic system effectively addresses the {t['resource_constraint']} and the challenge to {t['economic_challenge']}.",
            "The proposed economic principles or mechanisms are logical, well-reasoned, and innovative.",
            "The potential unintended consequence and its mitigation strategy are plausible, insightful, and demonstrate systemic thinking.",
            "The unique currency or medium of exchange is creative, appropriate for the given setting, and aligns with the economic system's principles.",
            "The explanation of societal impact demonstrates a deep understanding of the relationship between economics, culture, and social structures.",
            "The response follows the specified format with clearly labeled sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
