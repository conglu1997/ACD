import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_concepts = [
            {
                "concept": "Categorical Imperative",
                "description": "Kant's ethical principle that one should act only according to rules that could hold for everyone"
            },
            {
                "concept": "Utilitarianism",
                "description": "The ethical theory that the most ethical choice is the one that will produce the greatest good for the greatest number"
            },
            {
                "concept": "Existentialism",
                "description": "A philosophical theory emphasizing individual existence, freedom, and choice"
            },
            {
                "concept": "Epistemological Skepticism",
                "description": "The philosophical position that knowledge is impossible or that we can never be certain about our knowledge"
            }
        ]
        
        real_world_problems = [
            "Designing ethical AI systems",
            "Addressing climate change",
            "Reducing wealth inequality",
            "Balancing privacy and security in the digital age"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(philosophical_concepts)
            problem = random.choice(real_world_problems)
            tasks[str(i+1)] = {"concept": concept, "problem": problem}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply the philosophical concept of {t['concept']['concept']} to address the real-world problem of {t['problem']}. Your task is to:

1. Concept Analysis (200-250 words):
   a) Explain {t['concept']['concept']} in your own words, expanding on the given description: {t['concept']['description']}
   b) Discuss the key principles or implications of this philosophical concept.
   c) Analyze potential criticisms or limitations of this concept.

2. Problem Analysis (200-250 words):
   a) Describe the main challenges and complexities involved in {t['problem']}.
   b) Identify key stakeholders and their interests in this issue.
   c) Discuss current approaches to addressing this problem and their limitations.

3. Philosophical Application (250-300 words):
   a) Propose a novel solution or approach to {t['problem']} that applies principles from {t['concept']['concept']}.
   b) Explain how specific aspects of the philosophical concept inform your proposed solution.
   c) Discuss how your approach differs from current methods and why it might be more effective.

4. Ethical Implications (200-250 words):
   a) Analyze potential ethical concerns or dilemmas that might arise from your proposed solution.
   b) Discuss how these ethical issues might be addressed or mitigated.
   c) Consider how your solution aligns with or challenges other ethical frameworks.

5. Practical Implementation (150-200 words):
   a) Outline steps for implementing your philosophically-informed solution in the real world.
   b) Identify potential obstacles to implementation and how they might be overcome.
   c) Discuss how the success of your approach could be measured or evaluated.

Ensure your response demonstrates a deep understanding of both the philosophical concept and the real-world problem. Be creative and rigorous in your application of the concept, while considering practical constraints and ethical implications.

Format your response with clear headings for each section (e.g., '1. Concept Analysis:', '2. Problem Analysis:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly.

Your total response should be between 1000-1250 words. Please include a word count at the end of your response.

Your response will be evaluated based on your understanding of the philosophical concept, the depth of your problem analysis, the creativity and rigor of your proposed solution, your consideration of ethical implications, and the practicality of your implementation plan."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['concept']['concept']} and its implications",
            f"The analysis of {t['problem']} is comprehensive and insightful",
            "The proposed solution creatively and rigorously applies the philosophical concept to the real-world problem",
            "Ethical implications are thoroughly considered and addressed",
            "The practical implementation plan is realistic and well-thought-out",
            "The overall response shows depth of analysis, creativity, and critical thinking",
            "The response follows the specified format and is within the 1000-1250 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
