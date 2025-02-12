import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'Working Memory',
            'Attention',
            'Decision Making',
            'Emotional Processing',
            'Pattern Recognition'
        ]
        brain_regions = [
            'Prefrontal Cortex',
            'Amygdala',
            'Hippocampus',
            'Visual Cortex',
            'Basal Ganglia'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'cognitive_process': random.choice(cognitive_processes),
                'brain_region': random.choice(brain_regions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates abstract art based on the neurocognitive process of {t['cognitive_process']} and activity patterns in the {t['brain_region']}. Then, analyze its artistic and scientific implications. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system models the specified cognitive process and brain activity patterns.
   c) Detail how your system translates neurocognitive data into visual artistic elements.
   d) Propose a novel feature that enhances the system's ability to generate meaningful abstract art.

2. Neurocognitive-Artistic Mapping (200-250 words):
   a) Explain how specific aspects of {t['cognitive_process']} are represented in the generated art.
   b) Describe how activity patterns in the {t['brain_region']} influence the artistic output.
   c) Discuss any challenges in translating neurocognitive processes into visual art and how your system addresses them.

3. Art Generation Process (200-250 words):
   a) Outline the step-by-step process your AI uses to create an abstract artwork.
   b) Explain how your algorithm balances neuroscientific accuracy with artistic creativity.
   c) Describe how your system ensures aesthetic quality and coherence in the generated art.

4. Sample Artwork Analysis (200-250 words):
   a) Provide a detailed description of an abstract artwork that your AI might generate.
   b) Analyze how specific elements of this artwork relate to the cognitive process and brain region involved.
   c) Discuss the potential artistic merit and neuroscientific insights of this generated piece.

5. Evaluation and Interpretation (150-200 words):
   a) Propose methods for evaluating both the scientific accuracy and artistic quality of the generated artworks.
   b) Describe how you would use these evaluations to refine and improve your AI system.
   c) Discuss potential applications of this system in both neuroscience research and the art world.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss ethical considerations related to using AI to create art based on human cognitive processes.
   b) Explore philosophical questions about creativity, consciousness, and the nature of art that this system might raise.
   c) Propose guidelines for the responsible development and use of neurocognitive art-generating AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and artistic integrity.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory.",
            f"The system effectively incorporates the cognitive process of {t['cognitive_process']} and activity patterns in the {t['brain_region']}.",
            "The proposed AI system presents a novel and plausible approach to generating abstract art based on neurocognitive processes.",
            "The sample artwork analysis shows a clear connection between the generated art and the specified cognitive process and brain region.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
