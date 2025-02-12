import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_feature": "Grammatical gender",
                "cultural_practice": "Division of labor",
                "time_span": "500 generations"
            },
            {
                "linguistic_feature": "Evidentiality markers",
                "cultural_practice": "Information sharing norms",
                "time_span": "1000 generations"
            },
            {
                "linguistic_feature": "Honorifics",
                "cultural_practice": "Social hierarchy",
                "time_span": "750 generations"
            },
            {
                "linguistic_feature": "Tense system",
                "cultural_practice": "Time perception",
                "time_span": "1250 generations"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a computational model that simulates the co-evolution of language and culture over {t['time_span']}, focusing on how the linguistic feature of {t['linguistic_feature']} and the cultural practice of {t['cultural_practice']} influence each other. Your response should include:\n\n" \
               f"1. Model Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your co-evolution simulation model.\n" \
               f"   b) Explain how your model represents and tracks changes in {t['linguistic_feature']}.\n" \
               f"   c) Detail how the model simulates changes in {t['cultural_practice']}.\n" \
               f"   d) Discuss the mechanisms for interaction between linguistic and cultural elements.\n" \
               f"   e) Include a simple diagram or flowchart illustrating your model's architecture.\n\n" \
               f"2. Simulation Process (250-300 words):\n" \
               f"   a) Outline the initial conditions and parameters for your simulation.\n" \
               f"   b) Describe the step-by-step process of running the simulation over {t['time_span']}.\n" \
               f"   c) Explain how your model handles generational transmission of language and culture.\n" \
               f"   d) Discuss any emergent properties or unexpected outcomes from your simulation.\n\n" \
               f"3. Data Analysis and Visualization (200-250 words):\n" \
               f"   a) Describe the data collected from your simulation.\n" \
               f"   b) Explain your approach to analyzing the co-evolutionary patterns.\n" \
               f"   c) Propose a novel visualization technique to represent the interplay between {t['linguistic_feature']} and {t['cultural_practice']}.\n\n" \
               f"4. Theoretical Implications (200-250 words):\n" \
               f"   a) Discuss how your model and its results contribute to our understanding of language-culture co-evolution.\n" \
               f"   b) Analyze potential implications for theories in linguistics, anthropology, and cognitive science.\n" \
               f"   c) Propose a new hypothesis about the relationship between {t['linguistic_feature']} and {t['cultural_practice']} based on your simulation results.\n\n" \
               f"5. Limitations and Future Directions (150-200 words):\n" \
               f"   a) Identify potential limitations of your model and simulation approach.\n" \
               f"   b) Suggest improvements or extensions to address these limitations.\n" \
               f"   c) Propose a future research direction that builds on your model.\n\n" \
               f"6. Ethical Considerations (100-150 words):\n" \
               f"   a) Discuss potential ethical implications of using computational models to study cultural evolution.\n" \
               f"   b) Address concerns about determinism or reductionism in modeling complex cultural phenomena.\n" \
               f"   c) Propose guidelines for the responsible development and use of such models in research.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistics, anthropology, cognitive science, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model effectively simulates the co-evolution of {t['linguistic_feature']} and {t['cultural_practice']} over {t['time_span']}.",
            "The response demonstrates a deep understanding of linguistics, anthropology, cognitive science, and complex systems modeling.",
            "The simulation process and data analysis approaches are well-explained and scientifically plausible.",
            "The response includes innovative ideas while maintaining scientific rigor.",
            "Theoretical implications and future research directions are thoughtfully considered.",
            "Ethical considerations are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
