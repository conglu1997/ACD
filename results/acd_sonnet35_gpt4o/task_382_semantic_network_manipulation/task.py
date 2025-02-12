import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Time",
                "related_concepts": ["Clock", "Past", "Future", "Perception", "Relativity"]
            },
            {
                "concept": "Knowledge",
                "related_concepts": ["Learning", "Information", "Wisdom", "Experience", "Education"]
            }
        ]
        return {"1": random.choice(tasks), "2": random.choice(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a semantic network for the concept of '{t['concept']}'. Your task has four parts:

1. Semantic Network Creation (200-250 words):
   a) Create a semantic network with '{t['concept']}' as the central node.
   b) Include at least 10 nodes (including the central node) and 15 edges.
   c) Use the following related concepts in your network: {', '.join(t['related_concepts'])}.
   d) Describe your network, explaining the relationships between nodes.

2. Network Analysis (150-200 words):
   a) Identify the node with the highest degree centrality (most connections).
   b) Explain how this node influences the overall meaning of the network.
   c) Discuss any interesting patterns or clusters you observe in your network.

3. Cognitive Implications (150-200 words):
   a) Explain how your semantic network might represent human understanding of the concept.
   b) Discuss potential differences between this representation and how an AI might structure this knowledge.

4. Creative Application (200-250 words):
   Propose an innovative application of your semantic network in one of the following fields:
   - Natural Language Processing
   - Artificial Intelligence
   - Education
   - Psychology
   Explain how your application would work and its potential benefits.

Ensure your response demonstrates a deep understanding of semantic networks, linguistic concepts, and their applications. Be creative in your network design and application proposal while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The semantic network is well-constructed with at least 10 nodes and 15 edges, including all required related concepts.",
            "The network analysis is insightful and correctly identifies the node with the highest degree centrality.",
            "The cognitive implications discussion shows a deep understanding of human cognition and AI knowledge representation.",
            "The creative application is innovative, well-explained, and demonstrates a clear understanding of how semantic networks can be applied in the chosen field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
