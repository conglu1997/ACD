import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_abilities = [
            "Memory enhancement",
            "Attention regulation",
            "Emotional processing",
            "Decision-making speed"
        ]
        ethical_concerns = [
            "Privacy and data security",
            "Cognitive liberty and autonomy",
            "Social inequality and access",
            "Identity and authenticity"
        ]
        tasks = [
            {
                "cognitive_ability": ca,
                "ethical_concern": ec
            }
            for ca in cognitive_abilities
            for ec in ethical_concerns
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for a brain-computer interface (BCI) that enhances the cognitive ability of {t['cognitive_ability']} while addressing the ethical concern of {t['ethical_concern']}. Your task is to create a comprehensive proposal that integrates neuroscience, artificial intelligence, and ethical considerations. Provide your response in the following format:

1. BCI-AI System Architecture (300-350 words):
   a) Describe the key components of your BCI-AI system, including both hardware and software elements.
   b) Explain how your system interfaces with the brain to enhance {t['cognitive_ability']}.
   c) Detail the AI algorithms and techniques used to process neural signals and provide cognitive enhancement.
   d) Discuss how your system addresses the ethical concern of {t['ethical_concern']} in its design and implementation.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neurological mechanisms involved in {t['cognitive_ability']}.
   b) Describe how your BCI-AI system interacts with these mechanisms to enhance cognitive function.
   c) Discuss potential neuroplasticity considerations and long-term effects of using your system.

3. AI and Machine Learning Approach (250-300 words):
   a) Detail the specific AI and machine learning techniques used in your system.
   b) Explain how these techniques adapt to individual users and optimize cognitive enhancement.
   c) Discuss any novel AI approaches you've developed for this application.

4. Ethical Framework and Safeguards (250-300 words):
   a) Propose a comprehensive ethical framework for the development and use of your BCI-AI system.
   b) Explain how your system specifically addresses the ethical concern of {t['ethical_concern']}.
   c) Describe technical and policy safeguards implemented to protect users and society.

5. Societal Impact Analysis (200-250 words):
   a) Analyze potential positive and negative societal impacts of widespread adoption of your BCI-AI system.
   b) Discuss how your system might affect social dynamics, education, work, and healthcare.
   c) Propose strategies to mitigate negative impacts and promote equitable access.

6. Future Research and Development (150-200 words):
   a) Identify key challenges and limitations in your current system design.
   b) Propose future research directions to address these challenges.
   c) Speculate on potential long-term developments in BCI-AI symbiosis technology.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and bioethics",
            f"The proposed BCI-AI system effectively addresses the enhancement of {t['cognitive_ability']}",
            f"The ethical concern of {t['ethical_concern']} is thoroughly addressed in the system design and ethical framework",
            "The response provides innovative yet scientifically plausible solutions",
            "The societal impact analysis is comprehensive and balanced"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
