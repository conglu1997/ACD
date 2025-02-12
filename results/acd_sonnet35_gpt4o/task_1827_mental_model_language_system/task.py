import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_concepts = [
            {
                "concept": "schema",
                "description": "A cognitive framework or concept that helps organize and interpret information"
            },
            {
                "concept": "mental simulation",
                "description": "The ability to imagine and mentally rehearse actions or scenarios"
            },
            {
                "concept": "cognitive load",
                "description": "The total amount of mental effort being used in the working memory"
            },
            {
                "concept": "conceptual blending",
                "description": "The process of combining different mental spaces to create new meaning"
            }
        ]
        
        problem_domains = [
            "ethical decision-making",
            "scientific discovery",
            "creative problem-solving",
            "strategic planning"
        ]
        
        return {
            "1": {
                "cognitive_concept": random.choice(cognitive_concepts),
                "problem_domain": random.choice(problem_domains)
            },
            "2": {
                "cognitive_concept": random.choice(cognitive_concepts),
                "problem_domain": random.choice(problem_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system for representing and manipulating mental models, focusing on the cognitive concept of {t['cognitive_concept']['concept']}. Then, apply this system to solve a complex reasoning problem in the domain of {t['problem_domain']}. Your task has the following components:

1. Language System Design (300-350 words):
   a) Describe the fundamental elements of your language system for representing mental models.
   b) Explain how your system incorporates the cognitive concept of {t['cognitive_concept']['concept']}.
   c) Provide examples of basic 'expressions' or 'statements' in this language system.
   d) Discuss how your system allows for the manipulation and evolution of mental models.

2. Cognitive Integration (200-250 words):
   a) Explain the theoretical basis for applying {t['cognitive_concept']['concept']} to mental model representation.
   b) Describe how your language system reflects current understanding of human cognition.
   c) Discuss any novel insights your system might offer about cognitive processes.

3. Problem-Solving Application (250-300 words):
   a) Present a complex reasoning problem in the domain of {t['problem_domain']}.
   b) Demonstrate how your language system would represent the mental models involved in this problem.
   c) Show how your system would manipulate these models to solve the problem.
   d) Provide a step-by-step explanation of the problem-solving process using your language system.

4. Comparative Analysis (200-250 words):
   a) Compare your mental model language system to traditional approaches in AI reasoning.
   b) Analyze potential advantages and limitations of your approach.
   c) Discuss how your system might offer new insights into {t['problem_domain']} or cognitive processes.

5. Implications for AI Development (150-200 words):
   a) Discuss how your language system could influence the development of more advanced AI systems.
   b) Explore potential applications of your system in improving human-AI interaction.
   c) Address any ethical considerations related to implementing such a system.

6. Future Research Directions (150-200 words):
   a) Propose two potential extensions or improvements to your language system.
   b) Suggest experiments that could validate or refine your approach.
   c) Speculate on how this line of research might evolve in the next decade.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1550 words.

Format your response with clear headings for each section, numbered paragraphs, and include a brief conclusion summarizing the key points of your design and its potential impact."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed language system that clearly incorporates the given cognitive concept into mental model representation and manipulation.",
            "The problem-solving application demonstrates a coherent and logical use of the language system to address a complex issue in the specified domain.",
            "The comparative analysis shows a deep understanding of both traditional AI approaches and the potential advantages of the proposed system.",
            "The discussion of implications for AI development and future research directions is insightful and demonstrates foresight.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence, with creative yet scientifically plausible ideas.",
            "The overall response is well-structured, coherent, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
