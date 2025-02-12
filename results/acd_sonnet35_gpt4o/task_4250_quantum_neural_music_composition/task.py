import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque",
            "Classical",
            "Romantic",
            "Jazz",
            "Electronic"
        ]
        neural_processes = [
            "Synaptic plasticity",
            "Neuronal oscillations",
            "Spike-timing-dependent plasticity",
            "Cortical column dynamics",
            "Neurotransmitter release"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference",
            "Quantum annealing"
        ]
        
        task1 = {
            "musical_style": random.choice(musical_styles),
            "neural_process": random.choice(neural_processes),
            "quantum_principle": random.choice(quantum_principles)
        }
        task2 = {
            "musical_style": random.choice(musical_styles),
            "neural_process": random.choice(neural_processes),
            "quantum_principle": random.choice(quantum_principles)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates neural processes to compose music, then analyze its output and potential applications in neuroscience and musicology. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the neural process of {t['neural_process']}, and apply it to compose music in the style of {t['musical_style']}. Your response should include the following sections:

1. Quantum-Neural-Musical Integration (300-350 words):
   a) Explain how you integrate {t['quantum_principle']} with {t['neural_process']} to compose {t['musical_style']} music.
   b) Describe the novel quantum algorithms or techniques used in your system.
   c) Discuss how quantum principles enhance the modeling of neural processes for music composition.
   d) Include a high-level description of your system architecture.
   e) Provide a concrete example or hypothetical scenario to illustrate your integration approach.

2. Quantum Simulation of Neural Processes (250-300 words):
   a) Detail how your system represents neural features as quantum states.
   b) Explain how quantum operations model changes in neural activity during the composition process.
   c) Describe how your system handles the interaction between multiple neural components.
   d) Discuss how you address the challenge of maintaining quantum coherence in your system.
   e) Include a specific example of how a neural feature is represented and manipulated in your quantum system.

3. Music Composition Process (200-250 words):
   a) Explain how your system generates musical elements (e.g., melody, harmony, rhythm) using quantum-neural processes.
   b) Describe how the system ensures adherence to the principles of {t['musical_style']}.
   c) Provide an example of a specific musical passage your system might generate, including a brief musical notation or description.

4. Output Analysis (200-250 words):
   a) Analyze the characteristics of the music composed by your quantum-neural system.
   b) Compare the output to traditional computer-generated and human-composed music in the {t['musical_style']} style.
   c) Discuss any unique features or patterns that emerge from your quantum-neural approach.
   d) Provide a hypothetical listener's perspective on the composed music.

5. Neuroscientific and Musicological Implications (200-250 words):
   a) Discuss how your system's music composition process might inform our understanding of {t['neural_process']} in the brain.
   b) Explore potential insights into musical creativity and cognition that your system might provide.
   c) Propose an experiment that could test a hypothesis derived from your quantum-neural music composition system.
   d) Speculate on how your system might contribute to our understanding of the relationship between brain function and musical expression.

6. Future Directions and Applications (150-200 words):
   a) Suggest two potential extensions or applications of your quantum-neural music composition system.
   b) Discuss how this research might influence our understanding of consciousness, creativity, and quantum systems.
   c) Speculate on the long-term implications of quantum computing in neuroscience and musicology.
   d) Propose a novel research question that could be explored using your system.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and music theory. Use appropriate technical terminology from all three fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Throughout your response, strive to provide concrete examples, hypothetical scenarios, or specific illustrations to support your ideas.

Format your response with clear headings for each section, and number your paragraphs within each section for clarity. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response integrates {t['quantum_principle']}, {t['neural_process']}, and {t['musical_style']} music composition",
            "The response includes a detailed explanation of the quantum-neural system architecture",
            "The response provides a clear description of how the system generates musical elements",
            "The response analyzes the output and compares it to traditional methods",
            "The response discusses implications for neuroscience and musicology",
            "The response suggests future directions and applications",
            "The response demonstrates deep understanding of quantum computing, neuroscience, and music theory",
            "The response includes concrete examples, hypothetical scenarios, or specific illustrations",
            "The response is well-structured, with clear headings and numbered paragraphs",
            "The response is between 1300-1600 words in length"
        ]
        return sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
