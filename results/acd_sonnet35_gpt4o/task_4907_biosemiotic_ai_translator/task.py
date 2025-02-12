import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organisms = [
            {"name": "Honey bees", "communication": "Dance language"},
            {"name": "Cephalopods", "communication": "Skin color and pattern changes"},
            {"name": "Whales", "communication": "Complex vocalizations"},
            {"name": "Plants", "communication": "Chemical signaling"}
        ]
        ethical_questions = [
            "How might interspecies communication change our understanding of consciousness and intelligence?",
            "What are the ethical implications of potentially altering natural communication systems through AI intervention?",
            "How could this technology impact conservation efforts and our relationship with nature?",
            "What are the risks of misinterpreting or manipulating biosemiotic signals across species?"
        ]
        return {
            "1": {
                "organism": random.choice(organisms),
                "question": random.choice(ethical_questions)
            },
            "2": {
                "organism": random.choice(organisms),
                "question": random.choice(ethical_questions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret and translate biosemiotic signals from {t['organism']['name']} ({t['organism']['communication']}) into human language, then use it to facilitate interspecies communication. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for biosemiotic interpretation and translation.
   b) Explain how your system captures and processes the specific communication modality of {t['organism']['name']}.
   c) Detail the AI algorithms or models used for signal interpretation and language generation.
   d) Discuss how your system handles the contextual and embodied nature of biosemiotic communication.
   e) Include a high-level diagram or flowchart of your system (use ASCII art or a structured text description).

2. Biosemiotic Analysis (250-300 words):
   a) Explain the key biosemiotic principles underlying your system's design.
   b) Discuss how your system accounts for the unique semiotic processes of {t['organism']['name']}.
   c) Analyze potential challenges in translating between vastly different semiotic systems (e.g., human language vs. {t['organism']['communication']}).

3. Interspecies Communication Protocol (200-250 words):
   a) Describe how your system facilitates two-way communication between humans and {t['organism']['name']}.
   b) Explain any novel interfaces or technologies necessary for this communication.
   c) Discuss potential applications and limitations of your interspecies communication system.

4. Ethical Implications (250-300 words):
   a) Address the ethical question: {t['question']}
   b) Discuss potential unintended consequences of your technology.
   c) Propose guidelines for the responsible development and use of biosemiotic AI translators.

5. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or applications of your biosemiotic AI system.
   b) Discuss how these extensions might further our understanding of communication and cognition across species.

Ensure your response demonstrates a deep understanding of biosemiotics, artificial intelligence, and the biology of {t['organism']['name']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics, AI, and the biology of the specified organism, using appropriate terminology and concepts from each field.",
            "The AI system design is innovative, scientifically plausible, and clearly explained, including its mechanisms for interpreting and translating biosemiotic signals.",
            "The interspecies communication protocol is well-thought-out and addresses potential challenges and limitations.",
            "The ethical implications are thoroughly considered, with well-reasoned guidelines for responsible development and use of the technology.",
            "The response is creative and original while maintaining scientific rigor throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
