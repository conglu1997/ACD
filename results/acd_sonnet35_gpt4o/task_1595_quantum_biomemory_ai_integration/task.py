import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "quantum coherence",
                "memory_process": "long-term potentiation",
                "ai_application": "continuous learning in robotics"
            },
            {
                "quantum_principle": "quantum entanglement",
                "memory_process": "memory reconsolidation",
                "ai_application": "adaptive natural language processing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological model of memory formation and retrieval, incorporating the quantum principle of {t['quantum_principle']} and the biological process of {t['memory_process']}. Then, propose how this model could be integrated into an AI system to enhance {t['ai_application']}. Your response should include:

1. Quantum Biomemory Model (300-350 words):
   a) Explain the key features of your quantum biological memory model.
   b) Describe how {t['quantum_principle']} is incorporated into the model.
   c) Detail how your model accounts for the biological process of {t['memory_process']}.
   d) Discuss the potential advantages of your model over classical neuroscientific models of memory.
   e) Provide at least one mathematical equation or formulation representing a key aspect of your model.

2. Biological Plausibility (200-250 words):
   a) Assess the biological plausibility of your quantum memory model.
   b) Identify potential biological structures or processes that could support quantum effects in the brain.
   c) Discuss any experimental evidence that supports or challenges your model.

3. AI Integration (250-300 words):
   a) Propose how your quantum biomemory model could be integrated into an AI system for {t['ai_application']}.
   b) Explain the potential benefits of this integration for AI performance and capabilities.
   c) Describe any novel AI architectures or algorithms that would be required to implement your model.
   d) Provide a high-level pseudocode or flowchart illustrating the key steps of your integrated AI system.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired AI system to traditional AI approaches in {t['ai_application']}.
   b) Discuss potential performance improvements and new capabilities enabled by your system.
   c) Analyze any trade-offs or limitations of your approach.

5. Ethical Implications (150-200 words):
   a) Identify at least two ethical concerns raised by the development and use of quantum-inspired AI systems based on biological memory models.
   b) Propose guidelines or safeguards to address these ethical issues.
   c) Discuss the broader societal implications of AI systems that mimic quantum biological processes.

6. Future Research Directions (100-150 words):
   a) Propose two specific research questions or experiments that could further validate or refine your quantum biomemory model.
   b) Suggest potential applications of your model beyond AI, in fields such as medicine or cognitive enhancement.

Ensure your response demonstrates a deep understanding of quantum physics, biology, neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Do not provide direct answers or solutions, but rather demonstrate your reasoning and problem-solving process."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum biological model of memory incorporating {t['quantum_principle']} and {t['memory_process']}, with at least one mathematical equation or formulation",
            f"The model is applied to enhance AI capabilities in {t['ai_application']}, with a clear explanation of the integration process",
            "The analysis demonstrates a deep understanding of quantum physics, biology, neuroscience, and AI concepts, using appropriate technical terminology",
            "The response includes creative and plausible ideas while maintaining scientific integrity and addressing biological plausibility",
            "Ethical implications are thoughtfully addressed with specific guidelines or safeguards proposed",
            "The response follows the required format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
