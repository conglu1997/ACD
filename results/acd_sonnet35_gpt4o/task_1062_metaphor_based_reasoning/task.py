import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'domain': 'artificial intelligence',
                'problem': 'ethical decision-making in autonomous systems',
                'source_domain': 'ecosystem'
            },
            {
                'domain': 'economics',
                'problem': 'wealth distribution in a global economy',
                'source_domain': 'fluid dynamics'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply conceptual metaphor theory to analyze and solve an abstract problem in {t['domain']} using a metaphor from {t['source_domain']}. Your task is to use metaphorical thinking to gain new insights and propose innovative solutions to the problem of {t['problem']}. Provide a detailed response addressing the following points:

1. Metaphor Construction (200-250 words):
   a) Develop a conceptual metaphor that maps elements from {t['source_domain']} to {t['domain']}.
   b) Explain the key mappings between the source and target domains.
   c) Discuss how this metaphor provides a new perspective on the problem.

2. Problem Analysis (200-250 words):
   a) Use your conceptual metaphor to analyze the problem of {t['problem']}.
   b) Identify at least three novel insights or reframings of the problem that emerge from the metaphorical mapping.
   c) Explain how these insights challenge or extend traditional understandings of the problem.

3. Solution Generation (250-300 words):
   a) Propose at least two innovative solutions to the problem, derived from your metaphorical analysis.
   b) Explain how each solution leverages the conceptual metaphor you developed.
   c) Discuss the potential advantages and limitations of each solution.

4. Cognitive Process Analysis (150-200 words):
   a) Analyze the cognitive processes involved in applying the conceptual metaphor to problem-solving.
   b) Discuss how metaphorical thinking influences reasoning and decision-making in this context.
   c) Explain any potential cognitive biases or limitations that might arise from this approach.

5. AI Implementation (200-250 words):
   a) Propose a method for implementing your metaphor-based reasoning approach in an AI system.
   b) Discuss the challenges and potential benefits of incorporating metaphorical thinking in AI.
   c) Suggest how this approach might enhance AI's problem-solving capabilities in {t['domain']}.

Ensure your response demonstrates a deep understanding of conceptual metaphor theory, creative problem-solving skills, and the ability to apply abstract concepts to real-world problems. Be innovative in your approach while maintaining logical consistency and scientific plausibility.

Format your response using clear headings for each section and subsections where appropriate. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response develops a clear and relevant conceptual metaphor mapping {t['source_domain']} to {t['domain']}.",
            "The metaphor is used effectively to analyze and gain new insights into the given problem.",
            "At least two innovative solutions are proposed, clearly derived from the metaphorical analysis.",
            "The cognitive processes involved in metaphorical thinking and problem-solving are thoroughly analyzed.",
            "A plausible method for implementing metaphor-based reasoning in AI is proposed and discussed.",
            "The response demonstrates a deep understanding of conceptual metaphor theory and its application to problem-solving.",
            "The writing is clear, well-structured, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
