import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "isolated islands",
            "interconnected city-states",
            "nomadic tribes in a vast desert",
            "underwater colonies",
            "space stations orbiting different planets"
        ]
        cognitive_factors = [
            "varying memory capacities",
            "different perceptual abilities",
            "diverse emotional processing",
            "varying levels of abstract reasoning",
            "different rates of learning and adaptation"
        ]
        linguistic_features = [
            "phonological inventories",
            "syntactic structures",
            "semantic categorizations",
            "pragmatic conventions",
            "writing systems"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "cognitive_factor": random.choice(cognitive_factors),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "environment": random.choice(environments),
                "cognitive_factor": random.choice(cognitive_factors),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a multi-agent simulation system that models the evolution of language and thought patterns in a dynamic environment of {t['environment']}, then analyze the emergent linguistic phenomena. Your simulation should incorporate {t['cognitive_factor']} as a key cognitive factor influencing agent interactions, and focus on the evolution of {t['linguistic_feature']} as the primary linguistic feature of interest.

Your response should include the following sections:

1. Simulation Design (300-350 words):
   a) Describe the overall architecture of your multi-agent simulation system.
   b) Explain how you model the {t['environment']} and implement {t['cognitive_factor']} in your agents.
   c) Detail how you represent and evolve {t['linguistic_feature']} within the simulation.
   d) Discuss how agents interact and communicate within the system.

2. Implementation Approach (250-300 words):
   a) Outline the key algorithms or computational techniques used in your simulation.
   b) Explain how you handle the evolution and transmission of linguistic features over time.
   c) Describe how you measure and analyze the emergent linguistic phenomena.
   d) Provide a short pseudocode snippet (10-15 lines) illustrating a crucial part of your implementation.

3. Simulation Results and Analysis (300-350 words):
   a) Describe the outcomes of running your simulation over an extended period.
   b) Analyze the patterns or trends observed in the evolution of {t['linguistic_feature']}.
   c) Discuss any unexpected or emergent phenomena that arose during the simulation.
   d) Explain how the {t['cognitive_factor']} influenced the evolution of language in your simulation.

4. Theoretical Implications (200-250 words):
   a) Discuss how your simulation results relate to existing theories in linguistics or cognitive science.
   b) Propose a new hypothesis or theoretical framework based on your findings.
   c) Suggest potential real-world applications or implications of your simulation results.

5. Limitations and Future Work (150-200 words):
   a) Acknowledge any limitations or simplifying assumptions in your simulation.
   b) Propose extensions or improvements to address these limitations.
   c) Suggest future research directions based on your findings.

Ensure your response demonstrates a deep understanding of multi-agent systems, linguistic evolution, cognitive modeling, and complex systems analysis. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The simulation design effectively incorporates the {t['environment']} and {t['cognitive_factor']}.",
            f"The implementation approach clearly explains how {t['linguistic_feature']} are modeled and evolved.",
            "The analysis of simulation results is thorough and insightful.",
            "The theoretical implications are well-reasoned and innovative.",
            "The response demonstrates a deep understanding of multi-agent systems, linguistic evolution, and cognitive modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
