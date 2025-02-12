import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            {"concept": "Justice", "domain": "Ethics"},
            {"concept": "Entropy", "domain": "Physics"},
            {"concept": "Consciousness", "domain": "Philosophy"},
            {"concept": "Recursion", "domain": "Computer Science"},
            {"concept": "Synergy", "domain": "Business"},
            {"concept": "Homeostasis", "domain": "Biology"}
        ]
        return {
            "1": random.choice(abstract_concepts),
            "2": random.choice(abstract_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the abstract concept of {t['concept']} from the domain of {t['domain']} into a universal visual language. Your response should include the following sections:

1. Conceptual Analysis (200-250 words):
   a) Analyze the key components and attributes of the concept {t['concept']}.
   b) Discuss how this concept is understood across different cultures.
   c) Identify any challenges in representing this concept visually.

2. Visual Language Design (250-300 words):
   a) Describe the core elements of your universal visual language (e.g., shapes, colors, spatial relationships).
   b) Explain how these elements can be combined to represent complex ideas.
   c) Provide a detailed description of how your system would visually represent {t['concept']}.
   d) Discuss how your visual language ensures cross-cultural understanding.
   e) Include a text-based description or ASCII art representation of your visual language applied to {t['concept']}.

3. Translation Algorithm (200-250 words):
   a) Outline the step-by-step process your system uses to translate {t['concept']} into the visual language.
   b) Explain how your algorithm handles nuances and context-dependent meanings.
   c) Describe any machine learning or AI techniques used in the translation process.

4. Cognitive Science Foundation (200-250 words):
   a) Discuss how your system aligns with cognitive theories of concept representation and visual processing.
   b) Explain how you've incorporated principles of human perception and memory into your design.
   c) Analyze potential cognitive load and learning curve for users of your visual language.

5. Cross-cultural Validation (150-200 words):
   a) Propose a method to test the cross-cultural effectiveness of your visual representation.
   b) Discuss potential cultural biases in your system and how you would address them.
   c) Explain how your system could adapt to cultural feedback and improve over time.

6. AI-Human Interaction Applications (200-250 words):
   a) Describe two potential applications of your system in AI-human interaction.
   b) Analyze how your visual language could enhance AI's understanding of abstract human concepts.
   c) Discuss any ethical considerations in using this system for AI-human communication.

7. Limitations and Future Work (150-200 words):
   a) Identify potential limitations of your approach.
   b) Suggest two areas for future research or improvement.
   c) Discuss how emerging technologies might enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the abstract concept {t['concept']} and its representation across cultures.",
            "The proposed visual language design is innovative, well-explained, and plausibly universal, with a clear text-based or ASCII art example provided.",
            "The translation algorithm is clearly outlined, step-by-step, and incorporates advanced AI or machine learning techniques.",
            "The system design is well-grounded in specific cognitive science principles and theories.",
            "The cross-cultural validation method is detailed, thoughtful, and addresses potential biases with concrete strategies.",
            "The proposed AI-human interaction applications are novel, well-analyzed, and consider both benefits and risks.",
            "The response identifies meaningful limitations and proposes specific, relevant areas for future research.",
            "The overall response shows strong interdisciplinary integration, creative problem-solving, and maintains scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
