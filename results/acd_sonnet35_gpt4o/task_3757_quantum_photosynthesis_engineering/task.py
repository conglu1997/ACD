import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_effect": "quantum coherence",
                "plant_type": "cereal crops (e.g., wheat, rice)"
            },
            {
                "quantum_effect": "quantum entanglement",
                "plant_type": "legumes (e.g., soybeans, lentils)"
            },
            {
                "quantum_effect": "quantum tunneling",
                "plant_type": "fruit-bearing trees (e.g., apple trees, orange trees)"
            },
            {
                "quantum_effect": "superposition",
                "plant_type": "leafy greens (e.g., spinach, lettuce)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-enhanced photosynthesis system for {t['plant_type']}, focusing on the quantum effect of {t['quantum_effect']}. Then, analyze its potential impact on global food production and climate change mitigation. Your response should include:

1. Quantum-Enhanced Photosynthesis Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum-enhanced photosynthesis system.
   b) Explain how you incorporate {t['quantum_effect']} into the photosynthetic process.
   c) Discuss how your design improves upon natural photosynthesis in {t['plant_type']}.
   d) Address potential challenges in implementing this system in living plants.
   e) Provide a diagram or equation illustrating a key aspect of your design (describe it textually).

2. Quantum Biology Principles (200-250 words):
   a) Explain the relevant quantum mechanical principles underlying your design.
   b) Discuss how these quantum effects can persist in a warm, wet biological environment.
   c) Compare your proposed mechanism to known or hypothesized quantum effects in biological systems.
   d) Cite at least two relevant scientific papers or resources to support your explanations.

3. Agricultural Impact Analysis (250-300 words):
   a) Estimate the potential increase in crop yield or efficiency for {t['plant_type']} (provide a quantitative estimate with justification).
   b) Analyze how widespread adoption of your system could affect global food production and security.
   c) Discuss potential ecological impacts of introducing quantum-enhanced plants into agricultural ecosystems.
   d) Critically analyze potential limitations or drawbacks of your proposed system.

4. Climate Change Mitigation (200-250 words):
   a) Calculate the potential increase in carbon sequestration resulting from your enhanced photosynthesis system (provide a quantitative estimate with justification).
   b) Analyze how this could contribute to global efforts to mitigate climate change.
   c) Discuss any potential negative climate impacts and how they might be addressed.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss ethical considerations of using quantum-enhanced plants in agriculture.
   b) Analyze potential socioeconomic impacts, including effects on farmers and global food markets.
   c) Propose guidelines for responsible development and deployment of this technology.

6. Future Research Directions (150-200 words):
   a) Suggest next steps for experimentally validating your quantum-enhanced photosynthesis system.
   b) Propose potential applications of your system beyond agriculture (e.g., in energy production or environmental remediation).
   c) Discuss how your approach could be extended to other biological processes.

Ensure your response demonstrates a deep understanding of quantum mechanics, plant biology, and global agricultural systems. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above (1, 2, 3, 4, 5, 6). Begin each section with the heading on a new line, followed by your response for that section. Use subheadings (a, b, c, d, e) within each section to organize your thoughts. Provide in-text citations where appropriate, and include a brief references section at the end of your response.

Your total response should be between 1250-1550 words, excluding the references section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the quantum effect of {t['quantum_effect']} and apply it to {t['plant_type']}",
            "The quantum-enhanced photosynthesis design should be detailed, innovative, and scientifically plausible",
            "The response should demonstrate a deep understanding of both quantum mechanics and plant biology",
            "The analysis of agricultural impact and climate change mitigation should be thorough and include quantitative estimates with justification",
            "The ethical and societal implications should be thoughtfully considered",
            "The proposed future research directions should be relevant and promising",
            "The response should include at least one diagram or equation (described textually) illustrating a key concept",
            "The response should cite at least two relevant scientific papers or resources",
            "The response should critically analyze potential limitations or drawbacks of the proposed system",
            "The response should follow the specified format with clear headings and subheadings"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
