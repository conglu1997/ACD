class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "An ecosystem consists of various species of plants and animals that interact with each other and their environment. Suppose a new species of predator is introduced to this ecosystem. The predator primarily preys on a specific herbivore species, which in turn feeds on a particular plant species. The initial population sizes are: Predators: 0, Herbivores: 100, Plants: 500. The new predator has a high reproduction rate and no natural enemies in the ecosystem.", "question": "Analyze the potential impact of introducing the new predator on the ecosystem over the next 10 years. Consider the effects on the populations of the predator, herbivore, and plant species, as well as any broader ecosystem impacts."},
            "2": {"scenario": "A small economy consists of three sectors: agriculture, manufacturing, and services. The government decides to implement a policy that heavily subsidizes the manufacturing sector to boost industrial growth. Initially, the economy is balanced with 30% of the workforce in agriculture, 40% in manufacturing, and 30% in services. The manufacturing sector's increased productivity leads to cheaper goods, but also to environmental pollution.", "question": "Analyze the potential short-term and long-term effects of this policy on the economy, workforce distribution, and environment. Consider the interdependencies between the sectors and any potential unintended consequences."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following complex system scenario:

{t['scenario']}

Your response should include:
1. A detailed analysis of the system's components and their interactions.
2. Predictions of the short-term and long-term effects of the described change.
3. Consideration of any broader implications or unintended consequences.
4. A clear and logical explanation of your reasoning.

Ensure your response is well-organized, logically structured, and includes all required components in a clear manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed analysis of the system's components and their interactions.",
            "The response should provide predictions of the short-term and long-term effects of the described change.",
            "The response should consider any broader implications or unintended consequences.",
            "The response should be well-organized and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
