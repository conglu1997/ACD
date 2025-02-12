import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        biological_processes = [
            "DNA replication",
            "protein folding",
            "neural signaling",
            "photosynthesis"
        ]
        application_domains = [
            "drug discovery",
            "climate modeling",
            "financial forecasting",
            "cryptography"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid system that integrates quantum computing, biological processes, and artificial intelligence to solve complex problems in a specific domain. Your system should incorporate the following elements:

1. Quantum Principle: {t['quantum_principle']}
2. Biological Process: {t['biological_process']}
3. Application Domain: {t['application_domain']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your hybrid quantum-bio-AI system.
   b) Explain how you integrate the specified quantum principle with the given biological process.
   c) Detail how AI is incorporated into your system to enhance its capabilities.
   d) Provide a high-level diagram or pseudocode snippet illustrating a key component of your system.

2. Quantum-Biological Interface (250-300 words):
   a) Explain the mechanism by which quantum effects interact with the biological process in your system.
   b) Discuss challenges in maintaining quantum coherence in a biological environment and how you address them.
   c) Describe how information is encoded, processed, and transferred between the quantum and biological components.

3. AI Integration and Problem-Solving (250-300 words):
   a) Detail how AI algorithms are used to control, optimize, or interpret the quantum-biological processes.
   b) Explain how your system applies its capabilities to solve problems in the specified application domain.
   c) Provide a specific example of a problem your system could tackle more effectively than traditional approaches.

4. Performance Analysis (200-250 words):
   a) Discuss the theoretical performance capabilities of your system compared to classical computing approaches.
   b) Identify potential bottlenecks or limitations in your system and propose ways to address them.
   c) Suggest metrics or experiments to evaluate the effectiveness of your hybrid approach.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss potential ethical issues arising from the development and use of your quantum-bio-AI hybrid system.
   b) Analyze possible societal impacts, both positive and negative, of widespread adoption of this technology.
   c) Propose guidelines for responsible development and use of quantum-bio-AI systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, biological processes, and artificial intelligence. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle, biological process, and their potential integration.",
            "The proposed system architecture is innovative, well-explained, and scientifically plausible.",
            "The quantum-biological interface is described in detail, with thoughtful consideration of challenges and potential solutions.",
            "The AI integration is well-conceived and adds significant value to the system's problem-solving capabilities.",
            "The performance analysis is thorough and includes meaningful comparisons to existing technologies.",
            "Ethical considerations and societal impacts are thoughtfully addressed.",
            "The response is well-structured, clear, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
