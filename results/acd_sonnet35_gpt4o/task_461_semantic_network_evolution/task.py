import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "seed_concept": "tree",
                "related_concepts": ["forest", "leaf", "branch", "root", "ecosystem", "photosynthesis", "oxygen", "timber", "shade", "growth"],
                "target_concept": "climate change"
            },
            {
                "seed_concept": "democracy",
                "related_concepts": ["vote", "freedom", "election", "government", "representation", "citizen", "debate", "equality", "constitution", "rights"],
                "target_concept": "artificial intelligence"
            },
            {
                "seed_concept": "music",
                "related_concepts": ["rhythm", "melody", "instrument", "composer", "concert", "emotion", "harmony", "genre", "performance", "sound"],
                "target_concept": "quantum physics"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze the evolution of a semantic network based on the given concepts, then compare it with AI-generated semantic expansions. A semantic network is a graph structure for representing knowledge in patterns of interconnected nodes and arcs, where concepts are represented by nodes and relationships between concepts by arcs.

Your task involves the following steps:

1. Semantic Network Design (200-250 words):
   a) Starting with the seed concept "{t['seed_concept']}", create a semantic network using the provided related concepts: {', '.join(t['related_concepts'])}.
   b) Explain the relationships between concepts, including hierarchical, associative, and causal connections.
   c) Describe how you would visually represent this network (e.g., nodes, edges, weights).
   d) Provide a simple ASCII art representation of your initial semantic network.

2. Network Evolution (200-250 words):
   a) Propose a method to evolve this semantic network towards the target concept "{t['target_concept']}".
   b) Describe 3-4 intermediate steps in this evolution, explaining how new concepts are introduced and connections are formed or strengthened.
   c) Discuss any cognitive principles or heuristics you're applying in this evolution process.

3. AI Comparison (150-200 words):
   a) Hypothesize how an AI language model might approach this task of semantic expansion.
   b) Discuss potential differences between human-designed and AI-generated semantic networks.
   c) Propose a method to quantitatively compare the two approaches.

4. Cognitive Implications (100-150 words):
   a) Discuss what this task reveals about human cognition and knowledge representation.
   b) Explain how this might inform our understanding of artificial intelligence and machine learning.

5. Practical Applications (100-150 words):
   a) Propose two practical applications of this semantic network evolution in fields such as education, scientific research, or AI development.
   b) Briefly explain how each application would work and its potential benefits.

Ensure your response demonstrates a deep understanding of semantic relationships, cognitive science principles, and AI concepts. Be creative in your network design and evolution while maintaining logical consistency. Use clear headings for each section of your response, and include subheadings within each main section to improve clarity and structure."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The semantic network design clearly incorporates the seed concept '{t['seed_concept']}' and the provided related concepts",
            "An ASCII art representation of the initial semantic network is provided and is consistent with the description",
            "The network evolution process is logically explained and shows a clear progression towards the target concept",
            "The AI comparison demonstrates an understanding of both human cognition and AI language models",
            "The cognitive implications and practical applications are insightful and well-reasoned",
            "The response shows creativity and depth of understanding in semantic relationships and knowledge representation",
            "The overall analysis is coherent, well-structured, and adheres to the specified word limits and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
