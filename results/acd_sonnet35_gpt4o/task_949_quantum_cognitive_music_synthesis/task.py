import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse"
        ]
        cognitive_processes = [
            "Working memory",
            "Attention",
            "Pattern recognition",
            "Divergent thinking"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody",
            "Timbre"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-cognitive model for musical composition that integrates the quantum concept of {t['quantum_concept']}, the cognitive process of {t['cognitive_process']}, and the musical element of {t['musical_element']}. Your response should include:

1. Model Overview (200-250 words):
   a) Describe the key components and structure of your quantum-cognitive music composition model.
   b) Explain how it integrates the specified quantum concept, cognitive process, and musical element.
   c) Discuss the theoretical basis for your model, citing relevant research in quantum physics, cognitive science, and music theory.

2. Quantum-Cognitive Integration (200-250 words):
   a) Detail how {t['quantum_concept']} is applied in your model to represent or process musical information.
   b) Explain how this quantum concept interacts with the cognitive process of {t['cognitive_process']}.
   c) Provide a mathematical or conceptual representation of a key operation in your model, focusing on the quantum-cognitive interaction.

3. Musical Application (150-200 words):
   a) Describe how your model specifically addresses the musical element of {t['musical_element']}.
   b) Explain how the quantum-cognitive aspects of your model enhance or transform traditional approaches to this musical element.
   c) Provide an example of how your model might generate or analyze a musical piece, focusing on {t['musical_element']}.

4. Creative Potential Analysis (150-200 words):
   a) Discuss how your model might enhance musical creativity or generate novel musical ideas.
   b) Analyze potential limitations or challenges in applying quantum-cognitive principles to music composition.
   c) Propose a method for evaluating the creative output of your model compared to traditional composition techniques.

5. Interdisciplinary Implications (100-150 words):
   a) Explore how your model might contribute to advancements in quantum computing, cognitive science, or music theory.
   b) Suggest potential applications of your model outside of music composition.

6. Ethical and Philosophical Considerations (100-150 words):
   a) Discuss the ethical implications of using quantum-cognitive models in creative arts.
   b) Explore philosophical questions raised by your model regarding consciousness, creativity, and the nature of music.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and music theory. Use appropriate technical terminology and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response with clear headings for each section.

Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['quantum_concept']}, {t['cognitive_process']}, and {t['musical_element']}.",
            "The quantum-cognitive model for musical composition is innovative and well-explained.",
            "The integration of quantum concepts, cognitive processes, and musical elements is logically sound and creative.",
            "The response includes appropriate technical terminology from quantum physics, cognitive science, and music theory.",
            "The model's potential for enhancing musical creativity is thoroughly analyzed.",
            "Interdisciplinary implications and ethical considerations are thoughtfully discussed.",
            "The response is well-structured with clear headings for each section as requested.",
            "The response maintains scientific plausibility while showcasing creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
