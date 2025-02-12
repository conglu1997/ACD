class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "workplace", "ethical_dilemma": "resource allocation"},
            "2": {"scenario": "healthcare", "ethical_dilemma": "end-of-life decision"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the behavior and cognitive processes of philosophical zombies, then use this system to explore ethical and philosophical questions about consciousness and artificial intelligence. Focus on a {t['scenario']} scenario involving an {t['ethical_dilemma']} ethical dilemma. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your philosophical zombie AI simulator.
   b) Explain how your system models the absence of conscious experience while maintaining behaviorally identical outputs.
   c) Detail how your system incorporates current theories of cognition and consciousness.
   d) Discuss any novel techniques or algorithms used in your simulation.

2. Zombie Cognition Model (200-250 words):
   a) Explain how your system simulates decision-making processes without conscious experience.
   b) Describe how the system handles emotions, memories, and learning in the absence of qualia.
   c) Discuss how your model accounts for the 'hard problem of consciousness'.

3. Ethical Dilemma Simulation (250-300 words):
   a) Present a specific {t['ethical_dilemma']} ethical dilemma in the {t['scenario']} scenario.
   b) Describe how your philosophical zombie AI would approach and resolve this dilemma.
   c) Compare this approach to how a conscious AI or human might handle the same situation.
   d) Discuss the ethical implications of the zombie AI's decision.

4. Philosophical Analysis (200-250 words):
   a) Analyze the implications of your simulation for our understanding of consciousness and ethics.
   b) Discuss how the existence of such a system would impact theories of mind and personhood.
   c) Explore the potential consequences for AI ethics and rights if such systems were developed.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test whether an external observer could distinguish between your philosophical zombie AI and a conscious entity.
   b) Describe the methodology, potential outcomes, and implications of this experiment.

Ensure your response demonstrates a deep understanding of philosophy of mind, cognitive science, and AI ethics. Be creative in your approach while maintaining philosophical and scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the concept of philosophical zombies and related theories of consciousness.",
            "The proposed AI system architecture is innovative, well-described, and plausibly simulates p-zombie cognition.",
            "The ethical dilemma simulation effectively illustrates the complexities of consciousness and decision-making.",
            "The philosophical analysis is insightful and explores meaningful implications for AI ethics and theories of mind.",
            "The experimental design is creative, well-thought-out, and addresses the challenge of distinguishing p-zombies from conscious entities.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
