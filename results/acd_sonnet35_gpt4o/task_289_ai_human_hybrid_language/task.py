import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "context": "Visual Arts and Design",
                "specific_focus": "Create a hybrid language for communicating complex visual concepts and emotions between human artists and AI image generation systems."
            },
            {
                "context": "Scientific Research",
                "specific_focus": "Develop a hybrid language for expressing and exploring abstract scientific hypotheses collaboratively between human scientists and AI research assistants."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hybrid communication system for efficient and nuanced information exchange between humans and advanced AI systems in the context of {t['context']}. {t['specific_focus']}\n\nYour task is to:\n\n1. Language Structure (200-250 words):\n   a) Describe the basic elements of your hybrid language (e.g., symbols, syntax, grammar).\n   b) Explain how it incorporates both human linguistic features and AI-friendly data structures.\n   c) Provide an example of how a simple concept would be expressed in this language.\n\n2. Cognitive Considerations (150-200 words):\n   a) Discuss how your language accounts for differences in human and AI cognitive processes.\n   b) Explain how it facilitates mutual understanding and reduces potential misinterpretations.\n\n3. Technological Implementation (150-200 words):\n   a) Describe the technical infrastructure required to support this hybrid language.\n   b) Explain how the system would handle input/output for both human and AI users.\n\n4. Learning and Adaptation (100-150 words):\n   a) Propose a method for humans and AIs to learn and become fluent in this hybrid language.\n   b) Discuss how the language could evolve over time to meet changing needs.\n\n5. Practical Application (150-200 words):\n   a) Provide a specific example of how your hybrid language would be used in the given context.\n   b) Discuss the potential benefits and challenges of implementing this system.\n\n6. Ethical Implications (100-150 words):\n   a) Identify potential ethical concerns related to the use of this hybrid language.\n   b) Propose guidelines to address these concerns and ensure responsible use.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and the specific context provided. Be creative in your approach while grounding your ideas in established theories and considering practical implications.\n\nFormat your response using clear headings for each section (e.g., '1. Language Structure', '2. Cognitive Considerations', etc.). Your total response should be between 900-1150 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence principles.",
            "The hybrid language design is creative, coherent, and addresses both human and AI communication needs.",
            "The submission considers practical implementation details and potential challenges.",
            "Ethical implications are thoughtfully addressed with proposed guidelines.",
            "The response is well-structured, clear, and within the specified word limits for each section.",
            "The response follows the required format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
