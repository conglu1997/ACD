import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = ['Ant Colony', 'Bee Hive', 'Fish School', 'Bird Flock', 'Slime Mold']
        urban_problems = ['Traffic Congestion', 'Waste Management', 'Energy Distribution', 'Emergency Response', 'Public Transportation']
        swarm_behaviors = ['Foraging', 'Path Finding', 'Task Allocation', 'Consensus Decision-Making', 'Adaptive Self-Organization']
        
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "urban_problem": random.choice(urban_problems),
                "swarm_behavior": random.choice(swarm_behaviors)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "urban_problem": random.choice(urban_problems),
                "swarm_behavior": random.choice(swarm_behaviors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic swarm intelligence system inspired by the collective behavior of {t['biological_system']}, focusing on the specific behavior of {t['swarm_behavior']}. Then, apply this system to solve the urban planning problem of {t['urban_problem']}. Your response should include the following sections:

1. Biological System Analysis (250-300 words):
   a) Describe the key characteristics and mechanisms of the chosen biological system.
   b) Explain how the specific swarm behavior functions in nature.
   c) Discuss the evolutionary advantages of this behavior for the biological system.

2. Biomimetic Swarm Intelligence Design (300-350 words):
   a) Outline the architecture of your swarm intelligence system.
   b) Explain how you translate the biological mechanisms into algorithmic and robotic components.
   c) Describe the communication and decision-making processes in your system.
   d) Provide a simple pseudocode or algorithmic representation of a key component in your system (50-100 words).
   e) Discuss how your design maintains the key advantages of the biological system while adapting to an artificial context.

3. Urban Problem Application (250-300 words):
   a) Analyze the chosen urban planning problem and its current challenges.
   b) Explain how your biomimetic swarm intelligence system addresses this problem.
   c) Provide a specific scenario demonstrating your system in action.
   d) Compare your biomimetic approach to a traditional AI approach for solving this urban planning problem.
   e) Discuss potential advantages and limitations of your approach.

4. Implementation and Scaling (200-250 words):
   a) Describe the physical or virtual components needed to implement your system.
   b) Explain how your system would be deployed and integrated into existing urban infrastructure.
   c) Discuss challenges in scaling your system to city-wide implementation and propose solutions.

5. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical concerns or unintended consequences of implementing your system.
   b) Discuss how these issues might be addressed or mitigated.
   c) Analyze the potential long-term impact of your system on urban development and society.

6. Future Research Directions (150-200 words):
   a) Propose two areas for further research to enhance your biomimetic swarm intelligence system.
   b) Explain how these research directions could address current limitations or expand the system's capabilities.
   c) Speculate on potential applications of your system beyond urban planning.

Ensure your response demonstrates a deep understanding of swarm intelligence, the chosen biological system, urban planning, and robotics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Adhere strictly to the word limits provided for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['biological_system']} system and its {t['swarm_behavior']} behavior.",
            f"The biomimetic swarm intelligence system design effectively translates biological mechanisms into algorithmic and robotic components, including a clear pseudocode or algorithmic representation.",
            f"The application to the urban planning problem of {t['urban_problem']} is well-explained, plausible, and compared to a traditional AI approach.",
            "The response addresses implementation, scaling, ethical implications, and future research directions comprehensively, including potential limitations.",
            "The submission demonstrates creativity and interdisciplinary knowledge integration while maintaining scientific plausibility.",
            "The response adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
