import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "bias": "Confirmation Bias",
                "policy_area": "Environmental Policy",
                "target_audience": "General Public"
            },
            {
                "bias": "Availability Heuristic",
                "policy_area": "Public Health",
                "target_audience": "Policymakers"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates human language affected by cognitive biases into more objective language, and vice versa. Then, apply this system to analyze and rewrite policy documents. Focus on the {t['bias']} in the context of {t['policy_area']}, targeting {t['target_audience']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for bias translation.
   b) Explain how your system identifies and quantifies the specified cognitive bias in text.
   c) Detail the mechanisms for translating biased language to objective language and vice versa.
   d) Discuss how your system adapts to different policy areas and target audiences.
   e) Include a simple diagram of your system architecture (described in text).

2. Cognitive Bias Analysis (250-300 words):
   a) Provide a detailed explanation of the specified cognitive bias and its effects on decision-making.
   b) Describe how this bias typically manifests in language, particularly in policy documents.
   c) Explain how your system distinguishes between biased language and field-specific jargon or technical terms.
   d) Discuss any challenges in quantifying or measuring the degree of bias in text.

3. Language Translation Process (250-300 words):
   a) Describe the step-by-step process your system uses to translate biased language to objective language.
   b) Explain how your system ensures that the core message is preserved during translation.
   c) Discuss how your system handles context-dependent biases or ambiguities.
   d) Provide a specific example of how your system would translate a biased statement in the given policy area.

4. Policy Document Analysis and Rewriting (300-350 words):
   a) Outline the process for analyzing a policy document using your AI system.
   b) Explain how your system identifies sections of the document that may be influenced by the specified bias.
   c) Describe how your system would rewrite these sections to be more objective.
   d) Discuss how your system balances objectivity with the need for persuasive language in policy documents.
   e) Provide a brief example of an original policy statement and its AI-rewritten version.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss the ethical implications of using AI to 'debias' human language.
   b) Address potential concerns about AI systems influencing public policy.
   c) Explain how your system might handle conflicting biases or ideological differences.
   d) Discuss the limitations of your approach and potential unintended consequences.

6. Practical Applications and Future Directions (200-250 words):
   a) Propose three potential applications of your system beyond policy document analysis.
   b) Discuss how this technology could be used to improve decision-making processes.
   c) Suggest how your system could be expanded to handle multiple cognitive biases simultaneously.
   d) Propose a research agenda for further developing and refining cognitive bias translation systems.

Ensure your response demonstrates a deep understanding of cognitive science, natural language processing, and public policy analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified cognitive bias and its impact on language and decision-making.",
            "The AI system design is well-structured, with clear explanations of components and mechanisms for bias identification and language translation.",
            "The language translation process is clearly explained, with consideration for preserving core messages and handling context-dependent biases.",
            "The policy document analysis and rewriting process is thoroughly described, with a balance between objectivity and persuasive language.",
            "Ethical considerations and limitations of the approach are thoughtfully discussed.",
            "Practical applications and future directions are innovative and well-reasoned.",
            "The response shows creativity and interdisciplinary knowledge integration throughout.",
            "The submission adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
