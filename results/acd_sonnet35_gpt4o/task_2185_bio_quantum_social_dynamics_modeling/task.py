import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_phenomena = [
            {
                "phenomenon": "Cultural Evolution",
                "description": "The process by which cultures change and develop over time",
                "key_feature": "Transmission and modification of cultural traits"
            },
            {
                "phenomenon": "Collective Intelligence",
                "description": "The ability of groups to solve problems or make decisions that are better than those of individual members",
                "key_feature": "Emergent group-level cognitive capabilities"
            },
            {
                "phenomenon": "Social Contagion",
                "description": "The spread of behaviors, attitudes, or emotions through a population",
                "key_feature": "Network-based transmission of social information"
            },
            {
                "phenomenon": "Societal Tipping Points",
                "description": "Critical thresholds at which small changes can lead to large-scale societal shifts",
                "key_feature": "Nonlinear dynamics in social systems"
            }
        ]
        quantum_principles = ["Superposition", "Entanglement", "Quantum Tunneling", "Quantum Coherence"]
        biological_processes = ["Neural Signaling", "Genetic Inheritance", "Cellular Differentiation", "Symbiosis"]
        
        return {
            "1": {
                "social_phenomenon": random.choice(social_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes)
            },
            "2": {
                "social_phenomenon": random.choice(social_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical bio-quantum computing system for modeling and predicting the complex emergent phenomenon of {t['social_phenomenon']['phenomenon']} in social systems. Your system should incorporate the quantum principle of {t['quantum_principle']} and draw inspiration from the biological process of {t['biological_process']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your bio-quantum computing system.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your system.
   c) Describe how your system draws inspiration from {t['biological_process']}.
   d) Explain how these elements come together to model {t['social_phenomenon']['phenomenon']}.
   e) Include a simple diagram or schematic representation of your system (using ASCII art or a clear textual description). The diagram description should not exceed 100 words.

2. Modeling Approach (250-300 words):
   a) Explain how your system models the key feature of {t['social_phenomenon']['phenomenon']}: {t['social_phenomenon']['key_feature']}.
   b) Describe the data inputs your system would require and how it would process them.
   c) Discuss how your bio-quantum approach might offer advantages over classical modeling techniques for this social phenomenon.

3. Predictive Capabilities (200-250 words):
   a) Describe the types of predictions or insights your system could generate about {t['social_phenomenon']['phenomenon']}.
   b) Explain how these predictions could be validated or tested.
   c) Discuss any limitations or potential biases in your system's predictive capabilities.

4. Potential Applications (200-250 words):
   a) Propose two potential real-world applications of your bio-quantum social modeling system.
   b) For each application, explain the potential benefits and any challenges in implementation.
   c) Discuss how these applications might impact social science research or policy-making.

5. Ethical Implications (250-300 words):
   a) Identify three potential ethical concerns raised by your bio-quantum social modeling system.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Discuss the broader societal implications of using such advanced predictive systems for social phenomena.

6. Future Research Directions (150-200 words):
   a) Suggest two areas for further research to enhance or expand your bio-quantum social modeling system.
   b) Explain how these research directions could address current limitations or open up new possibilities.
   c) Discuss potential interdisciplinary collaborations that could drive innovation in this field.

Ensure your response demonstrates a deep understanding of quantum computing, biology, sociology, and complex systems theory. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words, not including the system diagram. The system diagram should be included as a separate, clearly labeled section after the main text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']}, {t['biological_process']}, and {t['social_phenomenon']['phenomenon']}.",
            "The proposed bio-quantum computing system is innovative and coherently integrates concepts from multiple disciplines.",
            f"The modeling approach effectively addresses the key feature of {t['social_phenomenon']['phenomenon']}: {t['social_phenomenon']['key_feature']}.",
            "The predictive capabilities and their limitations are well-explained and plausible.",
            "The potential applications are relevant, and their implications are thoroughly analyzed.",
            "The ethical analysis is comprehensive and thoughtful, with appropriate use of ethical frameworks.",
            "The proposed future research directions are insightful and have the potential to advance the field.",
            "The response is well-structured, coherent, and adheres to the specified word limits, including the 100-word limit for the system diagram description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
