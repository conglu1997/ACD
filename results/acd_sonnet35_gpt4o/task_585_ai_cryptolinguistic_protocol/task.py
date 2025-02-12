import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'context': 'interplanetary communication',
                'constraint': 'minimize transmission time',
                'security_level': 'high'
            },
            {
                'context': 'global financial transactions',
                'constraint': 'ensure backward compatibility',
                'security_level': 'very high'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven cryptolinguistic communication protocol that evolves its own language and encryption methods for {t['context']}. Your protocol should {t['constraint']} and provide {t['security_level']} security. Include the following in your response:

1. Protocol Overview (200-250 words):
   a) Describe the key components of your AI-driven cryptolinguistic protocol.
   b) Explain how it generates and evolves its own language and encryption methods.
   c) Discuss how it addresses the given context and constraints.

2. Language Evolution Mechanism (200-250 words):
   a) Detail the AI algorithms or techniques used for language generation and evolution.
   b) Explain how semantic meaning is preserved during language evolution.
   c) Describe how the protocol handles ambiguity and ensures mutual understanding between communicating parties.

3. Encryption Method (200-250 words):
   a) Explain the core encryption technique used in your protocol.
   b) Describe how the encryption method evolves over time.
   c) Discuss how key exchange and authentication are handled in your protocol.

4. Implementation and Training (150-200 words):
   a) Outline the steps to implement and train your AI-driven protocol.
   b) Discuss any specific machine learning architectures or techniques you would use.
   c) Address how you would evaluate the protocol's effectiveness during development.

5. Security Analysis (150-200 words):
   a) Analyze potential vulnerabilities in your protocol.
   b) Explain how it resists common cryptographic attacks.
   c) Discuss any trade-offs between security and efficiency in your design.

6. Practical Application (100-150 words):
   a) Describe a specific use case for your protocol in the given context.
   b) Explain the benefits and challenges of implementing your protocol in this scenario.

7. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of your AI-driven cryptolinguistic protocol.
   b) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, cryptography, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific and mathematical plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The protocol design is innovative and coherently integrates AI, linguistics, and cryptography.",
            "The language evolution mechanism is well-explained and theoretically sound.",
            "The encryption method is robust and evolves in a logical manner.",
            "The implementation and training process is clearly outlined and feasible.",
            "The security analysis is thorough and addresses relevant concerns.",
            "The practical application is relevant and well-reasoned.",
            "Ethical considerations are thoughtfully discussed.",
            f"The design adequately addresses the context of {t['context']} and the constraint to {t['constraint']}.",
            f"The protocol provides {t['security_level']} security as required."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
