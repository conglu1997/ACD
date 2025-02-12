import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "superposition",
                "description": "The principle that a quantum system can exist in multiple states simultaneously until observed."
            },
            {
                "concept": "entanglement",
                "description": "A quantum phenomenon where particles become interconnected and the state of each particle cannot be described independently."
            },
            {
                "concept": "quantum tunneling",
                "description": "The quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount."
            },
            {
                "concept": "wave function collapse",
                "description": "The phenomenon in which a wave function—initially in a superposition of several eigenstates—reduces to a single eigenstate due to interaction with the external world."
            }
        ]
        
        linguistic_aspects = [
            "semantic analysis",
            "syntactic parsing",
            "language generation",
            "translation"
        ]
        
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_aspect": random.choice(linguistic_aspects)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_aspect": random.choice(linguistic_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language processing model that applies the quantum mechanical principle of {t['quantum_concept']['concept']} to the linguistic aspect of {t['linguistic_aspect']}. Your task is to create a novel approach to language analysis or generation that incorporates quantum mechanical thinking.

Brief explanation of the quantum concept: {t['quantum_concept']['description']}

Your response should include:

1. Model Design (250-300 words):
   a) Describe the basic structure and components of your quantum linguistic model.
   b) Explain how the model incorporates the given quantum concept into linguistic processing.
   c) Detail how the model would handle the specified linguistic aspect.
   d) Discuss any novel emergent properties or capabilities of your model.

2. Mathematical Formulation (150-200 words):
   a) Provide a basic mathematical representation of your model.
   b) Explain the key variables, operators, or equations used.
   c) Describe how the mathematical formulation reflects both quantum and linguistic principles.

3. Practical Implementation (200-250 words):
   a) Outline how your model could be implemented in a computational system.
   b) Discuss any technical challenges and potential solutions.
   c) Explain how the model would interface with existing NLP systems or linguistic resources.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum linguistic model to traditional approaches in the specified linguistic aspect.
   b) Analyze potential advantages and limitations of your approach.
   c) Discuss how your model might offer new insights into language processing or quantum systems.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the effectiveness of your quantum linguistic model.
   b) Describe the data you would use and the metrics for evaluation.
   c) Predict potential outcomes and their implications for the fields of linguistics and quantum mechanics.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed model that clearly incorporates the given quantum concept into linguistic processing.",
            "The mathematical formulation is coherent and reflects both quantum and linguistic principles.",
            "The practical implementation discussion addresses technical challenges and integration with existing systems.",
            "The comparative analysis demonstrates a strong understanding of traditional linguistic approaches and the potential impact of the quantum model.",
            "The proposed experiment is well-designed and would effectively test the model's capabilities.",
            "The response demonstrates a deep understanding of both quantum mechanics and linguistics, with creative yet scientifically plausible ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
