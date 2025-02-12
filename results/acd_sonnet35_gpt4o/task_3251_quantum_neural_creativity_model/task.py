import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            ('quantum superposition', 'the ability of a quantum system to exist in multiple states simultaneously'),
            ('quantum entanglement', 'a phenomenon where particles become interconnected and share properties regardless of distance')
        ]
        neural_processes = [
            ('neural plasticity', 'the ability of the brain to form and reorganize synaptic connections'),
            ('default mode network', 'a network of interacting brain regions active when a person is not focused on the outside world')
        ]
        creativity_aspects = [
            ('divergent thinking', 'the ability to generate multiple unique ideas or solutions'),
            ('conceptual blending', 'the cognitive process of combining different mental concepts to form new ideas')
        ]
        tasks = [
            {
                'quantum_concept': qc[0],
                'quantum_concept_description': qc[1],
                'neural_process': np[0],
                'neural_process_description': np[1],
                'creativity_aspect': ca[0],
                'creativity_aspect_description': ca[1]
            }
            for qc in quantum_concepts
            for np in neural_processes
            for ca in creativity_aspects
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that integrates quantum mechanics, neural networks, and creativity theory to explain and potentially enhance human creative problem-solving abilities. Your model should incorporate the quantum concept of {t['quantum_concept']} ({t['quantum_concept_description']}), the neural process of {t['neural_process']} ({t['neural_process_description']}), and the creativity aspect of {t['creativity_aspect']} ({t['creativity_aspect_description']}). Your response should include:

1. Theoretical Framework (350-400 words):
   a) Explain how you integrate the specified quantum concept, neural process, and creativity aspect into a coherent theoretical framework.
   b) Describe the key components of your model and their interactions.
   c) Discuss how your model accounts for the emergence of creative thought from the interplay of quantum and neural processes.
   d) Provide a visual representation or diagram of your theoretical model (described in text format, max 20 lines).

2. Quantum-Neural Interface (300-350 words):
   a) Describe the proposed mechanism by which quantum processes might influence neural activity in your model.
   b) Explain how this interface could potentially contribute to creative problem-solving.
   c) Discuss any challenges or limitations in establishing this quantum-neural connection.

3. Creativity Enhancement Mechanism (300-350 words):
   a) Propose a specific mechanism by which your model could enhance creative problem-solving abilities.
   b) Explain how this mechanism leverages the integration of quantum and neural processes.
   c) Provide a hypothetical example of how this enhancement might manifest in a real-world creative task.

4. Experimental Design (250-300 words):
   a) Propose an experiment to test a key prediction of your quantum neural creativity model.
   b) Describe the methodology, including variables, procedures, and expected results.
   c) Explain how the results would support or refute your model.

5. Implications and Future Directions (250-300 words):
   a) Discuss the potential implications of your model for our understanding of human creativity and consciousness.
   b) Explore how your model might inform the development of new AI systems for creative tasks.
   c) Propose two directions for future research based on your model.

6. Ethical Considerations (200-250 words):
   a) Identify potential ethical concerns related to enhancing human creativity through quantum-neural interventions.
   b) Discuss the implications for individual autonomy and the nature of human achievement.
   c) Propose guidelines for the responsible development and application of such technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and creativity theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Include relevant citations or references to support your model and ideas. Your total response should be between 1650-1950 words. Include a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and creativity theory, with appropriate use of technical terminology and clear explanations of complex concepts.",
            f"The proposed model coherently integrates the specified quantum concept ({t['quantum_concept']}), neural process ({t['neural_process']}), and creativity aspect ({t['creativity_aspect']}) in a scientifically plausible manner.",
            "The response addresses all required sections with appropriate depth and creativity, adhering to the specified word counts and including relevant citations or references.",
            "The response includes a clear, detailed text description of a visual representation or diagram of the theoretical model.",
            "The proposed experimental design is well-thought-out, directly tests a key prediction of the model, and includes specific methodology and expected results.",
            "The response maintains scientific plausibility while being innovative and creative, and thoroughly discusses ethical implications and future research directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
