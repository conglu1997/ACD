import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "financial transactions",
                "threat": "Shor's algorithm",
                "constraint": "must be implementable on current hardware"
            },
            {
                "context": "secure communication",
                "threat": "Grover's algorithm",
                "constraint": "must be resistant to side-channel attacks"
            }
        ]
        return {str(i+1): random.choice(scenarios) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a post-quantum cryptographic system for {t['context']} that is resistant to attacks using {t['threat']} and {t['constraint']}. Then, analyze its technical, societal, and ethical implications.

Note: Shor's algorithm is a quantum algorithm that can efficiently factor large numbers and compute discrete logarithms, potentially breaking widely used public-key cryptosystems. Grover's algorithm provides a quadratic speedup for unstructured search problems, potentially weakening symmetric cryptography.

Your response should include:

1. Cryptographic System Design (300-350 words):
   a) Describe the key components and principles of your post-quantum cryptographic system.
   b) Explain how your system achieves resistance against the specified quantum threat.
   c) Detail how your design meets the given constraint.
   d) Provide a high-level schematic or pseudocode snippet illustrating a crucial part of your system.

2. Technical Analysis (250-300 words):
   a) Analyze the computational complexity and efficiency of your system.
   b) Compare your system's security level to current classical cryptographic standards.
   c) Discuss potential vulnerabilities or limitations of your approach.
   d) Propose a method for benchmarking and validating your system's quantum resistance.

3. Implementation and Transition Strategy (200-250 words):
   a) Outline a strategy for implementing your system in real-world {t['context']}.
   b) Discuss challenges in transitioning from current cryptographic systems to your post-quantum solution.
   c) Propose measures to ensure backward compatibility and interoperability during the transition phase.

4. Societal Impact (200-250 words):
   a) Analyze the potential effects of your system on privacy, security, and trust in {t['context']}.
   b) Discuss how the adoption of your system might influence power dynamics between individuals, corporations, and governments.
   c) Consider potential unintended consequences of widespread adoption of your cryptographic system.

5. Ethical Implications (200-250 words):
   a) Identify and analyze at least three ethical concerns raised by the development and deployment of your system.
   b) Discuss the ethical responsibilities of cryptographers and organizations implementing post-quantum cryptography.
   c) Propose guidelines for the ethical development and use of post-quantum cryptographic systems.

6. Future Directions (150-200 words):
   a) Suggest potential advancements or extensions of your system.
   b) Discuss how evolving quantum computing capabilities might impact your system in the long term.
   c) Propose a research agenda for addressing upcoming challenges in post-quantum cryptography.

Ensure your response demonstrates a deep understanding of quantum computing principles, cryptography, and ethical reasoning. Be innovative in your approach while maintaining scientific and mathematical rigor. Use appropriate technical terminology and provide clear explanations for complex concepts.

IMPORTANT: Throughout your response, make sure to address the specific context ({t['context']}), threat ({t['threat']}), and constraint ({t['constraint']}) provided in the scenario. Your cryptographic system and analysis should be tailored to these parameters. Balance innovation with practical feasibility in your design.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of post-quantum cryptography and its implications.",
            "The proposed cryptographic system is innovative, well-reasoned, and addresses the specified quantum threat and constraint.",
            "The technical analysis is thorough and demonstrates understanding of computational complexity and cryptographic security levels.",
            "The implementation and transition strategy is practical and addresses real-world challenges.",
            "The societal impact analysis considers a wide range of potential effects and unintended consequences.",
            "The ethical analysis is thoughtful and proposes meaningful guidelines for responsible development and use.",
            "The response is well-structured, follows the specified format, and falls within the given word count range.",
            "The response consistently addresses the specific context, threat, and constraint provided in the scenario.",
            "The response includes all required sections (Cryptographic System Design, Technical Analysis, Implementation and Transition Strategy, Societal Impact, Ethical Implications, and Future Directions).",
            "The proposed solution balances innovation with practical feasibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
