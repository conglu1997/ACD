import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        error_types = ['bit flip', 'phase flip', 'measurement error', 'gate error']
        ai_techniques = ['reinforcement learning', 'neural networks', 'evolutionary algorithms', 'bayesian inference']
        quantum_architectures = ['superconducting qubits', 'trapped ions', 'photonic qubits', 'topological qubits']
        
        return {
            "1": {
                "error_type": random.choice(error_types),
                "ai_technique": random.choice(ai_techniques),
                "quantum_architecture": random.choice(quantum_architectures)
            },
            "2": {
                "error_type": random.choice(error_types),
                "ai_technique": random.choice(ai_techniques),
                "quantum_architecture": random.choice(quantum_architectures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical AI system for real-time quantum error correction in large-scale quantum computers. Your system should focus on correcting {t['error_type']} errors using {t['ai_technique']} in a {t['quantum_architecture']} based quantum computer. Your response should address the following:

1. System Architecture (300-350 words):
   a) Describe the key components of your hybrid quantum-classical AI system for error correction.
   b) Explain how the classical AI component interfaces with the quantum hardware.
   c) Detail how your system detects and corrects {t['error_type']} errors in real-time.
   d) Discuss any novel technologies or theoretical concepts your system employs.
   e) Include a high-level diagram or flowchart of your system architecture (use text-based representation).

2. Quantum Error Correction Mechanism (250-300 words):
   a) Explain the quantum error correction code or protocol used in your system.
   b) Describe how your system implements this protocol using {t['ai_technique']}.
   c) Discuss how your approach addresses the specific challenges of {t['error_type']} errors in {t['quantum_architecture']} systems.
   d) Analyze the theoretical error threshold and scalability of your approach.

3. AI Component Design (250-300 words):
   a) Detail the design and functioning of your {t['ai_technique']} based AI component.
   b) Explain how the AI is trained to recognize and respond to quantum errors.
   c) Discuss any quantum-inspired algorithms or techniques used in your AI design.
   d) Describe how the AI component adapts to changing error patterns or quantum circuit complexity.

4. Performance Analysis (200-250 words):
   a) Provide a theoretical analysis of your system's performance in terms of error correction fidelity and speed.
   b) Compare your hybrid approach to traditional quantum error correction methods.
   c) Discuss any trade-offs between error correction effectiveness and computational overhead.
   d) Propose a method for benchmarking your system against other quantum error correction approaches.

5. Challenges and Future Directions (150-200 words):
   a) Identify potential challenges in implementing your system with current technology.
   b) Discuss any assumptions made in your design and their implications.
   c) Propose future research directions to enhance your system's capabilities.
   d) Speculate on how your approach could impact the development of fault-tolerant quantum computers.

6. Broader Implications (150-200 words):
   a) Discuss how your hybrid quantum-AI approach might influence other areas of quantum computing or AI research.
   b) Consider potential applications of your system beyond error correction.
   c) Analyze any ethical considerations or potential risks associated with your technology.

Ensure your response demonstrates a deep understanding of quantum computing principles, error correction techniques, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the correction of {t['error_type']} errors.",
            f"The system design incorporates {t['ai_technique']} in a meaningful way.",
            f"The proposed solution is appropriate for {t['quantum_architecture']} based quantum computers.",
            "The response demonstrates a deep understanding of quantum computing principles and AI techniques.",
            "The system architecture is clearly described and includes a hybrid quantum-classical approach.",
            "The AI component design is well-explained and integrated with the quantum error correction mechanism.",
            "The performance analysis includes a comparison with traditional quantum error correction methods.",
            "Challenges and future directions are thoughtfully considered.",
            "The broader implications of the proposed system are discussed.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
