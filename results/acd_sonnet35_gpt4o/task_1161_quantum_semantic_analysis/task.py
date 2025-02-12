import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_property": "superposition",
                "nlp_task": "word sense disambiguation",
                "text_domain": "scientific literature"
            },
            {
                "quantum_property": "entanglement",
                "nlp_task": "sentiment analysis",
                "text_domain": "social media posts"
            },
            {
                "quantum_property": "quantum tunneling",
                "nlp_task": "named entity recognition",
                "text_domain": "legal documents"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm for semantic analysis of natural language texts, focusing on {t['nlp_task']} in the domain of {t['text_domain']}. Your algorithm should leverage the quantum property of {t['quantum_property']} to enhance meaning extraction and contextual understanding. Your response should include:

1. Quantum Algorithm Design (250-300 words):
   a) Describe the overall structure of your quantum algorithm for semantic analysis.
   b) Explain how it incorporates the specified quantum property ({t['quantum_property']}).
   c) Detail how the algorithm addresses the given NLP task ({t['nlp_task']}).
   d) Provide a high-level pseudocode or quantum circuit diagram of your algorithm.

2. Quantum-Classical Interface (200-250 words):
   a) Explain how classical text data is encoded into quantum states.
   b) Describe how quantum operations are applied to these states to perform semantic analysis.
   c) Discuss how the results are measured and interpreted classically.

3. Advantage Over Classical Methods (150-200 words):
   a) Analyze the potential advantages of your quantum approach compared to classical NLP methods.
   b) Discuss any unique capabilities or insights offered by the quantum algorithm.
   c) Address potential limitations or challenges of the quantum approach.

4. Application in {t['text_domain']} (200-250 words):
   a) Provide a specific example of how your algorithm would analyze a text from the given domain.
   b) Explain how the quantum property enhances the analysis in this context.
   c) Discuss potential impacts or benefits of using this algorithm in the specified domain.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to quantum-enhanced semantic analysis.
   b) Analyze possible societal impacts of deploying such technology.
   c) Propose guidelines for responsible development and use of quantum NLP algorithms.

Ensure your response demonstrates a deep understanding of both quantum computing principles and advanced NLP techniques. Be innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology from both fields and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed quantum algorithm design that incorporates {t['quantum_property']} for {t['nlp_task']}",
            "The response should explain the quantum-classical interface for text analysis",
            "The response should analyze advantages over classical methods",
            f"The response should provide a specific application example in {t['text_domain']}",
            "The response should discuss ethical and societal implications",
            "The response should demonstrate deep understanding of both quantum computing and NLP",
            "The response should be innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
