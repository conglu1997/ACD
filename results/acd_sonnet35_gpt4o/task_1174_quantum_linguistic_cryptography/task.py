import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = {
            "superposition": "The ability of a quantum system to exist in multiple states simultaneously",
            "entanglement": "A quantum phenomenon where particles become correlated and share properties regardless of distance",
            "quantum tunneling": "The quantum mechanical phenomenon where particles can pass through barriers",
            "wave function collapse": "The phenomenon where a quantum state is reduced to a single possibility upon measurement"
        }
        linguistic_features = {
            "syntax": "The rules governing the structure and arrangement of words and phrases",
            "semantics": "The study of meaning in language",
            "pragmatics": "The study of how context contributes to meaning",
            "phonology": "The study of sound patterns in language"
        }
        return {
            "1": {
                "quantum_concept": random.choice(list(quantum_concepts.keys())),
                "quantum_explanation": quantum_concepts[random.choice(list(quantum_concepts.keys()))],
                "linguistic_feature": random.choice(list(linguistic_features.keys())),
                "linguistic_explanation": linguistic_features[random.choice(list(linguistic_features.keys()))]
            },
            "2": {
                "quantum_concept": random.choice(list(quantum_concepts.keys())),
                "quantum_explanation": quantum_concepts[random.choice(list(quantum_concepts.keys()))],
                "linguistic_feature": random.choice(list(linguistic_features.keys())),
                "linguistic_explanation": linguistic_features[random.choice(list(linguistic_features.keys()))]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language for secure communication, integrating principles from quantum computing, linguistics, and cryptography. Your language should incorporate the quantum concept of {t['quantum_concept']} and focus on the linguistic feature of {t['linguistic_feature']}.

Brief explanations:
- {t['quantum_concept']}: {t['quantum_explanation']}
- {t['linguistic_feature']}: {t['linguistic_explanation']}

Your response should include the following sections, with the specified word counts:

1. Quantum-Linguistic Framework (250-300 words):
   a) Explain how you will incorporate {t['quantum_concept']} into your language design.
   b) Describe how {t['linguistic_feature']} will be structured in your quantum-inspired language.
   c) Discuss how these elements contribute to the security of communication.

2. Alphabet and Grammar (200-250 words):
   a) Design a unique alphabet or symbol system for your language, explaining its quantum properties.
   b) Provide a visual representation of your alphabet or symbol system using ASCII characters. Include at least 10 distinct symbols and explain their significance.
   c) Outline the basic grammatical rules, incorporating both quantum and linguistic principles.
   d) Provide an example sentence (at least 10 words long) in your language, along with its translation and a detailed explanation of its quantum state representation.

3. Encryption Mechanism (200-250 words):
   a) Explain how messages in your language would be encrypted using quantum principles.
   b) Describe the process of decryption and how it relates to {t['quantum_concept']}.
   c) Discuss potential vulnerabilities and how your system addresses them.

4. Practical Implementation (150-200 words):
   a) Propose a method for implementing your language in a real-world communication system.
   b) Discuss any technological requirements or limitations.
   c) Explain how your system could be scaled for wider use.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum-linguistic cryptographic system to traditional cryptographic methods.
   b) Discuss potential advantages and disadvantages of your approach.
   c) Suggest potential applications beyond secure communication.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical concerns related to your quantum-linguistic cryptographic system.
   b) Address societal implications of unbreakable encryption methods.
   c) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theories, and cryptographic techniques. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

IMPORTANT:
- Your design should be original and scientifically plausible. Strive for creativity while maintaining consistency with known principles of quantum mechanics and linguistics.
- Balance creativity with scientific accuracy. While novel ideas are encouraged, they should have a basis in established scientific concepts.
- Address all parts (a, b, c, etc.) of each section thoroughly.
- Adhere to the specified word counts for each section.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_concept']} and {t['linguistic_feature']}, integrating them coherently into the language design.",
            "The proposed language design is original, creative, and scientifically plausible, balancing innovation with established scientific principles.",
            "The alphabet and grammar system is well-defined and includes a visual ASCII representation with at least 10 distinct symbols and explanations of their significance.",
            "The example sentence is at least 10 words long, with a translation and detailed explanation of its quantum state representation.",
            "The encryption mechanism effectively utilizes quantum principles for security and clearly relates to the specified quantum concept.",
            "The practical implementation is well-reasoned, addressing technological requirements, limitations, and scalability.",
            "The comparative analysis provides a thorough comparison with traditional methods and suggests novel applications.",
            "Ethical and societal implications are thoughtfully considered, with specific guidelines for responsible development and use.",
            "The response adheres to the specified structure, addresses all parts of each section, and meets the word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
