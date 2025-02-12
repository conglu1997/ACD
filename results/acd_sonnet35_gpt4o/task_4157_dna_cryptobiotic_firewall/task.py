import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "organism": "bacteria",
                "encryption_method": "DNA sequence patterns",
                "threat": "quantum computing attacks"
            },
            {
                "organism": "algae",
                "encryption_method": "protein folding structures",
                "threat": "AI-powered hacking attempts"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cybersecurity system that uses engineered {t['organism']} to encrypt and protect digital information using {t['encryption_method']}, with a focus on defending against {t['threat']}. Then, analyze its potential applications and ethical implications.

Key concepts:
- DNA encryption: A method of storing and transmitting data using the genetic code.
- Cryptobiotic systems: The use of living organisms or biological processes for cryptographic purposes.

Your response should include:

1. Biotechnological Design (300-350 words):
   a) Describe how you would engineer the {t['organism']} to perform encryption functions.
   b) Explain the mechanism by which {t['encryption_method']} are used for data encryption.
   c) Discuss any novel genetic modifications or synthetic biology techniques used in your design.
   d) Address potential challenges in maintaining the stability and reliability of your bio-based encryption system.
   e) Provide a specific example or illustration of your design.

2. Cryptographic Framework (250-300 words):
   a) Explain how your system translates digital information into biological data and vice versa.
   b) Describe the encryption and decryption processes, including key generation and management.
   c) Discuss how your system ensures the security and integrity of the encrypted data.
   d) Explain how your approach defends specifically against {t['threat']}.
   e) Compare your bio-based approach to a traditional non-biological encryption method.

3. Implementation and Scalability (200-250 words):
   a) Propose a method for integrating your bio-cryptographic system with existing digital infrastructure.
   b) Discuss challenges in scaling this technology for widespread use and potential solutions.
   c) Address any special environmental or containment requirements for your engineered organisms.

4. Performance Analysis (200-250 words):
   a) Compare the theoretical performance of your system to current non-biological encryption methods.
   b) Discuss potential advantages and limitations of your bio-based approach.
   c) Propose metrics for evaluating the efficiency and security of your system.
   d) Provide a hypothetical performance scenario with specific numbers or percentages.

5. Potential Applications (150-200 words):
   a) Suggest two novel applications of your DNA cryptobiotic firewall beyond traditional data protection.
   b) Discuss how this technology might impact fields such as secure communication, data storage, or blockchain technology.

6. Ethical and Security Implications (200-250 words):
   a) Analyze potential ethical concerns related to using engineered organisms for data security.
   b) Discuss biosafety and biosecurity risks associated with your system and how they might be mitigated.
   c) Consider potential dual-use implications and propose guidelines for responsible development and use.

7. Future Research Directions (150-200 words):
   a) Propose two areas for future research that could enhance or extend your DNA cryptobiotic firewall.
   b) Discuss how advancements in synthetic biology or quantum computing might impact the future of bio-based cybersecurity.

Ensure your response demonstrates a deep understanding of biotechnology, cryptography, and cybersecurity principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Balance creativity with scientific plausibility, addressing potential limitations and drawbacks of your proposed system.

Cite relevant research or theories to support your proposed design and analysis where appropriate.

Format your response with clear headings for each section. Adhere strictly to the word count requirements for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of biotechnology, cryptography, and cybersecurity principles, using appropriate technical terminology.",
            f"The proposed system effectively uses engineered {t['organism']} for encryption using {t['encryption_method']}, with a clear explanation of the mechanism.",
            f"The cryptographic framework adequately addresses defense against {t['threat']} and includes a comparison with traditional non-biological encryption methods.",
            "The response balances creativity with scientific plausibility, addressing potential limitations and drawbacks of the proposed system.",
            "Ethical implications and security concerns are thoroughly analyzed, including biosafety and biosecurity risks.",
            "The response provides specific examples, illustrations, or hypothetical scenarios to demonstrate the proposed system's functionality and performance.",
            "The response follows the specified format, adheres to word count requirements for each section, and has a total word count between 1450-1800 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
