import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        embodied_principles = [
            "sensorimotor coupling",
            "environmental situatedness",
            "temporal extension",
            "affordances",
            "enaction"
        ]
        hci_problems = [
            "intuitive gesture control",
            "adaptive user interfaces",
            "emotion recognition in virtual environments",
            "spatial navigation in augmented reality",
            "haptic feedback in teleoperation"
        ]
        return {
            "1": {
                "principle": random.choice(embodied_principles),
                "problem": random.choice(hci_problems)
            },
            "2": {
                "principle": random.choice(embodied_principles),
                "problem": random.choice(hci_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming paradigm based on the embodied cognition principle of {t['principle']} and apply it to solve the human-computer interaction problem of {t['problem']}. Your response should include:

1. Paradigm Overview (200-250 words):
   a) Explain the chosen embodied cognition principle and its relevance to programming.
   b) Describe the key features and concepts of your programming paradigm.
   c) Explain how your paradigm differs from traditional programming approaches.

2. Language Design (200-250 words):
   a) Outline the basic syntax and structure of a programming language based on your paradigm.
   b) Provide examples of how common programming constructs (e.g., variables, functions, control structures) would be represented.
   c) Explain how your language design reflects the chosen embodied cognition principle.

3. Problem Solution (250-300 words):
   a) Describe how your programming paradigm can be applied to solve the given HCI problem.
   b) Provide a high-level pseudocode or algorithm that demonstrates your solution.
   c) Explain how your solution leverages the embodied cognition principle to improve upon traditional approaches.

4. Implementation Considerations (150-200 words):
   a) Discuss potential challenges in implementing your paradigm on current computer architectures.
   b) Propose strategies to overcome these challenges.
   c) Speculate on how future hardware developments might better support your paradigm.

5. Cognitive Impact Analysis (200-250 words):
   a) Analyze how programming in your paradigm might affect a developer's cognitive processes.
   b) Discuss potential benefits and drawbacks of your approach for learning and problem-solving.
   c) Propose an experiment to test the cognitive effects of using your paradigm compared to traditional programming.

6. Broader Implications (150-200 words):
   a) Discuss how your paradigm might influence software development practices and methodologies.
   b) Speculate on potential applications of your paradigm beyond the given HCI problem.
   c) Consider ethical implications or societal impacts of widespread adoption of your paradigm.

Ensure your response demonstrates a deep understanding of both embodied cognition and programming concepts. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The programming paradigm must be based on the embodied cognition principle of {t['principle']} and applied to the HCI problem of {t['problem']}.",
            "The response must include a clear overview of the programming paradigm, including its key features and how it differs from traditional approaches.",
            "A basic language design must be outlined, with examples of how common programming constructs would be represented.",
            "The solution to the given HCI problem must be described, including a high-level pseudocode or algorithm.",
            "Implementation challenges and strategies to overcome them must be discussed.",
            "An analysis of the cognitive impact of the paradigm on developers must be provided, including a proposed experiment.",
            "Broader implications of the paradigm, including potential applications and ethical considerations, must be discussed.",
            "The response must demonstrate a deep understanding of both embodied cognition and programming concepts, using appropriate technical terminology.",
            "The response must be formatted with clear headings for each section and numbered paragraphs within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
