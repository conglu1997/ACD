import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "justice", "freedom", "love", "time", "consciousness",
            "beauty", "truth", "infinity", "chaos", "harmony"
        ]
        neural_network_types = [
            "biological sensory cortex", "artificial feedforward network",
            "biological hippocampus", "artificial recurrent network",
            "biological prefrontal cortex", "artificial transformer network"
        ]
        mapping_techniques = [
            "representational similarity analysis",
            "cross-modal decoding",
            "semantic feature extraction",
            "conceptual space modeling",
            "graph-based alignment"
        ]
        
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "source_network": random.choice(neural_network_types),
                "target_network": random.choice(neural_network_types),
                "mapping_technique": random.choice(mapping_techniques)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "source_network": random.choice(neural_network_types),
                "target_network": random.choice(neural_network_types),
                "mapping_technique": random.choice(mapping_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to map the semantic representation of the abstract concept '{t['concept']}' from a {t['source_network']} to a {t['target_network']} using {t['mapping_technique']}. Your response should include:

1. Semantic Representation Design (250-300 words):
   a) Describe how the concept of '{t['concept']}' might be represented in the {t['source_network']}.
   b) Explain how this representation differs from or aligns with potential representations in the {t['target_network']}.
   c) Discuss any challenges specific to representing '{t['concept']}' in neural networks.

2. Mapping Technique Implementation (200-250 words):
   a) Explain how you would apply {t['mapping_technique']} to map between the two neural network types.
   b) Describe any modifications or novel approaches needed for this specific concept and network pair.
   c) Discuss potential limitations of this technique and how you might address them.

3. Analysis and Interpretation (200-250 words):
   a) Propose methods to validate the accuracy and meaningfulness of your semantic mapping.
   b) Discuss how differences in semantic representation between the networks might be interpreted.
   c) Explain how your analysis could contribute to our understanding of both biological and artificial neural processing of abstract concepts.

4. Implications and Applications (150-200 words):
   a) Discuss potential implications of your findings for theories of cognition and AI development.
   b) Propose a specific application of your semantic mapping system in either neuroscience or AI research.
   c) Consider any ethical implications of mapping abstract concepts between biological and artificial systems.

5. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your semantic mapping system.
   b) Propose a follow-up study that builds on the results of your current design.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the mapping of '{t['concept']}' between {t['source_network']} and {t['target_network']}",
            f"The implementation of {t['mapping_technique']} is clearly explained and appropriate for the task",
            "The response demonstrates a deep understanding of neuroscience, AI, and linguistics",
            "The analysis and interpretation section provides meaningful insights",
            "The implications and applications discussed are relevant and well-reasoned",
            "The proposed future research directions are innovative and build on the presented work",
            "The response follows the required format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
