import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Annealing"
        ]
        neuroscience_concepts = [
            "Neuroplasticity",
            "Predictive Coding",
            "Connectome Mapping",
            "Neuromodulation"
        ]
        ai_paradigms = [
            "Reinforcement Learning",
            "Generative Adversarial Networks",
            "Attention Mechanisms",
            "Federated Learning"
        ]
        cognitive_functions = [
            "Decision Making",
            "Memory Formation",
            "Pattern Recognition",
            "Language Processing"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "ai_paradigm": random.choice(ai_paradigms),
                "cognitive_function": random.choice(cognitive_functions)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "ai_paradigm": random.choice(ai_paradigms),
                "cognitive_function": random.choice(cognitive_functions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical cognitive architecture that integrates quantum computing principles with neuroscience and artificial intelligence to create a novel framework for information processing and decision making. Your architecture should specifically incorporate the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the AI paradigm of {t['ai_paradigm']}. Focus on how this integration enhances the cognitive function of {t['cognitive_function']}.

Your response should include the following sections:

1. Architectural Overview (300-350 words):
   a) Describe the overall structure of your quantum cognitive architecture, including its main components and their interactions.
   b) Explain how quantum computing principles are integrated into the architecture, focusing on {t['quantum_principle']}.
   c) Discuss how your design incorporates {t['neuroscience_concept']} and how it relates to brain function.
   d) Explain how the AI paradigm of {t['ai_paradigm']} is implemented in your architecture.
   e) Provide a high-level diagram or description of your quantum cognitive architecture.

2. Quantum-Neural Integration (250-300 words):
   a) Explain in detail how {t['quantum_principle']} is utilized in your cognitive system.
   b) Describe how this quantum principle enhances or enables neural processes related to {t['neuroscience_concept']}.
   c) Discuss any novel emergent properties or capabilities that arise from this integration.

3. Information Processing and Learning (200-250 words):
   a) Explain how your architecture processes information using the integrated quantum-neural framework.
   b) Describe how the AI paradigm of {t['ai_paradigm']} is enhanced by quantum and neural components.
   c) Discuss any unique learning mechanisms or adaptations in your system.

4. Cognitive Function Enhancement (200-250 words):
   a) Explain how your architecture specifically enhances the cognitive function of {t['cognitive_function']}.
   b) Provide a detailed example or scenario demonstrating this enhanced cognitive capability.
   c) Compare your approach to traditional (non-quantum, non-neural) methods for this cognitive function.

5. Theoretical Performance Analysis (200-250 words):
   a) Analyze the potential advantages of your quantum cognitive architecture over classical systems.
   b) Discuss any theoretical limitations or challenges in your design.
   c) Propose methods to evaluate or benchmark the performance of your architecture.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of developing quantum-enhanced cognitive architectures.
   b) Explore the philosophical implications of your design, particularly regarding consciousness and free will.
   c) Propose guidelines for responsible development and use of such advanced cognitive systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, artificial intelligence, and cognitive science. Be innovative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cognitive architecture clearly incorporates the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the AI paradigm of {t['ai_paradigm']}.",
            f"The response demonstrates how the integration enhances the cognitive function of {t['cognitive_function']}.",
            "The proposed architecture is innovative, scientifically plausible, and well-reasoned.",
            "The integration of quantum principles, neuroscience concepts, and AI paradigms is clearly explained and justified.",
            "The response adequately addresses the theoretical performance, limitations, and ethical implications of the proposed architecture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
