import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "embodied cognition",
                "linguistic_focus": "metaphor comprehension",
                "application_domain": "sentiment analysis in social media"
            },
            {
                "cognitive_principle": "conceptual blending",
                "linguistic_focus": "neologism interpretation",
                "application_domain": "automated pun detection"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language model incorporating the cognitive linguistics principle of {t['cognitive_principle']}, focusing on {t['linguistic_focus']}. Then, apply your model to solve a specific problem in {t['application_domain']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen cognitive linguistics principle and its relevance to language understanding.
   b) Describe how this principle relates to the specified linguistic focus.
   c) Discuss potential challenges in implementing this principle in a computational model.

2. Language Model Design (300-350 words):
   a) Propose a detailed design for a language model that incorporates the chosen cognitive principle.
   b) Describe the key components and their functions, including any novel architectural elements.
   c) Explain how the design addresses the specific linguistic focus.
   d) Include a diagram or schematic representation of your language model architecture.
   e) Discuss any innovative features that distinguish your model from traditional approaches.

3. Implementation Details (200-250 words):
   a) Describe the data structures and algorithms central to your model.
   b) Explain how your model would process and represent language input.
   c) Discuss how the model would be trained or calibrated.
   d) Address any computational challenges and how you would overcome them.

4. Application to the Problem Domain (250-300 words):
   a) Explain how your model would be applied to the specified problem in natural language understanding.
   b) Describe the expected advantages of your approach over traditional methods.
   c) Provide a step-by-step example of how your model would process a relevant input.
   d) Discuss potential limitations or edge cases in this application.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the performance of your model in the given application domain.
   b) Describe key metrics and explain why they are appropriate for this task.
   c) Suggest a baseline model or approach for comparison.

6. Broader Implications (150-200 words):
   a) Discuss the potential impact of your model on the fields of linguistics and artificial intelligence.
   b) Explore possible applications of your approach in other areas of natural language processing.
   c) Consider any ethical implications or potential misuses of the technology.

Ensure your response demonstrates a deep understanding of cognitive linguistics, natural language processing, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and include your diagram in the Language Model Design section. Your total response should be between 1300-1600 words, adhering to the word count for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['cognitive_principle']} and its application to {t['linguistic_focus']}.",
            "The language model design is innovative and well-explained, addressing the specified linguistic focus.",
            f"The application to {t['application_domain']} is clearly described and demonstrates potential advantages over traditional methods.",
            "The evaluation methodology is appropriate and well-justified.",
            "The response shows interdisciplinary knowledge integration and creative problem-solving.",
            "The response is well-structured, coherent, and within the specified word count range for each section and overall."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
