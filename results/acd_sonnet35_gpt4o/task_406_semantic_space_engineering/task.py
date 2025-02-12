import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "emotions",
                "constraint": "temporal dynamics",
                "application": "sentiment analysis in social media"
            },
            {
                "domain": "colors",
                "constraint": "cultural variations",
                "application": "cross-cultural marketing strategies"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel semantic space model for representing and manipulating word meanings in the domain of {t['domain']}, incorporating the constraint of {t['constraint']}. Then, analyze its potential application in {t['application']}. Your response should include:

1. Model Design (250-300 words):
   - Describe the key components and structure of your semantic space model.
   - Explain how it represents word meanings and relationships in the given domain.
   - Detail how your model incorporates the specified constraint.

2. Cognitive Science Principles (150-200 words):
   - Discuss how your model aligns with or challenges current theories of semantic representation in cognitive science.
   - Explain any cognitive processes or phenomena that your model aims to capture or simulate.

3. Implementation and AI Integration (200-250 words):
   - Outline a potential method for implementing your model computationally.
   - Describe how existing AI techniques (e.g., neural networks, knowledge graphs) could be utilized or adapted for your model.
   - Discuss any novel AI approaches that might be necessary to fully realize your model.

4. Application Analysis (150-200 words):
   - Analyze how your semantic space model could be applied to the specified application.
   - Discuss potential benefits and challenges of using your model in this context.
   - Propose a specific use case or experiment to demonstrate the model's effectiveness.

5. Limitations and Future Directions (100-150 words):
   - Identify potential limitations or drawbacks of your semantic space model.
   - Suggest areas for future research or improvement.
   - Propose one novel research question that arises from your model.

Ensure your response demonstrates a deep understanding of semantic representation, cognitive science principles, and AI techniques. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response as follows:

Model Design:
[Your model design description]

Cognitive Science Principles:
[Your discussion of cognitive science principles]

Implementation and AI Integration:
[Your implementation and AI integration description]

Application Analysis:
[Your application analysis]

Limitations and Future Directions:
[Your discussion of limitations and future directions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the domain of {t['domain']} and incorporates the constraint of {t['constraint']}.",
            f"The model's application to {t['application']} is thoroughly analyzed.",
            "The semantic space model design is novel, coherent, and scientifically plausible.",
            "The response demonstrates a deep understanding of semantic representation, cognitive science, and AI techniques.",
            "All five sections (Model Design, Cognitive Science Principles, Implementation and AI Integration, Application Analysis, Limitations and Future Directions) are adequately addressed.",
            "The response is creative while maintaining scientific accuracy and interdisciplinary coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
