import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "initial_language": "Proto-Indo-European",
                "time_span": "5000 years",
                "focus_area": "phonological changes",
                "initial_characteristics": "Laryngeal consonants, ablaut vowel alternations"
            },
            {
                "initial_language": "Classical Latin",
                "time_span": "2000 years",
                "focus_area": "grammatical structures",
                "initial_characteristics": "Case system, synthetic verb forms"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model to simulate the evolution of {t['initial_language']} over a period of {t['time_span']}, focusing primarily on {t['focus_area']}. Consider the initial characteristics: {t['initial_characteristics']}. Your task has seven parts:

1. Model Design (300-350 words):
   a) Describe the key components of your language evolution simulator.
   b) Explain how your model incorporates both cultural and cognitive factors influencing language change.
   c) Detail the parameters and variables used in your model, including their interactions.
   d) Outline the algorithms or techniques used to simulate language evolution over time.
   e) Explain how your model accounts for language contact and borrowing.
   f) Discuss how your model handles the balance between regularization and irregularization in language evolution.
   g) Provide a textual description of a visual representation (e.g., a flowchart or diagram) of your model's architecture or a key process in the simulation.
   h) Cite relevant research or theories that support your model design.

2. Implementation Details (250-300 words):
   a) Provide pseudocode for the main simulation loop and one key language change mechanism. The pseudocode should be detailed enough to demonstrate the logic of your implementation but not necessarily in a specific programming language.
   b) Explain how you initialize the model with the characteristics of {t['initial_language']}, including the provided initial characteristics.
   c) Describe how your model handles the interaction between different linguistic features during evolution.

3. Simulation Results (250-300 words):
   a) Present a hypothetical set of results from your simulation, focusing on {t['focus_area']}.
   b) Describe three significant linguistic changes observed over the {t['time_span']} period.
   c) Explain how these changes emerged from the interaction of cultural and cognitive factors in your model.
   d) Propose a novel, plausible linguistic feature that might emerge from your simulation. Justify its development based on your model's parameters and mechanisms.

4. Analysis and Interpretation (250-300 words):
   a) Compare your simulated language evolution to known historical changes in languages derived from {t['initial_language']}.
   b) Discuss any unexpected or emergent behaviors observed in your simulation.
   c) Analyze the relative influence of cultural versus cognitive factors in your simulated language evolution.
   d) Explain how language contact and borrowing affected the evolution in your model.
   e) Briefly compare your model with an existing computational model of language evolution from the literature, highlighting key differences and similarities.

5. Model Evaluation and Future Directions (200-250 words):
   a) Propose two methods to validate your language evolution model against historical linguistic data.
   b) Discuss the limitations of your current model and suggest two potential improvements.
   c) Describe how your model could be adapted to study other aspects of language evolution not focused on in this simulation.
   d) Propose a hypothetical experiment that could test a specific prediction made by your model.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of language evolution simulation and its applications.
   b) Consider how such models might impact language preservation efforts or language policies.
   c) Analyze potential misuse or unintended consequences of language evolution models.
   d) Propose guidelines for the responsible use of language evolution models in linguistic research and policy-making.

7. Reflection and Interdisciplinary Connections (150-200 words):
   a) Reflect on the challenges encountered in designing this language evolution model.
   b) Discuss how insights from this model might contribute to other fields of study (e.g., cultural evolution, cognitive science, or artificial intelligence).
   c) Propose a research question that bridges your language evolution model with another scientific discipline.

Ensure your response demonstrates a deep understanding of historical linguistics, cognitive science, and computational modeling. Use appropriate linguistic terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each of the seven main sections, and use subheadings for each sub-task. Adhere to the word count guidelines provided for each section. Cite relevant research or theories where appropriate to support your model design and analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of language evolution, incorporating cultural and cognitive factors, language contact, borrowing, and the balance between regularization and irregularization.",
            "The computational model design is well-structured, with clear explanations of components, parameters, and algorithms, supported by relevant research citations and a textual description of a visual representation.",
            f"The simulation results focus on {t['focus_area']}, present plausible linguistic changes over the specified time period, and propose a novel, justified emergent linguistic feature.",
            "The analysis compares simulated changes to known historical linguistic developments, discusses emergent behaviors, explains the impact of language contact, and includes a comparison with an existing computational model.",
            "The response proposes valid methods for model validation, suggests relevant improvements, and includes a hypothetical experiment to test a model prediction.",
            "The submission includes a thoughtful discussion of ethical implications, potential misuse, and responsible use of language evolution models.",
            "The reflection demonstrates an understanding of the challenges in model design and proposes interdisciplinary connections.",
            "The overall submission shows creativity, interdisciplinary knowledge integration, and scientific plausibility.",
            "The response adheres to the specified word count guidelines for each section and provides sufficiently detailed pseudocode."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
