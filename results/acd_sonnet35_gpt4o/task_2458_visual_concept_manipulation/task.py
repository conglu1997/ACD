import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_concepts = [
            {"name": "cube", "properties": ["three-dimensional", "six faces", "right angles"]},
            {"name": "spiral", "properties": ["curved", "winding", "continuous"]},
            {"name": "tree", "properties": ["branching", "organic", "hierarchical"]},
            {"name": "wave", "properties": ["oscillating", "periodic", "fluid"]}
        ]
        transformations = [
            {"name": "inversion", "description": "turning the concept inside out or reversing its key properties"},
            {"name": "fragmentation", "description": "breaking the concept into smaller, disconnected parts"},
            {"name": "fusion", "description": "combining the concept with another, unrelated concept"},
            {"name": "dimensionality shift", "description": "changing the number of dimensions the concept exists in"}
        ]
        tasks = {}
        for i in range(2):
            concept = random.choice(visual_concepts)
            transformation = random.choice(transformations)
            tasks[str(i+1)] = {
                "concept": concept,
                "transformation": transformation
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to manipulate the visual concept of a {t['concept']['name']} using the transformation of {t['transformation']['name']}. This task is inspired by theories of mental imagery and visual perception in cognitive science.

{t['transformation']['name']} is defined as: {t['transformation']['description']}

Please respond to the following steps:

1. Conceptual Analysis (100-150 words):
   a) Describe the key visual properties of a {t['concept']['name']}, including but not limited to {', '.join(t['concept']['properties'])}.
   b) Explain how these properties contribute to our mental representation of a {t['concept']['name']}.

2. Transformation Process (150-200 words):
   a) Describe in detail how you would apply the {t['transformation']['name']} transformation to the {t['concept']['name']} concept.
   b) Explain how this transformation might alter our mental imagery of the {t['concept']['name']}.
   c) Discuss any challenges or ambiguities in this transformation process.

3. Resulting Concept (150-200 words):
   a) Describe the new visual concept resulting from the transformation.
   b) Explain how the original properties of the {t['concept']['name']} have been altered or preserved.
   c) Propose a name for this new concept that captures its essential features.
   d) Provide a brief visual description or sketch of the transformed concept (50-100 words).

4. Cognitive Science Perspective (100-150 words):
   a) Discuss how this transformation process relates to theories of mental imagery or visual perception in cognitive science.
   b) Explain what this task might reveal about the nature of visual concepts and their manipulation in the mind.

5. Practical Application (100-150 words):
   Propose a practical application or experiment that could utilize this transformed concept, either in cognitive science research, art and design, or another field of your choice.

Ensure your response demonstrates a deep understanding of visual concepts, mental imagery, and cognitive science principles. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section in your response, and adhere to the specified word counts.

Your total response should be between 650-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent analysis and transformation of the {t['concept']['name']} concept using {t['transformation']['name']}",
            "The explanation of the transformation process is detailed and plausible",
            "The resulting concept is creative and logically follows from the transformation",
            "A visual description or sketch of the transformed concept is provided",
            "The discussion of cognitive science principles is accurate and relevant",
            "The proposed practical application is innovative and well-reasoned",
            "The overall response demonstrates both understanding of visual concepts and creative thinking",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
