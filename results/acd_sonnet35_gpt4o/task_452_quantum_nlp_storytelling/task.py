import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_concepts": ["superposition", "entanglement", "quantum tunneling"],
                "story_theme": "A day in the life of a quantum particle",
                "word_limit": 250
            },
            "2": {
                "quantum_concepts": ["wave-particle duality", "quantum teleportation", "Schrödinger's cat"],
                "story_theme": "A love story across parallel universes",
                "word_limit": 300
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model and use it to generate a short story. Your task has the following steps:

1. Quantum Language Model Design (200-250 words):
   a) Describe a language model that incorporates principles from quantum computing.
   b) Explain how your model represents words or sentences using quantum states.
   c) Describe how your model performs text generation using quantum operations.
   d) Discuss any advantages your quantum-inspired model might have over classical language models.

2. Quantum Storytelling (Word limit: {t['word_limit']}):
   Using your quantum-inspired language model, generate a short story that incorporates the following elements:
   a) Theme: {t['story_theme']}
   b) Quantum concepts to include: {', '.join(t['quantum_concepts'])}
   Ensure that the quantum concepts are integral to the plot or setting of the story, not just mentioned in passing.

3. Model and Story Analysis (150-200 words):
   a) Explain how your quantum language model influenced the story generation process.
   b) Analyze how the quantum concepts were integrated into the narrative structure.
   c) Discuss any challenges or unique features that emerged during the storytelling process.

4. Scientific and Literary Merit (100-150 words):
   a) Evaluate the scientific accuracy of the quantum concepts as presented in the story.
   b) Discuss the potential literary or educational value of using quantum-inspired storytelling.

Ensure your response demonstrates a deep understanding of quantum computing principles, natural language processing, and creative writing techniques. Be innovative in your approach while maintaining scientific plausibility and literary coherence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of a quantum-inspired language model.",
            f"A short story of approximately {t['word_limit']} words is generated using the described model.",
            f"The story incorporates the theme '{t['story_theme']}' and the quantum concepts: {', '.join(t['quantum_concepts'])}.",
            "The response includes an analysis of how the quantum language model influenced the story generation.",
            "The scientific accuracy and literary merit of the story are evaluated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
