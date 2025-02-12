class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random
        ambiguous_sentences = [
            "The old man the boat.",
            "The complex houses married and single soldiers and their families.",
            "The horse raced past the barn fell.",
            "The cotton clothing is made of grows in Mississippi.",
            "The man who hunts ducks out on weekends."
        ]
        tasks = random.sample(ambiguous_sentences, 2)
        return {
            "1": {"sentence": tasks[0]},
            "2": {"sentence": tasks[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a neurolinguistic simulation of syntactic ambiguity resolution for the following sentence: "{t['sentence']}"

        Your task has the following parts:

        1. Linguistic Analysis (150-200 words):
           a) Identify and explain the syntactic ambiguity in the given sentence.
           b) Provide two possible interpretations of the sentence.
           c) Discuss the linguistic principles involved in creating and resolving such ambiguities.

        2. Neuroscientific Model (200-250 words):
           a) Describe a neuroscientific model of how the brain might process and resolve this syntactic ambiguity.
           b) Identify key brain regions involved and their roles in the process.
           c) Explain how neural activation patterns might differ between the two interpretations.

        3. Computational Simulation (250-300 words):
           a) Propose a computational model that simulates the neural processes involved in resolving the ambiguity.
           b) Describe the key components of your model, including inputs, processing steps, and outputs.
           c) Explain how your model integrates linguistic and neuroscientific principles.
           d) Provide a high-level pseudocode or flowchart of your simulation algorithm.

        4. Predictions and Implications (150-200 words):
           a) Describe the expected outputs or behaviors of your simulation for the given sentence.
           b) Discuss how your model's predictions align with or diverge from current neurolinguistic theories.
           c) Propose an experiment that could test the validity of your model's predictions.

        5. Limitations and Future Directions (100-150 words):
           a) Identify at least two limitations of your proposed model or simulation.
           b) Suggest two potential improvements or extensions to address these limitations.

        Ensure your response demonstrates a deep understanding of both linguistics and neuroscience, as well as computational modeling principles. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section. Your total response should be between 850-1100 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of syntactic ambiguity and its linguistic principles.",
            "The neuroscientific model accurately describes relevant brain regions and processes involved in ambiguity resolution.",
            "The computational simulation effectively integrates linguistic and neuroscientific principles in a coherent model.",
            "The predictions and implications section provides insightful analysis and a well-designed experiment proposal.",
            "The limitations and future directions are thoughtfully considered and relevant to the proposed model.",
            "The overall response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
