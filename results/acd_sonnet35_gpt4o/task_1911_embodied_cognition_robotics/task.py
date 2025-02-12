import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Sensorimotor Coupling",
            "Situated Action",
            "Affordance-Based Design",
            "Enactive Perception",
            "Extended Mind",
            "Distributed Cognition"
        ]
        robotic_applications = [
            "Search and Rescue Operations",
            "Assistive Technologies for the Elderly",
            "Environmental Monitoring and Conservation",
            "Autonomous Exploration of Extreme Environments",
            "Human-Robot Collaboration in Manufacturing",
            "Adaptive Prosthetics and Orthotics"
        ]
        
        tasks = [
            {
                "principle1": random.choice(cognitive_principles),
                "principle2": random.choice(cognitive_principles),
                "application": random.choice(robotic_applications)
            },
            {
                "principle1": random.choice(cognitive_principles),
                "principle2": random.choice(cognitive_principles),
                "application": random.choice(robotic_applications)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a robotic system based on the principles of {t['principle1']} and {t['principle2']} from embodied cognition theory, applied to the domain of {t['application']}. Then, propose experiments to test its cognitive capabilities. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen principles of embodied cognition and their relevance to robotics.
   b) Describe how these principles could enhance robotic performance in the given application.
   c) Discuss potential challenges in implementing these principles in a robotic system.

2. Robotic System Design (300-350 words):
   a) Propose a detailed design for a robotic system that incorporates the chosen embodied cognition principles.
   b) Describe the key components and their functions, including sensors, actuators, and processing units.
   c) Explain how the design embodies the chosen cognitive principles and addresses the specific requirements of the application domain.
   d) Include a diagram or schematic representation of your robotic system design.
   e) Discuss any novel or unconventional features of your design.

3. Cognitive Architecture (200-250 words):
   a) Describe the cognitive architecture of your robotic system.
   b) Explain how it implements the chosen embodied cognition principles.
   c) Discuss how the architecture supports decision-making and learning in the given application.

4. Experimental Design (250-300 words):
   a) Propose two experiments to test the cognitive capabilities of your robotic system.
   b) For each experiment, describe the setup, methodology, and expected outcomes.
   c) Explain how these experiments would demonstrate the advantages of your embodied cognition-based design.
   d) Discuss potential challenges in conducting these experiments and how you would address them.

5. Limitations and Ethical Considerations (150-200 words):
   a) Discuss potential limitations or drawbacks of your proposed design.
   b) Analyze any ethical implications of implementing your robotic system in the given application.
   c) Propose guidelines for responsible development and use of embodied cognition-based robotic systems.

6. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your design for the fields of robotics and cognitive science.
   b) Propose two potential future research directions or applications that could build on your work.
   c) Speculate on how this approach might influence our understanding of human cognition.

Ensure your response demonstrates a deep understanding of embodied cognition, robotics, and experimental design. Be creative in your approach while maintaining scientific accuracy and plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and include your diagram or schematic in the Robotic System Design section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the chosen embodied cognition principles and their relevance to robotics.",
            "The robotic system design is innovative, detailed, and effectively incorporates the embodied cognition principles.",
            "A clear and relevant diagram or schematic of the robotic system is included.",
            "The cognitive architecture is well-explained and clearly implements the chosen principles.",
            "The proposed experiments are well-designed and would effectively test the system's cognitive capabilities.",
            "Potential limitations and ethical considerations are thoroughly discussed.",
            "The implications and future directions show insightful thinking about the broader impact of the work.",
            "The response is well-structured, clear, and adheres to the specified format and word count.",
            "The ideas presented are creative while maintaining scientific plausibility and accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
