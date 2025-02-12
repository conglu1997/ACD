import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        fundamental_constants = [
            'speed of light',
            'gravitational constant',
            'Planck constant',
            'fine-structure constant'
        ]
        physical_laws = [
            'conservation of energy',
            'second law of thermodynamics',
            'equivalence principle',
            'quantum superposition'
        ]
        cosmic_phenomena = [
            'galaxy formation',
            'star life cycles',
            'black hole dynamics',
            'cosmic inflation'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'modified_constant': random.choice(fundamental_constants),
                'altered_law': random.choice(physical_laws),
                'focus_phenomenon': random.choice(cosmic_phenomena)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an alternative universe where the {t['modified_constant']} is significantly different and the {t['altered_law']} is modified. Explore how these changes would affect the universe's evolution, focusing on {t['focus_phenomenon']}. Your response should include:

1. Modified Physics (250-300 words):
   a) Describe how you would change the {t['modified_constant']} and modify the {t['altered_law']}.
   b) Explain the immediate consequences of these changes on fundamental physics.
   c) Discuss any new physical phenomena that might emerge from these modifications.

2. Cosmological Evolution (300-350 words):
   a) Outline how your modified universe would evolve from its inception.
   b) Compare and contrast this evolution with our current understanding of the Big Bang and cosmic evolution.
   c) Explain how the changes affect {t['focus_phenomenon']} in particular.
   d) Describe any unique large-scale structures that might form in your universe.

3. Potential for Complexity (250-300 words):
   a) Analyze whether your universe could support the formation of stable atoms, molecules, and more complex structures.
   b) Discuss the potential for life to emerge in your universe, considering the necessary conditions for life as we know it.
   c) If life is possible, speculate on how it might differ from life in our universe.

4. Mathematical Formulation (200-250 words):
   a) Provide at least one key equation that describes a fundamental aspect of your modified universe.
   b) Explain how this equation differs from its counterpart in our universe.
   c) Discuss the implications of this mathematical change on the universe's properties.

5. Observational Predictions (200-250 words):
   a) Describe what an observer in this universe might see when looking out at the cosmos.
   b) Propose an experiment or observation that could distinguish your universe from ours.
   c) Discuss any paradoxes or seemingly impossible phenomena that might arise in your universe.

6. Implications and Philosophical Considerations (200-250 words):
   a) Explore the philosophical implications of your universe, particularly regarding concepts of causality, determinism, or the nature of existence.
   b) Discuss how studying such alternative universes might contribute to our understanding of our own universe.
   c) Consider the implications of your universe for the anthropic principle or the idea of a 'multiverse'.

Ensure your response demonstrates a deep understanding of physics, cosmology, and related scientific fields. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining logical consistency and scientific plausibility. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately describes modifications to the {t['modified_constant']} and the {t['altered_law']}.",
            f"The analysis of {t['focus_phenomenon']} is thorough and logically consistent with the proposed changes.",
            "The cosmological evolution described is coherent and follows from the modified physics.",
            "The mathematical formulation provided is relevant and correctly differentiated from standard physics.",
            "The response demonstrates creativity while maintaining scientific plausibility.",
            "The implications and philosophical considerations are thoughtfully explored.",
            "The response shows a deep understanding of physics, cosmology, and related scientific fields.",
            "The writing is clear, well-structured, and uses appropriate scientific terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
