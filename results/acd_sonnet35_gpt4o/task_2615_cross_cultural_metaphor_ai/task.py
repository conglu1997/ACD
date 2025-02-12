import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "time",
            "love",
            "power",
            "justice",
            "knowledge"
        ]
        cultures = [
            "Chinese",
            "Maori",
            "Inuit",
            "Yoruba",
            "Navajo"
        ]
        applications = [
            "cross-cultural communication",
            "literary analysis",
            "conflict resolution",
            "mental health therapy",
            "educational tools"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "application": random.choice(applications)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract conceptual metaphors across different languages and cultures, focusing on the concept of {t['concept']} in {t['culture1']} and {t['culture2']} cultures. Then, analyze its potential application in {t['application']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system processes linguistic and cultural data to generate and interpret metaphors.
   c) Detail any novel algorithms or techniques used in your system.
   d) Discuss how your system accounts for cultural context and nuances in metaphor generation and interpretation.

2. Metaphor Analysis (250-300 words):
   a) Provide an example of a metaphor for {t['concept']} that your system might generate for each of the two cultures.
   b) Explain how these metaphors reflect the cultural and linguistic contexts of {t['culture1']} and {t['culture2']}.
   c) Analyze how your system interprets and translates these metaphors between the two cultures.

3. Cognitive Science Integration (200-250 words):
   a) Explain how your AI system incorporates principles from cognitive science and conceptual metaphor theory.
   b) Discuss how your system models the cognitive processes involved in metaphor comprehension and generation.
   c) Describe any novel insights your system might provide about human cognition and metaphor use.

4. Application in {t['application']} (200-250 words):
   a) Propose a specific application of your AI system in the field of {t['application']}.
   b) Explain how the system's ability to generate and interpret cross-cultural metaphors would be beneficial in this context.
   c) Discuss potential challenges and limitations of using your system in this application.

5. Ethical Implications (150-200 words):
   a) Identify potential ethical concerns related to the development and use of your AI system.
   b) Discuss issues of cultural appropriation, misrepresentation, or oversimplification.
   c) Propose guidelines for the responsible development and use of cross-cultural metaphor AI systems.

6. Evaluation and Future Directions (150-200 words):
   a) Propose a method for evaluating the accuracy and cultural sensitivity of your AI system's metaphor generation and interpretation.
   b) Suggest two potential improvements or extensions to your system for future research.
   c) Discuss how this technology might impact our understanding of language, culture, and cognition in the long term.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, AI, and cultural anthropology.",
            "The AI system design is innovative, technically sound, and addresses the complexities of cross-cultural metaphor generation and interpretation.",
            "The metaphor analysis shows a nuanced understanding of cultural differences and linguistic structures.",
            "The application of the AI system in the specified field is well-reasoned and considers potential challenges.",
            "Ethical implications are thoroughly considered, and responsible development guidelines are proposed.",
            "The evaluation method and future directions demonstrate critical thinking and awareness of the technology's broader implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
