import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            {
                'task': 'Text classification',
                'description': 'Categorize text documents into predefined classes',
                'example': 'Classify news articles into topics like politics, sports, or technology'
            },
            {
                'task': 'Named entity recognition',
                'description': 'Identify and classify named entities in text',
                'example': 'Recognize and categorize names of persons, organizations, and locations in a sentence'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(nlp_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum circuit for the NLP task of {t['task']} ({t['description']}). Your response should include the following sections:

1. Quantum Circuit Design (300-350 words):
   a) Describe the overall architecture of your quantum circuit for the given NLP task.
   b) Explain how classical data (text) is encoded into quantum states.
   c) Detail the quantum operations (gates) used in your circuit and their purpose.
   d) Discuss how the circuit outputs are measured and interpreted for the NLP task.
   e) Provide a simple text-based diagram of your quantum circuit using ASCII characters. The diagram should include at least 3 qubits and 5 gates.
   f) Briefly explain how this circuit might be implemented on current quantum hardware.

2. Quantum Advantage Analysis (250-300 words):
   a) Identify potential advantages of your quantum approach over classical NLP methods for this task.
   b) Explain any quantum phenomena (e.g., superposition, entanglement) that your circuit leverages.
   c) Provide a theoretical analysis of the computational complexity or speed-up, if applicable.
   d) Discuss potential error rates or accuracy comparisons between your quantum approach and classical methods.

3. Limitations and Challenges (200-250 words):
   a) Discuss potential limitations or challenges in implementing your quantum NLP circuit.
   b) Address issues such as decoherence, error correction, or scalability.
   c) Suggest possible solutions or areas for further research to overcome these challenges.

4. Comparative Example (200-250 words):
   a) Provide a specific example of how your quantum circuit would process the following: {t['example']}
   b) Compare this to how a classical NLP algorithm might approach the same example.
   c) Highlight key differences in methodology and potential outcomes.

5. Future Implications (150-200 words):
   a) Speculate on how quantum NLP might evolve and impact the field of natural language processing.
   b) Discuss potential applications or advancements that could result from this integration of quantum computing and NLP.
   c) Consider any ethical implications or societal impacts of advanced quantum NLP systems.

Ensure your response demonstrates a deep understanding of both quantum computing principles and natural language processing techniques. Use appropriate terminology from both fields and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific and theoretical plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1100-1350 words.

Important notes:
- Present any mathematical formulas using LaTeX notation.
- For the quantum circuit diagram, use ASCII characters to represent gates and qubits (e.g., |0> for qubit initialization, H for Hadamard gate, X for NOT gate, etc.).
- Do not use any external quantum computing libraries or resources. Rely solely on your own knowledge and understanding.
- Ensure that your response is self-contained and does not refer to external information or assumptions not provided in the task description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and NLP principles, using appropriate terminology and concepts from both fields.",
            "The quantum circuit design is creative, well-explained, and theoretically plausible for the given NLP task.",
            "The quantum circuit diagram is provided in ASCII format, includes at least 3 qubits and 5 gates, and correctly represents the described circuit.",
            "The analysis of quantum advantages and limitations is thorough, scientifically grounded, and includes a discussion of computational complexity, speed-up, and potential error rates or accuracy comparisons.",
            "The comparative example effectively illustrates the differences between quantum and classical approaches for the specific NLP task.",
            "The response includes a brief explanation of how the quantum circuit might be implemented on current quantum hardware.",
            "The future implications section considers ethical implications or societal impacts of advanced quantum NLP systems.",
            "The response adheres to the specified structure, word count requirements, and formatting guidelines (including LaTeX for formulas).",
            "The submission does not appear to rely on external quantum computing libraries or resources."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
