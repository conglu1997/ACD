import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                "process": "working memory",
                "description": "The cognitive system responsible for temporarily holding and manipulating information"
            },
            {
                "process": "semantic memory",
                "description": "The memory of meanings, understandings, and other concept-based knowledge"
            },
            {
                "process": "predictive processing",
                "description": "The brain's mechanism for anticipating and predicting incoming sensory input"
            },
            {
                "process": "attention mechanisms",
                "description": "Cognitive processes that allow focusing on specific aspects of sensory input while ignoring others"
            }
        ]
        
        nlp_tasks = [
            "text summarization",
            "sentiment analysis",
            "language translation",
            "question answering"
        ]
        
        return {
            "1": {"cognitive_process": random.choice(cognitive_processes), "nlp_task": random.choice(nlp_tasks)},
            "2": {"cognitive_process": random.choice(cognitive_processes), "nlp_task": random.choice(nlp_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language model architecture inspired by the cognitive process of {t['cognitive_process']['process']} for the NLP task of {t['nlp_task']}. Your response should include:

1. Architecture Overview (4-5 sentences):
   Provide a high-level description of your proposed language model architecture, explaining how it incorporates principles from the specified cognitive process.

2. Key Components (3-4 points):
   List and briefly describe the main components of your architecture, highlighting how each relates to aspects of the cognitive process or the NLP task.

3. Information Flow (3-4 sentences):
   Explain how information moves through your model, from input to output, detailing any unique processing steps inspired by the cognitive process.

4. Training Approach (2-3 sentences):
   Propose a training method for your model, considering how it might differ from traditional language model training to better reflect the cognitive process.

5. Advantages for NLP Task (2-3 points):
   Discuss specific advantages your cognitive-inspired architecture might have for the given NLP task compared to traditional approaches.

6. Potential Limitations (2-3 points):
   Identify possible drawbacks or challenges of your proposed architecture.

7. Future Research Direction (2-3 sentences):
   Suggest a specific area for further research that could enhance your model's performance or expand its capabilities.

Ensure your response demonstrates a deep understanding of both the specified cognitive process ({t['cognitive_process']['description']}) and the requirements of the NLP task. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate principles from {t['cognitive_process']['process']} into the language model architecture.",
            f"The architecture should be tailored to the NLP task of {t['nlp_task']}.",
            "The proposed model should be novel and creative while remaining scientifically plausible.",
            "The response should demonstrate a deep understanding of both cognitive science and AI principles.",
            "All seven requested sections should be present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
