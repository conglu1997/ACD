import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R",
                "description": "Adaptive Control of Thought-Rational, emphasizing the modular structure of cognition"
            },
            {
                "name": "SOAR",
                "description": "State, Operator, and Result, focusing on problem-solving and learning"
            },
            {
                "name": "Global Workspace Theory",
                "description": "Emphasizing the role of consciousness in cognitive processing"
            },
            {
                "name": "Predictive Processing",
                "description": "Viewing the brain as a prediction machine that constantly generates and updates internal models"
            }
        ]
        return {
            "1": random.choice(cognitive_architectures),
            "2": random.choice(cognitive_architectures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a programming language based on the cognitive architecture of {t['name']} ({t['description']}). Your task has the following components:\n\n1. Language Design (250-300 words):\n   a) Describe the key features and syntax of your programming language.\n   b) Explain how these features reflect the principles of the {t['name']} cognitive architecture.\n   c) Provide a simple code example in your language, with comments explaining its cognitive basis.\n\n2. Cognitive-Computational Mapping (200-250 words):\n   a) Analyze how specific aspects of the {t['name']} architecture are translated into computational constructs.\n   b) Discuss any challenges in this translation and how you addressed them.\n   c) Explain how your language might model or simulate cognitive processes.\n\n3. Problem-Solving Approach (200-250 words):\n   a) Describe how programmers would approach problem-solving using your language.\n   b) Provide an example of how a specific problem might be solved differently in your language compared to traditional languages.\n   c) Discuss potential cognitive benefits or challenges for programmers using your language.\n\n4. Learning and Adaptation (150-200 words):\n   a) Explain how your language incorporates learning or adaptation, if applicable.\n   b) Discuss how this feature might affect long-term software development and maintenance.\n\n5. Practical Applications (150-200 words):\n   a) Propose two potential practical applications or domains where your language might be particularly useful.\n   b) Explain why these applications are well-suited to the cognitive principles embodied in your language.\n\n6. Implications and Limitations (150-200 words):\n   a) Discuss potential implications of widespread adoption of cognitive architecture-based programming languages.\n   b) Analyze limitations or potential negative consequences of your approach.\n   c) Suggest areas for future research or development in this field.\n\nEnsure your response demonstrates a deep understanding of both cognitive science and computer science principles. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1100-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['name']} cognitive architecture and its principles.",
            "The proposed programming language features are clearly linked to cognitive processes and principles.",
            "The language design is innovative yet plausible, with a coherent syntax and structure.",
            "The response includes a thoughtful analysis of problem-solving approaches and potential applications.",
            "The implications and limitations of the proposed language are thoroughly discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
