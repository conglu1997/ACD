class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_ability": "Symbolic thinking",
                "archaeological_evidence": "Cave paintings (e.g., Lascaux Cave in France, dated to around 17,000 years ago)",
                "time_period": "Upper Paleolithic"
            },
            "2": {
                "cognitive_ability": "Theory of mind",
                "archaeological_evidence": "Burial practices (e.g., Neanderthal burials with grave goods, dated to around 60,000 years ago)",
                "time_period": "Middle Paleolithic"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the cognitive evolution of early humans based on archaeological evidence, then use it to generate and test hypotheses about the development of {t['cognitive_ability']}. Focus on the archaeological evidence of {t['archaeological_evidence']} from the {t['time_period']} period. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the key components of your computational model.
   b) Explain how it integrates principles from cognitive science, archaeology, and evolutionary biology.
   c) Detail how the model simulates cognitive evolution over time.
   d) Provide a simple diagram or flowchart of your model architecture. Use ASCII art or a clear text-based representation.

2. Archaeological Evidence Integration (200-250 words):
   a) Explain how your model incorporates the specified archaeological evidence.
   b) Discuss any challenges in translating physical evidence into cognitive processes.
   c) Describe how your model accounts for the limitations and biases in the archaeological record.

3. Cognitive Ability Simulation (250-300 words):
   a) Detail how your model simulates the development of the specified cognitive ability.
   b) Explain the key factors and mechanisms in your model that contribute to this cognitive evolution.
   c) Discuss how your model accounts for environmental and social influences on cognitive development.

4. Hypothesis Generation and Testing (200-250 words):
   a) Generate two novel hypotheses about the development of the specified cognitive ability based on your model.
   b) Describe how you would test these hypotheses using your model.
   c) Discuss potential implications of your hypotheses for our understanding of human cognitive evolution.

5. Model Validation and Limitations (150-200 words):
   a) Propose methods to validate your model against existing archaeological and cognitive data.
   b) Discuss the limitations of your model and potential biases in its predictions.
   c) Suggest improvements or extensions to address these limitations.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your model could contribute to advancements in cognitive archaeology.
   b) Explain potential applications of your model in other fields (e.g., anthropology, psychology).
   c) Propose a research question in a related field that could be investigated using your model.

Ensure your response demonstrates a deep understanding of cognitive science, archaeology, and evolutionary biology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your model design while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Strictly adhere to the word counts specified for each section. Include your diagram or flowchart within the Model Architecture section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, archaeology, and evolutionary biology.",
            "The computational model design is innovative, plausible, and effectively integrates principles from multiple disciplines.",
            "The model's approach to simulating cognitive evolution and incorporating archaeological evidence is well-explained and logically consistent.",
            "The generated hypotheses are novel and their proposed testing methods are appropriate.",
            "The response addresses model validation, limitations, and potential biases thoroughly.",
            "The discussion of interdisciplinary implications shows insightful analysis and creative thinking.",
            "The response adheres to the specified format and word limits.",
            "The response includes a clear model architecture diagram or flowchart using ASCII art or text-based representation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
