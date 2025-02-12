import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                'concept': 'Superposition',
                'description': 'The ability of a quantum system to exist in multiple states simultaneously'
            },
            {
                'concept': 'Entanglement',
                'description': 'A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently'
            }
        ]
        biological_processes = [
            {
                'process': 'DNA replication',
                'description': 'The biological process of producing two identical replicas of DNA from one original DNA molecule'
            },
            {
                'process': 'Genetic recombination',
                'description': 'The production of offspring with combinations of traits that differ from those found in either parent'
            }
        ]
        tasks = []
        for qc in quantum_concepts:
            for bp in biological_processes:
                tasks.append({
                    'quantum_concept': qc['concept'],
                    'quantum_description': qc['description'],
                    'biological_process': bp['process'],
                    'biological_description': bp['description']
                })
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-inspired model for genetic information processing and evolution, incorporating the quantum mechanical concept of {t['quantum_concept']} and the biological process of {t['biological_process']}. Your task has the following components:

1. Conceptual Framework (250-300 words):
   a) Explain how you would integrate {t['quantum_concept']} ({t['quantum_description']}) with {t['biological_process']} ({t['biological_description']}) in a genetic information processing model.
   b) Describe the key components and structure of your model.
   c) Explain how this integration might enhance or change our understanding of genetic processes and evolution.

2. Theoretical Justification (200-250 words):
   a) Provide a theoretical justification for your model, drawing on relevant literature from quantum mechanics, molecular biology, and information theory.
   b) Discuss any existing theories or experimental evidence that support or inspire your approach.
   c) Propose a novel hypothesis about genetic information processing or evolution that your model could test.

3. Mathematical Representation (200-250 words):
   a) Present a mathematical representation of a key aspect of your model.
   b) Explain the variables, operators, or functions in your formulation.
   c) Describe how this mathematical representation captures the integration of quantum and biological principles.

4. Evolutionary Implications (150-200 words):
   a) Discuss how your model might affect our understanding of evolutionary processes.
   b) Propose a mechanism by which quantum effects could influence genetic variation or selection.
   c) Explain how your model might account for observed phenomena in evolutionary biology.

5. Experimental Proposal (200-250 words):
   a) Design an experiment to test a key prediction of your model.
   b) Describe the methodology, including the system you would study, the measurements you would make, and the controls you would use.
   c) Explain how you would analyze the results and what outcomes would support or refute your model.

6. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations of your model and any assumptions you've made.
   b) Suggest areas for future research or refinement of your model.
   c) Consider potential technological applications if your model proves accurate.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_concept']} and {t['biological_process']}.",
            "The proposed model creatively integrates quantum and biological principles in a plausible manner.",
            "The mathematical representation is coherent and relevant to the model.",
            "The evolutionary implications and experimental proposal are well-reasoned and scientifically sound.",
            "The response shows critical thinking in addressing limitations and future directions.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
