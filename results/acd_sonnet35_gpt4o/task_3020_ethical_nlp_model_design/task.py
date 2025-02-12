import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            "text classification",
            "named entity recognition",
            "sentiment analysis",
            "machine translation",
            "text summarization",
            "question answering",
            "dialogue generation"
        ]
        ethical_considerations = [
            "bias mitigation",
            "fairness",
            "transparency",
            "privacy preservation",
            "accountability",
            "robustness against adversarial attacks"
        ]
        cognitive_principles = [
            "attention mechanisms",
            "working memory simulation",
            "hierarchical processing",
            "multi-modal integration",
            "adaptive learning",
            "context-dependent processing"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "nlp_task": random.choice(nlp_tasks),
                "ethical_consideration": random.choice(ethical_considerations),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel natural language processing model for {t['nlp_task']} that incorporates the ethical consideration of {t['ethical_consideration']} and the cognitive science principle of {t['cognitive_principle']}. Then, analyze its potential impact on AI language technologies. Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the key components of your NLP model.
   b) Explain how the model incorporates the specified ethical consideration.
   c) Detail how the cognitive science principle is implemented in the model.
   d) Discuss any novel features that enhance the model's performance or ethical stance.

2. Ethical Implementation (250-300 words):
   a) Elaborate on how the ethical consideration is integrated into the model's design and function.
   b) Discuss potential challenges in implementing this ethical aspect and how you address them.
   c) Propose metrics or evaluation methods to assess the model's adherence to the ethical consideration.

3. Cognitive Science Integration (250-300 words):
   a) Explain how the specified cognitive principle enhances the model's capabilities.
   b) Describe how this integration differs from traditional NLP approaches.
   c) Discuss any limitations or trade-offs introduced by incorporating this cognitive principle.

4. Performance and Evaluation (200-250 words):
   a) Propose a method for evaluating your model's performance on the specified NLP task.
   b) Discuss how the ethical and cognitive aspects might impact traditional performance metrics.
   c) Suggest novel evaluation criteria that account for both performance and ethical considerations.

5. Potential Impact Analysis (200-250 words):
   a) Analyze how your model could influence future developments in NLP and AI language technologies.
   b) Discuss potential benefits and risks of widespread adoption of such ethically-aware and cognitively-inspired models.
   c) Consider implications for AI governance and policy-making in the field of language technology.

6. Limitations and Future Work (150-200 words):
   a) Identify potential limitations or weaknesses in your proposed model.
   b) Suggest areas for future research or improvement.
   c) Propose an experiment to further explore the intersection of ethics, cognitive science, and NLP.

Ensure your response demonstrates a deep understanding of natural language processing, cognitive science, and AI ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an NLP model for {t['nlp_task']} that incorporates {t['ethical_consideration']} and {t['cognitive_principle']}.",
            "The model architecture is clearly explained and incorporates novel features that address both ethical and cognitive aspects.",
            "The ethical implementation is thoroughly discussed, including challenges and evaluation methods.",
            "The integration of the cognitive science principle is well-explained and differentiated from traditional approaches.",
            "The performance evaluation proposal includes both traditional metrics and novel criteria for ethical considerations.",
            "The potential impact analysis covers both benefits and risks, and considers implications for AI governance.",
            "Limitations are identified and future work is proposed, including a relevant experiment.",
            "The response demonstrates a deep understanding of NLP, cognitive science, and AI ethics, using appropriate terminology.",
            "The proposed model is innovative while maintaining scientific and technological plausibility.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
