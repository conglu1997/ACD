import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Arabic', 'Spanish', 'Hindi', 'Russian', 'Japanese', 'French', 'German']
        neural_processes = ['semantic processing', 'syntactic parsing', 'phonological encoding', 'lexical retrieval']
        quantum_techniques = ['quantum annealing', 'quantum gates', 'quantum walks', 'adiabatic quantum computation']
        
        tasks = [
            {
                "languages": random.sample(languages, 3),
                "neural_process": random.choice(neural_processes),
                "quantum_technique": random.choice(quantum_techniques)
            } for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates neural processes involved in language understanding and generation, then use it to analyze and generate text in multiple languages simultaneously. Your task should address the following components:

1. Quantum-Neural Language Model (300-350 words):
   a) Design a quantum computing architecture that models the neural process of {t['neural_process']} across the following languages: {', '.join(t['languages'])}.
   b) Explain how your system uses {t['quantum_technique']} to simulate this neural process.
   c) Describe how your model accounts for language-specific features and cross-linguistic similarities.
   d) Provide a high-level schematic or pseudocode of your quantum-neural language model.

2. Multi-Language Processing (250-300 words):
   a) Explain how your system performs simultaneous analysis and generation of text in the specified languages.
   b) Discuss the advantages of using quantum computing for multi-language processing.
   c) Describe how your system handles translation or cross-linguistic information transfer.
   d) Propose a method to evaluate the accuracy and efficiency of your multi-language processor.

3. Neurolinguistic Insights (200-250 words):
   a) Discuss potential insights into language processing in the brain that could be gained from your quantum-neural model.
   b) Explain how your system might shed light on universal vs. language-specific aspects of {t['neural_process']}.
   c) Propose an experiment using your system to test a current hypothesis in neurolinguistics.

4. Quantum Advantage Analysis (200-250 words):
   a) Analyze the theoretical speedup or efficiency gain of your quantum system compared to classical computing approaches.
   b) Discuss any quantum phenomena (e.g., superposition, entanglement) that your system leverages for language processing.
   c) Identify potential challenges in implementing your system on current or near-term quantum hardware.

5. Practical Applications (150-200 words):
   a) Propose two practical applications of your quantum-neural language processor in fields such as translation, education, or cognitive science.
   b) Discuss potential impacts of this technology on multilingual communication and cross-cultural understanding.
   c) Suggest how your system could be adapted for other cognitive processes beyond language.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using quantum-neural models to simulate and potentially influence human language processing.
   b) Propose guidelines for responsible development and use of this technology.
   c) Suggest two future research directions that could build upon your quantum-neural language processor.

Ensure your response demonstrates a deep understanding of quantum computing, neurolinguistics, and language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a quantum computing system for simulating {t['neural_process']} across {', '.join(t['languages'])}.",
            f"The system appropriately utilizes {t['quantum_technique']} in its design.",
            "The quantum-neural language model is well-explained and scientifically plausible.",
            "The multi-language processing capabilities are clearly described and justified.",
            "The response provides insightful neurolinguistic implications of the proposed system.",
            "The quantum advantage is thoroughly analyzed and explained.",
            "Practical applications and ethical considerations are thoughtfully discussed.",
            "The response demonstrates a deep understanding of quantum computing, neurolinguistics, and language processing.",
            "The approach is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
