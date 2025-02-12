import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {"name": "Coral Reef", "key_species": ["coral", "clownfish", "parrotfish", "sea urchin"]},
            {"name": "Tropical Rainforest", "key_species": ["jaguar", "toucan", "bromeliad", "leaf-cutter ant"]},
            {"name": "Arctic Tundra", "key_species": ["polar bear", "arctic fox", "lemming", "caribou"]},
            {"name": "Savanna Grassland", "key_species": ["lion", "elephant", "acacia tree", "termite"]}
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm to simulate and optimize evolutionary processes in a {t['name']} ecosystem, focusing on the following key species: {', '.join(t['key_species'])}. Your response should include:

1. Quantum Representation (150-200 words):
   Explain how you would represent the genetic information and environmental factors of the ecosystem using quantum states. Describe the quantum gates or operations you would use to encode this information.

2. Evolutionary Operators (200-250 words):
   Design quantum versions of common evolutionary operators (e.g., mutation, crossover, selection). Explain how these quantum operators would work and how they differ from classical evolutionary algorithms.

3. Fitness Evaluation (150-200 words):
   Describe a quantum method for evaluating the fitness of individuals in the ecosystem. Explain how this method leverages quantum superposition or entanglement to efficiently compute fitness across multiple criteria.

4. Optimization Process (200-250 words):
   Outline the steps of your quantum evolutionary algorithm, explaining how it would simulate and optimize the evolutionary processes in the given ecosystem. Include at least one quantum subroutine (e.g., Grover's algorithm, quantum Fourier transform) in your design.

5. Complexity Analysis (100-150 words):
   Provide a brief analysis of the time and space complexity of your quantum algorithm. Compare its theoretical performance to a classical evolutionary algorithm for the same problem.

6. Ecological Insights (150-200 words):
   Discuss how your quantum evolutionary algorithm might provide new insights into the dynamics of the given ecosystem. Propose a specific ecological question that your algorithm could help answer.

7. Technical Challenges (100-150 words):
   Identify at least two technical challenges in implementing your algorithm on current or near-term quantum hardware. Suggest potential approaches to addressing these challenges.

Ensure your response demonstrates a deep understanding of both quantum computing principles and evolutionary biology concepts. Be creative in your approach while maintaining scientific and mathematical rigor. Use appropriate notation and terminology from both fields."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of quantum computing principles and evolutionary biology concepts.",
            "The quantum representation of genetic information and environmental factors is well-explained and plausible.",
            "The quantum versions of evolutionary operators are creative and leverage quantum properties effectively.",
            "The fitness evaluation method uses quantum mechanics principles innovatively.",
            "The overall algorithm design is coherent and incorporates at least one quantum subroutine appropriately.",
            "The complexity analysis compares quantum and classical approaches meaningfully.",
            "The proposed ecological insights and questions are relevant and thoughtful.",
            "Technical challenges are realistically assessed with potential solutions proposed.",
            "The response uses appropriate notation and terminology from both quantum computing and evolutionary biology.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
