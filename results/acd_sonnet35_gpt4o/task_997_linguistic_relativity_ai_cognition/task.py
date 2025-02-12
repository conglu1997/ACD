import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Hopi",
                "feature": "Tenseless language",
                "description": "Hopi lacks grammatical tenses and instead uses evidential and modal particles to indicate time relations."
            },
            {
                "name": "Guugu Yimithirr",
                "feature": "Absolute spatial reference",
                "description": "Guugu Yimithirr uses absolute directions (north, south, east, west) instead of relative directions (left, right, front, back)."
            }
        ]
        
        problems = [
            {
                "name": "Time management",
                "description": "Optimize a schedule for a complex project with multiple interdependent tasks."
            },
            {
                "name": "Navigation",
                "description": "Plan an efficient route through a city with a complex layout and various obstacles."
            }
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "language": random.choice(languages),
                "problem": random.choice(problems)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of dynamically altering its internal cognitive framework based on the linguistic features of {t['language']['name']}, specifically its {t['language']['feature']}. Then, apply this altered framework to solve the following problem: {t['problem']['description']}

Your response should include:

1. Cognitive Framework Design (250-300 words):
   a) Explain how your AI system would modify its internal representations and reasoning processes to align with the given linguistic feature.
   b) Describe the key components of this modified cognitive framework.
   c) Discuss potential challenges in implementing this framework and how you would address them.

2. Problem-Solving Approach (200-250 words):
   a) Describe how your AI system would approach the given problem using its modified cognitive framework.
   b) Explain how this approach differs from a traditional problem-solving method.
   c) Discuss any advantages or insights this approach might offer.

3. Implications Analysis (150-200 words):
   a) Analyze the potential implications of your system for our understanding of linguistic relativity and artificial intelligence.
   b) Discuss how this approach might influence AI development or cognitive science research.

4. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues or concerns related to an AI system that can alter its cognitive framework.
   b) Propose guidelines or safeguards to address these concerns.

5. Evaluation Method (100-150 words):
   a) Propose a method to evaluate the effectiveness and accuracy of your AI system's altered cognitive framework.
   b) Describe how you would measure the system's problem-solving performance compared to traditional AI approaches.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given linguistic feature and its potential impact on cognition.",
            "The AI system design is innovative and plausibly incorporates the linguistic feature into its cognitive framework.",
            "The problem-solving approach clearly demonstrates how the modified cognitive framework would be applied.",
            "The response includes thoughtful analysis of the implications and ethical considerations of such an AI system.",
            "The proposed evaluation method is logical and addresses both the cognitive framework and problem-solving performance."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
