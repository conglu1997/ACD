import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_problem": "Plastic degradation in marine environments",
                "target_organism": "Marine bacteria",
                "evolutionary_constraint": "High salt concentration"
            },
            {
                "biological_problem": "Improved photosynthesis efficiency in crops",
                "target_organism": "C3 plants",
                "evolutionary_constraint": "Limited CO2 availability"
            },
            {
                "biological_problem": "Radiation resistance for space exploration",
                "target_organism": "Extremophile bacteria",
                "evolutionary_constraint": "High levels of ionizing radiation"
            },
            {
                "biological_problem": "Bioremediation of heavy metal contamination",
                "target_organism": "Soil fungi",
                "evolutionary_constraint": "Toxicity of metal ions"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel protein sequence to address the biological problem of {t['biological_problem']} in {t['target_organism']}, considering the evolutionary constraint of {t['evolutionary_constraint']}. Your task has the following components:

1. Problem Analysis (200-250 words):
   a) Explain the biological problem and its significance.
   b) Describe the current limitations in addressing this problem.
   c) Analyze how the evolutionary constraint affects potential solutions.

2. Evolutionary Context (200-250 words):
   a) Discuss the evolutionary history of similar proteins or functions in related organisms.
   b) Explain how evolutionary principles can guide the design of a novel protein.
   c) Describe potential trade-offs between protein function and evolutionary constraints.

3. Protein Design (350-400 words):
   a) Propose a name for your engineered protein following standard naming conventions.
   b) Provide the first 50 amino acids of your novel protein sequence using the single-letter code, formatted in groups of 10 for readability (e.g., MKVLWAALLV VFLAGCQAKV EQAVETEPEP ELRQQTEWQS GQRWELALGR).
   c) Explain the rationale behind your sequence design, including any motifs or domains.
   d) Justify the choice of specific amino acids in at least 5 key positions and how they contribute to the protein's function or stability.
   e) Describe how your design addresses the biological problem and evolutionary constraint.
   f) Discuss any potential post-translational modifications or structural features.

4. Computational Analysis (250-300 words):
   a) Describe computational methods you would use to analyze your protein sequence.
   b) Predict the secondary and tertiary structure of your protein (provide a brief description, not actual structures).
   c) Explain how you would computationally assess the protein's potential functionality.
   d) Compare your proposed protein to existing solutions in the field, highlighting potential advantages.

5. Experimental Validation (200-250 words):
   a) Propose an experimental approach to test your protein's function in vitro.
   b) Describe how you would assess the protein's performance in the target organism.
   c) Explain potential challenges in expressing and testing your engineered protein.

6. Ecological and Ethical Considerations (150-200 words):
   a) Discuss potential ecological impacts of introducing your engineered protein into the environment.
   b) Address ethical considerations related to protein engineering and its applications.
   c) Propose guidelines for responsible development and use of engineered proteins.

7. Literature Citations (throughout your response):
   Include at least 5 relevant scientific citations throughout your response to support your arguments and demonstrate depth of knowledge. Use a consistent citation format (e.g., [Author, Year]).

Ensure your response demonstrates a deep understanding of molecular biology, evolution, bioinformatics, and protein engineering. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your protein design while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response comprehensively addresses the biological problem of {t['biological_problem']} in {t['target_organism']}.",
            f"The protein design explicitly considers and addresses the evolutionary constraint of {t['evolutionary_constraint']}.",
            "The protein sequence is provided in the correct format (groups of 10 amino acids) and includes a detailed justification for at least 5 key amino acid choices.",
            "The proposed protein is given a name following standard naming conventions.",
            "The computational analysis includes a comparison with existing solutions in the field.",
            "The experimental validation approach is well-explained, relevant, and addresses potential challenges.",
            "The response demonstrates a deep understanding of molecular biology, evolution, and bioinformatics, using appropriate terminology throughout.",
            "At least 5 relevant and recent (within the last 10 years) scientific citations are included throughout the response.",
            "The ecological and ethical considerations are thoughtfully addressed with specific examples and proposed guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
