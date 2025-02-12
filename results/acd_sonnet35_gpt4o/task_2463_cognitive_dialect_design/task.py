import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_skills = [
            {
                "skill": "Analogical reasoning",
                "domain": "Scientific discovery",
                "challenge": "Identifying cross-disciplinary connections"
            },
            {
                "skill": "Spatial-temporal reasoning",
                "domain": "Urban planning",
                "challenge": "Optimizing future city layouts"
            },
            {
                "skill": "Counterfactual thinking",
                "domain": "Strategic decision-making",
                "challenge": "Evaluating potential outcomes of policy decisions"
            }
        ]
        return {str(i+1): skill for i, skill in enumerate(random.sample(cognitive_skills, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized 'cognitive dialect' to enhance {t['skill']} in the domain of {t['domain']}, specifically addressing the challenge of {t['challenge']}. Your response should include the following sections:

1. Dialect Overview (200-250 words):
   a) Describe the key features of your cognitive dialect, including its basic structure and unique elements.
   b) Explain how these features are specifically designed to enhance {t['skill']}.
   c) Provide 2-3 example phrases or sentences in your dialect with their English translations and explanations of how they support the target cognitive skill.

2. Cognitive Enhancement Mechanism (250-300 words):
   a) Explain the theoretical basis for how your dialect enhances {t['skill']}.
   b) Describe the specific cognitive processes your dialect aims to optimize or modify.
   c) Discuss how the dialect's features interact with neural pathways or cognitive architectures to produce the desired enhancement.

3. Application in {t['domain']} (200-250 words):
   a) Illustrate how your cognitive dialect would be applied to address the challenge of {t['challenge']}.
   b) Provide a specific scenario in {t['domain']} where using this dialect could lead to improved outcomes.
   c) Discuss any potential limitations or drawbacks of using your dialect in this context.

4. AI Integration (200-250 words):
   a) Describe how an AI system could be designed or trained to utilize this cognitive dialect.
   b) Explain any modifications needed to adapt the dialect for AI use.
   c) Discuss potential advantages or challenges of AI systems using this dialect compared to humans.

5. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to enhancing specific cognitive abilities through linguistic means.
   b) Discuss the broader societal implications if this cognitive dialect were to become widely adopted.
   c) Propose guidelines for responsible development and use of cognitive dialects.

6. Experimental Validation (150-200 words):
   a) Design an experiment to test the effectiveness of your cognitive dialect in enhancing {t['skill']}.
   b) Describe the methodology, including control groups and measurable outcomes.
   c) Discuss potential challenges in validating the effects of the dialect and how you would address them.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your dialect design while maintaining scientific plausibility and logical consistency. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence",
            "The cognitive dialect design is creative, well-described, and plausibly linked to enhancing the specified cognitive skill",
            "The application of the dialect to the given domain and challenge is logical and well-explained",
            "The AI integration section provides insightful analysis of how the dialect could be used by AI systems",
            "The ethical and societal implications are thoughtfully considered",
            "The experimental validation proposal is well-designed and addresses potential challenges",
            "The response is well-structured and adheres to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
