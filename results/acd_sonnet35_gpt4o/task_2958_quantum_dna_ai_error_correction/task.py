import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dna_errors = [
            {
                'error_type': 'Single nucleotide polymorphism',
                'description': 'A single base pair mutation'
            },
            {
                'error_type': 'Insertion/Deletion',
                'description': 'Addition or removal of nucleotides'
            }
        ]
        quantum_techniques = [
            {
                'technique': 'Surface code',
                'description': 'A type of quantum error correction code'
            },
            {
                'technique': 'Quantum annealing',
                'description': 'A quantum-mechanical method for finding global minimum'
            }
        ]
        tasks = []
        for de in dna_errors:
            for qt in quantum_techniques:
                tasks.append({
                    'dna_error': de['error_type'],
                    'error_description': de['description'],
                    'quantum_technique': qt['technique'],
                    'technique_description': qt['description']
                })
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical AI system for DNA error correction using principles from quantum error correction codes and evolutionary algorithms. Your system should address the DNA error type of {t['dna_error']} ({t['error_description']}) and incorporate the quantum technique of {t['quantum_technique']} ({t['technique_description']}). Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your hybrid quantum-classical AI system for DNA error correction.
   b) Explain how you integrate quantum computing, classical computing, and AI in your design.
   c) Detail how your system incorporates the specified quantum technique.
   d) Discuss how your system is tailored to address the given DNA error type.
   e) Include a high-level diagram or flowchart of your system architecture (describe this textually).
   f) Provide at least one relevant citation or reference to current research in this area.

2. Quantum-Classical Integration (250-300 words):
   a) Explain how the quantum component enhances the classical error correction process.
   b) Describe any novel algorithms or techniques you've developed to leverage both quantum and classical capabilities.
   c) Discuss potential synergies between quantum computing and evolutionary algorithms in the context of DNA error correction.
   d) Propose a novel quantum-classical algorithm specific to your system's design.
   e) Provide at least one relevant citation or reference to current research in this area.

3. Error Correction Process (200-250 words):
   a) Outline the steps your system takes to identify and correct DNA errors.
   b) Explain how your system balances accuracy and efficiency in the error correction process.
   c) Describe how your approach might improve upon traditional DNA error correction methods.
   d) Provide at least one relevant citation or reference to current research in this area.

4. Evolutionary Algorithm Design (200-250 words):
   a) Describe the evolutionary algorithm component of your system.
   b) Explain how it interacts with the quantum component.
   c) Discuss how the evolutionary approach contributes to error correction and adaptation.
   d) Provide at least one relevant citation or reference to current research in this area.

5. Challenges and Solutions (150-200 words):
   a) Identify potential technical challenges in implementing your hybrid quantum-classical AI system for DNA error correction.
   b) Propose solutions or approaches to overcome these challenges.
   c) Discuss any limitations of your system and how they might be addressed in future iterations.
   d) Provide at least one relevant citation or reference to current research in this area.

6. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate the performance of your system.
   b) Describe how you would compare your system's results to classical DNA error correction methods.
   c) Suggest an experimental setup to validate the effectiveness of your system.
   d) Provide at least one relevant citation or reference to current research in this area.

7. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical concerns related to using quantum-enhanced AI for DNA error correction.
   b) Analyze possible societal impacts of advanced DNA manipulation techniques.
   c) Propose guidelines for responsible development and use of such technology.
   d) Provide at least one relevant citation or reference to current research in this area.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and genetics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_technique']} and its application to DNA error correction, specifically for {t['dna_error']}.",
            "The proposed hybrid quantum-classical AI system is innovative, scientifically plausible, and thoroughly explained.",
            "The integration of quantum computing, classical computing, and AI is well-reasoned and clearly described.",
            "The evolutionary algorithm design is coherent and its interaction with the quantum component is well-explained.",
            "The response addresses technical challenges, ethical considerations, and performance evaluation thoughtfully.",
            "The writing is clear, well-structured, and uses appropriate technical terminology from multiple disciplines.",
            "Each section includes at least one relevant citation or reference to current research.",
            "A novel quantum-classical algorithm is proposed in the Quantum-Classical Integration section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
