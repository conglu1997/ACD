import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            'Superposition',
            'Entanglement',
            'Quantum tunneling',
            'Wave function collapse'
        ]
        cognitive_theories = [
            'Working memory model',
            'Dual-process theory',
            'Predictive coding',
            'Connectionism'
        ]
        philosophical_concepts = [
            'Free will',
            'Consciousness',
            'Reality perception',
            'Time and causality'
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_theory": random.choice(cognitive_theories),
                "philosophical_concept": random.choice(philosophical_concepts)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_theory": random.choice(cognitive_theories),
                "philosophical_concept": random.choice(philosophical_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a narrative structure based on the quantum computing principle of {t['quantum_concept']} and the cognitive science theory of {t['cognitive_theory']}. Then, use this structure to create a short story that explores the philosophical concept of {t['philosophical_concept']}. Your response should include:

1. Narrative Structure Design (300-350 words):
   a) Explain how you integrate {t['quantum_concept']} with {t['cognitive_theory']} to create a unique narrative structure.
   b) Describe the key elements of your narrative structure and how they relate to both quantum and cognitive concepts.
   c) Discuss how this structure can be used to explore complex philosophical ideas.
   d) Provide a visual representation or diagram of your narrative structure.

2. Story Outline (200-250 words):
   a) Present a brief outline of a story using your quantum-cognitive narrative structure.
   b) Explain how each part of the outline reflects elements of your narrative structure.
   c) Describe how the story will explore the concept of {t['philosophical_concept']}.

3. Short Story (400-500 words):
   Write a short story using your quantum-cognitive narrative structure that explores {t['philosophical_concept']}. Ensure that elements of {t['quantum_concept']} and {t['cognitive_theory']} are evident in the story's structure and content.

4. Analysis (250-300 words):
   a) Analyze how your story effectively incorporates {t['quantum_concept']}, {t['cognitive_theory']}, and explores {t['philosophical_concept']}.
   b) Discuss any challenges you faced in integrating these diverse concepts into a coherent narrative.
   c) Explain how this approach to storytelling might offer new insights into the philosophical concept explored.

5. Potential Applications (150-200 words):
   a) Propose how this quantum-cognitive narrative approach could be applied in fields such as education, psychotherapy, or scientific communication.
   b) Discuss the potential benefits and limitations of using such complex, interdisciplinary narratives.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and philosophical concepts. Be creative and innovative in your approach while maintaining scientific and logical consistency. Use appropriate terminology from each field and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the quantum concept of {t['quantum_concept']} with the cognitive theory of {t['cognitive_theory']} to create a unique narrative structure.",
            f"The short story successfully explores the philosophical concept of {t['philosophical_concept']} using the quantum-cognitive narrative structure.",
            "The narrative structure and story demonstrate a deep understanding of quantum mechanics, cognitive science, and philosophy.",
            "The response shows creativity and innovation while maintaining scientific and logical consistency.",
            "The analysis and potential applications sections provide insightful reflections on the interdisciplinary approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
