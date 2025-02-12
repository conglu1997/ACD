import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = ['Photosynthesis', 'Termite mounds', 'Spider silk', 'Lotus leaf', 'Whale fin']
        engineering_challenges = ['Energy efficiency', 'Climate control', 'Structural integrity', 'Water management', 'Transportation']
        urban_contexts = ['Skyscrapers', 'Public transportation', 'Green spaces', 'Waste management', 'Urban agriculture']
        
        tasks = {
            "1": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "urban_context": random.choice(urban_contexts)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "urban_context": random.choice(urban_contexts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of biomimicry to solve complex engineering problems, focusing on the biological system of {t['biological_system']}. Then, apply your system to address the engineering challenge of {t['engineering_challenge']} in the context of {t['urban_context']} for sustainable urban development. Your response should include:

1. Biomimetic AI System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they integrate principles from {t['biological_system']}.
   b) Explain how your system analyzes and extracts relevant features from the biological model.
   c) Detail how the AI translates biological principles into engineering solutions.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Biological System Analysis (250-300 words):
   a) Provide an overview of the key features and mechanisms of {t['biological_system']}.
   b) Explain how these features contribute to the system's efficiency or effectiveness in nature.
   c) Identify specific aspects that could be applied to the engineering challenge of {t['engineering_challenge']}.

3. Engineering Solution Generation (250-300 words):
   a) Describe how your AI system would generate solutions for {t['engineering_challenge']} based on {t['biological_system']}.
   b) Explain the process of adapting biological principles to the urban context of {t['urban_context']}.
   c) Provide an example of a potential solution your system might generate.

4. Implementation and Evaluation (200-250 words):
   a) Discuss how the generated solution could be implemented in {t['urban_context']}.
   b) Propose methods to evaluate the effectiveness and sustainability of the biomimetic solution.
   c) Address potential challenges in implementing the solution and how they might be overcome.

5. Ethical and Environmental Considerations (200-250 words):
   a) Discuss ethical implications of using AI and biomimicry in urban development.
   b) Analyze the potential environmental impact of implementing your solution.
   c) Propose guidelines for responsible development and use of biomimetic AI in urban planning.

6. Future Directions and Broader Impact (150-200 words):
   a) Suggest potential extensions or improvements to your biomimetic AI system.
   b) Discuss how this approach could be applied to other urban development challenges.
   c) Explore the potential long-term impact of biomimetic AI on sustainable urban design and human-nature relationships.

Ensure your response demonstrates a deep understanding of the chosen biological system, engineering principles, and artificial intelligence. Use appropriate terminology from biology, engineering, and AI fields. Be creative and innovative in your approach while maintaining scientific accuracy and feasibility. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate word counts.",
            f"The AI system design effectively integrates principles from {t['biological_system']}.",
            f"The proposed solution addresses the engineering challenge of {t['engineering_challenge']} in the context of {t['urban_context']}.",
            "The response demonstrates a deep understanding of the biological system, engineering principles, and AI.",
            "The proposed solution is innovative while maintaining scientific accuracy and feasibility.",
            "Ethical and environmental considerations are thoroughly addressed.",
            "The response explores future directions and broader impacts of the biomimetic AI approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
