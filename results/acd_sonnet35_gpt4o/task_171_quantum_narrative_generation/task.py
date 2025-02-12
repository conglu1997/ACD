import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "Superposition",
                "description": "A quantum state where a particle exists in multiple states simultaneously until observed."
            },
            {
                "concept": "Quantum Entanglement",
                "description": "A phenomenon where particles become interconnected and the state of one instantly influences the other, regardless of distance."
            }
        ]
        narrative_elements = [
            "character development",
            "plot progression"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "narrative_element": random.choice(narrative_elements)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "narrative_element": random.choice(narrative_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story (300-500 words) that incorporates the quantum computing concept of {t['quantum_concept']['concept']} into its {t['narrative_element']}. Your story should:

1. Clearly demonstrate an understanding of the quantum concept: {t['quantum_concept']['description']}
2. Use the quantum concept as a central element in the story's {t['narrative_element']}.
3. Create a coherent narrative that creatively applies the quantum concept to a fictional scenario.
4. Maintain scientific accuracy while engaging in speculative fiction.
5. Evoke a sense of wonder or philosophical contemplation related to the implications of quantum phenomena.

Ensure your story is creative, engaging, and demonstrates a deep understanding of both quantum principles and storytelling techniques."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately represents the quantum concept of {t['quantum_concept']['concept']}.",
            f"The quantum concept is central to the story's {t['narrative_element']}.",
            "The narrative is coherent and creatively applies the quantum concept to a fictional scenario.",
            "The story maintains scientific accuracy while engaging in speculative fiction.",
            "The story evokes a sense of wonder or philosophical contemplation related to quantum phenomena.",
            "The writing demonstrates a deep understanding of both quantum principles and storytelling techniques."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
