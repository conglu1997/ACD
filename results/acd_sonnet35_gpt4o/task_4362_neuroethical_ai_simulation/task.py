import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "prefrontal cortex",
            "anterior cingulate cortex",
            "amygdala"
        ]
        ethical_frameworks = [
            "utilitarianism",
            "deontology",
            "virtue ethics"
        ]
        moral_dilemmas = [
            "trolley problem",
            "organ transplant dilemma",
            "AI rights and personhood"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "ethical_framework": random.choice(ethical_frameworks),
                "moral_dilemma": random.choice(moral_dilemmas)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "ethical_framework": random.choice(ethical_frameworks),
                "moral_dilemma": random.choice(moral_dilemmas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system that simulates complex ethical decision-making processes based on human neuroscience, then apply it to a challenging moral dilemma. Your system should focus on the brain region {t['brain_region']}, incorporate the ethical framework of {t['ethical_framework']}, and be applied to the moral dilemma of {t['moral_dilemma']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your neuroethical AI system.
   b) Explain how it incorporates the specified brain region's function into its decision-making process.
   c) Detail how the chosen ethical framework is implemented in the AI's reasoning.
   d) Discuss any novel approaches you've incorporated to enhance the system's ethical reasoning capabilities.

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the specified brain region in human ethical decision-making.
   b) Describe how your AI system models or emulates this brain region's function.
   c) Discuss any simplifications or abstractions made in translating neuroscience to AI.
   d) Address potential limitations in our current understanding of the brain's role in moral reasoning.

3. Ethical Framework Implementation (250-300 words):
   a) Describe how the specified ethical framework is encoded into your AI system.
   b) Explain how this framework interacts with the neuroscience-based components.
   c) Discuss any challenges in translating philosophical ethical theories into computational models.
   d) Propose a method for validating the AI's adherence to the chosen ethical framework.

4. Application to Moral Dilemma (300-350 words):
   a) Briefly describe the specified moral dilemma.
   b) Explain how your AI system processes and analyzes this dilemma.
   c) Provide the AI's decision or recommendation for the dilemma, with a detailed explanation of its reasoning process.
   d) Compare the AI's decision to typical human responses to this dilemma, highlighting similarities and differences.

5. Implications and Limitations (200-250 words):
   a) Discuss the potential implications of using such an AI system for real-world ethical decision-making.
   b) Analyze the limitations and potential biases of your approach.
   c) Explore the ethical considerations of developing AI systems that make moral judgments.
   d) Propose guidelines for the responsible development and use of neuroethical AI systems.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions of your system.
   b) Discuss how advancements in neuroscience or AI could enhance neuroethical AI systems in the future.
   c) Propose a novel application of your system beyond ethical decision-making.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and ethical philosophy.",
            "The proposed AI system effectively incorporates the specified brain region and ethical framework.",
            "The application to the moral dilemma is thorough and well-reasoned.",
            "The response addresses all required sections and stays within the specified word count range.",
            "The ideas presented are innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
