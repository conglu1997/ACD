import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        crops = [
            {
                'crop': 'rice',
                'climate_challenge': 'increasing temperatures',
                'quantum_principle': 'quantum coherence'
            },
            {
                'crop': 'wheat',
                'climate_challenge': 'drought',
                'quantum_principle': 'quantum entanglement'
            }
        ]
        return {str(i+1): crop for i, crop in enumerate(crops)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired system to optimize photosynthesis in {t['crop']} for enhanced agricultural productivity and resilience to {t['climate_challenge']}. Your system should incorporate the quantum principle of {t['quantum_principle']}. Provide your response in the following format:

1. Conceptual Framework (250-300 words):
   a) Explain how {t['quantum_principle']} can be applied to enhance photosynthesis in {t['crop']}.
   b) Describe how this quantum-inspired approach could address the challenge of {t['climate_challenge']}.
   c) Outline the key components of your proposed system and their interactions.

2. Quantum-Biological Mechanism (200-250 words):
   a) Detail the specific quantum mechanisms you propose to enhance photosynthetic efficiency.
   b) Explain how these mechanisms interact with the classical biological processes of photosynthesis.
   c) Discuss any potential trade-offs or limitations of your approach.

3. Implementation Strategy (200-250 words):
   a) Describe how your quantum-inspired system could be practically implemented in {t['crop']} cultivation.
   b) Outline any genetic modifications or bioengineering techniques that might be necessary.
   c) Discuss potential challenges in scaling this technology from laboratory to field conditions.

4. Climate Resilience Analysis (150-200 words):
   a) Analyze how your system enhances {t['crop']}'s resilience to {t['climate_challenge']}.
   b) Quantify the potential improvement in crop yield or resource efficiency, providing realistic estimates.
   c) Discuss any potential vulnerabilities or limitations of your approach in addressing climate challenges.

5. Ethical and Ecological Considerations (150-200 words):
   a) Identify potential ethical concerns related to the use of quantum-inspired modifications in food crops.
   b) Discuss possible ecological impacts, both positive and negative, of implementing your system.
   c) Propose guidelines for responsible development and use of quantum-enhanced crops.

6. Future Research Directions (150-200 words):
   a) Suggest two potential research projects that could further develop or validate your quantum-inspired approach.
   b) Discuss how these projects could contribute to our understanding of quantum effects in biological systems.
   c) Propose potential applications of your approach beyond {t['crop']} cultivation.

Ensure your response demonstrates a deep understanding of quantum mechanics, plant biology, and agricultural science. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum mechanics, plant biology, and agricultural science, particularly in relation to {t['crop']} and {t['climate_challenge']}",
            f"The proposed system effectively incorporates {t['quantum_principle']} to enhance photosynthesis",
            "The implementation strategy is practical and addresses real-world challenges",
            "The climate resilience analysis provides realistic and quantifiable improvements",
            "Ethical and ecological considerations are thoroughly addressed",
            "Future research directions are insightful and well-reasoned",
            "The response is innovative while maintaining scientific plausibility",
            "The response adheres to the specified word limit (1100-1400 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
