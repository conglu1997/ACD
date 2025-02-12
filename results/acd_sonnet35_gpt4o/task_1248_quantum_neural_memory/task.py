import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_processes = [
            {
                "process": "encoding",
                "brain_region": "hippocampus",
                "quantum_principle": "superposition",
                "principle_explanation": "Quantum superposition allows particles to exist in multiple states simultaneously until observed."
            },
            {
                "process": "consolidation",
                "brain_region": "neocortex",
                "quantum_principle": "entanglement",
                "principle_explanation": "Quantum entanglement is a phenomenon where particles become interconnected and the quantum state of each particle cannot be described independently."
            },
            {
                "process": "retrieval",
                "brain_region": "prefrontal cortex",
                "quantum_principle": "quantum tunneling",
                "principle_explanation": "Quantum tunneling is the quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount."
            },
            {
                "process": "reconsolidation",
                "brain_region": "amygdala",
                "quantum_principle": "quantum annealing",
                "principle_explanation": "Quantum annealing is a process for finding the global minimum of a given objective function over a given set of candidate solutions by a process using quantum fluctuations."
            }
        ]
        return {
            "1": random.choice(memory_processes),
            "2": random.choice(memory_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing system that simulates and enhances the human memory process of {t['process']}, focusing on the {t['brain_region']} and utilizing the quantum principle of {t['quantum_principle']}. Brief explanation of the quantum principle: {t['principle_explanation']}\n\nYour response should include:\n\n1. Quantum-Neural Architecture (200-250 words):\n   a) Describe the key components of your quantum system and how they correspond to structures in the {t['brain_region']}.\n   b) Explain how your system implements the quantum principle of {t['quantum_principle']} to enhance the {t['process']} process.\n   c) Discuss how your architecture integrates quantum and neural network principles.\n   d) Include a brief diagram or flowchart of your system's architecture (described in words).\n\n2. Memory Process Simulation (150-200 words):\n   a) Explain how your system simulates the {t['process']} process at a quantum level.\n   b) Describe the algorithms or quantum circuits used for this simulation.\n   c) Discuss how your system could potentially enhance this memory process beyond human capabilities.\n\n3. Information Encoding and Retrieval (150-200 words):\n   a) Describe how information is encoded into quantum states in your system.\n   b) Explain the process of retrieving or manipulating this information.\n   c) Discuss any error correction or noise reduction techniques used in your system.\n\n4. Comparative Analysis (100-150 words):\n   a) Compare your quantum-neural approach to traditional computing methods for simulating memory processes.\n   b) Discuss potential advantages and limitations of your system.\n   c) Address any technical challenges in implementing your system with current quantum computing technology.\n\n5. Neuroscientific Implications (100-150 words):\n   a) Discuss what your system's performance might reveal about human memory processes.\n   b) Explore potential applications of your system in neuroscience research or clinical settings.\n   c) Address any ethical considerations related to enhancing or manipulating memory processes.\n\n6. Future Research Directions (50-100 words):\n   a) Propose two potential research questions or experiments that could further explore the intersection of quantum computing and neuroscience based on your system.\n   b) Briefly outline a methodology for investigating one of these research questions.\n\nExample approach (for the quantum-neural architecture section):\nYou might consider using quantum dots to represent neurons, where the superposition state of each quantum dot corresponds to the neuron's firing state. The entanglement between quantum dots could then represent synaptic connections.\n\nEnsure your response demonstrates a deep understanding of both quantum computing principles and neuroscience concepts. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Remember that your proposed system should be innovative but grounded in current scientific understanding.\n\nFormat your response using clear headings for each section. Your total response should be between 750-1050 words, not including the headings."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of the quantum principle of {t['quantum_principle']} and attempts to apply it to enhance the {t['process']} memory process in the {t['brain_region']}.",
            "The quantum-neural architecture description integrates quantum computing principles with neural network concepts.",
            "The proposed system presents an approach to simulating and enhancing human memory processes using quantum computing while attempting to maintain scientific plausibility.",
            "The response addresses some potential advantages, limitations, or technical challenges of implementing the proposed system.",
            "The discussion of neuroscientific implications and future research directions shows consideration of the field's current state and potential developments.",
            "The response is structured and attempts to adhere to the specified format guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
