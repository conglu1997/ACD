import random
import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        texts = [
            {
                "title": "The Lorax",
                "excerpt": "Unless someone like you cares a whole awful lot, nothing is going to get better. It's not.",
                "theme": "environmental conservation"
            },
            {
                "title": "1984",
                "excerpt": "War is peace. Freedom is slavery. Ignorance is strength.",
                "theme": "totalitarianism and surveillance"
            }
        ]
        return {
            "1": random.choice(texts),
            "2": random.choice(texts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following excerpt from '{t['title']}' and complete these tasks:

1. Semantic Network Creation (200-250 words):
   a) Identify key concepts, entities, and their relationships in the text.
   b) Create a semantic network representation of these elements.
   c) Explain how this network captures the essence of the excerpt and its theme of {t['theme']}.

2. Network Analysis (150-200 words):
   a) Identify central nodes and important connections in your semantic network.
   b) Explain how these elements contribute to the overall meaning of the text.
   c) Discuss any emergent properties or patterns in the network.

3. Poem Generation (poem of 8-12 lines):
   Using your semantic network as inspiration, compose a poem that:
   a) Captures the essence of the original text and its theme.
   b) Incorporates at least 3 key concepts from your semantic network.
   c) Maintains a coherent structure and flow.

4. Poetic Analysis (150-200 words):
   a) Explain how your poem reflects the semantic structure of the original text.
   b) Discuss the creative decisions you made in translating the semantic network into poetry.
   c) Analyze how well your poem captures the theme of {t['theme']}.

Excerpt: "{t['excerpt']}"

Ensure your response demonstrates a deep understanding of semantic analysis, network theory, and poetic composition. Be creative in your approach while maintaining analytical rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed semantic network analysis of the given text.",
            "The semantic network analysis demonstrates a deep understanding of the text's key concepts and their relationships.",
            "The generated poem effectively captures the essence and theme of the original text.",
            "The poem incorporates at least 3 key concepts from the semantic network.",
            "The poetic analysis provides insightful explanations of how the semantic structure was translated into poetry.",
            "The overall response demonstrates strong interdisciplinary skills in linguistics, network analysis, and creative writing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
