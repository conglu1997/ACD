import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        encryption_schemes = [
            {
                "name": "Quantum Key Distribution",
                "key_features": ["entanglement", "superposition", "no-cloning theorem"]
            },
            {
                "name": "Homomorphic Encryption",
                "key_features": ["computation on ciphertext", "preserving data privacy", "algebraic operations"]
            },
            {
                "name": "Post-Quantum Cryptography",
                "key_features": ["lattice-based cryptography", "multivariate cryptography", "hash-based signatures"]
            },
            {
                "name": "Zero-Knowledge Proofs",
                "key_features": ["verifiable computation", "privacy preservation", "interactive proofs"]
            }
        ]
        return {
            "1": random.choice(encryption_schemes),
            "2": random.choice(encryption_schemes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolving cryptographic conlang (constructed language) that adapts its encryption scheme based on AI-detected linguistic patterns. Your conlang should incorporate principles from the {t['name']} encryption scheme. Follow this structure in your response:

1. Conlang Design (300-350 words):
   a) Basic structure (phonology, morphology, syntax)
   b) Integration of {t['name']} encryption scheme
   c) Representation of key features: {', '.join(t['key_features'])}
   d) 2 example sentences with format:
      Conlang: [Your sentence]
      English: [Translation]
      Cryptographic properties: [Brief explanation]
   e) Glossary: 3-5 key terms in your conlang

2. AI-driven Evolution Mechanism (150-200 words):
   a) AI system for pattern detection
   b) Triggering language evolution
   c) Two specific evolution examples

3. Cryptanalysis Resilience (150-200 words):
   a) Potential vulnerabilities
   b) Resilience mechanisms
   c) Long-term security through evolution

4. Practical Application (100-150 words):
   a) Realistic usage scenario
   b) Advantages over traditional methods
   c) Implementation challenges

5. Ethical Considerations (100-150 words):
   a) Ethical implications
   b) Potential misuse and safeguards
   c) Societal impact

Ensure your response demonstrates understanding of cryptography, linguistics, and AI. Balance creativity with plausibility.

Example approach (for inspiration, not to be directly copied):
For a quantum-based conlang, you might use superposition to represent multiple meanings simultaneously, resolved only upon 'observation' (i.e., context). E.g., a word 'qux' might represent both 'hello' and 'goodbye' until used in a sentence.

Total response: 800-1050 words.

Scoring Rubric (100 points total):
- Conlang Design: 35 points
- AI Evolution Mechanism: 25 points
- Cryptanalysis Resilience: 20 points
- Practical Application: 10 points
- Ethical Considerations: 10 points

Points awarded based on creativity, scientific plausibility, depth of understanding, and adherence to the given encryption scheme principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang incorporates principles from the {t['name']} encryption scheme",
            f"The language represents the key features of {t['name']}: {', '.join(t['key_features'])}",
            "The response includes 2 example sentences with translations and cryptographic explanations",
            "A glossary of 3-5 key terms is provided",
            "An AI-driven evolution mechanism is described",
            "The response analyzes vulnerabilities and proposes resilience mechanisms",
            "A practical application scenario is provided",
            "Ethical implications are discussed",
            "The response demonstrates understanding of cryptography, linguistics, and AI",
            "The design balances creativity with plausibility",
            "The submission adheres to the word count and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
