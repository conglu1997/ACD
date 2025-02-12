import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'relativistic_effect': 'Time dilation',
                'computing_challenge': 'Parallel processing'
            },
            {
                'relativistic_effect': 'Length contraction',
                'computing_challenge': 'Data compression'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical computing paradigm that leverages the relativistic effect of {t['relativistic_effect']} to address the computing challenge of {t['computing_challenge']}. 

Relativistic effects are phenomena that occur when objects move at very high speeds, approaching the speed of light. These effects, predicted by Einstein's theory of relativity, can cause changes in the perceived passage of time and the measurement of distances.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen relativistic effect and its potential relevance to computing.
   b) Describe how this effect could be harnessed in a computing system.
   c) Outline the key components and principles of your relativistic computing paradigm.

2. System Architecture (250-300 words):
   a) Provide a detailed description of the architecture of your relativistic computing system.
   b) Explain how it incorporates the specified relativistic effect.
   c) Describe how it addresses the given computing challenge.
   d) Include a diagram or schematic representation of your system (describe it textually).

3. Information Processing Model (200-250 words):
   a) Explain how information is encoded, processed, and retrieved in your system.
   b) Describe any novel data structures or algorithms that leverage relativistic effects.
   c) Discuss how your model differs from classical computing paradigms.

4. Theoretical Performance Analysis (200-250 words):
   a) Analyze the potential advantages of your relativistic computing paradigm.
   b) Compare its theoretical performance to classical computing systems for the given challenge.
   c) Discuss any trade-offs or limitations inherent in your approach.

5. Implementation Challenges (150-200 words):
   a) Identify potential technological hurdles in realizing your relativistic computing system.
   b) Propose possible solutions or research directions to address these challenges.
   c) Discuss any fundamental physical limits that might constrain your system.

6. Broader Implications (150-200 words):
   a) Explore potential applications of your relativistic computing paradigm beyond the given challenge.
   b) Discuss how this approach might impact our understanding of the relationship between physics and information.
   c) Consider any philosophical implications of your system (e.g., for our concepts of time, causality, or computation).

7. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns or societal impacts of relativistic computing systems.
   b) Propose guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of both relativity and computing principles. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Adhere strictly to the word count for each section as specified above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both relativistic physics and computing principles.",
            "The proposed relativistic computing paradigm is innovative, scientifically plausible, and well-justified.",
            "The system architecture and information processing model effectively leverage the specified relativistic effect.",
            "The proposed solution directly addresses the given computing challenge.",
            "The theoretical performance analysis is thorough and compares the proposed system to classical computing approaches.",
            "Implementation challenges and potential solutions are identified and discussed realistically.",
            "The broader implications and ethical considerations are thoughtfully explored.",
            "The response shows strong integration of knowledge from physics, computer science, and related fields.",
            "The response includes creative solutions while maintaining scientific rigor.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
