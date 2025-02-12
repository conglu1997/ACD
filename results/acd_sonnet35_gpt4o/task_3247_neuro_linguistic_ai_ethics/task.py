import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "Broca's area",
                "linguistic_feature": "Syntax processing",
                "ai_application": "Automated content moderation",
                "ethical_framework": "Utilitarianism"
            },
            {
                "brain_region": "Wernicke's area",
                "linguistic_feature": "Semantic processing",
                "ai_application": "Mental health chatbots",
                "ethical_framework": "Virtue ethics"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics human language processing based on neuroscientific principles, focusing on {t['brain_region']} and its role in {t['linguistic_feature']}. Then, analyze the ethical implications of using this system in {t['ai_application']}, applying the framework of {t['ethical_framework']}. Your response should include:

1. Neuroscientific Basis (250-300 words):
   a) Explain the function of {t['brain_region']} in human language processing.
   b) Describe how {t['linguistic_feature']} is processed in this brain region.
   c) Discuss any relevant neuroscientific theories or models related to this process.

2. AI System Design (300-350 words):
   a) Propose an AI architecture that mimics the function of {t['brain_region']}.
   b) Explain how your system models {t['linguistic_feature']} based on neuroscientific principles.
   c) Describe the key components and processes of your AI system.
   d) Discuss any novel techniques or approaches used in your design.

3. Implementation in {t['ai_application']} (200-250 words):
   a) Explain how your AI system would be applied in the context of {t['ai_application']}.
   b) Describe the potential benefits and challenges of using this system in this application.
   c) Discuss how the system's neuroscientific basis might enhance its performance or capabilities.

4. Ethical Analysis (250-300 words):
   a) Apply the framework of {t['ethical_framework']} to analyze the ethical implications of using your AI system in {t['ai_application']}.
   b) Identify potential ethical concerns or dilemmas that may arise.
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Discuss any potential conflicts between neuroscientific accuracy and ethical considerations.

5. Comparative Analysis (150-200 words):
   a) Compare your neuroscience-based AI approach to traditional NLP methods.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose a hypothetical experiment to evaluate the effectiveness of your system compared to existing technologies.

6. Future Implications (150-200 words):
   a) Discuss the potential long-term impacts of neuroscience-inspired AI on language processing technologies.
   b) Explore how this approach might influence our understanding of human cognition and language.
   c) Propose a novel research direction that combines neuroscience, AI, and ethics in language processing.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, linguistics, and ethical philosophy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical considerations.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified brain region and its role in language processing",
            "The AI system design effectively mimics the neuroscientific principles of the given brain region",
            "The implementation in the specified AI application is well-explained and plausible",
            "The ethical analysis applies the given framework thoroughly and identifies relevant concerns",
            "The comparative analysis provides insightful comparisons with traditional NLP methods",
            "The discussion of future implications is thoughtful and proposes novel research directions",
            "The response shows creativity and innovation while maintaining scientific plausibility",
            "The writing is clear, well-structured, and uses appropriate technical terminology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
