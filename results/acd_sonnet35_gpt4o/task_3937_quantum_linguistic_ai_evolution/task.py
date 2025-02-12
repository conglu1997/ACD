import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'interference']
        linguistic_aspects = ['phonology', 'syntax', 'semantics']
        initial_languages = ['Proto-Indo-European', 'Proto-Sino-Tibetan']
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_aspect': random.choice(linguistic_aspects),
                'time_span': random.randint(100, 1000),
                'initial_language': random.choice(initial_languages)
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_aspect': random.choice(linguistic_aspects),
                'time_span': random.randint(100, 1000),
                'initial_language': random.choice(initial_languages)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial intelligence system that simulates the evolution of language over {t['time_span']} years, starting from {t['initial_language']}. Focus on the linguistic aspect of {t['linguistic_aspect']} and incorporate the quantum principle of {t['quantum_principle']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-linguistic AI system.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your language evolution model.
   c) Detail how your system models and processes the linguistic aspect of {t['linguistic_aspect']}.
   d) Discuss any novel algorithms or data structures used in your design.
   e) Include a high-level diagram or pseudocode illustrating your system's architecture.

2. Quantum-Linguistic Interface (200-250 words):
   a) Explain how your system translates linguistic concepts into quantum states or operations.
   b) Describe how quantum computations are mapped back to linguistic phenomena.
   c) Discuss any challenges in reconciling quantum and linguistic paradigms.
   d) Provide a mathematical formulation or equation representing a key aspect of your quantum-linguistic interface.

3. Language Evolution Simulation (250-300 words):
   a) Outline the process your system uses to simulate language evolution over the given time span.
   b) Explain how quantum effects influence the trajectory of language change in your model.
   c) Provide an example of a specific linguistic change your system might generate, starting from {t['initial_language']}.
   d) Include a simulated timeline or graph showing the evolution of a linguistic feature over time.

4. Information Processing Analysis (200-250 words):
   a) Analyze how your quantum-linguistic system processes and stores linguistic information.
   b) Compare the efficiency of your system to classical computational linguistics approaches.
   c) Discuss any novel insights into language or information theory that your system might provide.
   d) Include a quantitative comparison (e.g., computational complexity, information capacity) between your system and a classical approach.

5. Potential Applications (150-200 words):
   a) Propose two potential real-world applications of your quantum-linguistic AI system.
   b) Discuss how these applications might impact fields such as linguistics, AI, or quantum computing.
   c) Provide a brief example scenario for each application.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to simulating language evolution with quantum AI.
   b) Discuss any limitations of your current system design.
   c) Propose safeguards or guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, quantum computing principles, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and include the requested diagrams, equations, and examples. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, quantum computing (especially {t['quantum_principle']}), and artificial intelligence.",
            f"The proposed system effectively integrates the quantum principle of {t['quantum_principle']} with the linguistic aspect of {t['linguistic_aspect']}, starting from {t['initial_language']}.",
            "The language evolution simulation is plausible, creative, and includes a specific example of linguistic change.",
            "The analysis of information processing is insightful, compares quantum and classical approaches, and includes a quantitative comparison.",
            "The proposed applications and ethical considerations are thoughtful, well-reasoned, and include specific examples or scenarios.",
            "The response includes the requested diagrams, equations, and examples for each section.",
            "The response is well-structured, clear, and adheres to the specified word count range (1200-1500 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
