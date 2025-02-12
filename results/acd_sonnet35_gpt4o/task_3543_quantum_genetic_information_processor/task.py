import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        genetic_processes = [
            "DNA replication",
            "transcription",
            "translation",
            "recombination"
        ]
        return {
            "1": {"quantum_principle": random.choice(quantum_principles), "genetic_process": random.choice(genetic_processes)},
            "2": {"quantum_principle": random.choice(quantum_principles), "genetic_process": random.choice(genetic_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum computing model for processing genetic information, incorporating the quantum principle of {t['quantum_principle']} and the genetic process of {t['genetic_process']}. Then, analyze its potential applications in genomics and quantum biology. Your response should include the following sections:\n\n" + \
               "1. Quantum-Genetic Model Design (300-350 words):\n" + \
               "   a) Describe the key components and architecture of your quantum-genetic information processing model.\n" + \
               "   b) Explain how your model incorporates the specified quantum principle and genetic process.\n" + \
               "   c) Provide a mathematical formalism (e.g., equations, matrices) to represent key aspects of your model.\n" + \
               "   d) Discuss how your model differs from classical approaches to genetic information processing.\n\n" + \
               "2. Information Processing Mechanism (250-300 words):\n" + \
               "   a) Explain in detail how genetic information is encoded and processed in your quantum model.\n" + \
               "   b) Describe how the quantum properties enhance or transform the genetic information processing.\n" + \
               "   c) Discuss any novel features or capabilities of your model compared to classical genetic processing.\n\n" + \
               "3. Theoretical Performance Analysis (200-250 words):\n" + \
               "   a) Analyze the theoretical advantages of your quantum-genetic model over classical methods.\n" + \
               "   b) Discuss potential limitations or challenges in implementing your model.\n" + \
               "   c) Propose metrics for evaluating the performance and accuracy of your model.\n\n" + \
               "4. Applications in Genomics and Quantum Biology (200-250 words):\n" + \
               "   a) Propose two potential applications of your quantum-genetic model in genomics research.\n" + \
               "   b) Describe how your model could advance our understanding of quantum effects in biological systems.\n" + \
               "   c) Discuss the potential impact of your model on personalized medicine or genetic engineering.\n\n" + \
               "5. Experimental Design (150-200 words):\n" + \
               "   a) Propose an experiment to test a key aspect of your quantum-genetic model.\n" + \
               "   b) Describe the setup, methodology, and expected results of your experiment.\n" + \
               "   c) Discuss any technological challenges in realizing this experiment with current or near-term quantum hardware.\n\n" + \
               "6. Ethical Considerations and Future Directions (150-200 words):\n" + \
               "   a) Discuss potential ethical implications of using quantum computing in genetic information processing.\n" + \
               "   b) Propose two future research directions that could further advance your quantum-genetic model.\n" + \
               "   c) Speculate on how this technology might impact society and scientific research in the long term.\n\n" + \
               "Ensure your response demonstrates a deep understanding of quantum physics, genetics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility throughout your model design and analysis.\n\n" + \
               "Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words. Include a word count at the end of your response.\n\n" + \
               "Your response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your model design, the thoroughness of your analysis across all sections, and adherence to the specified word count."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately incorporates and explains the quantum principle of {t['quantum_principle']} and the genetic process of {t['genetic_process']} in the model design, with a clear mathematical formalism.",
            "The quantum-genetic model design is innovative, scientifically plausible, and well-explained, demonstrating a deep understanding of both quantum physics and genetics.",
            "The response provides a thorough analysis of the model's performance, potential applications, and ethical implications, with specific examples and detailed explanations.",
            "The proposed experiment is well-designed, relevant to testing the model's key aspects, and considers current technological limitations.",
            "The response demonstrates a deep understanding of quantum physics, genetics, and information theory, creatively integrating these disciplines while maintaining scientific plausibility.",
            "The response adheres to the specified word count (1250-1550 words) and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
