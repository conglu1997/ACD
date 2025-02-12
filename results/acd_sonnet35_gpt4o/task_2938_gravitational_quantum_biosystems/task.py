import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "gravitational_context": "microgravity environment in low Earth orbit",
                "quantum_process": "quantum entanglement in photosynthetic complexes",
                "biological_system": "cyanobacteria colonies",
                "gravitational_field_strength": "9.5 m/s^2",
                "quantum_coherence_time": "500 femtoseconds"
            },
            "2": {
                "gravitational_context": "varying gravitational fields on a rogue planet",
                "quantum_process": "quantum tunneling in enzyme catalysis",
                "biological_system": "extremophile microbial mats",
                "gravitational_field_strength": "3.7 m/s^2 to 15.2 m/s^2",
                "quantum_coherence_time": "200 femtoseconds"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for studying the effects of gravitational fields on quantum information processing in biological systems, and propose a complex adaptive system model based on this framework. Your task focuses on the following specific scenario:

Gravitational context: {t['gravitational_context']}
Quantum process: {t['quantum_process']}
Biological system: {t['biological_system']}
Gravitational field strength: {t['gravitational_field_strength']}
Quantum coherence time: {t['quantum_coherence_time']}

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how gravitational fields might influence quantum information processing in biological systems.
   b) Describe the potential interactions between the specified quantum process and gravitational context.
   c) Discuss how these interactions could affect the functioning of the given biological system.
   d) Propose a unified model that integrates gravitational biology, quantum information theory, and complex adaptive systems.

2. Mathematical Formulation (250-300 words):
   a) Develop a mathematical representation of your model, incorporating elements from general relativity, quantum mechanics, and complex systems theory.
   b) Explain the key variables, equations, or algorithms in your formulation.
   c) Discuss how your mathematical model captures the interplay between gravitational effects, quantum processes, and biological adaptation.

3. Complex Adaptive System Model (200-250 words):
   a) Describe how your framework can be used to model the specified biological system as a complex adaptive system.
   b) Explain the emergent properties or behaviors you expect to observe in this system.
   c) Discuss how the gravitational context and quantum processes contribute to the system's adaptability and evolution.

4. Predictions and Testable Hypotheses (200-250 words):
   a) Describe at least two specific, testable predictions that your model makes about the behavior or properties of the biological system under the given conditions.
   b) Explain how these predictions differ from those of conventional biological or physical models.
   c) Propose experiments or observations that could validate or refute your model, considering the challenges of the gravitational context.

5. Implications and Applications (200-250 words):
   a) Discuss the broader implications of your framework for our understanding of life in extreme environments, including potential extraterrestrial contexts.
   b) Explore potential technological applications that could arise from your model, such as in biotechnology or quantum computing.
   c) Address how your framework might contribute to the search for life in the universe or the development of life support systems for space exploration.

6. Limitations and Future Directions (150-200 words):
   a) Acknowledge the limitations and potential criticisms of your model.
   b) Suggest areas for future research or refinement of your theory.
   c) Discuss how advancements in gravitational biology, quantum information theory, or complex systems science might impact your model.

Ensure your response demonstrates a deep understanding of general relativity, quantum mechanics, biology, and complex systems theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Theoretical Framework:') on a new line, followed by your response for that section. Use subheadings (a, b, c, d) within each section as outlined above. Your total response should be between 1300-1600 words, with each section adhering to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all six required sections with appropriate content and word counts.",
            "The theoretical framework should coherently integrate gravitational biology, quantum information theory, and complex adaptive systems, specifically addressing the given gravitational context, quantum process, and biological system.",
            "The mathematical formulation should incorporate elements from general relativity, quantum mechanics, and complex systems theory, and include at least one equation or algorithm.",
            "The complex adaptive system model should clearly explain how the biological system adapts and evolves under the given gravitational and quantum conditions.",
            "At least two specific, testable predictions should be provided, along with proposed experiments or observations that are feasible given the gravitational context.",
            "The response should demonstrate a deep understanding of the relevant scientific fields, use appropriate technical terminology, and correctly utilize the provided gravitational field strength and quantum coherence time in the analysis.",
            "The proposed framework should be innovative and speculative while maintaining scientific plausibility and logical consistency with current understanding of gravitational biology and quantum processes.",
            "The response must follow the specified format, including clear headings, subheadings, and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
