import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "name": "Culinary Arts",
                "concept": "Molecular Gastronomy",
                "ideas": ["Flavor pairing", "Texture modification", "Edible packaging"]
            },
            {
                "name": "Architecture",
                "concept": "Biomimicry",
                "ideas": ["Self-cleaning surfaces", "Energy-efficient structures", "Adaptive building materials"]
            },
            {
                "name": "Music",
                "concept": "Algorithmic Composition",
                "ideas": ["Generative melodies", "Emotion-based harmonies", "Fractal rhythms"]
            },
            {
                "name": "Fashion",
                "concept": "Wearable Technology",
                "ideas": ["Mood-responsive fabrics", "Customizable digital patterns", "Health-monitoring accessories"]
            }
        ]
        problems = [
            "Sustainability",
            "Cultural Preservation",
            "Mental Health",
            "Education"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "problem": random.choice(problems)
            },
            "2": {
                "domain": random.choice(domains),
                "problem": random.choice(problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that implements conceptual blending theory for creative idea generation, then apply it to solve a problem in a specific domain. Your task has the following components:

1. Conceptual Blending System Design (300-350 words):
   a) Explain the key principles of conceptual blending theory and how they inform your AI system design.
   b) Describe the architecture of your AI system, including its main components and how they interact.
   c) Explain how your system generates, evaluates, and refines blended concepts.
   d) Discuss any novel features or improvements your system offers over traditional approaches to AI creativity.
   e) Provide a visual representation or diagram of your AI system design (describe it textually).

2. Implementation in the Given Domain (250-300 words):
   Domain: {t['domain']['name']}
   Key Concept: {t['domain']['concept']}
   Related Ideas: {', '.join(t['domain']['ideas'])}
   Problem to Address: {t['problem']}

   a) Describe how your AI conceptual blending system would be applied to the given domain.
   b) Explain how it would incorporate the key concept and related ideas within this domain.
   c) Provide an example of a creative solution your system might generate to address the specified problem.
   d) Analyze the potential impact of this solution on the domain and the problem.

3. Cognitive Science Analysis (200-250 words):
   a) Discuss how your AI system's approach to conceptual blending compares to human cognitive processes.
   b) Analyze potential cognitive benefits and challenges for humans interacting with or using outputs from this system.
   c) Propose an experiment to test whether your AI system's conceptual blending capabilities match or exceed human performance.

4. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues or misuses of your AI conceptual blending system.
   b) Discuss limitations of your system and areas for future improvement.
   c) Propose guidelines for responsible development and use of AI systems for creative tasks.

5. Interdisciplinary Implications (150-200 words):
   a) Explore how your AI conceptual blending system might impact or be applied to other fields not mentioned in the given domain.
   b) Discuss potential long-term consequences of widespread adoption of such systems for human creativity and problem-solving.

Ensure your response demonstrates a deep understanding of conceptual blending theory, AI systems, and the specified domain. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section (e.g., '1. Conceptual Blending System Design', '2. Implementation in the Given Domain', etc.). Your total response should be between 1050-1300 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively, following the specified format and word count guidelines.",
            "The AI system design demonstrates a clear understanding and application of conceptual blending theory, including a textual description of a visual representation or diagram.",
            f"The implementation in the given domain ({t['domain']['name']}) is creative, relevant to the problem ({t['problem']}), and incorporates the key concept ({t['domain']['concept']}) and related ideas.",
            "The cognitive science analysis shows deep understanding of human cognitive processes and AI capabilities, including a well-designed experiment proposal.",
            "The response demonstrates interdisciplinary knowledge integration and analytical reasoning throughout all sections.",
            "The ethical considerations and limitations are thoughtfully addressed, with specific guidelines proposed for responsible AI development and use.",
            "The interdisciplinary implications section explores novel applications and long-term consequences of the proposed AI system.",
            "The writing is clear, well-structured, and demonstrates a high level of creativity while maintaining scientific and technological plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
