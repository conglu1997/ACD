import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "biotechnology": "CRISPR-based enhancement of human memory capacity",
                "quantum_principle": "quantum coherence in neural networks",
                "ethical_framework": "virtue ethics focusing on intellectual excellence"
            },
            {
                "biotechnology": "Synthetic photosynthetic organisms for atmospheric carbon capture",
                "quantum_principle": "quantum entanglement in energy transfer",
                "ethical_framework": "utilitarianism emphasizing global well-being"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates the ethical implications of a specific aspect of an advanced biotechnology, focusing on the intersection of quantum biology and moral philosophy. Your task involves the following:

Biotechnology: {t['biotechnology']}
Quantum principle: {t['quantum_principle']}
Ethical framework: {t['ethical_framework']}

Your response should include the following sections:

1. Quantum-Biological Model (200-250 words):
   a) Describe how you would model the specified biotechnology using quantum computing principles.
   b) Explain how the given quantum principle is incorporated into your model.
   c) Provide a simple quantum circuit diagram or pseudocode to illustrate your approach.

2. Ethical Framework Integration (200-250 words):
   a) Explain how you incorporate the specified ethical framework into your quantum simulation.
   b) Describe how at least two ethical principles are represented in your quantum system.

3. Simulation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system simulates the ethical implications of the biotechnology.
   b) Explain how quantum and classical computing elements interact in your simulation.

4. Ethical Analysis (200-250 words):
   a) Describe one potential ethical dilemma or implication revealed by your simulation.
   b) Discuss how quantum effects in your simulation might lead to novel ethical insights or challenges.

5. Societal Impact and Policy Recommendation (150-200 words):
   a) Based on your simulation results, propose one policy recommendation for the ethical governance of the specified biotechnology.
   b) Discuss potential societal impacts of implementing this policy.

6. Limitations and Future Directions (100-150 words):
   a) Identify one potential limitation of your quantum bioethics simulation approach.
   b) Propose one idea for future research or improvement to your system.

Ensure your response demonstrates an understanding of quantum computing, biology, and ethical philosophy. Your quantum computing knowledge should include basic concepts such as qubits, superposition, and entanglement. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words. Include at least two relevant citations or references to support your proposed ideas and concepts. You have 120 minutes to complete this task.

A successful response will:
1. Clearly connect the quantum principle to the biological system.
2. Demonstrate a logical integration of the ethical framework into the quantum simulation.
3. Provide a coherent simulation process that combines quantum and classical elements.
4. Present a plausible ethical dilemma arising from the simulation.
5. Offer a reasonable policy recommendation based on the simulation results.
6. Identify a relevant limitation and future direction for the approach."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The quantum-biological model incorporates the specified quantum principle and includes a simple quantum circuit diagram or pseudocode.",
            "The ethical framework integration explains how at least two ethical principles are represented in the quantum system.",
            "The simulation process describes both quantum and classical computing elements.",
            "The ethical analysis presents one ethical dilemma or implication derived from the simulation, with a clear link to quantum effects.",
            "The response includes one specific policy recommendation based on the simulation results, with analysis of its potential societal impact.",
            "The limitations and future directions section addresses one potential shortcoming of the approach and suggests one concrete improvement.",
            "The response demonstrates an understanding of basic quantum computing concepts, biology, and ethical philosophy, using appropriate terminology.",
            "The response includes at least two relevant citations or references to support the proposed ideas.",
            "The response adheres to the specified word count guidelines for each section (within 10% margin)."
        ]
        scores = [int(eval_with_llm_judge(instructions, submission, [criterion])) for criterion in criteria]
        return max(0.1, sum(scores) / len(scores))  # Ensure a minimum score of 0.1 for any submission
