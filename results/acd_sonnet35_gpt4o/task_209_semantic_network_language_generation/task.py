import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        semantic_networks = [
            {
                "network_type": "Hierarchical Network",
                "description": "Organizes concepts in a tree-like structure with broader concepts at the top and more specific ones below."
            },
            {
                "network_type": "Associative Network",
                "description": "Connects concepts based on associations or relationships, without a strict hierarchy."
            },
            {
                "network_type": "Feature-based Network",
                "description": "Represents concepts as collections of features or attributes."
            }
        ]
        return {str(i+1): network for i, network in enumerate(random.sample(semantic_networks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given semantic network type and create a hybrid semantic network for language generation. Your task has four parts:

1. Network Analysis (100-150 words):
   Analyze the {t['network_type']}. {t['description']}
   Explain its strengths and weaknesses in representing linguistic knowledge.

2. Hybrid Network Design (150-200 words):
   Create a hybrid semantic network that combines features of the {t['network_type']} with another type of semantic network of your choice.
   Describe the structure and key features of your hybrid network.
   Explain how it addresses the weaknesses of the original network while maintaining its strengths.

3. Concept Representation (100-150 words):
   Choose three abstract concepts: 'time', 'emotion', and 'causality'.
   Explain how these concepts would be represented in your hybrid semantic network.
   Provide specific examples of connections or attributes for each concept.

4. Language Generation (150-200 words):
   Based on your hybrid semantic network, generate a short paragraph (3-5 sentences) that incorporates the three abstract concepts.
   Explain how the structure of your semantic network influenced the generated text.
   Discuss any challenges or unique features that emerged during the language generation process.

Ensure your response demonstrates a deep understanding of semantic networks, linguistic representation, and creative problem-solving in combining these concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must analyze the given semantic network type and create a hybrid network",
            "The hybrid network design should address weaknesses of the original network while maintaining its strengths",
            "The representation of abstract concepts should be clear and consistent with the hybrid network design",
            "The generated language should incorporate the abstract concepts and reflect the structure of the hybrid network",
            "The response should demonstrate interdisciplinary reasoning and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0