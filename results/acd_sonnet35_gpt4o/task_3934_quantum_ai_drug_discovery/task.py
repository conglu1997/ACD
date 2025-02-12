import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genetic_disorders = [
            'Cystic Fibrosis',
            'Huntington\'s Disease',
            'Duchenne Muscular Dystrophy',
            'Sickle Cell Anemia'
        ]
        quantum_techniques = [
            'quantum annealing',
            'variational quantum eigensolver (VQE)',
            'quantum approximate optimization algorithm (QAOA)',
            'quantum machine learning'
        ]
        tasks = [
            {
                'genetic_disorder': random.choice(genetic_disorders),
                'quantum_technique': random.choice(quantum_techniques)
            },
            {
                'genetic_disorder': random.choice(genetic_disorders),
                'quantum_technique': random.choice(quantum_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for personalized drug discovery targeting {t['genetic_disorder']}, utilizing {t['quantum_technique']} as a key component. Then, analyze its potential impact on treating this complex genetic disorder. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI system for drug discovery.
   b) Explain how it integrates quantum computing, AI, and genetic analysis.
   c) Detail how {t['quantum_technique']} is specifically utilized in your system.
   d) Include a high-level diagram or flowchart of your system architecture (describe it textually).

2. Drug Discovery Process (250-300 words):
   a) Explain the steps your system takes to discover potential drug candidates for {t['genetic_disorder']}.
   b) Describe how your system accounts for individual genetic variations in patients.
   c) Discuss how quantum computing enhances the drug discovery process compared to classical methods.

3. Quantum-Classical Hybrid Approach (200-250 words):
   a) Detail how your system combines quantum and classical computing resources.
   b) Explain which parts of the process are handled by quantum computing and which by classical computing.
   c) Discuss the advantages and challenges of this hybrid approach.

4. Genetic Analysis and Personalization (200-250 words):
   a) Describe how your system analyzes genetic data to personalize drug discovery for {t['genetic_disorder']}.
   b) Explain how it accounts for epigenetic factors and gene-environment interactions.
   c) Discuss potential privacy and ethical considerations related to genetic data use.

5. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate the performance of your quantum-enhanced AI system.
   b) Compare the expected performance of your system to current drug discovery methods for {t['genetic_disorder']}.
   c) Discuss potential limitations and areas for improvement in your approach.

6. Potential Impact and Future Directions (200-250 words):
   a) Analyze the potential impact of your system on treating {t['genetic_disorder']}.
   b) Discuss how this approach could be extended to other genetic disorders or areas of medicine.
   c) Propose future research directions to further enhance quantum-AI integration in drug discovery.

7. Ethical Considerations and Societal Implications (150-200 words):
   a) Discuss ethical implications of using quantum-enhanced AI for personalized medicine.
   b) Address concerns about data privacy, algorithmic bias, and equitable access to this technology.
   c) Propose guidelines for responsible development and deployment of such systems in healthcare.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, genetics, and pharmacology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, AI, genetics, and pharmacology.",
            "The system design is innovative, plausible, and well-explained, integrating concepts from multiple disciplines.",
            "The drug discovery process and genetic analysis approach are thorough and scientifically sound.",
            "The potential impact and ethical considerations are adequately addressed.",
            f"The use of {t['quantum_technique']} is well-explained and integrated into the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
