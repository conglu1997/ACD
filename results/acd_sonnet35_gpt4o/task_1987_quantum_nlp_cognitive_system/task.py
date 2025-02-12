import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            {'task': 'sentiment analysis', 'quantum_principle': 'superposition', 'example_input': 'The movie was both entertaining and disappointing.'},
            {'task': 'machine translation', 'quantum_principle': 'entanglement', 'example_input': 'The cat sat on the mat.'},
            {'task': 'text summarization', 'quantum_principle': 'quantum annealing', 'example_input': 'Quantum computing uses quantum mechanics to perform computations. It leverages superposition and entanglement to process information in ways classical computers cannot. This technology has the potential to revolutionize fields such as cryptography, drug discovery, and financial modeling.'},
            {'task': 'question answering', 'quantum_principle': 'quantum tunneling', 'example_input': 'What is the capital of France?'}
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(nlp_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing and generation system that focuses on the task of {t['task']} and incorporates the quantum computing principle of {t['quantum_principle']}. Your system should also integrate relevant principles from cognitive science. Provide a comprehensive response covering the following aspects:

1. System Architecture (300-350 words):
   a) Describe at least 5 key components of your quantum-inspired NLP system.
   b) Explain how your system incorporates the specified quantum principle ({t['quantum_principle']}) in its design and operation.
   c) Detail how at least 2 cognitive science principles are integrated into the system architecture.
   d) Provide a high-level diagram of your system architecture (described in words).
   e) Describe at least 2 novel quantum algorithms or circuits used in your system.

2. Language Processing Mechanism (250-300 words):
   a) Detail how your system processes and represents language data.
   b) Explain how the quantum principle of {t['quantum_principle']} is applied to language processing.
   c) Describe how cognitive models of language processing inform your system's design.
   d) Provide a step-by-step example of how your system would process the following input for {t['task']}: "{t['example_input']}"

3. Performance Analysis (200-250 words):
   a) Propose 3 specific methods to evaluate your system's performance on {t['task']}.
   b) Compare your quantum-inspired approach to 2 traditional NLP methods for this task.
   c) Discuss 3 potential advantages and 2 limitations of your system.

4. Cognitive and Linguistic Implications (200-250 words):
   a) Analyze how your system's performance might inform our understanding of human language processing.
   b) Discuss 2 potential insights into the relationship between quantum phenomena and cognitive processes.
   c) Propose a detailed experiment to test a specific hypothesis about language processing using your system.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Identify 3 potential ethical implications of using quantum-inspired systems for NLP tasks.
   b) Suggest 2 potential improvements or extensions to your system for future research.
   c) Discuss how your approach could contribute to the development of more advanced AI systems.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response using numbered sections as outlined above, with each main section having its specified word count. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, cognitive science, and computational linguistics.",
            "The system design includes at least 5 key components and 2 novel quantum algorithms or circuits.",
            "The quantum principle is effectively incorporated into the NLP system design and operation.",
            "The response adequately addresses all required sections with appropriate depth and clarity, adhering to the specified word counts.",
            "The proposed system effectively integrates at least 2 cognitive science principles with quantum-inspired NLP techniques.",
            "The performance analysis includes 3 evaluation methods and compares the approach to 2 traditional NLP methods.",
            "The response provides a detailed step-by-step example of processing the given input for the specified NLP task.",
            "Ethical considerations and future directions are thoughtfully discussed, including 3 ethical implications and 2 potential improvements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
