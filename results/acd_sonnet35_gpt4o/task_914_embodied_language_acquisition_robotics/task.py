import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        embodiment_types = [
            "Humanoid robot with articulated limbs and sensory inputs",
            "Wheeled robot with manipulator arms and advanced visual processing",
            "Soft robotics system with distributed tactile sensors",
            "Aerial drone with multi-modal sensory array"
        ]
        
        linguistic_challenges = [
            "Acquisition of spatial prepositions and motion verbs",
            "Development of conceptual metaphors based on physical experiences",
            "Learning of deictic expressions and perspective-taking",
            "Grounding of abstract concepts in sensorimotor experiences"
        ]
        
        return {
            "1": {
                "embodiment": random.choice(embodiment_types),
                "challenge": random.choice(linguistic_challenges)
            },
            "2": {
                "embodiment": random.choice(embodiment_types),
                "challenge": random.choice(linguistic_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a robotic system capable of acquiring language through embodied experiences, focusing on the following specifications:

Embodiment Type: {t['embodiment']}
Linguistic Challenge: {t['challenge']}

Note: Embodied cognition is the theory that many features of cognition are shaped by aspects of the entire body of the organism. In the context of this task, consider how the physical experiences and interactions of the robot influence its language acquisition and understanding.

Your response should include:

1. System Design (250-300 words):
   a) Describe the key components and architecture of your robotic system.
   b) Explain how the system's embodiment supports language acquisition.
   c) Detail the sensory inputs and motor outputs relevant to the linguistic challenge.

2. Language Acquisition Model (200-250 words):
   a) Propose a cognitive model for embodied language acquisition in your system.
   b) Explain how this model addresses the specific linguistic challenge.
   c) Discuss how your model integrates theories of embodied cognition and developmental linguistics.

3. Learning Process (200-250 words):
   a) Describe the step-by-step process by which your system would acquire language.
   b) Provide a specific example of how it would learn a relevant linguistic concept.
   c) Explain how the system's embodied experiences contribute to its understanding of language.

4. Evaluation Methods (150-200 words):
   a) Propose a method to evaluate the system's language acquisition progress.
   b) Describe potential metrics or benchmarks for success.
   c) Discuss how you would compare the system's performance to human language acquisition.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of creating robots with advanced language capabilities.
   b) Explore the philosophical implications of embodied language acquisition in AI systems.
   c) Consider potential societal impacts of this technology.

6. Future Research Directions (100-150 words):
   a) Suggest two areas for further research that could enhance your system.
   b) Briefly explain how these advancements could contribute to our understanding of language and cognition.

Ensure your response demonstrates a deep understanding of robotics, linguistics, and cognitive science. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section.

Your entire response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of robotics, linguistics, and cognitive science.",
            "The system design is creative, plausible, and well-suited to the given embodiment type and linguistic challenge.",
            "The language acquisition model effectively integrates theories of embodied cognition and developmental linguistics.",
            "The learning process is clearly explained with a specific, relevant example.",
            "The evaluation methods are appropriate and well-reasoned.",
            "Ethical and philosophical implications are thoughtfully considered.",
            "Future research directions are insightful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
