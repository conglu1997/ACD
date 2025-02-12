import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        developmental_stages = [
            {
                "stage": "Sensorimotor",
                "age_range": "0-2 years",
                "key_concepts": ["object permanence", "cause-effect relationships", "basic motor skills"]
            },
            {
                "stage": "Preoperational",
                "age_range": "2-7 years",
                "key_concepts": ["symbolic thinking", "egocentrism", "language development"]
            },
            {
                "stage": "Concrete Operational",
                "age_range": "7-11 years",
                "key_concepts": ["logical thinking", "conservation", "classification"]
            },
            {
                "stage": "Formal Operational",
                "age_range": "11+ years",
                "key_concepts": ["abstract reasoning", "hypothetical thinking", "moral reasoning"]
            }
        ]
        return {
            "1": random.choice(developmental_stages),
            "2": random.choice(developmental_stages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive robotic system that simulates human cognitive development during the {t['stage']} stage ({t['age_range']}), focusing on the integration of sensorimotor experiences with abstract concept formation. Your response should include the following sections:

1. Developmental Stage Analysis (200-250 words):
   a) Describe the key characteristics of the {t['stage']} stage of cognitive development.
   b) Explain how children typically acquire and demonstrate the concepts of {', '.join(t['key_concepts'])} during this stage.
   c) Discuss the role of sensorimotor experiences in the development of these concepts.

2. Robotic System Design (300-350 words):
   a) Propose a robotic system architecture that can simulate cognitive development during the {t['stage']} stage.
   b) Describe the key components of your system, including sensors, actuators, and processing units.
   c) Explain how your system integrates sensorimotor experiences with abstract concept formation.
   d) Include a high-level diagram or pseudocode representing your system architecture.

3. Learning and Adaptation Mechanisms (250-300 words):
   a) Describe the learning algorithms or mechanisms your system uses to acquire new concepts and skills.
   b) Explain how your system simulates the development of {', '.join(t['key_concepts'])}.
   c) Discuss how your system adapts its behavior based on interactions with the environment.

4. Evaluation and Benchmarking (200-250 words):
   a) Propose methods to evaluate your system's performance in simulating cognitive development.
   b) Describe specific experiments or tests that could assess the system's acquisition of {', '.join(t['key_concepts'])}.
   c) Discuss how you would compare your system's development to that of human children.

5. Ethical Considerations and Implications (150-200 words):
   a) Discuss potential ethical issues in developing robots that simulate child cognitive development.
   b) Explore the implications of your system for our understanding of human cognition and development.
   c) Consider potential applications and misapplications of this technology.

6. Future Directions (100-150 words):
   a) Propose two potential research directions to extend or improve your cognitive robotic system.
   b) Discuss how your system could be adapted to study or simulate other stages of cognitive development.

Ensure your response demonstrates a deep understanding of cognitive development, robotics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections with appropriate word counts",
            f"The developmental stage analysis accurately describes the {t['stage']} stage and the acquisition of {', '.join(t['key_concepts'])}",
            "The robotic system design is innovative, plausible, and integrates sensorimotor experiences with abstract concept formation",
            "The learning and adaptation mechanisms are well-explained and appropriate for simulating cognitive development",
            "The evaluation and benchmarking methods are specific and relevant to the developmental stage",
            "The response demonstrates a deep understanding of cognitive development, robotics, and artificial intelligence",
            "The ethical considerations are thoughtfully explored and relevant to the proposed system",
            "The future directions proposed are innovative and build upon the presented system"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
