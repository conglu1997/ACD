import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        themes = ['nature', 'technology', 'emotions', 'time']
        concepts = {
            'nature': ['tree', 'river', 'mountain', 'sun', 'wind'],
            'technology': ['computer', 'robot', 'network', 'algorithm', 'data'],
            'emotions': ['love', 'fear', 'joy', 'anger', 'sadness'],
            'time': ['past', 'future', 'moment', 'eternity', 'change']
        }
        metaphor_types = ['personification', 'synesthesia', 'conceptual metaphor']
        
        theme1, theme2 = random.sample(themes, 2)
        return {
            "1": {"theme": theme1, "concepts": concepts[theme1], "metaphor_type": random.choice(metaphor_types)},
            "2": {"theme": theme2, "concepts": concepts[theme2], "metaphor_type": random.choice(metaphor_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a semantic network and use it to generate metaphorical poetry. Follow these steps:

1. Semantic Network Design (200-250 words):
   a) Create a semantic network using the theme '{t['theme']}' and the following concepts: {', '.join(t['concepts'])}.
   b) Define at least 10 nodes (including the given concepts) and establish meaningful connections between them.
   c) Explain the rationale behind your network structure and connections.
   d) Represent your semantic network using the following format:
      Node1: [Connection1, Connection2, ...]
      Node2: [Connection1, Connection2, ...]
      ...

2. Poetry Generation (100-150 words):
   a) Using your semantic network, generate a short metaphorical poem (4-6 lines) that incorporates at least three concepts from your network.
   b) Your poem must use the metaphor type: {t['metaphor_type']}.
   c) Explain how the structure of your semantic network influenced the metaphors and imagery in your poem.

3. Cognitive Analysis (150-200 words):
   a) Analyze how your semantic network and resulting poem relate to theories of conceptual metaphor and mental spaces in cognitive linguistics.
   b) Discuss how this approach might model aspects of human creative cognition.
   c) Compare and contrast your approach with at least one other theory of creative cognition.

4. AI Application (100-150 words):
   a) Propose how your semantic network approach could be implemented in an AI system for natural language understanding or generation.
   b) Discuss potential advantages and limitations of this approach compared to current NLP techniques.
   c) Compare your proposed approach with a specific existing AI model or technique for language tasks.

Ensure your response demonstrates a deep understanding of semantic networks, cognitive linguistics, and creative language use. Be innovative in your network design and poetic interpretation while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 550-750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The semantic network design is comprehensive, well-explained, and incorporates all given concepts from the '{t['theme']}' theme.",
            f"The poem effectively uses the {t['metaphor_type']} metaphor type and incorporates at least three concepts from the semantic network.",
            "The cognitive analysis demonstrates a clear understanding of conceptual metaphor theory and mental spaces, and includes a comparison with another theory.",
            "The AI application proposal is innovative, well-reasoned, and includes a comparison with an existing AI model or technique.",
            "The response shows creativity and interdisciplinary knowledge application throughout, while adhering to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
