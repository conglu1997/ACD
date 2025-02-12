import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling",
            "quantum superposition"
        ]
        cognitive_processes = [
            "decision-making",
            "memory formation",
            "consciousness",
            "attention"
        ]
        neural_structures = [
            "microtubules",
            "ion channels",
            "synaptic vesicles",
            "neuronal membranes"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "cognitive_process": random.choice(cognitive_processes),
                "neural_structure": random.choice(neural_structures)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "cognitive_process": random.choice(cognitive_processes),
                "neural_structure": random.choice(neural_structures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a theoretical neuroscientist exploring the frontiers of quantum biology and its potential implications for cognition. While highly speculative, some researchers propose that quantum effects might play a role in brain function. Your task is to develop and analyze a hypothesis for how {t['quantum_effect']} in {t['neural_structure']} might influence {t['cognitive_process']}, design an experiment to test this hypothesis, and propose a novel quantum-inspired computational model based on your hypothesis.

Remember, this is a speculative area of research. While your responses should be grounded in scientific principles, you are encouraged to think creatively and propose novel ideas. Strive to balance speculative thinking with scientific plausibility.

A quantum-inspired computational model adapts principles from quantum mechanics to classical computing, potentially offering new approaches to problem-solving or information processing.

Your response should include:

1. Hypothesis Development (180-220 words):
   a) Clearly state your hypothesis about how {t['quantum_effect']} in {t['neural_structure']} could affect {t['cognitive_process']}.
   b) Explain the theoretical basis for your hypothesis, drawing on relevant research in quantum biology and neuroscience.
   c) Discuss potential mechanisms by which the quantum effect could influence the cognitive process.

2. Interdisciplinary Analysis (130-170 words):
   a) Analyze how your hypothesis integrates concepts from quantum mechanics, neurobiology, and cognitive science.
   b) Discuss any challenges in reconciling quantum-level phenomena with macro-level cognitive processes.
   c) Address potential criticisms of applying quantum mechanics to biological systems.

3. Experimental Design (180-220 words):
   a) Propose a detailed experiment to test your hypothesis.
   b) Describe the methodology, including any novel techniques or technologies required.
   c) Explain how your experiment could differentiate between quantum and classical effects in {t['cognitive_process']}.
   d) Discuss potential confounding factors and how you would control for them.

4. Quantum-Inspired Computational Model (180-220 words):
   a) Propose a novel computational model inspired by your quantum cognition hypothesis.
   b) Describe the key components and principles of your model.
   c) Explain how this model could be implemented in silico and how it differs from classical computational models.
   d) Discuss potential applications of your model in artificial intelligence or cognitive computing.

5. Implications and Future Directions (80-120 words):
   a) Discuss the potential implications of your hypothesis and computational model for our understanding of cognition and consciousness.
   b) Suggest how your work could inform future research in neuroscience, quantum biology, and artificial intelligence.
   c) Propose one potential real-world application of your findings, if the hypothesis is supported and the model is successful.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, cognitive science, and computational modeling. Be creative and speculative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section. Your total response should be between 750-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, cognitive science, and computational modeling.",
            "The hypothesis is creative, speculative, and scientifically plausible.",
            "The experimental design is well-thought-out and addresses potential confounding factors.",
            "The analysis integrates concepts from multiple disciplines effectively.",
            "The proposed quantum-inspired computational model is innovative and well-described.",
            "The implications and future directions are insightful and relevant.",
            "The response uses appropriate technical terminology and provides clear explanations of complex concepts.",
            "The response adheres to the specified word counts for each section.",
            "The response balances speculative thinking with scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
