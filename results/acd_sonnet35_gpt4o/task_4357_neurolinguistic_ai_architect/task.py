import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                'region': 'Broca\'s area',
                'function': 'speech production and language processing',
                'ai_focus': 'natural language generation',
                'case_study': 'Develop an AI system to assist individuals with expressive aphasia in producing coherent speech.'
            },
            {
                'region': 'Wernicke\'s area',
                'function': 'language comprehension',
                'ai_focus': 'natural language understanding',
                'case_study': 'Create an AI system to help simultaneous interpreters better understand and process complex, technical language in real-time.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(brain_regions)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural-inspired AI system for language processing based on {t['region']} ({t['function']}), focusing on {t['ai_focus']}. Then, analyze its potential for enhancing human-AI communication. Use the following case study as a concrete example for your system: {t['case_study']}

Your response should include:

1. Neuroscientific Foundation (250-300 words):
   a) Explain the key functions and neural architecture of {t['region']}.
   b) Describe how this brain region processes language information.
   c) Discuss any relevant neuroscientific theories or models related to this region's role in language.

2. AI System Architecture (300-350 words):
   a) Design an AI architecture inspired by the neural structure and function of {t['region']}.
   b) Explain how your AI system mimics or improves upon the brain's approach to {t['ai_focus']}.
   c) Describe the key components of your system and their interactions.
   d) Discuss any novel features that distinguish your design from traditional language AI models.

3. Implementation and Training (200-250 words):
   a) Outline the data requirements and preprocessing steps for training your AI system.
   b) Describe the training process, including any neuroscience-inspired learning algorithms.
   c) Explain how you would evaluate the system's performance in {t['ai_focus']}.

4. Human-AI Communication Enhancement (250-300 words):
   a) Analyze how your neural-inspired AI system could improve human-AI communication, specifically in the context of the given case study.
   b) Provide specific examples of how it might outperform current language models in certain tasks related to the case study.
   c) Discuss potential applications in fields such as education, healthcare, or human-computer interaction.

5. Limitations and Ethical Considerations (200-250 words):
   a) Identify potential limitations or challenges of your neural-inspired approach.
   b) Discuss ethical implications of developing AI systems that closely mimic human brain functions, particularly in the context of the case study.
   c) Propose guidelines for responsible development and use of neuroscience-inspired AI language systems.

6. Future Research Directions (150-200 words):
   a) Suggest areas for further research in combining neuroscience and AI for language processing.
   b) Discuss how advancements in brain-computer interfaces might impact the development of such systems.
   c) Propose an experiment to further validate or improve your neural-inspired AI system, specifically addressing the needs outlined in the case study.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the neuroscientific basis of {t['region']} and its role in {t['function']}.",
            f"The AI system architecture is clearly inspired by the neural structure and function of {t['region']} and focuses on {t['ai_focus']}.",
            "The implementation and training process is well-described and incorporates neuroscience-inspired elements.",
            f"The analysis of human-AI communication enhancement is thorough and provides specific, plausible examples related to the case study: {t['case_study']}",
            "The response addresses limitations, ethical considerations, and future research directions in a thoughtful manner, particularly in the context of the given case study.",
            "The overall response is creative, scientifically plausible, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
