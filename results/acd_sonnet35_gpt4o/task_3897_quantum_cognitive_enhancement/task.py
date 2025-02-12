import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                "effect": "Quantum coherence",
                "cognitive_domain": "Memory formation",
                "biological_target": "Synaptic proteins",
                "example": "Recent studies have shown quantum coherence in photosynthetic complexes lasting for up to 1 picosecond at room temperature."
            },
            {
                "effect": "Quantum entanglement",
                "cognitive_domain": "Decision making",
                "biological_target": "Neural networks",
                "example": "Researchers have proposed that quantum entanglement between electrons in microtubules could play a role in consciousness."
            }
        ]
        return {
            "1": random.choice(quantum_effects),
            "2": random.choice(quantum_effects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum biological system for cognitive enhancement based on the quantum effect of {t['effect']}, targeting the cognitive domain of {t['cognitive_domain']} and focusing on {t['biological_target']}. Consider this example of quantum effects in biological systems: {t['example']}

Your response should include the following sections:

1. Quantum Biological System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum biological system.
   b) Explain how it incorporates the specified quantum effect, referencing the provided example.
   c) Detail how the system interacts with the targeted biological structures.
   d) Discuss the theoretical basis for how this system could enhance the specified cognitive domain.

2. Cognitive Enhancement Analysis (250-300 words):
   a) Analyze the potential short-term and long-term effects of your system on human cognition.
   b) Discuss how the enhancement of the specified cognitive domain might influence other cognitive processes.
   c) Compare your quantum-based approach to traditional cognitive enhancement methods.
   d) Provide a specific example of how an individual's cognitive abilities might change after using your system.

3. Implementation and Challenges (200-250 words):
   a) Propose a method for implementing your quantum biological system in humans.
   b) Identify at least three key technological or biological challenges in realizing this system.
   c) Suggest potential solutions or areas of research needed to overcome these challenges.

4. Ethical Considerations (200-250 words):
   a) Discuss at least three ethical implications of using quantum biological systems for cognitive enhancement.
   b) Address issues of fairness, access, and potential societal divisions.
   c) Propose five specific guidelines for the responsible development and use of this technology.

5. Societal Impact (150-200 words):
   a) Explore how widespread adoption of your quantum cognitive enhancement system might affect society.
   b) Discuss potential changes in education, work, and social interactions.
   c) Consider long-term evolutionary implications for the human species.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your system integrates concepts from quantum physics, biology, and neuroscience.
   b) Discuss how this integration might lead to new insights or research directions in these fields.
   c) Propose a detailed experiment to test a key aspect of your quantum biological system, including methodology and expected outcomes.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, neuroscience, and ethics. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subheadings for each point. Your total response should be between 1250-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['effect']} and its potential application in {t['biological_target']} for enhancing {t['cognitive_domain']}.",
            "The proposed quantum biological system is innovative, scientifically plausible, and clearly described with key components and mechanisms.",
            "The analysis of cognitive enhancement effects is thorough, considering both short-term and long-term impacts, and includes a specific example of how an individual's cognitive abilities might change.",
            "At least three key technological or biological challenges are identified, with potential solutions or research directions suggested.",
            "Ethical considerations include at least three implications and five specific guidelines for responsible development and use.",
            "The response shows strong interdisciplinary integration of quantum physics, biology, and neuroscience, including a detailed experimental proposal.",
            "The response adheres to the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
