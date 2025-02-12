import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'scenario': 'time travel paradox',
                'entities': ['past self', 'future self', 'timeline'],
                'temporal_concepts': ['causality', 'parallel timelines', 'temporal loops'],
                'problem': 'Resolve a grandfather paradox where a time traveler attempts to prevent their own birth',
                'example_symbol': '⌛'
            },
            {
                'scenario': 'project scheduling',
                'entities': ['tasks', 'resources', 'deadlines'],
                'temporal_concepts': ['concurrency', 'dependencies', 'critical path'],
                'problem': 'Optimize a project schedule with limited resources and overlapping task dependencies',
                'example_symbol': '⏱'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized language for expressing and reasoning about complex temporal relationships, then use this language to solve a problem involving {t['scenario']}. Your response should follow this structure and include ALL of the following sections:

1. Temporal Language Design (300-350 words):
   a) Create a set of at least 5 symbols (including {t['example_symbol']}), 3 operators, and 3 rules for expressing temporal relationships and concepts.
   b) Explain how your language represents time-based entities, relationships, and transformations.
   c) Provide examples of how basic temporal operations (e.g., sequencing, simultaneity, duration) are expressed in your language.
   d) Include a visual representation of your language's key elements using ASCII art or a text-based diagram.
   e) Explain how your language handles the temporal concepts of {', '.join(t['temporal_concepts'])}.

2. Scenario Representation (200-250 words):
   a) Use your language to represent a complex temporal scenario involving {t['scenario']}.
   b) Include the entities {', '.join(t['entities'])} in your representation.
   c) Explain the meaning of your representation and how it captures the essential temporal aspects of the scenario.
   d) Provide a visual representation of this scenario using your language.

3. Problem Solving (250-300 words):
   a) Address the following problem: {t['problem']}
   b) Use your language to show the step-by-step process of solving this problem.
   c) Provide detailed explanations for each operation in your solution.
   d) Discuss how your language facilitates the problem-solving process in this temporal domain.

4. Cognitive Process Analysis (150-200 words):
   a) Analyze how your language and problem-solving approach relate to human cognitive processes for temporal reasoning.
   b) Discuss any similarities or differences between your approach and how humans might mentally represent and manipulate temporal information.

5. AI Implementation (150-200 words):
   a) Propose how an AI system could be designed to work with your temporal reasoning language.
   b) Discuss potential challenges and advantages of implementing this system.
   c) Explain how this AI system might handle temporal reasoning differently from traditional AI approaches.

6. Implications and Applications (150-200 words):
   a) Discuss potential applications of your temporal reasoning language in fields such as AI, cognitive science, or computer science.
   b) Explore how this approach might advance our understanding of temporal cognition or improve AI capabilities in time-based reasoning tasks.
   c) Consider any ethical implications or potential misuses of advanced temporal reasoning systems.

Ensure your response demonstrates a deep understanding of temporal cognition, linguistics, and artificial intelligence. Be creative in your language design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed temporal language with at least 5 symbols (including {t['example_symbol']}), 3 operators, and 3 rules.",
            f"The language effectively represents the scenario of {t['scenario']} and includes the specified entities ({', '.join(t['entities'])}) and temporal concepts ({', '.join(t['temporal_concepts'])}).",
            f"The problem-solving section addresses the specific problem: {t['problem']}",
            "The cognitive process analysis shows insight into human temporal reasoning and compares it with the designed language.",
            "The AI implementation proposal is plausible, addresses potential challenges and advantages, and explains how it differs from traditional AI approaches.",
            "The implications and applications section provides thoughtful considerations of the language's potential impact, including ethical implications.",
            "The overall response demonstrates creativity, logical consistency, and a deep understanding of temporal cognition and linguistics.",
            "The response follows the specified format, includes all required sections, and is within the 1200-1500 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
