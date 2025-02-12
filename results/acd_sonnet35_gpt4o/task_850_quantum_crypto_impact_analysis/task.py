class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"crypto_method": "RSA", "quantum_algorithm": "Shor's algorithm", "key_size": 2048, "qubits": 4000},
            "2": {"crypto_method": "Elliptic Curve Cryptography", "quantum_algorithm": "Grover's algorithm", "key_size": 256, "qubits": 2330}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the impact of quantum computing on {t['crypto_method']} using {t['quantum_algorithm']} and propose a novel post-quantum cryptographic solution. Consider a {t['key_size']}-bit key for {t['crypto_method']} and a quantum computer with {t['qubits']} qubits. Your response should include:

1. Technical Analysis (250-300 words):
   a) Explain how {t['quantum_algorithm']} works and its implications for {t['crypto_method']}.
   b) Estimate the timeframe for when quantum computers might pose a significant threat to this cryptographic method, considering current technological progress.
   c) Discuss any current limitations or challenges in implementing {t['quantum_algorithm']} for cryptanalysis.

2. Novel Post-Quantum Solution (300-350 words):
   a) Propose a new post-quantum cryptographic method that could potentially resist attacks from quantum algorithms.
   b) Explain the mathematical or computational principles behind your proposed solution.
   c) Discuss how your solution addresses the vulnerabilities exposed by {t['quantum_algorithm']}.
   d) Provide a high-level description of the encryption and decryption processes in your proposed system.

3. Comparative Analysis (200-250 words):
   a) Compare your proposed solution to existing post-quantum cryptographic methods (e.g., lattice-based, hash-based, or multivariate cryptography).
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze the computational complexity and efficiency of your solution compared to {t['crypto_method']}.

4. Implementation and Transition Strategy (150-200 words):
   a) Outline a strategy for implementing and transitioning to your proposed post-quantum cryptographic solution.
   b) Discuss potential challenges in adoption and how they might be addressed.
   c) Propose a timeline for development, testing, and deployment of your solution.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical implications of the development of quantum computing for cryptography and cybersecurity.
   b) Analyze potential dual-use concerns of your proposed solution.
   c) Suggest policy recommendations for managing the transition to post-quantum cryptography.

Ensure your response demonstrates a deep understanding of both quantum computing and cryptography. Use technical terminology appropriately and provide explanations where necessary. Be creative in your proposed solution while maintaining scientific and mathematical plausibility.

Format your response with clear headings for each section, numbered subsections, and a concluding paragraph summarizing your key points. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing and cryptography concepts, including accurate explanations of the specified quantum algorithm and cryptographic method.",
            "The proposed post-quantum cryptographic solution is novel, scientifically plausible, and adequately addresses vulnerabilities exposed by the given quantum algorithm.",
            "The analysis includes a comprehensive discussion of technical, implementation, and ethical aspects, with specific reference to the given key size and number of qubits.",
            "The response is well-structured, clear, follows the specified format, and is within the specified word count range.",
            "The comparative analysis includes references to existing post-quantum cryptographic methods and provides a thoughtful discussion of advantages and limitations.",
            "The ethical implications and policy recommendations are well-reasoned and demonstrate an understanding of the broader impacts of quantum computing on cybersecurity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
