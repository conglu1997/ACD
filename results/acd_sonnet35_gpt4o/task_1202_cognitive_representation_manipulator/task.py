class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_process": "analogical reasoning",
                "representation_type": "visual-spatial",
                "problem_domain": "scientific discovery",
                "cognitive_bias": "confirmation bias"
            },
            "2": {
                "cognitive_process": "conceptual blending",
                "representation_type": "semantic network",
                "problem_domain": "creative writing",
                "cognitive_bias": "availability heuristic"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling and manipulating mental representations for {t['cognitive_process']}, using {t['representation_type']} as the primary representation format. Then, apply this system to solve problems in {t['problem_domain']} while analyzing the influence of {t['cognitive_bias']}.

Note: {t['cognitive_process']} refers to {'the process of identifying and transferring relational patterns between different domains' if t['cognitive_process'] == 'analogical reasoning' else 'the cognitive operation of combining two or more input mental spaces to yield a new, emergent structure'}.

Your response should include:

1. Representation System Design (300-350 words):
   a) Describe the key components and structure of your {t['representation_type']} representation system.
   b) Explain how this system captures and represents the essential elements of {t['cognitive_process']}.
   c) Provide an example of how a specific concept or relationship would be represented in your system.
   d) Include a visual representation of your system using ASCII art or a detailed textual description.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system for manipulating these representations.
   b) Explain how the system performs {t['cognitive_process']} using the designed representations.
   c) Describe how your system integrates knowledge from cognitive science and AI to achieve its functionality.
   d) Propose a novel algorithmic approach for one aspect of your system's operation.

3. Problem-Solving Application (300-350 words):
   a) Present a specific, complex problem in {t['problem_domain']} that your system will attempt to solve.
   b) Describe step-by-step how your AI system approaches this problem, including:
      - Generating relevant mental representations
      - Manipulating these representations through {t['cognitive_process']}
      - Deriving insights or solutions from the manipulated representations
   c) Provide a detailed hypothetical example of the AI's problem-solving process, including sample representations at different stages.
   d) Explain how your system's approach differs from traditional problem-solving methods in this domain.

4. Cognitive Bias Analysis (200-250 words):
   a) Explain how {t['cognitive_bias']} might influence the problem-solving process in your system.
   b) Describe how your AI system could detect and mitigate the effects of this bias.
   c) Discuss the implications of modeling cognitive biases in AI systems designed to emulate human-like reasoning.
   d) Propose a method to evaluate the effectiveness of your bias mitigation strategies.

5. Comparative Analysis (200-250 words):
   a) Compare your system's approach to {t['cognitive_process']} with traditional AI methods for similar tasks.
   b) Discuss the potential advantages and limitations of using your representation system for {t['problem_domain']}.
   c) Analyze how your system's performance might differ from human performance on similar tasks.
   d) Identify potential challenges or limitations in implementing your system in real-world scenarios.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns related to developing AI systems that model and manipulate human-like mental representations.
   b) Address any potential risks or misuses of your system, particularly in the context of {t['problem_domain']}.
   c) Propose guidelines for the responsible development and use of AI systems that emulate cognitive processes.

7. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose a novel research question that could be explored using your system as a foundation.
   c) Briefly describe an experiment design to test the effectiveness of your system in real-world applications.

Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of cognitive science, AI, and the specific cognitive process and problem domain. Use clear headings for each section and adhere to the word count guidelines provided.

Your total response should be between 1500-1850 words. Please include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive process and representation type.",
            "The AI system design effectively integrates principles from cognitive science and artificial intelligence.",
            "The problem-solving application is thoroughly explained with a complex example and demonstrates creative use of the designed system.",
            "The analysis of the specified cognitive bias is insightful and well-integrated into the system design, with a proposed evaluation method.",
            "The comparative analysis shows a nuanced understanding of both AI and human cognitive approaches, including potential limitations.",
            "Ethical implications are thoughtfully considered and addressed with specific guidelines.",
            "The response includes a visual representation (ASCII art or detailed textual description) of the representation system.",
            "Future research directions are proposed with clear connections to the designed system.",
            "The response adheres to the specified word count guidelines and uses clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
