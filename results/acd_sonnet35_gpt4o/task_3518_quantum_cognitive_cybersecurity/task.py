import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        cognitive_processes = [
            "Pattern recognition",
            "Decision making",
            "Learning and adaptation"
        ]
        cybersecurity_threats = [
            "DDoS attacks",
            "Zero-day exploits",
            "Social engineering"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "cybersecurity_threat": random.choice(cybersecurity_threats)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "cybersecurity_threat": random.choice(cybersecurity_threats)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for cybersecurity threat detection, focusing on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the cybersecurity threat of {t['cybersecurity_threat']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how the specified quantum principle can be analogously applied to cognitive processes in cybersecurity.
   b) Describe how the chosen cognitive process can be enhanced or reimagined using quantum-inspired algorithms.
   c) Discuss the potential advantages of this approach in detecting and mitigating the specified cybersecurity threat.
   d) Provide a specific example of how your quantum-inspired approach might process a typical data pattern related to the given cybersecurity threat.

2. Model Architecture (300-350 words):
   a) Design a detailed architecture for your quantum-inspired cognitive model.
   b) Explain how each component integrates principles from quantum computing, cognitive science, and cybersecurity.
   c) Describe the data flow and processing stages in your model.
   d) Include a diagram or flowchart of your model architecture (described in text).
   e) Provide a high-level pseudocode (10-15 lines) for a key algorithm in your model that demonstrates the integration of quantum principles and cognitive processes.

3. Threat Detection Mechanism (250-300 words):
   a) Explain how your model would detect and analyze the specified cybersecurity threat.
   b) Describe any novel algorithms or techniques used in the detection process.
   c) Discuss how your model's quantum-inspired cognitive approach differs from traditional threat detection methods.
   d) Provide a specific scenario demonstrating how your model would respond to an emerging instance of the given cybersecurity threat.

4. Implementation and Scalability (200-250 words):
   a) Propose a method for implementing your model using current or near-future technologies.
   b) Discuss potential challenges in scaling your model for real-world cybersecurity applications.
   c) Suggest ways to optimize your model's performance and efficiency.
   d) Estimate the computational resources required for your model and compare them to traditional approaches.

5. Ethical and Security Implications (200-250 words):
   a) Analyze potential ethical concerns related to using quantum-inspired cognitive models in cybersecurity.
   b) Discuss how your model might impact privacy and data protection.
   c) Explore potential vulnerabilities of your model and how they might be addressed.
   d) Propose guidelines for responsible development and deployment of quantum-inspired cybersecurity systems.

6. Future Research Directions (150-200 words):
   a) Propose two potential extensions or improvements to your model.
   b) Discuss how this approach might influence future trends in cybersecurity and cognitive computing.
   c) Suggest a potential interdisciplinary collaboration that could further advance this field.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and cybersecurity. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response incorporates the quantum principle of {t['quantum_principle']} in a plausible and innovative way, with a clear example of its application.",
            f"The model effectively enhances or reimagines the cognitive process of {t['cognitive_process']} using quantum-inspired algorithms, demonstrated in the pseudocode.",
            f"The threat detection mechanism is well-designed for addressing {t['cybersecurity_threat']}, with a specific scenario demonstrating its effectiveness.",
            "The response demonstrates a deep understanding of quantum computing, cognitive science, and cybersecurity, using appropriate technical terminology.",
            "The model architecture is clearly described, integrates all three disciplines effectively, and includes a coherent pseudocode snippet.",
            "The implementation and scalability section provides a realistic assessment of technological requirements and challenges.",
            "The ethical and security implications are thoughtfully considered, with proposed guidelines for responsible development.",
            "The response is creative and speculative while maintaining scientific plausibility, especially in the future research directions.",
            "The response follows the specified format, adheres to the word count guidelines, and includes all required elements such as examples and pseudocode."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
