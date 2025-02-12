class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "complex_concept": "Quantum entanglement is a physical phenomenon that occurs when pairs or groups of particles are generated, interact, or share spatial proximity in ways such that the quantum state of each particle cannot be described independently of the state of the others, even when the particles are separated by a large distance. This phenomenon challenges classical intuitions about the separability of distant objects and has implications for quantum information theory.",
                "layman_description": "When two particles become connected in such a way that the state of one instantly affects the state of the other, no matter how far apart they are."
            },
            "2": {
                "complex_concept": "Photosynthesis is a process used by plants and other organisms to convert light energy, usually from the Sun, into chemical energy that can later be released to fuel the organisms' activities. This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water. Photosynthesis maintains atmospheric oxygen levels and supplies all of the organic compounds and most of the energy necessary for life on Earth.",
                "layman_description": "Plants use sunlight to turn water and carbon dioxide into food and oxygen."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following complex scientific concept into layman's terms. Your translation should be accurate, easily understandable, and capture the essence of the concept:

Concept: {t['complex_concept']}

And translate the following layman's description back into scientific terminology. Use appropriate scientific language in your translation and ensure it accurately reflects the description:

Description: {t['layman_description']}

Submit your response in the following format:

Layman's Terms Translation: [Your translation here]
Scientific Terminology Translation: [Your translation here]

Example (Note: This is just an example and not related to the actual tasks):

Layman's Terms Translation: When two particles become connected in such a way that the state of one instantly affects the state of the other, no matter how far apart they are.
Scientific Terminology Translation: Quantum entanglement is a physical phenomenon that occurs when pairs or groups of particles are generated, interact, or share spatial proximity in ways such that the quantum state of each particle cannot be described independently of the state of the others, even when the particles are separated by a large distance."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The layman's terms translation should accurately and clearly convey the scientific concept.",
            "The scientific terminology translation should correctly reflect the layman's description using appropriate scientific language.",
            "Both translations should be coherent and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
