import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        propulsion_challenges = [
            {
                'target': 'Alpha Centauri',
                'distance': '4.37 light-years',
                'constraint': 'No faster-than-light travel',
                'focus': 'Efficiency'
            },
            {
                'target': 'Trappist-1 system',
                'distance': '39 light-years',
                'constraint': 'Minimal environmental impact',
                'focus': 'Sustainability'
            }
        ]
        return {str(i+1): challenge for i, challenge in enumerate(random.sample(propulsion_challenges, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical propulsion system for interstellar travel to {t['target']}, located {t['distance']} from Earth. Your design must adhere to the constraint: {t['constraint']}, with a focus on {t['focus']}. Your task has five parts:

1. Propulsion System Concept (200-250 words):
   a) Propose an innovative propulsion system for interstellar travel.
   b) Explain the fundamental physical principles underlying your design.
   c) Describe how your system would function to propel a spacecraft.

2. Technical Specifications (150-200 words):
   a) Provide estimated performance metrics for your propulsion system (e.g., thrust, specific impulse, power requirements).
   b) Explain how these specifications address the given constraint and focus.
   c) Discuss any theoretical limits or challenges to achieving these specifications.

3. Materials and Engineering (150-200 words):
   a) Suggest potential materials or technologies required for your propulsion system.
   b) Discuss any engineering challenges in constructing and operating your system.
   c) Propose solutions to overcome these challenges, considering both current and speculative future technologies.

4. Mission Profile (200-250 words):
   a) Outline a hypothetical mission using your propulsion system to reach the target.
   b) Estimate the duration of the journey and any significant mission milestones.
   c) Discuss how your system addresses the challenges of long-duration interstellar travel (e.g., life support, shielding).

5. Comparative Analysis (150-200 words):
   a) Compare your propulsion system to at least two other theoretical or proposed methods of interstellar travel.
   b) Analyze the advantages and disadvantages of your system relative to these alternatives.
   c) Discuss potential areas for further research or improvement in your design.

Ensure your response demonstrates a deep understanding of physics principles, creative application of scientific concepts, and logical reasoning. Use appropriate scientific terminology and provide clear explanations of complex ideas. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The propulsion system design adheres to the constraint: {t['constraint']} and focuses on {t['focus']}.",
            "The response demonstrates a deep understanding of physics principles and their application to interstellar travel.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The technical specifications and mission profile are logically consistent and well-reasoned.",
            "The comparative analysis shows critical thinking and a broad understanding of interstellar travel concepts.",
            "The response is well-structured, using clear headings for each section as specified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
