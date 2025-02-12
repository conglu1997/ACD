import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            {
                "principle": "Image schemas",
                "explanation": "Mental patterns derived from embodied experience that structure our understanding of abstract concepts"
            },
            {
                "principle": "Conceptual metaphor",
                "explanation": "Understanding and experiencing one kind of thing in terms of another, often grounded in physical experience"
            }
        ]
        return {
            "1": random.choice(cognitive_principles),
            "2": random.choice(cognitive_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI language processing system based on the principle of {t['principle']} from embodied cognition and cognitive linguistics. Then, analyze its potential impact on natural language understanding and generation. Your response should include:

1. Principle Overview (100-150 words):
   a) Explain the concept of {t['principle']} and its role in human cognition.
   b) Discuss how this principle relates to embodied cognition and language processing.

2. AI System Design (250-300 words):
   a) Describe the architecture of your AI system that incorporates {t['principle']}.
   b) Explain how the system would represent and process language using this principle.
   c) Discuss how your design differs from traditional NLP approaches.

3. Language Processing Example (200-250 words):
   a) Provide a specific example of how your system would process a complex linguistic input.
   b) Explain step-by-step how {t['principle']} is applied in this process.
   c) Compare this to how a traditional NLP system might handle the same input.

4. Cognitive Implications (150-200 words):
   a) Analyze how your system's approach might better mimic human language understanding.
   b) Discuss potential insights your system could provide into human cognition.

5. Challenges and Limitations (100-150 words):
   a) Identify potential challenges in implementing your system.
   b) Discuss any limitations of using {t['principle']} as a basis for AI language processing.

6. Future Directions (100-150 words):
   a) Propose how your system could be expanded or improved.
   b) Suggest potential applications in AI and cognitive science research.

Ensure your response demonstrates a deep understanding of embodied cognition, cognitive linguistics, and AI systems. Be innovative in your approach while maintaining scientific plausibility. Format your response with clear headings for each section.

Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly explain and incorporate the principle of {t['principle']} in the AI system design.",
            "The proposed AI system must demonstrate a clear and plausible integration of embodied cognition and cognitive linguistics principles.",
            "The language processing example should provide a detailed and logical explanation of how the system would handle complex linguistic input.",
            "The submission must include all six required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation while maintaining scientific plausibility.",
            "The analysis of cognitive implications and future directions should be insightful and well-reasoned.",
            "The response must show a deep understanding of embodied cognition, cognitive linguistics, and AI systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
