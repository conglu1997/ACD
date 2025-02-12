import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "infinity",
            "consciousness",
            "freedom",
            "time",
            "beauty",
            "justice",
            "chaos",
            "unity"
        ]
        tasks = [
            {
                'concept1': random.choice(abstract_concepts),
                'concept2': random.choice(abstract_concepts),
                'application_domain': random.choice(['education', 'art', 'philosophy', 'science'])
            },
            {
                'concept1': random.choice(abstract_concepts),
                'concept2': random.choice(abstract_concepts),
                'application_domain': random.choice(['politics', 'psychology', 'technology', 'ethics'])
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication protocol for direct transfer of abstract thoughts between minds, focusing on the concepts of {t['concept1']} and {t['concept2']}. Then, analyze its potential applications in the domain of {t['application_domain']}. Your response should include:

1. Protocol Design (300-350 words):
   a) Describe the fundamental principles of your abstract thought transfer protocol.
   b) Explain how your protocol encodes and decodes the abstract concepts of {t['concept1']} and {t['concept2']}.
   c) Detail the mechanism for transmitting these encoded thoughts between minds.
   d) Discuss how your protocol handles the subjective nature of abstract concepts.

2. Cognitive Interface (200-250 words):
   a) Explain how your protocol interfaces with the human (or AI) cognitive system.
   b) Describe any potential cognitive prerequisites or training needed to use the protocol.
   c) Discuss how the protocol might affect or be affected by individual differences in cognition.

3. Application Analysis (200-250 words):
   a) Analyze potential applications of your protocol in the domain of {t['application_domain']}.
   b) Provide two specific examples of how the protocol could be used in this domain.
   c) Discuss potential benefits and risks associated with these applications.

4. Ethical and Philosophical Implications (150-200 words):
   a) Explore the ethical considerations of direct abstract thought transfer.
   b) Discuss how your protocol might impact concepts of privacy, individuality, and consciousness.
   c) Consider potential long-term societal effects if such a protocol became widely used.

5. Technical Challenges and Future Development (150-200 words):
   a) Identify key technical challenges in implementing your protocol.
   b) Propose potential solutions or areas for future research to address these challenges.
   c) Speculate on how this technology might evolve in the next 50 years.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, information theory, and the chosen application domain. Be creative and rigorous in your approach while acknowledging the speculative nature of the task. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and information theory.",
            "The protocol design is innovative, logically consistent, and addresses the encoding and transmission of abstract concepts.",
            "The cognitive interface is well-explained and considers individual differences in cognition.",
            "The application analysis provides specific, relevant examples in the given domain.",
            "Ethical and philosophical implications are thoroughly explored.",
            "Technical challenges are identified and addressed with potential solutions or research directions.",
            "The response is creative while maintaining scientific plausibility.",
            "All sections are adequately addressed within the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
