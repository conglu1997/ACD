import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'animal_species': 'Leafcutter ants',
                'environmental_challenge': 'Reforestation of degraded landscapes',
                'target_environment': 'Tropical rainforest'
            },
            '2': {
                'animal_species': 'Humpback whales',
                'environmental_challenge': 'Ocean plastic pollution cleanup',
                'target_environment': 'Marine ecosystem'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a swarm of biomimetic robots inspired by {t['animal_species']} to address the environmental challenge of {t['environmental_challenge']} in a {t['target_environment']}. Your response should include the following sections:

1. Biological Inspiration (200-250 words):
   a) Describe the key characteristics and behaviors of {t['animal_species']} relevant to the environmental challenge.
   b) Explain how these traits could be adapted for robotic systems.
   c) Discuss any challenges in translating biological features into artificial systems.

2. Robot Design (250-300 words):
   a) Describe the physical design and key components of your biomimetic robots.
   b) Explain the sensory systems and data processing capabilities of individual robots.
   c) Discuss the locomotion and manipulation mechanisms of the robots.
   d) Include a simple diagram or schematic of a single robot unit (use ASCII art or a clear textual description).

3. Swarm Behavior (200-250 words):
   a) Explain the swarm intelligence algorithms or principles used by your robot system.
   b) Describe how individual robots communicate and coordinate their actions.
   c) Discuss how the swarm adapts to changes in the environment or mission parameters.

4. Environmental Solution (200-250 words):
   a) Detail how your robotic swarm would address {t['environmental_challenge']}.
   b) Provide a step-by-step explanation of the swarm's operation in the {t['target_environment']}.
   c) Discuss potential challenges and how your system would overcome them.

5. Ethical and Ecological Considerations (150-200 words):
   a) Analyze potential negative impacts of introducing your robotic swarm into the ecosystem.
   b) Discuss ethical concerns related to biomimicry and environmental intervention.
   c) Propose safeguards or guidelines for responsible deployment of your system.

6. Future Applications (150-200 words):
   a) Suggest two other potential applications for your biomimetic swarm technology.
   b) Briefly describe how the system could be adapted for these new purposes.

Ensure your response demonstrates a deep understanding of biology, robotics, swarm intelligence, and environmental science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words, not including the robot diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the biological inspiration and its relevance to the environmental challenge.",
            "The robot design is innovative, well-explained, and plausibly addresses the environmental challenge.",
            "The swarm behavior is clearly described and demonstrates an understanding of swarm intelligence principles.",
            "The environmental solution is comprehensive and addresses potential challenges.",
            "Ethical and ecological considerations are thoughtfully analyzed.",
            "Future applications are creative and well-justified.",
            "The response maintains a balance between creativity and scientific plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0