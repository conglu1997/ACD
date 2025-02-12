import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "nlp_task": "sentiment analysis",
                "quantum_feature": "superposition",
                "language_aspect": "semantic ambiguity"
            },
            {
                "nlp_task": "machine translation",
                "quantum_feature": "entanglement",
                "language_aspect": "syntactic structure"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum circuit for the NLP task of {t['nlp_task']}, leveraging the quantum feature of {t['quantum_feature']} to address the language aspect of {t['language_aspect']}. Then, analyze its potential impact on AI language models and linguistic theory. Your response should include:

1. Quantum NLP Circuit Design (300-350 words):
   a) Describe the overall architecture of your quantum NLP circuit.
   b) Explain how you incorporate the quantum feature of {t['quantum_feature']} into your design.
   c) Detail how your circuit addresses the language aspect of {t['language_aspect']}.
   d) Discuss any novel quantum gates or operations you've designed for this task.
   e) Provide a simple diagram or flowchart of your quantum circuit (describe it textually).

2. Quantum-Classical Interface (200-250 words):
   a) Explain how classical NLP data is encoded into quantum states for processing.
   b) Describe the measurement process to obtain meaningful results from the quantum circuit.
   c) Discuss any hybrid quantum-classical approaches in your design.

3. Performance Analysis (250-300 words):
   a) Hypothesize how your quantum NLP circuit might perform compared to classical algorithms for {t['nlp_task']}.
   b) Discuss potential advantages and limitations of your quantum approach.
   c) Analyze the scalability of your design for larger language processing tasks.
   d) Propose a specific experiment to benchmark your quantum NLP circuit against state-of-the-art classical methods.

4. Implications for AI and Linguistics (200-250 words):
   a) Discuss how your quantum NLP approach might influence the development of future AI language models.
   b) Analyze potential impacts on linguistic theory, especially regarding {t['language_aspect']}.
   c) Explore how quantum NLP could change our understanding of language processing in both machines and humans.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues or concerns raised by quantum NLP technology.
   b) Discuss how these ethical considerations might be addressed or mitigated.
   c) Propose guidelines for the responsible development and use of quantum NLP systems.

6. Future Research Directions (150-200 words):
   a) Suggest areas for future research in quantum NLP, building on your proposed circuit.
   b) Discuss potential interdisciplinary collaborations that could advance this field.
   c) Predict how quantum NLP might evolve over the next decade and its potential societal impacts.

Ensure your response demonstrates a deep understanding of quantum computing principles, natural language processing, and linguistic theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your response.

Remember to use appropriate quantum computing terminology throughout your response, especially when describing quantum gates, states, and operations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on designing a quantum circuit for {t['nlp_task']}.",
            f"The quantum feature of {t['quantum_feature']} is effectively incorporated into the design.",
            f"The circuit addresses the language aspect of {t['language_aspect']}.",
            "The quantum NLP circuit design is innovative yet plausible, demonstrating interdisciplinary knowledge.",
            "The response covers all six required sections with appropriate detail and coherence.",
            "The quantum-classical interface is thoughtfully explained.",
            "The performance analysis includes a comparison to classical methods and a proposed experiment.",
            "The response includes a textual description of a diagram or flowchart of the quantum circuit.",
            "The implications for AI and linguistics are thoroughly discussed.",
            "The ethical considerations section addresses potential issues and proposes guidelines.",
            "The future research directions are insightful and forward-thinking.",
            "The response uses appropriate quantum computing terminology throughout.",
            "The total word count is between 1250-1550 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
