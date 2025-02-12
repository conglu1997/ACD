import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Computer Vision",
                "task": "Identifying recurring patterns in satellite imagery",
                "data_type": "Time series of high-resolution satellite images",
                "specific_challenge": "Detecting gradual changes in land use over time"
            },
            {
                "domain": "Natural Language Processing",
                "task": "Detecting narrative structures in long-form text",
                "data_type": "Collection of novels and long-form articles",
                "specific_challenge": "Identifying recurring themes and character arcs across multiple works"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a machine learning model inspired by the hippocampus for memory formation and retrieval, then apply it to the following complex pattern recognition task in {t['domain']}: {t['task']}. Your model should specifically address the challenge of {t['specific_challenge']}. Your response should include:

1. Hippocampal-Inspired Architecture (300-350 words):
   a) Describe the key components of your model, explaining how they parallel hippocampal structures and functions (e.g., dentate gyrus, CA3, CA1 regions).
   b) Explain how your model simulates the processes of memory encoding, consolidation, and retrieval, drawing clear parallels to hippocampal function.
   c) Discuss any novel features or mechanisms in your design that enhance its pattern recognition capabilities, particularly for {t['specific_challenge']}.
   d) Include a high-level diagram or pseudocode snippet illustrating the main components and their interactions.

2. Learning and Memory Processes (250-300 words):
   a) Detail how your model learns and stores new information, relating it to synaptic plasticity in the hippocampus.
   b) Explain the mechanisms for pattern separation and pattern completion in your model, and how they relate to the given task.
   c) Describe how your model handles the stability-plasticity dilemma in memory formation, particularly in the context of {t['specific_challenge']}.

3. Application to Pattern Recognition (250-300 words):
   a) Explain how you would apply your model to the given task: {t['task']}, focusing on {t['specific_challenge']}.
   b) Describe how your model would process and analyze the provided data type: {t['data_type']}.
   c) Discuss any modifications or extensions to your base model necessary for this specific application.

4. Performance Analysis (200-250 words):
   a) Propose specific methods to evaluate your model's performance on the given task, including relevant metrics.
   b) Compare the expected performance of your model to traditional machine learning approaches for this task, highlighting potential advantages.
   c) Discuss potential advantages and limitations of your hippocampal-inspired approach, particularly in addressing {t['specific_challenge']}.

5. Neuroscientific Implications (150-200 words):
   a) Discuss how your model might inform or challenge current theories of hippocampal function, particularly in relation to {t['domain']}.
   b) Propose a specific experiment that could test predictions made by your model about human memory processes in the context of {t['task']}.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your model for future research, explaining their potential impact.
   b) Briefly describe how these extensions could advance our understanding of both machine learning and neuroscience in the context of {t['domain']}.

Ensure your response demonstrates a deep understanding of both neuroscience (particularly hippocampal function) and machine learning principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your model should be grounded in current neuroscientific understanding but can propose novel mechanisms where appropriate.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep and accurate understanding of both hippocampal function and machine learning principles, using appropriate terminology.",
            "The proposed model effectively integrates specific neuroscientific concepts (e.g., dentate gyrus, CA3, CA1 regions) with machine learning techniques in a plausible manner.",
            f"The application to the given pattern recognition task ({t['task']}) is well-explained and addresses the specific challenge of {t['specific_challenge']}.",
            "The response includes innovative ideas while maintaining scientific plausibility and grounding in current neuroscientific understanding.",
            "The performance analysis includes specific, relevant evaluation metrics and a thoughtful comparison to traditional approaches.",
            "The neuroscientific implications and proposed experiment are specific, relevant, and demonstrate a clear understanding of how the model relates to current theories.",
            "The response is well-structured, adheres to the specified format, and falls within the 1250-1550 word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
