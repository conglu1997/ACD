import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "Spanish"),
            ("Arabic", "English"),
            ("Russian", "Japanese"),
            ("Hindi", "French")
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Inferior frontal gyrus"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "language_pair": random.choice(language_pairs),
                "focus_brain_region": random.choice(brain_regions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate between {t['language_pair'][0]} and {t['language_pair'][1]} by directly interpreting and manipulating neural patterns associated with language processing, with a particular focus on the role of {t['focus_brain_region']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI translation system.
   b) Explain how your system interfaces with human neural activity.
   c) Detail how your system processes and interprets neural patterns related to language.
   d) Discuss how you incorporate the specified brain region into your design.
   e) Include a high-level diagram or pseudocode to illustrate your architecture.

2. Neural-Linguistic Mapping (250-300 words):
   a) Explain how your system maps neural patterns to linguistic elements.
   b) Describe how you account for differences in language structure and grammar.
   c) Discuss how your system handles idiomatic expressions and cultural nuances.

3. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system translates a sentence.
   b) Describe how your system ensures accuracy and preserves meaning.
   c) Explain how your system handles ambiguity or multiple possible translations.

4. Learning and Adaptation (150-200 words):
   a) Describe how your system learns and improves its translation capabilities.
   b) Explain how it adapts to individual users' neural patterns and language use.

5. Cultural and Ethical Considerations (200-250 words):
   a) Discuss potential cultural implications of direct neural-linguistic translation.
   b) Analyze ethical concerns related to privacy, consent, and potential misuse.
   c) Propose guidelines for responsible development and use of this technology.

6. Challenges and Future Directions (150-200 words):
   a) Identify key technical or scientific challenges in implementing your system.
   b) Propose two potential applications beyond language translation.
   c) Suggest areas for future research or improvement.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI technologies. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections: System Architecture, Neural-Linguistic Mapping, Translation Process, Learning and Adaptation, Cultural and Ethical Considerations, and Challenges and Future Directions",
            "The AI system design is innovative and plausible, incorporating principles from neuroscience, linguistics, and AI",
            "The response demonstrates a deep understanding of neural language processing and translation challenges",
            "Cultural and ethical implications are thoroughly discussed with proposed guidelines",
            "The response shows interdisciplinary knowledge integration and creative problem-solving",
            "Technical terminology is used appropriately and complex concepts are clearly explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
