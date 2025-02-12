import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "interplanetary communication",
            "secure voting system",
            "financial transaction verification",
            "medical data sharing",
            "autonomous vehicle network"
        ]
        quantum_properties = [
            "entanglement",
            "superposition",
            "no-cloning theorem",
            "quantum teleportation",
            "quantum key distribution"
        ]
        security_threats = [
            "man-in-the-middle attacks",
            "eavesdropping",
            "impersonation",
            "quantum computer-based attacks",
            "side-channel attacks"
        ]
        
        tasks = {
            "1": {
                "scenario": random.choice(scenarios),
                "quantum_property": random.choice(quantum_properties),
                "security_threat": random.choice(security_threats)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "quantum_property": random.choice(quantum_properties),
                "security_threat": random.choice(security_threats)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum cryptographic protocol for secure communication in the scenario of {t['scenario']}, leveraging the quantum property of {t['quantum_property']} and addressing the security threat of {t['security_threat']}. Your response should include the following sections:

1. Protocol Overview (200-250 words):
   a) Provide a high-level description of your quantum cryptographic protocol.
   b) Explain how it incorporates the specified quantum property.
   c) Describe how it addresses the given security threat.

2. Quantum Mechanics Principles (250-300 words):
   a) Explain the relevant quantum mechanical principles underlying your protocol.
   b) Discuss how these principles contribute to the security of your protocol.
   c) Provide a mathematical representation of the quantum state or operation central to your protocol, using Dirac notation or density matrix formalism. Explain the meaning of each term in your mathematical representation.

3. Protocol Implementation (300-350 words):
   a) Describe the step-by-step process of your protocol's operation.
   b) Explain the roles of the communicating parties and any potential third parties.
   c) Discuss any required quantum hardware or technologies for implementing your protocol.
   d) Include an ASCII art diagram illustrating the key steps or components of your protocol. (ASCII art uses text characters to create visual representations.)

4. Security Analysis (250-300 words):
   a) Analyze the security features of your protocol.
   b) Explain how it specifically addresses the given security threat.
   c) Discuss any potential vulnerabilities and how they might be mitigated.
   d) Compare the security of your protocol to at least one existing quantum cryptographic protocol (e.g., BB84, E91).

5. Practical Application (200-250 words):
   a) Propose a specific real-world application of your protocol in the given scenario.
   b) Discuss the potential benefits and challenges of implementing your protocol in this context.
   c) Explain how your protocol improves upon existing classical or quantum cryptographic methods for this application.

6. Societal Impact (150-200 words):
   a) Discuss the potential societal implications of widespread adoption of your quantum cryptographic protocol.
   b) Address any ethical concerns or policy considerations related to the implementation of your protocol.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your protocol.
   b) Propose a research question that could further the development of quantum cryptographic protocols in this area.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and information theory. Be creative in your protocol design while maintaining scientific plausibility and addressing real-world applicability. Strive for a balance between innovative ideas and scientific accuracy. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1450-1800 words. Manage your time wisely to address all sections thoroughly. Incomplete responses or those that fail to address all parts of each section may receive lower scores."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of a quantum cryptographic protocol for {t['scenario']}",
            f"The protocol incorporates the quantum property of {t['quantum_property']}",
            f"The protocol addresses the security threat of {t['security_threat']}",
            "The response demonstrates a deep understanding of quantum mechanics principles, including a mathematical representation with explanations",
            "A step-by-step implementation of the protocol is provided, including an ASCII art diagram",
            "The security features and potential vulnerabilities of the protocol are analyzed and compared to an existing protocol",
            "A specific real-world application of the protocol is proposed",
            "The response discusses potential societal impacts and ethical considerations",
            "The response suggests future improvements and research directions",
            "The ideas presented are creative while maintaining scientific plausibility",
            "The response is well-structured with clear headings and numbered paragraphs",
            "The total response falls within the specified word count range of 1450-1800 words",
            "All parts of each section are thoroughly addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
