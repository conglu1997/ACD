import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            'social interactions',
            'spatial navigation',
            'problem-solving strategies',
            'emotional regulation',
            'decision-making processes'
        ]
        example_schemas = {
            'social interactions': ['greeting', 'conflict resolution', 'cooperation'],
            'spatial navigation': ['landmark recognition', 'path integration', 'cognitive mapping'],
            'problem-solving strategies': ['divide and conquer', 'trial and error', 'analogical reasoning'],
            'emotional regulation': ['reappraisal', 'suppression', 'mindfulness'],
            'decision-making processes': ['risk assessment', 'cost-benefit analysis', 'heuristic-based decision making']
        }
        tasks = {}
        for i in range(2):
            domain = random.choice(domains)
            tasks[str(i+1)] = {
                'domain': domain,
                'example_schemas': example_schemas[domain]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model architecture that incorporates cognitive schemas, implement it for the domain of {t['domain']}, and analyze its performance on schema-related tasks. Your response should include the following sections:

1. Cognitive Schema Theory (200-250 words):
   a) Explain the concept of cognitive schemas and their role in human cognition.
   b) Discuss how schemas relate to knowledge representation and processing in the brain.
   c) Describe how schemas specifically function in the domain of {t['domain']}.

2. Language Model Architecture (250-300 words):
   a) Design a novel language model architecture that incorporates cognitive schemas.
   b) Explain how your model represents and utilizes schemas in its processing.
   c) Describe any modifications to traditional language model components (e.g., attention mechanisms, embeddings) to accommodate schemas.
   d) Discuss how your model might handle schema activation, modification, and creation.

3. Implementation for {t['domain']} (200-250 words):
   a) Describe how you would implement your schema-based language model for the specific domain of {t['domain']}.
   b) Provide examples of schemas relevant to this domain (including but not limited to {', '.join(t['example_schemas'])}) and how they would be represented in your model.
   c) Explain any domain-specific challenges and how your model addresses them.

4. Task Performance Analysis (200-250 words):
   a) Propose three specific tasks related to {t['domain']} that would test your model's schema-based capabilities.
   b) Predict how your model would perform on these tasks compared to traditional language models.
   c) Describe potential metrics for evaluating schema-related performance.

5. Cognitive Implications (150-200 words):
   a) Discuss how your schema-based language model might inform our understanding of human cognition.
   b) Explore potential insights into the nature of knowledge representation and processing.
   c) Consider implications for theories of language understanding and generation in humans.

6. Ethical Considerations and Limitations (100-150 words):
   a) Identify potential ethical concerns or limitations of implementing cognitive schemas in AI systems.
   b) Discuss any biases that might arise from schema-based processing and how to mitigate them.
   c) Propose guidelines for the responsible development and use of schema-based language models.

Ensure your response demonstrates a deep understanding of cognitive science, language models, and the specific domain of {t['domain']}. Be creative in your approach while maintaining scientific plausibility and logical consistency. Use appropriate terminology and provide clear explanations throughout your response.

Format your response with clear headings for each section and adhere to the specified word counts. Your total response should be between 1100-1400 words. Include a word count at the end of your submission.

Note: Do not provide a direct implementation or solution. Instead, focus on describing the conceptual design, potential approaches, and analysis of the proposed model."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive schema theory and its application to language models.",
            "The proposed language model architecture is novel, well-explained, and plausibly incorporates cognitive schemas.",
            f"The implementation for the domain of {t['domain']} is detailed and domain-appropriate, including relevant examples of schemas such as {', '.join(t['example_schemas'])}.",
            "The task performance analysis includes three relevant and challenging tasks with thoughtful predictions and appropriate evaluation metrics.",
            "The discussion of cognitive implications shows insight into human cognition and knowledge representation.",
            "Ethical considerations and limitations are thoughtfully addressed, including potential biases and mitigation strategies.",
            "The response is creative while maintaining scientific plausibility and logical consistency.",
            "The response adheres to the specified format and word count guidelines (1100-1400 words).",
            "The response does not provide a direct implementation or solution, but focuses on conceptual design and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
