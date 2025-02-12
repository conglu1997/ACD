import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Arabic', 'Spanish']
        quantum_principles = {
            'superposition': 'the ability of a quantum system to exist in multiple states simultaneously',
            'entanglement': 'a quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently',
            'quantum tunneling': 'a quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount'
        }
        message_types = ['diplomatic communication', 'financial transaction']
        tasks = {
            '1': {
                'language': random.choice(languages),
                'quantum_principle': random.choice(list(quantum_principles.keys())),
                'message_type': message_types[0],
                'sample_message': 'The eagle has landed at midnight.'
            },
            '2': {
                'language': random.choice(languages),
                'quantum_principle': random.choice(list(quantum_principles.keys())),
                'message_type': message_types[1],
                'sample_message': 'Transfer $1,000,000 to account #12345678.'
            }
        }
        for task in tasks.values():
            task['principle_description'] = quantum_principles[task['quantum_principle']]
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system for {t['language']} that incorporates the quantum principle of {t['quantum_principle']} ({t['principle_description']}) to secure {t['message_type']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your encryption system.
   b) Explain how it integrates principles from quantum computing, linguistics, and cryptography.
   c) Discuss how your system leverages {t['quantum_principle']} for enhanced security.
   d) Provide a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Encryption Process (200-250 words):
   a) Describe the step-by-step process of encrypting a message using your system.
   b) Explain how linguistic features of {t['language']} are utilized in the encryption.
   c) Discuss how your system ensures the security of {t['message_type']}.
   d) Demonstrate your encryption process using the following sample message: "{t['sample_message']}"

3. Decryption and Authentication (200-250 words):
   a) Explain the decryption process and how it relates to the encryption method.
   b) Describe any authentication mechanisms to verify the sender's identity.
   c) Discuss how your system prevents or detects tampering with the encrypted message.

4. Quantum Advantage Analysis (150-200 words):
   a) Analyze the advantages of your quantum-inspired system over classical encryption methods.
   b) Discuss any potential vulnerabilities or limitations of your approach.
   c) Explain how your system might resist quantum computing attacks.

5. Linguistic Impact (150-200 words):
   a) Discuss how your system might affect or be affected by linguistic patterns in {t['language']}.
   b) Analyze potential implications for natural language processing or machine translation.
   c) Consider how your system might handle dialects or linguistic variations.

6. Ethical and Legal Considerations (150-200 words):
   a) Discuss potential ethical implications of your encryption system.
   b) Consider legal aspects related to the use of quantum-inspired encryption for {t['message_type']}.
   c) Propose guidelines for responsible development and use of such systems.

7. Future Developments (100-150 words):
   a) Suggest two potential enhancements or extensions to your system.
   b) Discuss how these improvements could address current limitations or expand its applications.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theories, and cryptographic techniques. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words.

Note: Do not provide actual encryption algorithms or keys in your response. Focus on the conceptual design and theoretical aspects of the system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum-inspired linguistic encryption system for {t['language']}",
            f"The system should incorporate the quantum principle of {t['quantum_principle']} as described in the instructions",
            f"The encryption system should be tailored for {t['message_type']}",
            f"The response should demonstrate the encryption process using the sample message: \"{t['sample_message']}\"",
            "The response should demonstrate understanding of quantum computing, linguistics, and cryptography",
            "The proposed system should be innovative yet scientifically plausible",
            "The response should address all required sections with appropriate depth (word counts as specified in the instructions)",
            "The response should not provide actual encryption algorithms or keys",
            "The total response should be between 1200-1550 words",
            "Each section should contain substantive content addressing all sub-points specified in the instructions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
