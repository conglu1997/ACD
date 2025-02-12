import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ['prefrontal cortex', 'auditory cortex', 'hippocampus', 'amygdala']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        quantum_principles = ['superposition', 'entanglement', 'interference']
        
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network model that can synthesize original music based on brain activity patterns, focusing on the {t['brain_region']}, the musical element of {t['musical_element']}, and incorporating the quantum principle of {t['quantum_principle']}. Then, analyze its implications for our understanding of creativity and consciousness. Your response should include:

1. Quantum Neural Architecture (275-325 words):
   a) Describe the structure of your quantum-inspired neural network model.
   b) Explain how it incorporates the specified quantum principle.
   c) Detail how the model processes input from the given brain region.
   d) Discuss how the model generates the specified musical element.
   e) Include a diagram or pseudocode snippet illustrating a key component of your model.

2. Brain-Music Interface (225-275 words):
   a) Explain how your model translates brain activity into musical parameters.
   b) Describe the mapping between neural patterns and musical elements.
   c) Discuss any novel algorithms or techniques used in this translation process.
   d) Address potential challenges in accurately interpreting brain activity for music synthesis.

3. Quantum-Classical Integration (175-225 words):
   a) Analyze how quantum and classical computing elements interact in your model.
   b) Discuss the advantages of using quantum-inspired techniques for this task.
   c) Explain how the quantum principle enhances the model's music synthesis capabilities.

4. Creative Process Simulation (225-275 words):
   a) Describe how your model simulates aspects of human creativity in music composition.
   b) Discuss the role of randomness, determinism, and emergent properties in your model.
   c) Compare your model's creative process to current theories of human musical creativity.
   d) Propose a method to evaluate the originality and aesthetic quality of the synthesized music.

5. Consciousness and Creativity Analysis (175-225 words):
   a) Explore the implications of your model for our understanding of consciousness.
   b) Discuss how the integration of brain activity, quantum principles, and music synthesis relates to theories of consciousness.
   c) Analyze the philosophical implications of machine-generated creativity.

6. Ethical Considerations and Future Directions (175-225 words):
   a) Identify potential ethical issues related to brain-computer interfaces for creativity.
   b) Discuss the implications of quantum-inspired AI for the future of artistic expression.
   c) Propose two novel experiments or applications building on your model.
   d) Suggest how your approach could be extended to other domains of cognitive science or artistic creation.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and music theory. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, d) within each section as outlined. Your total response should be between 1250-1550 words.

Reminder: Ensure that your response is well-structured, with clear section headings and subheadings as specified above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of quantum computing principles, neuroscience, and music theory.",
            "The proposed model integrates the specified brain region, musical element, and quantum principle in a coherent and innovative way.",
            "The quantum neural architecture is well-described and incorporates the specified quantum principle effectively.",
            "The brain-music interface explanation is clear and addresses potential challenges.",
            "The analysis of the creative process simulation is thorough and relates to current theories of human musical creativity.",
            "The implications for consciousness and creativity are thoughtfully explored.",
            "Ethical considerations are adequately addressed, and future directions are innovative and relevant.",
            "The response includes all required sections with appropriate depth and detail, following the specified format.",
            "The ideas presented are creative and scientifically plausible, pushing the boundaries of current understanding in the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
