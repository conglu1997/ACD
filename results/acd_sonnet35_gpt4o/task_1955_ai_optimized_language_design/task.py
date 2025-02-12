import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        communication_scenarios = [
            {
                "scenario": "Distributed Problem Solving",
                "description": "AIs collaborating to solve complex mathematical and logical problems",
                "constraint": "The language must use no more than 64 unique symbols"
            },
            {
                "scenario": "Multi-Agent Negotiation",
                "description": "AIs negotiating resource allocation in a simulated economy",
                "constraint": "The language must be able to express probabilistic statements efficiently"
            }
        ]
        return {
            "1": random.choice(communication_scenarios),
            "2": random.choice(communication_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an optimized language for AI-to-AI communication, focusing on the scenario of {t['scenario']}. Your task is to create a detailed proposal for this language, addressing the following points:

1. Language Design Overview (250-300 words):
   a) Describe the key features and structure of your AI-to-AI communication language.
   b) Explain how these features optimize information transfer and processing for AIs.
   c) Discuss how your language design is particularly suited for {t['scenario']}.
   d) Explain how your design satisfies the constraint: {t['constraint']}.

2. Alphabet and Syntax (200-250 words):
   a) Define the basic units (alphabet) of your language and explain your choices.
   b) Describe the syntax rules of your language and how they contribute to its efficiency.
   c) Provide a simple example of how a message would be constructed in your language.

3. Semantic Encoding (200-250 words):
   a) Explain how meaning is encoded in your language.
   b) Discuss any novel approaches to semantic compression or representation.
   c) Describe how your language handles ambiguity or uncertainty.

4. Information Theoretic Analysis (200-250 words):
   a) Analyze the information density of your language compared to natural languages and existing computer protocols.
   b) Discuss the theoretical maximum information transfer rate of your language.
   c) Explain how your language minimizes redundancy while maintaining error tolerance.

5. Implementation and Processing (150-200 words):
   a) Describe how AIs would generate and parse messages in your language.
   b) Discuss any special hardware or software requirements for optimal use of your language.
   c) Explain how your language could be integrated with existing AI systems.

6. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or drawbacks of your language design.
   b) Discuss any ethical implications of using a highly optimized AI-to-AI language.
   c) Consider potential risks if such a language were to be adopted widely.

Ensure your response demonstrates a deep understanding of information theory, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design is well-suited for the scenario of {t['scenario']} and satisfies the constraint: {t['constraint']}.",
            "The proposal demonstrates a deep understanding of information theory, linguistics, and artificial intelligence.",
            "The language design is innovative and offers clear advantages over existing communication systems.",
            "The alphabet, syntax, and semantic encoding are well-defined and justified.",
            "The information theoretic analysis is thorough and demonstrates the efficiency of the language.",
            "The implementation and processing details are plausible and well-explained.",
            "Limitations and ethical considerations are thoughtfully addressed.",
            "The response is well-structured and addresses all required points comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
