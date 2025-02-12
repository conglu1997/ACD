import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "mental imagery",
            "spatial memory",
            "perceptual organization",
            "visual attention"
        ]
        
        problem_domains = [
            "abstract reasoning",
            "mathematical concepts",
            "process workflows",
            "emotional states"
        ]
        
        return {
            "1": {"principle": random.choice(cognitive_principles), "domain": random.choice(problem_domains)},
            "2": {"principle": random.choice(cognitive_principles), "domain": random.choice(problem_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual language system based on the cognitive principle of {t['principle']}, then use it to solve and communicate a complex problem in the domain of {t['domain']}. Your response should include:

1. Visual Language Design (250-300 words):
   a) Describe the key elements and rules of your visual language system.
   b) Explain how it incorporates the cognitive principle of {t['principle']}.
   c) Discuss how your system differs from existing visual languages or notation systems.
   d) Provide a simple example of how your language represents a basic concept.

2. Cognitive Science Foundation (200-250 words):
   a) Explain the chosen cognitive principle and its relevance to visual communication.
   b) Discuss how your visual language system leverages or enhances this cognitive process.
   c) Predict potential cognitive benefits or challenges for users of your system.

3. Problem-Solving Application (250-300 words):
   a) Present a complex problem from the domain of {t['domain']}.
   b) Describe step-by-step how you would use your visual language to approach and solve this problem.
   c) Explain how your visual language enhances problem-solving in this domain compared to traditional methods.

4. Visual Solution Representation (200-250 words):
   a) Provide a detailed description of how the solution to your chosen problem would be visually represented in your language system.
   b) Explain how each element of your visual representation corresponds to aspects of the problem or solution.
   c) Discuss how this representation facilitates understanding or communication of the solution.

5. Cross-modal Integration (150-200 words):
   a) Propose a method for translating your visual language into verbal or written form.
   b) Discuss challenges and opportunities in integrating your visual system with other forms of communication.

6. Evaluation and Refinement (150-200 words):
   a) Suggest criteria for evaluating the effectiveness of your visual language system.
   b) Propose an experiment to test its efficacy in problem-solving and communication.
   c) Discuss potential refinements or extensions to your system based on anticipated results.

Ensure your response demonstrates a deep understanding of cognitive science, visual communication principles, and problem-solving strategies. Be creative in your language design and application while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe a visual language system based on the cognitive principle of {t['principle']}.",
            f"The visual language should be applied to solve a complex problem in the domain of {t['domain']}.",
            "The proposed visual language system should be novel and creative while remaining scientifically plausible.",
            "The response should demonstrate a deep understanding of cognitive science, visual communication, and problem-solving strategies.",
            "All six requested sections should be present and adequately addressed.",
            "The visual language system should show potential for enhancing problem-solving and communication in the specified domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
