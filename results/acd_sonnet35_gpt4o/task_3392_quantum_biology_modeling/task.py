import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                "system": "photosynthesis",
                "quantum_effect": "quantum coherence",
                "application": "artificial photosynthesis for clean energy"
            },
            {
                "system": "avian magnetoreception",
                "quantum_effect": "radical pair mechanism",
                "application": "biomimetic quantum sensors for navigation"
            }
        ]
        return {str(i+1): system for i, system in enumerate(biological_systems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates quantum effects in biological systems, focusing on {t['system']} and the quantum effect of {t['quantum_effect']}. Then, use your model to investigate potential applications in {t['application']}. Your response should include the following sections:

1. Quantum Biology Background (200-250 words):
   a) Explain the current understanding of quantum effects in {t['system']}.
   b) Describe the role of {t['quantum_effect']} in this biological process.
   c) Discuss the challenges in studying and modeling these quantum effects.

2. Computational Model Design (300-350 words):
   a) Propose a computational framework for simulating {t['quantum_effect']} in {t['system']}.
   b) Describe the key components of your model, including quantum and classical elements.
   c) Explain how your model integrates quantum mechanics with biological complexity.
   d) Provide a high-level pseudocode or flow diagram of your simulation. (Note: This should include at least 5-7 key steps or components of your model, with brief explanations for each.)

3. Simulation Methodology (200-250 words):
   a) Describe the specific quantum algorithms or techniques used in your model.
   b) Explain how you would validate your model against experimental data.
   c) Discuss any simplifications or assumptions made in your model.

4. Predicted Outcomes (200-250 words):
   a) Describe the expected results from your quantum biology simulation.
   b) Explain how these results could provide insights into the biological process.
   c) Discuss any potential surprises or novel predictions from your model.

5. Application to {t['application']} (250-300 words):
   a) Propose a specific application of your model to {t['application']}.
   b) Describe how the quantum effects simulated could be harnessed or mimicked.
   c) Discuss the potential benefits and challenges of this application.
   d) Outline a research and development roadmap for realizing this application.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues related to your proposed application.
   b) Suggest guidelines for responsible development of quantum biology-inspired technologies.
   c) Propose two future research directions that could extend your work.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, and computational modeling",
            "The proposed computational model is innovative and plausibly incorporates quantum effects in biological systems",
            "The explanation of the simulation methodology is clear and scientifically sound",
            "The application proposal is creative and demonstrates a clear link to the quantum biology model",
            "The response addresses all required sections comprehensively and meets the word count requirement",
            "The discussion of ethical considerations and future directions is thoughtful and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
