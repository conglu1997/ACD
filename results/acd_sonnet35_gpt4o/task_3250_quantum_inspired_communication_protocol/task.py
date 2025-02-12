import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "classical_problem": "Byzantine Generals Problem",
                "quantum_concept": "quantum entanglement",
                "communication_constraint": "limited bandwidth",
                "example_scenario": "A network of 5 nodes with 2 potentially malicious nodes"
            },
            {
                "classical_problem": "Dining Cryptographers Problem",
                "quantum_concept": "quantum superposition",
                "communication_constraint": "anonymity preservation",
                "example_scenario": "A group of 3 cryptographers with one potential payer"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication protocol inspired by {t['quantum_concept']} to address the {t['classical_problem']}, considering the constraint of {t['communication_constraint']}. Your protocol must be original and not a direct application of existing quantum protocols. Consider the example scenario: {t['example_scenario']}. Your response should include:

1. Quantum Concept Analysis (200-250 words):
   a) Explain the key principles of {t['quantum_concept']} and how they relate to information processing.
   b) Discuss potential advantages of applying this quantum concept to classical communication problems.
   c) Describe any challenges in translating quantum phenomena to classical systems.

2. Classical Problem Overview (150-200 words):
   a) Provide a concise explanation of the {t['classical_problem']}.
   b) Discuss traditional approaches to solving this problem and their limitations.
   c) Explain why a quantum-inspired approach might be beneficial.

3. Protocol Design (250-300 words):
   a) Describe your quantum-inspired communication protocol in detail.
   b) Explain how it incorporates principles from {t['quantum_concept']}.
   c) Detail how your protocol addresses the {t['classical_problem']}.
   d) Discuss how your design considers the constraint of {t['communication_constraint']}.
   e) Illustrate how your protocol would work in the given example scenario.

4. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of a key aspect of your protocol.
   b) Define all variables, functions, and operations used in your formulation.
   c) Present at least one equation or algorithm that captures the core of your protocol.
   d) Explain how this mathematical model reflects the quantum-inspired nature of your protocol.

5. Protocol Analysis (200-250 words):
   a) Analyze the efficiency of your protocol compared to classical approaches.
   b) Discuss potential vulnerabilities or limitations of your design.
   c) Propose methods to evaluate the performance of your protocol.
   d) Provide a numerical example demonstrating your protocol's advantage over a classical approach.

6. Practical Implementation (150-200 words):
   a) Describe how your protocol could be implemented using current technology.
   b) Discuss any technological barriers to implementation and potential solutions.
   c) Propose a simple experiment to demonstrate the feasibility of your protocol.

7. Broader Implications (100-150 words):
   a) Discuss potential applications of your quantum-inspired protocol beyond the {t['classical_problem']}.
   b) Explore how your approach might influence the development of future communication technologies.
   c) Address any ethical considerations related to the implementation of your protocol.

Ensure your response demonstrates a deep understanding of both quantum mechanics and classical information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the {t['classical_problem']} using principles inspired by {t['quantum_concept']}.",
            f"The protocol design considers the constraint of {t['communication_constraint']} and applies to the given example scenario.",
            "The submission demonstrates a deep understanding of both quantum mechanics and classical information theory.",
            "The protocol design is novel, innovative, and not a direct application of existing quantum protocols.",
            "The mathematical formulation includes at least one equation or algorithm that accurately represents a key aspect of the protocol.",
            "The response includes a thorough analysis of the protocol's efficiency and limitations, with a numerical example demonstrating its advantage.",
            "The submission addresses all seven required sections with appropriate detail and coherence, using the specified formatting.",
            "The proposed protocol is scientifically plausible and could potentially be implemented with current or near-future technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
