import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "narrative_element": "Character development",
                "genre": "Science fiction"
            },
            {
                "quantum_principle": "Entanglement",
                "narrative_element": "Plot structure",
                "genre": "Mystery"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a narrative structure based on the quantum computing principle of {t['quantum_principle']}, focusing on the narrative element of {t['narrative_element']} in the {t['genre']} genre. Then, use this structure to create and analyze a short story. Your response should include:

1. Quantum Narrative Structure (200-250 words):
   a) Explain the quantum principle and how it relates to storytelling.
   b) Describe your novel narrative structure that incorporates this principle.
   c) Provide a diagram or schematic representation of your narrative structure.

2. Story Outline (150-200 words):
   a) Present a brief outline of a story using your quantum narrative structure.
   b) Explain how each major plot point or character development aligns with your structure.
   c) Discuss how the quantum principle influences the story's progression.

3. Short Story (400-500 words):
   Write a short story using your quantum narrative structure. Ensure that the story:
   a) Clearly demonstrates the influence of the quantum principle on the narrative.
   b) Focuses on the specified narrative element.
   c) Fits within the given genre.
   d) Is engaging and coherent despite its unconventional structure.

4. Analysis (200-250 words):
   a) Analyze how your story exemplifies the quantum narrative structure.
   b) Discuss the challenges and benefits of using this structure.
   c) Compare your quantum narrative structure to traditional storytelling methods.
   d) Explore potential applications of this narrative structure in literature or other media.

Ensure your response demonstrates a deep understanding of both quantum principles and narrative theory. Be creative in your approach while maintaining scientific accuracy and literary coherence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and applies the quantum principle of {t['quantum_principle']}.",
            f"The narrative structure effectively incorporates the quantum principle and focuses on {t['narrative_element']}.",
            f"The short story clearly demonstrates the quantum narrative structure and belongs to the {t['genre']} genre.",
            "The analysis provides insightful comparisons between the quantum narrative structure and traditional storytelling methods.",
            "The response shows creativity and originality in combining quantum concepts with narrative theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
