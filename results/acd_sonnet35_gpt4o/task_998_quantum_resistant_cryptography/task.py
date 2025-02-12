import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'name': 'Secure Communication',
                'description': 'Design a quantum-resistant key exchange protocol for secure communication between two parties.',
                'quantum_threat': 'Shor\'s algorithm breaking RSA and ECC',
                'constraints': 'Must be computationally efficient for classical computers and have a key size of at most 1 KB',
                'additional_requirement': 'Provide a security reduction to a hard lattice problem'
            },
            {
                'name': 'Digital Signatures',
                'description': 'Develop a quantum-resistant digital signature scheme for verifying the authenticity of software updates.',
                'quantum_threat': 'Grover\'s algorithm reducing the security of hash-based signatures',
                'constraints': 'Signature size must not exceed 1 KB and verification time must be under 100 ms on a standard CPU',
                'additional_requirement': 'Prove the scheme is existentially unforgeable under chosen message attacks'
            }
        ]
        
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-resistant cryptographic algorithm for the following cybersecurity scenario:

Scenario: {t['name']}
Description: {t['description']}
Quantum Threat: {t['quantum_threat']}
Constraints: {t['constraints']}
Additional Requirement: {t['additional_requirement']}

You have 45 minutes to complete this task. Your response should include the following sections:

1. Algorithm Design (250-300 words):
   a) Describe your proposed quantum-resistant algorithm in detail.
   b) Explain how it addresses the specific quantum threat mentioned.
   c) Discuss how your design meets the given constraints.
   d) Provide a high-level pseudocode or diagram of your algorithm.

2. Mathematical Foundation (200-250 words):
   a) Present the mathematical basis for your algorithm's security.
   b) Provide a simple mathematical proof or equation supporting your design.
   c) Explain how your algorithm relates to the additional requirement.

3. Security Analysis (200-250 words):
   a) Analyze the security of your algorithm against both classical and quantum attacks.
   b) Estimate the computational complexity for breaking your algorithm using the best known quantum algorithms.
   c) Discuss any potential vulnerabilities or limitations of your approach.

4. Implementation Considerations (150-200 words):
   a) Describe the key steps for implementing your algorithm in a real-world system.
   b) Discuss any challenges that might arise during implementation and how to address them.
   c) Propose a method for benchmarking the performance of your algorithm.

5. Comparative Analysis (150-200 words):
   a) Compare your algorithm to existing quantum-resistant proposals for similar purposes.
   b) Discuss the advantages and disadvantages of your approach.
   c) Explain how your algorithm might be combined with other post-quantum cryptographic techniques for enhanced security.

6. Future Directions (100-150 words):
   a) Propose two potential improvements or extensions to your algorithm.
   b) Discuss how your approach might be adapted to other cybersecurity scenarios.
   c) Speculate on the long-term viability of your algorithm in the face of advancing quantum computing capabilities.

Ensure your response demonstrates a deep understanding of quantum computing principles, cryptography, and cybersecurity. Be creative in your approach while maintaining scientific and mathematical rigor. Use appropriate terminology and provide clear, logical explanations for your design choices.

Important: Address all parts of each section thoroughly. Your response will be evaluated based on completeness, accuracy, and adherence to the given constraints and requirements.

Format your response with clear headings for each section. Your total response should be between 1050-1400 words.

Reminder: You have 45 minutes to complete this task. Manage your time wisely to address all sections comprehensively."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their implications for cryptography.",
            "The proposed algorithm is creative, well-designed, and addresses the specific quantum threat and constraints mentioned in the scenario.",
            "The mathematical foundation is sound and includes a valid proof or equation supporting the algorithm's security.",
            "The security analysis is thorough and considers both classical and quantum attack vectors.",
            "The implementation considerations are practical and show an understanding of real-world cybersecurity challenges.",
            "The comparative analysis and future directions demonstrate critical thinking and awareness of the broader field of post-quantum cryptography.",
            "The response addresses the additional requirement specified in the scenario.",
            "The overall solution is coherent, well-structured, and within the specified word count range.",
            "All parts of each section are thoroughly addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
