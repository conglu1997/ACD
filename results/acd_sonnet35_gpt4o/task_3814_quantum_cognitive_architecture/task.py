import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'working memory',
            'decision making',
            'pattern recognition',
            'language processing'
        ]
        quantum_principles = [
            'superposition',
            'entanglement',
            'quantum tunneling',
            'quantum annealing'
        ]
        tasks = [
            {
                'cognitive_process': random.choice(cognitive_processes),
                'quantum_principle': random.choice(quantum_principles)
            },
            {
                'cognitive_process': random.choice(cognitive_processes),
                'quantum_principle': random.choice(quantum_principles)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum computing architecture inspired by the cognitive process of {t['cognitive_process']}, utilizing the quantum principle of {t['quantum_principle']}. Then, analyze its potential applications in artificial intelligence and cognitive enhancement. Your response should include the following sections:

1. Quantum Cognitive Architecture Design (300-350 words):
   a) Describe the key components of your quantum cognitive architecture.
   b) Explain how your design incorporates the specified cognitive process.
   c) Detail how the quantum principle is utilized in the architecture.
   d) Discuss any novel approaches or innovations in your design.

2. Quantum-Cognitive Integration (250-300 words):
   a) Analyze how the quantum principle enhances or transforms the cognitive process in your architecture.
   b) Compare your quantum-inspired approach to classical computing approaches for the same cognitive process.
   c) Discuss potential advantages and challenges of your quantum cognitive architecture.

3. Artificial Intelligence Applications (200-250 words):
   a) Propose two specific AI applications that could benefit from your quantum cognitive architecture.
   b) Explain how these applications would leverage the unique features of your design.
   c) Discuss potential improvements in AI performance or capabilities.

4. Cognitive Enhancement Potential (200-250 words):
   a) Explore how your quantum cognitive architecture could be used for human cognitive enhancement.
   b) Discuss ethical considerations and potential risks of such enhancement.
   c) Propose a method for evaluating the effectiveness and safety of cognitive enhancement using your architecture.

5. Technical Feasibility and Challenges (150-200 words):
   a) Assess the technical feasibility of implementing your quantum cognitive architecture with current or near-future technology.
   b) Identify key challenges in realizing your design.
   c) Suggest potential approaches to overcome these challenges.

6. Future Research Directions (100-150 words):
   a) Propose two promising research directions to further develop your quantum cognitive architecture.
   b) Explain how these research directions could address current limitations or open up new possibilities.

Ensure your response demonstrates a deep understanding of both quantum computing principles and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing principles and cognitive science.",
            f"The quantum cognitive architecture effectively incorporates the cognitive process of {t['cognitive_process']} and the quantum principle of {t['quantum_principle']}.",
            "The proposed AI applications and cognitive enhancement potential are innovative and well-explained.",
            "The technical feasibility assessment and future research directions are thoughtful and plausible.",
            "The response is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
