import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "Metaphor",
            "Polysemy",
            "Syntactic ambiguity",
            "Pragmatic inference"
        ]
        quantum_properties = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference"
        ]
        cognitive_processes = [
            "Semantic memory retrieval",
            "Syntactic parsing",
            "Contextual interpretation",
            "Conceptual blending"
        ]
        sample_sentences = [
            "The pen is mightier than the sword.",
            "Time flies like an arrow; fruit flies like a banana.",
            "The complex houses married and single soldiers and their families.",
            "The old man the boat."
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "quantum_property": random.choice(quantum_properties),
                "cognitive_process": random.choice(cognitive_processes),
                "sample_sentence": random.choice(sample_sentences)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "quantum_property": random.choice(quantum_properties),
                "cognitive_process": random.choice(cognitive_processes),
                "sample_sentence": random.choice(sample_sentences)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that encodes and processes linguistic information using quantum states, inspired by theories of cognitive linguistics. Your system should focus on the linguistic feature of {t['linguistic_feature']}, utilize the quantum property of {t['quantum_property']}, and model the cognitive process of {t['cognitive_process']}.

Before you begin, here's a brief primer on quantum computing and the relevant concepts:

Quantum computing utilizes quantum-mechanical phenomena such as superposition and entanglement to perform computations. Unlike classical bits, quantum bits (qubits) can exist in multiple states simultaneously, allowing for potentially exponential speedups in certain types of calculations.

{t['linguistic_feature']}: This is a feature of language that [brief explanation of the linguistic feature].
{t['quantum_property']}: In quantum mechanics, this property refers to [brief explanation of the quantum property].
{t['cognitive_process']}: This is a mental process involved in [brief explanation of the cognitive process].

Your response should include:

1. Quantum Linguistic Encoding (200-250 words):
   a) Explain how you would encode linguistic information into quantum states.
   b) Describe how your encoding scheme incorporates the specified linguistic feature: {t['linguistic_feature']}.
   c) Discuss how the quantum property of {t['quantum_property']} is utilized in your encoding scheme.

2. Quantum Circuit Design (200-250 words):
   a) Propose a simplified quantum circuit design for processing the encoded linguistic information.
   b) Explain how your circuit implements the cognitive process of {t['cognitive_process']}.
   c) Include a simple diagram or detailed description of your quantum circuit.

3. Linguistic Analysis Capabilities (150-200 words):
   a) Describe the types of linguistic analyses your quantum system could perform.
   b) Explain how the system would handle the specified linguistic feature ({t['linguistic_feature']}).

4. Concrete Example (200-250 words):
   Provide a step-by-step walkthrough of how your system would process the following input: '{t['sample_sentence']}'
   a) Explain how this sentence would be encoded into quantum states.
   b) Describe how your quantum circuit would process this input.
   c) Detail the output or analysis your system would produce.

5. Advantages and Limitations (150-200 words):
   a) Discuss potential advantages of your quantum approach over classical NLP techniques.
   b) Identify key technical challenges or limitations in implementing your proposed system.

Ensure your response demonstrates an understanding of quantum computing principles, linguistics, and cognitive science. Use technical terminology appropriately and provide explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 900-1150 words.

A successful response will:
- Clearly explain how linguistic information is encoded into quantum states.
- Provide a plausible quantum circuit design that incorporates the specified cognitive process.
- Demonstrate how the system handles the given linguistic feature.
- Offer a detailed example of processing the sample sentence.
- Discuss both advantages and limitations of the proposed system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            ("The response demonstrates a basic understanding of quantum computing principles, linguistics, and cognitive science.", 0.2),
            (f"The proposed system incorporates the linguistic feature of {t['linguistic_feature']} in its encoding scheme.", 0.2),
            (f"The quantum property of {t['quantum_property']} is utilized in the system design.", 0.2),
            (f"The system attempts to model the cognitive process of {t['cognitive_process']} using quantum computations.", 0.2),
            ("The concrete example provides a plausible processing of the given sample sentence.", 0.2)
        ]
        
        score = 0.0
        for criterion, weight in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += weight
        return score
