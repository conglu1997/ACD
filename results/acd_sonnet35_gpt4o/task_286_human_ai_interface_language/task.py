class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "focus_area": "scientific research collaboration",
                "key_features": ["precision", "scalability", "domain-specific terminology"]
            },
            "2": {
                "focus_area": "creative problem-solving in design",
                "key_features": ["visual-verbal integration", "metaphor representation", "iterative refinement"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized language to facilitate more effective communication and collaboration between humans and AI systems in the area of {t['focus_area']}, incorporating the following key features: {', '.join(t['key_features'])}.

Your task is to create a language that bridges the gap between human cognition and AI processing capabilities. Provide your response in the following format:

1. Language Overview (100-150 words):
   Briefly describe your language and how it aims to enhance human-AI communication and collaboration in the given focus area.

2. Key Language Features (list 4-5 points, 30-50 words each):
   Describe the main features of your language, explaining how each addresses the given key features and facilitates human-AI interaction.

3. Syntax and Structure (100-150 words):
   Explain the basic syntax and structure of your language, highlighting how it balances human readability with AI processability.

4. Vocabulary and Concepts (100-150 words):
   Describe how your language represents and conveys complex concepts, especially those relevant to the focus area.

5. Sample Expressions (provide 3 examples):
   Give examples of expressions in your language, along with their meanings and explanations of how they enhance human-AI communication.

6. Learning and Adoption (100-150 words):
   Discuss how humans and AI systems would learn and adopt this language, addressing potential challenges and strategies to overcome them.

7. Ethical Considerations (100-150 words):
   Address potential ethical implications of a language designed for human-AI interaction, including issues of transparency, bias, and power dynamics.

Ensure your language design is innovative, theoretically grounded, and clearly demonstrates how it could potentially enhance human-AI communication and collaboration in the given focus area."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design effectively incorporates the given key features and addresses the specific focus area.",
            "The response demonstrates a strong understanding of linguistics, cognitive science, and AI capabilities.",
            "The language features are innovative and show potential for enhancing human-AI communication and collaboration.",
            "The syntax and structure balance human readability with AI processability.",
            "The sample expressions effectively demonstrate the language's potential in the given focus area.",
            "The response thoughtfully addresses learning, adoption, and ethical considerations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
