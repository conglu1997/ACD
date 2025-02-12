import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum tunneling",
            "quantum annealing"
        ]
        cognitive_models = [
            "spreading activation",
            "parallel distributed processing",
            "connectionist models",
            "predictive coding",
            "dynamic systems theory"
        ]
        nlp_tasks = [
            "sentiment analysis",
            "named entity recognition",
            "text summarization",
            "machine translation",
            "question answering"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_model": random.choice(cognitive_models),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_model": random.choice(cognitive_models),
                "nlp_task": random.choice(nlp_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired algorithm for natural language processing that incorporates the quantum computing concept of {t['quantum_concept']}, the cognitive model of {t['cognitive_model']}, and addresses the NLP task of {t['nlp_task']}. Structure your response using the following numbered sections:

1. Quantum Concept Analysis (150-200 words):
   a) Explain the given quantum concept and its relevance to computational processes.
   b) Discuss how this concept might be applied to language processing.

2. Cognitive Model Overview (150-200 words):
   a) Describe the specified cognitive model and its role in understanding language comprehension.
   b) Explain how this model relates to traditional computational approaches to language processing.

3. Algorithm Design (400-450 words):
   a) Propose a novel algorithm that integrates the quantum concept and cognitive model to address the given NLP task.
   b) Describe the key components and processes of your algorithm.
   c) Explain how your design differs from classical approaches to this NLP task.
   d) Include a high-level pseudocode or flow diagram of your algorithm.
   e) Provide a quantum circuit diagram for a key component of your algorithm (use ASCII art or Unicode characters).
   f) Present a mathematical formulation of your algorithm, using appropriate quantum computing notation (e.g., Dirac notation, matrix representations). Explain the meaning of each symbol and operation used.

4. Example Application (100-150 words):
   Provide a brief example of how your algorithm would process a specific input related to the given NLP task. Walk through the steps of how your algorithm would handle this input.

5. Comparative Analysis (200-250 words):
   a) Compare your proposed algorithm to existing quantum and classical approaches for the given NLP task.
   b) Discuss the potential advantages and disadvantages of your approach relative to these existing methods.
   c) Analyze the computational complexity of your algorithm compared to classical alternatives.

6. Theoretical Advantages (200-250 words):
   a) Discuss potential advantages of your quantum-inspired cognitive algorithm for the specified NLP task.
   b) Analyze possible improvements in efficiency, accuracy, or capabilities compared to classical methods.
   c) Explain any novel insights into language processing that your approach might provide.

7. Implementation Challenges (200-250 words):
   a) Identify and discuss potential challenges in implementing your algorithm.
   b) Propose solutions or areas for further research to address these challenges.
   c) Discuss any limitations of your approach and how they might be mitigated.

8. Broader Implications (150-200 words):
   a) Speculate on how your algorithm might influence the fields of quantum computing, cognitive science, and NLP.
   b) Discuss potential applications of your approach beyond the specified NLP task.
   c) Consider any ethical implications or societal impacts of using quantum-inspired cognitive algorithms for language processing.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and natural language processing. Be creative in your approach while maintaining scientific and theoretical plausibility. Adhere to the word count guidelines for each section and use clear numbering as outlined above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm must incorporate the quantum computing concept of {t['quantum_concept']}, the cognitive model of {t['cognitive_model']}, and address the NLP task of {t['nlp_task']}.",
            "The response must include a clear analysis of the given quantum concept and its potential application to language processing.",
            "An overview of the specified cognitive model and its relation to language comprehension must be provided.",
            "The proposed algorithm must integrate the quantum concept and cognitive model in a novel and plausible way to address the given NLP task.",
            "A high-level pseudocode or flow diagram of the algorithm must be included.",
            "A quantum circuit diagram for a key component of the algorithm must be provided using ASCII art or Unicode characters.",
            "A mathematical formulation of the algorithm using appropriate quantum computing notation (e.g., Dirac notation, matrix representations) must be presented, with explanations for each symbol and operation.",
            "A brief example of how the algorithm would process a specific input related to the given NLP task must be provided.",
            "The response must include a comparative analysis of the proposed algorithm against existing quantum and classical approaches, including computational complexity considerations.",
            "The response must discuss specific theoretical advantages, implementation challenges, and broader implications of the proposed approach.",
            "The response must demonstrate a deep understanding of quantum computing, cognitive science, and natural language processing, with accurate use of terminology from all three fields.",
            "The response must be creative while maintaining scientific and theoretical plausibility.",
            "The response must be formatted with clear numbering for each section as specified in the instructions, adhering to the given word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
