class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            "protein folding prediction",
            "drug discovery optimization",
            "climate model simulation",
            "cryptography",
            "financial market analysis"
        ]
        import random
        selected = random.sample(computational_problems, 2)
        return {
            "1": {"problem": selected[0]},
            "2": {"problem": selected[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system that utilizes biological molecules for qubit manipulation and storage, then simulate its performance in solving the complex computational problem of {t['problem']}. Your response should include:

        1. System Architecture (300-350 words):
           a) Describe the key components of your bio-quantum computing system.
           b) Explain how biological molecules are used for qubit manipulation and storage.
           c) Detail the interface between quantum and biological components.
           d) Discuss how your system maintains quantum coherence in a biological environment.

        2. Quantum Operations (250-300 words):
           a) Explain how your system performs basic quantum operations (e.g., superposition, entanglement).
           b) Describe any novel quantum gates or operations enabled by the biological components.
           c) Discuss how error correction is implemented in your bio-quantum system.

        3. Problem-Specific Implementation (250-300 words):
           a) Outline how your bio-quantum system approaches the given computational problem ({t['problem']}).
           b) Explain any quantum algorithms or techniques specific to this problem.
           c) Discuss potential advantages of your system over traditional quantum computers for this problem.

        4. Performance Simulation (200-250 words):
           a) Describe the simulation methodology for your bio-quantum system.
           b) Present hypothetical results of your system's performance on the given problem.
           c) Compare the simulated performance to classical and traditional quantum computing approaches.

        5. Challenges and Limitations (150-200 words):
           a) Identify key technical challenges in implementing your bio-quantum system.
           b) Discuss any limitations in the types of problems your system can efficiently solve.
           c) Propose potential solutions or areas for future research to address these challenges.

        6. Ethical Considerations and Societal Impact (150-200 words):
           a) Discuss ethical implications of developing bio-quantum computing systems.
           b) Analyze potential societal impacts of successful implementation of your system.
           c) Propose guidelines for responsible development and use of bio-quantum computing technology.

        Ensure your response demonstrates a deep understanding of quantum computing principles, molecular biology, and their potential integration. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of both quantum computing principles and molecular biology.",
            "The proposed bio-quantum computing system is creative and innovative while maintaining scientific plausibility.",
            "The system architecture and quantum operations are well-explained and logically consistent.",
            "The problem-specific implementation and performance simulation are detailed and relevant to the given computational problem.",
            "Challenges, limitations, and ethical considerations are thoroughly discussed.",
            "The response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
