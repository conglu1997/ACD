import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            "syntax",
            "semantics",
            "phonology",
            "pragmatics"
        ]
        neural_processes = [
            "synaptic plasticity",
            "neurogenesis",
            "pruning",
            "myelination"
        ]
        cognitive_functions = [
            "working memory",
            "attention",
            "executive function",
            "social cognition"
        ]
        developmental_stages = [
            "infancy",
            "early childhood",
            "adolescence",
            "adulthood"
        ]
        
        tasks = [
            {
                "language_feature": lf,
                "neural_process": np,
                "cognitive_function": cf,
                "developmental_stage": ds
            }
            for lf in language_features
            for np in neural_processes
            for cf in cognitive_functions
            for ds in developmental_stages
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a computational model that simulates the interaction between language acquisition and neural network formation in the human brain. Focus on the language feature of {t['language_feature']}, the neural process of {t['neural_process']}, the cognitive function of {t['cognitive_function']}, and the developmental stage of {t['developmental_stage']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain the relevance of {t['language_feature']} in language acquisition.
   b) Describe the neural process of {t['neural_process']} and its role in brain development.
   c) Discuss how {t['cognitive_function']} relates to language processing.
   d) Outline key characteristics of the {t['developmental_stage']} stage in terms of language and brain development.

2. Model Architecture (250-300 words):
   a) Design a computational model that integrates the specified language feature, neural process, cognitive function, and developmental stage.
   b) Describe the main components of your model and how they interact.
   c) Explain how your model simulates the bidirectional influence between language acquisition and neural network formation.
   d) Include a simple diagram or flowchart illustrating your model's architecture (described textually).
   e) Provide a brief pseudocode or code snippet (10-15 lines) for a key component of your model.

3. Simulation Process (200-250 words):
   a) Describe how your model simulates language acquisition and neural network formation over time.
   b) Explain how you incorporate the specified developmental stage into your simulation.
   c) Discuss any novel algorithms or techniques you've employed in your model.
   d) Compare your model to an existing neurolinguistic theory or model, highlighting similarities and differences.

4. Predictions and Hypotheses (200-250 words):
   a) Describe the key predictions your model makes about language acquisition and neural development.
   b) Propose at least two testable hypotheses derived from your model.
   c) Explain how these hypotheses relate to current theories in neurolinguistics.

5. Validation and Testing (200-250 words):
   a) Propose methods to validate your model against empirical data.
   b) Describe potential experiments or studies that could test your model's predictions.
   c) Discuss the challenges in validating computational models of neurolinguistic processes.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your model for our understanding of language acquisition and brain development.
   b) Propose two practical applications of your model in fields such as education, speech therapy, or artificial intelligence.

7. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns related to simulating brain development and language acquisition.
   b) Propose guidelines for the responsible development and use of neurolinguistic computational models.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and computational modeling. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words. Use markdown formatting for headings and code blocks. If you need to include mathematical formulas, use LaTeX notation within dollar signs (e.g., $E = mc^2$)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified language feature, neural process, cognitive function, and developmental stage.",
            "The proposed computational model is coherent, innovative, and plausibly integrates the given elements.",
            "The simulation process is well-described and incorporates the specified developmental stage effectively.",
            "The model is compared to an existing neurolinguistic theory or model, highlighting similarities and differences.",
            "The pseudocode or code snippet for a key component of the model is provided and relevant.",
            "The predictions and hypotheses are logically derived from the model and relevant to current neurolinguistic theories.",
            "The proposed validation methods and experiments are appropriate and feasible.",
            "The implications and applications are insightful and demonstrate an understanding of the model's potential impact.",
            "The ethical considerations are thoughtful and address relevant concerns in the field.",
            "The response effectively integrates concepts from neuroscience, linguistics, and computational modeling.",
            "The response adheres to the specified word count, structure, and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0