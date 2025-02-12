import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse",
            "Quantum interference"
        ]
        cognitive_processes = [
            "Memory formation",
            "Attention allocation",
            "Concept formation",
            "Decision making",
            "Pattern recognition"
        ]
        linguistic_phenomena = [
            "Syntactic ambiguity resolution",
            "Semantic priming",
            "Phonological acquisition",
            "Metaphor comprehension",
            "Bilingual code-switching"
        ]
        existing_models = [
            "Parallel Distributed Processing (PDP) model",
            "Declarative/Procedural model",
            "Competition model",
            "Usage-based model",
            "Connectionist model"
        ]
        sample_sentences = [
            "The old man the boat.",
            "Time flies like an arrow; fruit flies like a banana.",
            "The complex houses married and single soldiers and their families.",
            "The horse raced past the barn fell.",
            "The cotton clothing is made of grows in Mississippi."
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "existing_model": random.choice(existing_models),
                "sample_sentence": random.choice(sample_sentences)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "existing_model": random.choice(existing_models),
                "sample_sentence": random.choice(sample_sentences)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired cognitive model of language acquisition and processing, then apply it to solve a complex linguistic phenomenon. Your model should incorporate the quantum concept of {t['quantum_concept']}, focus on the cognitive process of {t['cognitive_process']}, and address the linguistic phenomenon of {t['linguistic_phenomenon']}.

Brief explanations:
- {t['quantum_concept']}: [Insert a brief, general explanation of the quantum concept]
- {t['cognitive_process']}: [Insert a brief, general explanation of the cognitive process]
- {t['linguistic_phenomenon']}: [Insert a brief, general explanation of the linguistic phenomenon]

Provide your response in the following format:

1. Quantum Cognitive Language Model (300-400 words):
   a) Describe your theoretical model that applies quantum principles to language processing.
   b) Explain how you incorporate {t['quantum_concept']} into your model.
   c) Discuss how your model represents and analyzes {t['cognitive_process']}.
   d) Provide a visual representation or detailed description of your model's architecture.

2. Mathematical Framework (250-350 words):
   a) Present a mathematical formulation of your model (you may use pseudo-equations or descriptive mathematics).
   b) Define key variables and operators in your model.
   c) Explain how your model quantifies or measures linguistic and cognitive phenomena.
   d) Describe how your model incorporates uncertainty or probabilistic reasoning.

3. Language Acquisition Simulation (250-350 words):
   a) Outline how your model simulates the process of language acquisition.
   b) Explain how quantum principles influence learning in your model.
   c) Describe how your model accounts for individual differences in language acquisition.
   d) Provide a specific example of how your model would simulate the acquisition of a linguistic feature.

4. Application to Linguistic Phenomenon (250-350 words):
   a) Apply your quantum cognitive language model to analyze {t['linguistic_phenomenon']}.
   b) Explain how your model provides new insights into this phenomenon.
   c) Compare your model's predictions or explanations to traditional linguistic theories.
   d) Propose a novel hypothesis about {t['linguistic_phenomenon']} based on your model.

5. Practical Application (200-300 words):
   a) Demonstrate how your model would process the following sentence: "{t['sample_sentence']}"
   b) Provide a step-by-step explanation of how your model interprets and analyzes this sentence.
   c) Discuss any ambiguities or challenges in processing this sentence and how your model addresses them.

6. Experimental Design (200-300 words):
   a) Propose an experiment to test a key aspect of your quantum cognitive language model.
   b) Describe the methodology, including data collection and analysis methods.
   c) Discuss potential challenges in empirically validating your model.
   d) Suggest how the results could be interpreted in light of your model's predictions.

7. Critical Evaluation and Comparison (200-300 words):
   a) Critically evaluate potential limitations of your quantum cognitive language model.
   b) Compare your model with the {t['existing_model']} of language processing, highlighting similarities and differences.
   c) Discuss how your model addresses any shortcomings of the {t['existing_model']}.

8. Implications and Future Directions (200-300 words):
   a) Discuss the broader implications of your model for cognitive science and linguistics.
   b) Address potential ethical considerations or societal impacts.
   c) Propose a potential real-world application of your model beyond purely theoretical research.
   d) Discuss potential interdisciplinary implications of your model in fields beyond linguistics and cognitive science.
   e) Suggest two future research directions or extensions of your model.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and linguistics. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Remember to balance creativity with scientific plausibility throughout your response. While we encourage innovative thinking, ensure that your model and its applications remain grounded in established scientific principles.

Format your response with clear headings for each section. Your total response should be between 1850-2650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model effectively incorporates the quantum concept of {t['quantum_concept']}.",
            f"The cognitive process of {t['cognitive_process']} is well-represented and analyzed in the model.",
            f"The model provides novel insights into the linguistic phenomenon of {t['linguistic_phenomenon']}.",
            "The mathematical framework is coherent and appropriately represents the model's key components.",
            f"The model demonstrates practical application by processing the sample sentence: '{t['sample_sentence']}'",
            "The proposed experiment is well-designed and addresses a key aspect of the model.",
            f"The model is critically evaluated and compared with the {t['existing_model']}.",
            "Interdisciplinary implications beyond linguistics and cognitive science are discussed.",
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, and linguistics.",
            "The model is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
