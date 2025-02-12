import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_biology_scenarios = [
            {
                "biological_process": "Photosynthesis",
                "quantum_effect": "Quantum coherence",
                "technological_constraint": "Limited ability to observe quantum effects in warm, wet environments"
            },
            {
                "biological_process": "Magnetoreception in birds",
                "quantum_effect": "Radical pair mechanism",
                "technological_constraint": "Difficulty in isolating and manipulating specific molecules in living organisms"
            },
            {
                "biological_process": "Enzyme catalysis",
                "quantum_effect": "Quantum tunneling",
                "technological_constraint": "Challenges in detecting and measuring quantum effects at the molecular level"
            },
            {
                "biological_process": "Olfaction (sense of smell)",
                "quantum_effect": "Vibrational theory of olfaction",
                "technological_constraint": "Difficulty in distinguishing quantum effects from classical molecular vibrations"
            }
        ]
        return {
            "1": random.choice(quantum_biology_scenarios),
            "2": random.choice(quantum_biology_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical experiment to detect and measure quantum effects in biological systems, focusing on the biological process of {t['biological_process']} and the quantum effect of {t['quantum_effect']}. Consider the technological constraint: {t['technological_constraint']}. Your response should include the following sections:

1. Background (150-200 words):
   a) Briefly explain the biological process and its significance.
   b) Describe the relevant quantum effect and its potential role in the biological process.
   c) Discuss the current state of research in this area of quantum biology.

2. Experimental Design (250-300 words):
   a) Outline your proposed experiment, including its objectives and hypotheses.
   b) Describe the experimental setup, including any novel equipment or techniques.
   c) Explain how your design addresses the given technological constraint.
   d) Include a diagram or flowchart of your experimental setup (use ASCII art or a clear textual description).

3. Measurement and Data Analysis (200-250 words):
   a) Describe the specific quantum measurements you plan to make.
   b) Explain the data collection process and any required controls.
   c) Outline your approach to data analysis, including statistical methods.
   d) Discuss how you would distinguish quantum effects from classical phenomena.

4. Potential Outcomes and Interpretations (150-200 words):
   a) Describe possible experimental outcomes and their implications.
   b) Explain how these outcomes would support or refute the presence of quantum effects.
   c) Discuss potential alternative explanations for your results.

5. Challenges and Future Directions (150-200 words):
   a) Identify potential challenges or limitations of your experimental design.
   b) Propose solutions or future technological advancements that could address these challenges.
   c) Suggest follow-up experiments or research directions based on your hypothetical results.

6. Interdisciplinary Implications (100-150 words):
   a) Discuss how your experiment integrates concepts from quantum physics and biology.
   b) Explain potential implications of your research for other scientific fields.
   c) Consider possible technological applications inspired by your findings.

7. References (not included in word count):
   Cite at least 3-5 relevant scientific papers or reviews that inform your experimental design or provide context for your research question.

Ensure your response demonstrates a deep understanding of both quantum mechanics and molecular biology. Be creative in your experimental design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1400 words, excluding references."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all seven required sections as outlined in the instructions.",
            f"The experimental design must clearly focus on detecting and measuring {t['quantum_effect']} in the biological process of {t['biological_process']}.",
            f"The proposed experiment must address the technological constraint: {t['technological_constraint']}.",
            "The response must demonstrate a deep understanding of both quantum mechanics and molecular biology.",
            "The experimental design must be creative and novel while remaining scientifically plausible.",
            "The response must include appropriate technical terminology and clear explanations for complex concepts.",
            "The response must adhere to the specified word count range (1000-1400 words, excluding references) and formatting requirements.",
            "The response must include at least 3-5 relevant scientific references."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
