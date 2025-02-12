import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Coral reef ecosystem",
                "disaster_type": "Oil spill",
                "swarm_behavior": "Self-assembly",
                "monitoring_focus": "Water quality"
            },
            {
                "environment": "Amazon rainforest",
                "disaster_type": "Wildfire",
                "swarm_behavior": "Stigmergy",
                "monitoring_focus": "Biodiversity"
            },
            {
                "environment": "Arctic tundra",
                "disaster_type": "Permafrost thaw",
                "swarm_behavior": "Flocking",
                "monitoring_focus": "Greenhouse gas emissions"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a swarm robotics system for environmental monitoring and disaster response in the {t['environment']}, focusing on {t['monitoring_focus']} and addressing the potential disaster of {t['disaster_type']}. Your system should incorporate the swarm behavior of {t['swarm_behavior']}. Provide your response in the following format:

1. Swarm Robot Design (250-300 words):
   a) Describe the physical characteristics and capabilities of individual robots in your swarm.
   b) Explain how the robots are adapted to operate in the {t['environment']}.
   c) Detail the sensors and instruments used for {t['monitoring_focus']}.
   d) Discuss how the robots are designed to respond to {t['disaster_type']}.

2. Swarm Behavior and Intelligence (250-300 words):
   a) Explain how you implement {t['swarm_behavior']} in your system.
   b) Describe the algorithms or rules governing the swarm's collective behavior.
   c) Discuss how the swarm coordinates to achieve its monitoring and disaster response goals.
   d) Explain how the swarm adapts to changing environmental conditions or emergencies.

3. Environmental Monitoring System (200-250 words):
   a) Detail how your swarm collects and processes data related to {t['monitoring_focus']}.
   b) Explain how the system integrates data from multiple robots to create a comprehensive environmental assessment.
   c) Describe any machine learning or AI techniques used for data analysis and pattern recognition.

4. Disaster Response Capabilities (200-250 words):
   a) Explain how your swarm detects and responds to the onset of {t['disaster_type']}.
   b) Describe specific actions the swarm takes to mitigate the disaster's impact.
   c) Discuss how the swarm communicates with human responders or other systems during a crisis.

5. Ethical and Environmental Considerations (150-200 words):
   a) Discuss potential ecological impacts of deploying your robotic swarm in the {t['environment']}.
   b) Address privacy and security concerns related to environmental monitoring.
   c) Propose guidelines for responsible development and deployment of swarm robotics in sensitive ecosystems.

6. Scalability and Future Developments (150-200 words):
   a) Explain how your system could be scaled up or adapted for use in different environments.
   b) Propose two potential improvements or extensions to your swarm robotics system.
   c) Discuss how this technology might evolve to address future environmental challenges.

Ensure your response demonstrates a deep understanding of robotics, swarm intelligence, environmental science, and disaster management. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all six required sections with appropriate content for the {t['environment']} scenario",
            f"The swarm robotics system effectively integrates {t['swarm_behavior']} behavior for environmental monitoring and disaster response",
            f"The system demonstrates innovative approaches to monitoring {t['monitoring_focus']} and responding to {t['disaster_type']}",
            "The response shows a deep understanding of robotics, swarm intelligence, environmental science, and disaster management",
            "The ethical and environmental considerations are thoughtfully addressed",
            "The proposed system is scientifically plausible and practically feasible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
