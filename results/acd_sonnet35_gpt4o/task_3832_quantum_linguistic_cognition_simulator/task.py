import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "semantic processing",
            "syntactic parsing",
            "phonological encoding",
            "pragmatic interpretation"
        ]
        quantum_phenomena = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        language_aspects = [
            "lexical acquisition",
            "grammar induction",
            "discourse comprehension",
            "metaphor understanding"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "language_aspect": random.choice(language_aspects)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "language_aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates the cognitive process of {t['cognitive_process']} in language acquisition and use, leveraging the quantum phenomenon of {t['quantum_phenomenon']}. Focus on how this system models the language aspect of {t['language_aspect']}. Then, analyze its implications for our understanding of consciousness and reality. Your response should include the following sections:

1. Quantum-Cognitive Model (300-350 words):
   a) Describe the key components of your quantum computing system for simulating {t['cognitive_process']}.
   b) Explain how your system leverages {t['quantum_phenomenon']} to model cognitive processes.
   c) Detail how your system specifically addresses {t['language_aspect']}.
   d) Discuss any novel quantum algorithms or approaches used in your design.
   e) Include a simple diagram or flowchart of your system architecture (using ASCII art or a clear textual description).

2. Quantum-Linguistic Interface (250-300 words):
   a) Explain how your system translates between quantum states and linguistic representations.
   b) Describe how {t['quantum_phenomenon']} is used to capture the complexities of {t['language_aspect']}.
   c) Discuss how your model accounts for the dynamic nature of language processing.
   d) Provide an example of how a specific linguistic feature might be represented in your quantum system.

3. Simulation Process and Results (250-300 words):
   a) Outline the steps involved in running a simulation of {t['cognitive_process']} for {t['language_aspect']}.
   b) Describe expected outcomes and how they would be interpreted.
   c) Discuss how your simulation results might differ from classical cognitive models.
   d) Explain how you would validate the accuracy of your quantum-linguistic simulations.

4. Implications for Consciousness and Reality (300-350 words):
   a) Analyze how your quantum-cognitive model of language might inform our understanding of consciousness.
   b) Discuss the philosophical implications of quantum effects in cognitive processes.
   c) Explore how your model might challenge or support existing theories of reality.
   d) Consider the potential impact of your findings on fields such as philosophy of mind and cognitive science.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues arising from simulating cognitive processes using quantum computing.
   b) Discuss the implications of your model for concepts like free will and determinism.
   c) Consider the potential societal impacts if your quantum-cognitive model were widely adopted.
   d) Propose guidelines for responsible development and use of quantum-cognitive technologies.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum-cognitive language model.
   b) Propose a research question that could be explored using an advanced version of your system.
   c) Discuss how your approach might be adapted to study other cognitive processes or aspects of consciousness.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a sophisticated understanding of quantum physics, linguistics, and cognitive science, particularly in relation to {t['cognitive_process']}, {t['quantum_phenomenon']}, and {t['language_aspect']}.",
            "The proposed quantum computing system is innovative and plausibly capable of simulating cognitive processes in language acquisition and use.",
            "The implications for consciousness and reality are thoroughly explored, showing depth in understanding both quantum mechanics and cognitive science.",
            "The ethical considerations and societal impacts are comprehensively addressed, showing awareness of the broader implications of quantum-cognitive technologies.",
            "The response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
