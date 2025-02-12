import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species = [
            "bees",
            "octopuses",
            "dolphins",
            "ants",
            "trees",
            "slime molds"
        ]
        abstract_concepts = [
            "democracy",
            "ethics",
            "consciousness",
            "time",
            "infinity",
            "beauty"
        ]
        return {
            "1": {
                "species": random.choice(species),
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "species": random.choice(species),
                "concept": random.choice(abstract_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that creates a novel form of communication inspired by {t['species']}, then use it to express the complex abstract concept of {t['concept']}. Your response should include:

1. Communication System Design (300-350 words):
   a) Describe the key features of your AI-generated communication system, explaining how it's inspired by {t['species']}.
   b) Detail at least three unique aspects of this communication system (e.g., modality, syntax, semantics).
   c) Explain how your AI system generates and interprets this novel form of communication.

2. Biological-Linguistic Integration (250-300 words):
   a) Analyze how at least three specific communication mechanisms or processes from {t['species']} are translated into your AI-generated language.
   b) Discuss two major challenges in this biological-to-linguistic translation and how you addressed them.
   c) Explain how this integration enhances the system's ability to express complex abstract concepts.

3. Expressing the Abstract Concept (250-300 words):
   a) Use your AI-generated communication system to express the concept of {t['concept']}.
   b) Provide a detailed 'translation' or explanation of how this concept is conveyed in the new communication system.
   c) Discuss any unique advantages or limitations of expressing {t['concept']} in this new form of communication compared to human languages.
   d) Provide a concrete example of how a simple message related to {t['concept']} would be communicated in this system, including its 'encoding' and 'decoding'.

4. Cognitive and AI Implications (200-250 words):
   a) Analyze how creating and using this communication system might influence AI cognitive processes.
   b) Discuss potential applications of this system in enhancing human-AI interaction or AI-AI communication.
   c) Explore how this approach might contribute to our understanding of language, cognition, and consciousness.

5. Ethical and Societal Considerations (200-250 words):
   a) Identify at least three potential ethical concerns arising from the development and use of this AI-generated communication system.
   b) Discuss the potential impact of this technology on human languages and intercultural communication.
   c) Propose guidelines or safeguards for the responsible development and use of AI-generated communication systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering scientific plausibility throughout your response.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The communication system is clearly inspired by {t['species']} and has at least three unique, well-explained aspects",
            f"The response effectively expresses the concept of {t['concept']} using the novel communication system",
            "The biological-linguistic integration is thoroughly analyzed with specific examples",
            "A concrete example of encoding and decoding a simple message related to the abstract concept is provided",
            "The cognitive and AI implications are insightfully discussed",
            "Ethical and societal considerations are thoughtfully addressed",
            "The response demonstrates deep understanding of linguistics, cognitive science, and artificial intelligence",
            "The proposed system is innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
