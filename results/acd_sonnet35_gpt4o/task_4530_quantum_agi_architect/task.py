import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "Superposition",
                "agi_capability": "Multi-task learning",
                "problem_domain": "Climate modeling and prediction",
                "constraint": "Must use no more than 100 qubits"
            },
            "2": {
                "quantum_principle": "Entanglement",
                "agi_capability": "Causal reasoning",
                "problem_domain": "Protein folding and drug discovery",
                "constraint": "Must operate at room temperature"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for a quantum-inspired Artificial General Intelligence (AGI) system, focusing on the quantum principle of {t['quantum_principle']} and the AGI capability of {t['agi_capability']}. Then, analyze its potential capabilities and limitations in solving complex real-world problems in the domain of {t['problem_domain']}. Your system {t['constraint']}. Your response should include the following sections:

1. Quantum-AGI Framework (300-350 words):
   a) Describe the key components of your quantum-inspired AGI system.
   b) Explain how you integrate {t['quantum_principle']} with {t['agi_capability']}.
   c) Discuss the theoretical advantages of this integration.
   d) Provide a high-level diagram of your framework using ASCII art or a clear textual description.

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your system interfaces between quantum and classical computing paradigms.
   b) Discuss challenges in this interface and how your framework addresses them.
   c) Describe any novel approaches in your design for quantum-classical integration.

3. AGI Capabilities Analysis (250-300 words):
   a) Analyze how your framework enhances the AGI capability of {t['agi_capability']}.
   b) Provide specific examples of how this enhancement manifests in cognitive processes.
   c) Compare your quantum-inspired approach to traditional AGI approaches for this capability.

4. Application to {t['problem_domain']} (250-300 words):
   a) Describe how your quantum-AGI system would approach problems in {t['problem_domain']}.
   b) Discuss potential breakthroughs or novel solutions enabled by your framework.
   c) Analyze limitations or challenges your system might face in this domain.
   d) Provide a specific example problem in {t['problem_domain']} and outline how your system would solve it.

5. Ethical and Societal Implications (200-250 words):
   a) Discuss potential ethical concerns arising from your quantum-AGI framework.
   b) Analyze societal impacts of deploying such a system for {t['problem_domain']}.
   c) Propose guidelines or safeguards for responsible development and use.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or refinements of your quantum-AGI framework.
   b) Discuss how advancements in quantum computing or neuroscience might influence your approach.
   c) Propose an experiment to validate a key aspect of your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, artificial intelligence, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and number subsections as shown above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all required sections with appropriate word counts and correct formatting.",
            f"The framework effectively integrates {t['quantum_principle']} with {t['agi_capability']} while adhering to the constraint: {t['constraint']}.",
            f"The analysis of capabilities and limitations in {t['problem_domain']} is thorough, plausible, and includes a specific example problem and solution.",
            "The response demonstrates deep understanding of quantum mechanics, AI, and cognitive science, using appropriate technical terminology.",
            "The proposed framework is innovative while maintaining scientific plausibility.",
            "The quantum-classical interface is well-explained with novel approaches discussed.",
            "Ethical and societal implications are thoughtfully considered with specific guidelines proposed.",
            "Future research directions and experiments are well-reasoned, relevant, and clearly described.",
            "The high-level diagram or textual description of the framework is clear and informative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
