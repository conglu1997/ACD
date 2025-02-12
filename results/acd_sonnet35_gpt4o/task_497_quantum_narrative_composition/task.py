import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Quantum Superposition",
                "description": "The principle that a quantum system can exist in multiple states simultaneously until observed or measured.",
                "example": "Schrödinger's cat thought experiment, where a cat in a box is considered both alive and dead until the box is opened."
            },
            {
                "concept": "Quantum Entanglement",
                "description": "A phenomenon where two or more quantum particles become correlated in such a way that the quantum state of each particle cannot be described independently of the others.",
                "example": "Einstein's 'spooky action at a distance', where measuring one particle instantly affects its entangled partner, regardless of the distance between them."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short story (800-1000 words) that incorporates the quantum computing concept of {t['concept']} as a central plot element. Your task has the following requirements:

1. Story Premise (50-75 words):
   Provide a brief overview of your story's setting and main character(s). The setting should be in a near-future world where quantum computing is more advanced than our current technology.

2. Quantum Concept Integration (throughout the story):
   Weave the concept of {t['concept']} into your narrative. The concept should be crucial to the plot development and resolution. Ensure that your use of the quantum concept is scientifically accurate and well-explained within the context of the story.

3. Character Development (throughout the story):
   Create at least one character who interacts with or is affected by the quantum concept. Show how their understanding or experience of {t['concept']} changes over the course of the story.

4. Narrative Structure:
   Your story should have a clear beginning, middle, and end. The quantum concept should drive the plot forward and be integral to the story's resolution.

5. Accessible Explanation (100-150 words within the story):
   Include a section where a character explains {t['concept']} in layman's terms to another character or the reader. This explanation should be accurate yet understandable to a non-expert.

6. Ethical or Philosophical Implication (100-150 words within the story):
   Explore an ethical or philosophical question raised by the application of {t['concept']} in your story's world.

7. Scientific Accuracy (throughout the story):
   While your story is fiction, ensure that all descriptions and applications of {t['concept']} are consistent with our current scientific understanding of quantum mechanics and quantum computing.

8. Word Count:
   Your story should be between 800-1000 words. Please include the word count at the end of your submission.

Ensure your story is engaging, scientifically accurate, and demonstrates a deep understanding of both quantum computing and narrative structure. Be creative in your approach while maintaining scientific plausibility.

Please format your response as a continuous narrative, with no separate sections or headings. Include the word count at the end of your story."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates and explains the quantum computing concept of {t['concept']}",
            "The quantum concept is central to the plot and drives the narrative forward",
            "The story includes a clear and accessible explanation of the quantum concept",
            "The narrative explores ethical or philosophical implications of the quantum concept",
            "The story demonstrates creativity while maintaining scientific accuracy",
            "The story has a coherent structure with well-developed characters and a satisfying resolution",
            "The story meets the required word count of 800-1000 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
