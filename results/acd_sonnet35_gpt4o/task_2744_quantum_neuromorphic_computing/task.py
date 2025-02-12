class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_property": "superposition",
                "neural_process": "pattern recognition",
                "application_domain": "natural language processing"
            },
            "2": {
                "quantum_property": "entanglement",
                "neural_process": "memory formation and retrieval",
                "application_domain": "autonomous decision-making"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Design a theoretical framework for a quantum-enhanced neuromorphic computing system that leverages the quantum property of {t['quantum_property']} to enhance the neural process of {t['neural_process']}. Then, analyze its potential advantages over classical systems and propose novel applications in {t['application_domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced neuromorphic computing system.
   b) Explain how quantum effects are integrated with neuromorphic circuits.
   c) Detail how {t['quantum_property']} is utilized to enhance {t['neural_process']}.
   d) Discuss any novel materials or technologies required for implementation.

2. Quantum-Neural Interface (250-300 words):
   a) Explain the theoretical basis for combining quantum computing with neuromorphic architectures.
   b) Describe how quantum states are mapped to neural representations.
   c) Discuss challenges in maintaining quantum coherence in a neural-inspired system and propose solutions.

3. Enhanced Capabilities (200-250 words):
   a) Analyze how your system improves {t['neural_process']} compared to classical neuromorphic systems.
   b) Quantify the expected performance gains, using appropriate metrics.
   c) Discuss any trade-offs or limitations of your approach.

4. Application in {t['application_domain']} (200-250 words):
   a) Propose a novel application of your system in {t['application_domain']}.
   b) Explain how the quantum-enhanced capabilities enable this application.
   c) Discuss potential societal or scientific impacts of this application.

5. Implementation Roadmap (150-200 words):
   a) Outline the key steps required to move from theory to practical implementation.
   b) Identify major technological hurdles and propose approaches to overcome them.
   c) Estimate a timeline for development, including major milestones.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of quantum-enhanced neuromorphic systems.
   b) Propose guidelines for responsible development and use of this technology.
   c) Consider long-term consequences for human cognition and society.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and computer architecture. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and computer architecture.",
            "The proposed system architecture is innovative, well-explained, and scientifically plausible.",
            "The quantum-neural interface is clearly described and addresses key challenges.",
            "The enhanced capabilities are well-analyzed and quantified where possible.",
            "The proposed application is novel and leverages the unique aspects of the system.",
            "The implementation roadmap is realistic and addresses major challenges.",
            "Ethical considerations are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
