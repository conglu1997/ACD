import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            "memory enhancement",
            "cognitive augmentation",
            "neuroprosthetic control",
            "dream interpretation",
            "direct brain-to-brain communication"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum error correction",
            "quantum annealing"
        ]
        neural_processes = [
            "synaptic plasticity",
            "neural oscillations",
            "information integration",
            "memory consolidation",
            "attention modulation"
        ]
        
        tasks = {}
        for i in range(2):
            application = random.choice(applications)
            quantum_principle = random.choice(quantum_principles)
            neural_process = random.choice(neural_processes)
            
            tasks[str(i+1)] = {
                "application": application,
                "quantum_principle": quantum_principle,
                "neural_process": neural_process
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced brain-computer interface (Q-BCI) that utilizes principles of quantum computing to improve neural signal processing and bidirectional communication between the human brain and artificial intelligence systems. Your design should focus on the application of {t['application']}, incorporate the quantum principle of {t['quantum_principle']}, and target the neural process of {t['neural_process']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your Q-BCI system and how they interact.
   b) Explain how quantum computing is integrated into the neural interface.
   c) Detail how your system targets and enhances the specified neural process.
   d) Discuss any novel technologies or theoretical concepts employed in your design.

2. Quantum-Neural Integration (250-300 words):
   a) Explain how the specified quantum principle is applied to enhance brain-computer communication.
   b) Describe the mechanisms by which quantum states are mapped to neural signals and vice versa.
   c) Discuss how your system maintains quantum coherence in the noisy biological environment of the brain.

3. Application Implementation (250-300 words):
   a) Provide a detailed explanation of how your Q-BCI system implements the specified application.
   b) Describe the expected improvements or novel capabilities enabled by the quantum enhancement.
   c) Discuss potential challenges in implementing this application and how your design addresses them.

4. Information Processing and AI Integration (200-250 words):
   a) Explain how your system processes and interprets the quantum-enhanced neural signals.
   b) Describe how artificial intelligence is integrated into the system to facilitate bidirectional communication.
   c) Discuss any novel algorithms or computational approaches used in your design.

5. Ethical and Safety Considerations (150-200 words):
   a) Identify potential ethical issues related to the use of quantum-enhanced BCIs.
   b) Discuss safety concerns and propose mitigation strategies.
   c) Suggest guidelines for responsible development and use of this technology.

6. Future Implications and Research Directions (150-200 words):
   a) Speculate on the long-term implications of quantum-enhanced BCIs for human cognition and AI development.
   b) Propose two potential research projects that could further advance this technology.
   c) Discuss how your Q-BCI system might impact our understanding of consciousness and cognitive processes.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence",
            "The Q-BCI system design is innovative and well-explained",
            "The application of the specified quantum principle to the neural process is clearly articulated",
            "The implementation of the given application is thoroughly described and plausible",
            "Ethical and safety considerations are comprehensively addressed",
            "The response follows the specified format with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
