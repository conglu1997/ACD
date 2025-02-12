import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Social Interactions",
                "entity1": "Friend",
                "entity2": "Colleague",
                "relation": "Trust",
                "transformation": "Betrayal"
            },
            {
                "domain": "Physical Systems",
                "entity1": "Gear",
                "entity2": "Lever",
                "relation": "Mechanical Advantage",
                "transformation": "Friction"
            }
        ]
        
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized language for expressing and manipulating mental models, then use this language to solve a problem in the domain of {t['domain']}. Your task has the following components:

1. Language Design (250-300 words):
   a) Create a set of symbols, operators, and rules for expressing mental models.
   b) Explain how your language represents entities, relationships, and transformations.
   c) Provide examples of how basic cognitive operations (e.g., inference, analogy) are expressed in your language.
   d) Include a visual representation of your language's key elements using ASCII art or a text-based diagram.

2. Mental Model Representation (150-200 words):
   a) Use your language to represent a mental model involving the entities '{t['entity1']}' and '{t['entity2']}', and the relation '{t['relation']}'.
   b) Explain the meaning of your representation and how it captures the essential aspects of the mental model.
   c) Provide a visual representation of this mental model using your language.

3. Problem Solving (250-300 words):
   a) Using your language, show how the mental model changes when the transformation '{t['transformation']}' is applied.
   b) Describe the step-by-step process of this transformation in your language, providing detailed explanations for each operation.
   c) Discuss the implications of this transformation on the original mental model.

4. Cognitive Process Analysis (150-200 words):
   a) Analyze how your language and problem-solving approach relate to human cognitive processes.
   b) Discuss any similarities or differences between your approach and how humans might mentally represent and manipulate this information.

5. AI Implementation (100-150 words):
   a) Propose how an AI system could be designed to work with your mental model language.
   b) Discuss potential challenges and advantages of implementing this system.

6. Ethical and Practical Implications (100-150 words):
   a) Discuss potential ethical considerations of using formalized languages for mental models.
   b) Explore practical applications of your approach in fields such as education, therapy, or AI development.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your language design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a well-defined language for expressing mental models, with clear symbols, operators, and rules",
            "The language design must include a visual representation using ASCII art or a text-based diagram",
            f"The mental model representation must involve '{t['entity1']}', '{t['entity2']}', and '{t['relation']}', and include a visual representation",
            f"The problem-solving section should demonstrate clear use of the designed language to apply the transformation '{t['transformation']}'",
            "The response should show a deep understanding of cognitive science and linguistics",
            "The designed language should be sufficiently expressive to represent complex mental models and transformations",
            "The AI implementation proposal should be plausible and well-reasoned",
            "Ethical implications must be thoughtfully considered",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1000-1300 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
