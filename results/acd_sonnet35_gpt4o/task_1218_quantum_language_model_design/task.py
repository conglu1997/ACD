import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Interference",
            "Quantum Tunneling"
        ]
        information_theory_concepts = [
            "Shannon Entropy",
            "Mutual Information",
            "Channel Capacity",
            "Kolmogorov Complexity"
        ]
        nlp_applications = [
            "Sentiment Analysis",
            "Machine Translation",
            "Text Summarization",
            "Question Answering"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "info_theory_concept": random.choice(information_theory_concepts),
                "nlp_application": random.choice(nlp_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "info_theory_concept": random.choice(information_theory_concepts),
                "nlp_application": random.choice(nlp_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that incorporates the quantum mechanical principle of {t['quantum_principle']}, the information theory concept of {t['info_theory_concept']}, and analyze its potential implications for the NLP application of {t['nlp_application']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the overall structure of your quantum-inspired language model.
   b) Explain how it incorporates the specified quantum principle ({t['quantum_principle']}) into its design.
   c) Detail how the model integrates the information theory concept ({t['info_theory_concept']}).

2. Quantum-Classical Integration (200-250 words):
   a) Explain how quantum and classical components interact in your model.
   b) Discuss any novel approaches to quantum-classical interfacing in your design.
   c) Describe how this integration enhances language processing capabilities.

3. Application to NLP (200-250 words):
   a) Analyze how your quantum-inspired language model could be applied to {t['nlp_application']}.
   b) Explain the potential advantages of your approach compared to classical language models for this application.
   c) Discuss any challenges or limitations specific to this application.

4. Training and Optimization (150-200 words):
   a) Propose a training method for your quantum-inspired language model.
   b) Discuss how quantum principles and information theory concepts might be leveraged in the optimization process.

5. Theoretical Implications (150-200 words):
   a) Discuss the theoretical implications of your model for our understanding of language processing and quantum information.
   b) Propose a testable hypothesis about language understanding or generation that could be explored using your model.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues or societal impacts of implementing your quantum-inspired language model.
   b) Suggest safeguards or guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, information theory, and computational linguistics. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate terminology and provide clear explanations of complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum-inspired language model that incorporates the specified quantum principle ({t['quantum_principle']}) and information theory concept ({t['info_theory_concept']}).",
            f"The application to {t['nlp_application']} is thoroughly analyzed, with clear advantages and challenges identified.",
            "The integration of quantum and classical components is clearly explained and justified.",
            "The training and optimization methods are appropriate and leverage quantum principles and information theory concepts.",
            "The theoretical implications and proposed hypothesis are insightful and well-reasoned.",
            "Ethical considerations are thoughtfully addressed with appropriate safeguards suggested.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and deep understanding of quantum mechanics, information theory, and computational linguistics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
