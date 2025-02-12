class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_process": "decision-making under uncertainty",
                "quantum_principle": "superposition",
                "application_domain": "financial market prediction"
            },
            "2": {
                "cognitive_process": "belief updating",
                "quantum_principle": "entanglement",
                "application_domain": "consumer behavior modeling"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for a quantum-inspired cognitive AI system that simulates human-like {t['cognitive_process']}, focusing on the quantum principle of {t['quantum_principle']}. Then, apply your system to solve complex problems in the domain of {t['application_domain']}. Your response should include the following sections:

1. Quantum Cognitive AI Framework (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive AI system.
   b) Explain how you integrate {t['quantum_principle']} with {t['cognitive_process']}.
   c) Discuss the theoretical advantages of this integration for AI cognition.
   d) Provide a high-level diagram of your framework using ASCII art or a clear textual description.

2. Quantum-Classical Cognitive Interface (200-250 words):
   a) Explain how your system bridges quantum and classical cognitive processes.
   b) Discuss challenges in this interface and how your framework addresses them.
   c) Describe any novel approaches in your design for quantum-classical cognitive integration.

3. Cognitive Capabilities Analysis (250-300 words):
   a) Analyze how your framework enhances the AI's capability for {t['cognitive_process']}.
   b) Provide specific examples of how this enhancement manifests in decision-making or reasoning processes.
   c) Compare your quantum-inspired approach to traditional AI approaches for this cognitive capability.

4. Application to {t['application_domain']} (250-300 words):
   a) Describe how your quantum cognitive AI system would approach problems in {t['application_domain']}.
   b) Discuss potential breakthroughs or novel solutions enabled by your framework.
   c) Analyze limitations or challenges your system might face in this domain.
   d) Provide a specific example problem in {t['application_domain']} and outline how your system would solve it.

5. Ethical and Societal Implications (200-250 words):
   a) Discuss potential ethical concerns arising from your quantum cognitive AI framework.
   b) Analyze societal impacts of deploying such a system for {t['application_domain']}.
   c) Propose guidelines or safeguards for responsible development and use.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or refinements of your quantum cognitive AI framework.
   b) Discuss how advancements in quantum computing or neuroscience might influence your approach.
   c) Propose an experiment to validate a key aspect of your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, artificial intelligence, and {t['application_domain']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and number subsections as shown above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a comprehensive and scientifically plausible framework for a quantum-inspired cognitive AI system.",
            f"The system effectively integrates the quantum principle of {t['quantum_principle']} with the cognitive process of {t['cognitive_process']}.",
            "The framework demonstrates a clear understanding of both quantum mechanics and cognitive science principles.",
            f"The application to {t['application_domain']} is well-explained and demonstrates potential for novel solutions.",
            "The response addresses ethical implications and future research directions thoughtfully.",
            "The submission is well-structured, within the specified word count, and demonstrates a sophisticated understanding of the interdisciplinary concepts involved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
