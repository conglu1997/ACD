import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            {
                "task": "Text summarization",
                "quantum_principle": "Superposition",
                "cognitive_process": "Attention"
            },
            {
                "task": "Sentiment analysis",
                "quantum_principle": "Entanglement",
                "cognitive_process": "Emotional processing"
            },
            {
                "task": "Machine translation",
                "quantum_principle": "Quantum teleportation",
                "cognitive_process": "Linguistic relativity"
            },
            {
                "task": "Question answering",
                "quantum_principle": "Quantum measurement",
                "cognitive_process": "Working memory"
            }
        ]
        return {
            "1": random.choice(nlp_tasks),
            "2": random.choice(nlp_tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for natural language processing, focusing on semantic analysis and generation. Your architecture should integrate the quantum computing principle of {t['quantum_principle']} and the cognitive process of {t['cognitive_process']}. Apply your architecture to solve the NLP task of {t['task']}.

Provide your response in the following format:

1. Conceptual Framework (200-250 words):
   a) Explain how the quantum principle of {t['quantum_principle']} can be applied to model language processing.
   b) Describe how the cognitive process of {t['cognitive_process']} relates to semantic analysis and generation.
   c) Propose a novel way to integrate these concepts into a cohesive architecture for NLP.

2. Architecture Design (300-350 words):
   a) Outline the key components of your quantum-inspired cognitive architecture for NLP.
   b) Explain how each component incorporates aspects of quantum computing and cognitive science.
   c) Describe the information flow and processing stages in your architecture.
   d) Include a diagram or flowchart of your architecture using ASCII art or Unicode characters.

3. Quantum-Cognitive Algorithms (250-300 words):
   a) Describe the core algorithms used in your architecture for semantic analysis and generation.
   b) Explain how these algorithms leverage both quantum principles and cognitive processes.
   c) Provide pseudocode or a mathematical formulation for a key algorithm in your system.

4. Application to {t['task']} (200-250 words):
   a) Explain how your architecture would approach the task of {t['task']}.
   b) Describe the specific advantages your quantum-cognitive approach offers for this task.
   c) Discuss any potential challenges or limitations in applying your architecture to this task.

5. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate your architecture's performance on {t['task']}.
   b) Describe an experiment to compare your approach with traditional NLP methods.
   c) Discuss how you would validate the quantum and cognitive aspects of your system.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using quantum-inspired cognitive architectures in NLP.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest two novel research questions that arise from your architecture.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles, cognitive science, and computational linguistics.",
            "The proposed architecture creatively integrates the specified quantum principle and cognitive process.",
            "The architecture design is clearly explained and includes a coherent diagram or flowchart.",
            "The quantum-cognitive algorithms are well-described and include pseudocode or mathematical formulation.",
            "The application to the specified NLP task is thoroughly explained, including advantages and potential challenges.",
            "The performance evaluation proposal is well-thought-out and includes appropriate metrics and experimental design.",
            "Ethical considerations are adequately addressed, and future research directions are insightful.",
            "The response is well-structured, within the specified word limit, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
