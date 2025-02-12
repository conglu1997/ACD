class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "word": "awesome",
                "time_period": "1950-2020"
            },
            "2": {
                "word": "literally",
                "time_period": "1900-2023"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical model of semantic drift using concepts from topology and information theory, then design and analyze experiments to test the model. Focus on the word '{t['word']}' over the time period {t['time_period']}. Your task has the following parts:

1. Mathematical Model (250-300 words):
   a) Define a topological space that represents the semantic field of the word. Consider using concepts such as metric spaces, manifolds, or simplicial complexes.
   b) Introduce a metric or distance function to quantify semantic similarity. This could be based on word embeddings, co-occurrence statistics, or other linguistic features.
   c) Use concepts from information theory (e.g., entropy, mutual information, Kullback-Leibler divergence) to model how the word's meaning changes over time.
   d) Explain how your model incorporates both continuous and discrete aspects of semantic change.
   e) Provide at least one equation or formal definition for a key component of your model.

2. Model Properties (200-250 words):
   a) Describe at least three mathematical properties of your model (e.g., compactness, connectedness, convergence).
   b) Explain how these properties relate to linguistic phenomena in semantic drift.
   c) Propose a novel property or theorem about your model and provide a sketch of its proof.

3. Experimental Design (200-250 words):
   a) Design an experiment to test your model using real-world language data.
   b) Specify the data sources, collection methods, and analysis techniques you would use.
   c) Describe how you would validate your model's predictions against linguistic evidence.
   d) Discuss potential confounding factors and how you would control for them.

4. Results Analysis (150-200 words):
   a) Provide a hypothetical set of results from your experiment.
   b) Analyze these results in the context of your model, explaining any unexpected outcomes.
   c) Discuss the implications of your findings for our understanding of semantic drift and language change.

5. Model Extension and Limitations (200-250 words):
   a) Propose an extension of your model to account for multi-word expressions or cross-linguistic semantic drift.
   b) Explain how this extension modifies the topological or information-theoretic aspects of your original model.
   c) Describe a potential application of your extended model in computational linguistics or natural language processing.
   d) Discuss at least two limitations of your model and potential approaches to address them.

Ensure your response demonstrates a deep understanding of topology, information theory, and linguistics. Use mathematical notation where appropriate, and explain any technical terms. Balance formal rigor with clear, accessible explanations.

Format your response with clear headings for each section and use LaTeX notation for mathematical expressions where appropriate. Your total response should be between 1000-1250 words.

Response Format:
[Mathematical Model]
(Your content here)

[Model Properties]
(Your content here)

[Experimental Design]
(Your content here)

[Results Analysis]
(Your content here)

[Model Extension and Limitations]
(Your content here)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of topology, information theory, and linguistics, using appropriate mathematical notation and explaining technical terms.",
            "The mathematical model of semantic drift is well-defined, incorporating both topological and information-theoretic concepts, with at least one equation or formal definition provided.",
            "The model properties are clearly described and related to linguistic phenomena, with a novel property or theorem proposed and a sketch of its proof provided.",
            "The experimental design is thorough, addressing data collection, analysis, validation, and potential confounding factors.",
            "The results analysis provides insightful interpretation of hypothetical findings and their implications.",
            "The model extension demonstrates creativity and potential for practical applications in computational linguistics or NLP.",
            "The response discusses at least two limitations of the model and potential approaches to address them.",
            "The response is well-structured, adhering to the specified word limits and format requirements, including the use of LaTeX notation for mathematical expressions where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
