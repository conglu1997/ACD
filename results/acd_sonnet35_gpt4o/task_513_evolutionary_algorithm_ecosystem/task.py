import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "deep sea hydrothermal vent",
            "Martian terraformed colony",
            "post-apocalyptic urban environment",
            "quantum realm microverse",
            "bioluminescent cave system"
        ]
        evolutionary_pressures = [
            "extreme temperature fluctuations",
            "limited energy resources",
            "high levels of radiation",
            "rapidly changing pH levels",
            "presence of exotic matter"
        ]
        organism_types = [
            "photosynthetic microorganisms",
            "silicon-based lifeforms",
            "energy field entities",
            "nanomachine swarms",
            "quantum-entangled organisms"
        ]
        
        tasks = {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "evolutionary_pressure": random.choice(evolutionary_pressures),
                "organism_type": random.choice(organism_types)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "evolutionary_pressure": random.choice(evolutionary_pressures),
                "organism_type": random.choice(organism_types)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and simulate a virtual ecosystem using evolutionary algorithms, then analyze its behavior and propose real-world applications. Your task involves the following steps:

1. Ecosystem Design (200-250 words):
   a) Describe a virtual ecosystem based on a {t['ecosystem']} environment.
   b) Explain how you would model the {t['evolutionary_pressure']} as the main evolutionary pressure.
   c) Describe the characteristics and behavior of {t['organism_type']} as the primary organisms in this ecosystem.
   d) Outline the key parameters and variables you would use in your simulation.

2. Evolutionary Algorithm (200-250 words):
   a) Design an evolutionary algorithm that simulates the adaptation of the organisms to the environment.
   b) Explain the fitness function, selection method, and genetic operators you would use.
   c) Describe how your algorithm handles the specific evolutionary pressure.

3. Simulation Results (200-250 words):
   a) Describe the expected outcomes of running your simulation over 100 generations.
   b) Explain any emergent behaviors or unexpected adaptations you might anticipate.
   c) Discuss how the organisms might evolve to cope with the main evolutionary pressure.

4. Analysis (150-200 words):
   a) Analyze the strengths and limitations of your model.
   b) Discuss how well this simulation might represent real-world evolutionary processes.
   c) Explain how this model could be improved or expanded.

5. Real-world Applications (150-200 words):
   a) Propose two potential real-world applications of your evolutionary algorithm or the insights gained from this simulation.
   b) Explain how these applications could contribute to scientific research or technological advancement.

Ensure your response demonstrates a deep understanding of evolutionary biology, computer science, and the specific ecosystem components. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 900-1150 words. Manage your time wisely to address all sections thoroughly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of a virtual {t['ecosystem']} environment",
            f"The simulation incorporates {t['evolutionary_pressure']} as the main evolutionary pressure",
            f"The primary organisms in the ecosystem are described as {t['organism_type']}",
            "An evolutionary algorithm is designed with a clear fitness function, selection method, and genetic operators",
            "The expected outcomes of the simulation over 100 generations are described",
            "The response includes an analysis of the model's strengths and limitations",
            "Two potential real-world applications of the algorithm or simulation insights are proposed",
            "The response demonstrates interdisciplinary knowledge of biology, computer science, and complex systems",
            "The ideas presented are creative while maintaining scientific plausibility",
            "The response is well-structured with clear headings and numbered paragraphs",
            "The total response falls within the specified word count range of 900-1150 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
