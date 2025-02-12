import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_constraints = [
            {
                'constraint': 'working memory capacity of 4 items',
                'comparison_system': 'American Sign Language'
            },
            {
                'constraint': 'color perception limited to 3 distinct hues',
                'comparison_system': 'Maritime signal flags'
            }
        ]
        
        return {str(i+1): constraint for i, constraint in enumerate(random.sample(cognitive_constraints, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial visual communication system (semaphore) based on the cognitive constraint: {t['constraint']}. Then, analyze its efficiency and compare it to {t['comparison_system']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the basic elements and rules of your visual communication system.
   b) Explain how your system accommodates the given cognitive constraint.
   c) Provide examples of how to represent at least 5 common concepts or words in your system.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your system leverages or works around the given cognitive constraint.
   b) Discuss potential cognitive load and learning curve for users of your system.
   c) Propose a hypothesis about how this system might affect users' thought patterns or perception.

3. Efficiency Analysis (200-250 words):
   a) Estimate the information density of your system (bits per symbol or transmission).
   b) Analyze the speed of communication possible with your system.
   c) Discuss trade-offs between complexity, expressiveness, and ease of use in your system.

4. Comparative Analysis (200-250 words):
   a) Compare your system to {t['comparison_system']} in terms of expressiveness, efficiency, and learnability.
   b) Identify unique advantages or disadvantages of your system.
   c) Discuss how the cognitive constraint of your system compares to cognitive factors in {t['comparison_system']}.

5. Potential Applications (100-150 words):
   Propose two potential real-world applications for your communication system, explaining why it would be particularly suitable for each context.

Ensure your response demonstrates a deep understanding of visual communication principles, cognitive science, and information theory. Be creative in your system design while maintaining scientific plausibility and adhering to the given constraint.

Format your response with clear headings for each section and adhere to the word count guidelines provided. Your entire response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The designed system clearly accommodates the cognitive constraint: {t['constraint']}.",
            "The system design is creative, coherent, and includes examples of concept representation.",
            "The cognitive and efficiency analyses demonstrate understanding of cognitive science and information theory principles.",
            f"The comparative analysis provides meaningful insights when comparing the designed system to {t['comparison_system']}.",
            "The proposed applications are plausible and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
