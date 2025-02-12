import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Multilingual Quantum Entanglement",
                "description": "A scenario where language learners' cognitive states become entangled, allowing for instantaneous transfer of linguistic knowledge across distances.",
                "quantum_principle": "Entanglement",
                "linguistic_aspect": "Cross-linguistic influence"
            },
            {
                "name": "Superposition of Grammar States",
                "description": "A learning environment where grammatical rules exist in superposition, allowing for simultaneous acquisition of multiple, potentially conflicting, grammatical structures.",
                "quantum_principle": "Superposition",
                "linguistic_aspect": "Grammar acquisition"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum cognitive model for language acquisition and processing, then apply it to predict language learning outcomes in the following scenario: {t['name']}.

1. Quantum Cognitive Model Design (300-350 words):
   a) Describe the key components of your quantum cognitive model for language acquisition and processing.
   b) Explain how your model incorporates the quantum principle of {t['quantum_principle']}.
   c) Detail how your model addresses the linguistic aspect of {t['linguistic_aspect']}.
   d) Discuss any novel quantum cognitive mechanisms you've designed for this model.
   e) Provide a conceptual diagram or flowchart of your model (describe it textually).

2. Theoretical Framework (200-250 words):
   a) Explain the theoretical basis for your quantum cognitive model, drawing from current research in quantum cognition and psycholinguistics.
   b) Discuss how your model challenges or extends classical theories of language acquisition and processing.
   c) Address potential criticisms or limitations of applying quantum principles to cognitive linguistics.

3. Scenario Analysis (250-300 words):
   a) Apply your quantum cognitive model to the given scenario: {t['description']}
   b) Predict specific language learning outcomes based on your model's principles.
   c) Explain how these outcomes differ from those expected under classical cognitive models.
   d) Discuss any emergent phenomena or unexpected results that arise from your quantum cognitive approach.

4. Empirical Testability (200-250 words):
   a) Propose an experimental design to test the predictions of your quantum cognitive model in the given scenario.
   b) Describe the data you would collect and the analyses you would perform.
   c) Discuss potential challenges in empirically validating a quantum cognitive model of language acquisition.
   d) Suggest how your model could be falsified or refined based on experimental results.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your quantum cognitive model for our understanding of language and cognition.
   b) Explore potential applications of your model in fields such as language education, translation technology, or artificial intelligence.
   c) Propose future research directions that could further develop or extend your quantum cognitive approach to language.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues or concerns raised by the application of quantum cognitive models to language acquisition.
   b) Discuss how these ethical considerations might be addressed or mitigated.
   c) Propose guidelines for the responsible development and use of quantum cognitive technologies in language learning and processing.

Ensure your response demonstrates a deep understanding of quantum physics principles, cognitive science, and linguistics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics principles, cognitive science, and linguistics.",
            "The quantum cognitive model is creative, novel, and scientifically plausible.",
            f"The model effectively incorporates the quantum principle of {t['quantum_principle']} and addresses the linguistic aspect of {t['linguistic_aspect']}.",
            "The scenario analysis provides specific, logical predictions based on the proposed model.",
            "The proposed experimental design is well-thought-out and addresses the challenges of empirically testing a quantum cognitive model.",
            "The response discusses broader implications, future directions, and ethical considerations in a thoughtful and comprehensive manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
