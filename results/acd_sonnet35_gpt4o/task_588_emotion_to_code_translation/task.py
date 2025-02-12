import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            'joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust',
            'anticipation', 'trust', 'love', 'jealousy', 'guilt', 'pride'
        ]
        scenarios = [
            'First day at a new job',
            'Unexpected reunion with an old friend',
            'Receiving news of a family emergency',
            'Winning a prestigious award',
            'Facing a difficult ethical dilemma'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'emotions': random.sample(emotions, 3),
                'scenario': random.choice(scenarios)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for translating human emotions into a programming language, create an 'emotional program' based on a given scenario, and provide a visual representation of the system. Your task has the following parts:

1. Emotion-to-Code System Design (250-300 words):
   a) Create a set of programming constructs or patterns to represent different emotional states and their intensities.
   b) Define how these constructs can be combined to represent complex emotional experiences.
   c) Explain how your system handles emotional transitions and conflicting emotions.
   d) Describe any special functions or methods for emotional processing or regulation.

2. Visual Representation (new section):
   Provide a visual representation of your emotion-to-code system using ASCII art or a clear textual description. This should illustrate the key components and their relationships within your system.

3. Emotional Vocabulary (100-150 words):
   Provide a brief 'emotional vocabulary' for your system, explaining how at least 5 different emotions are represented in your code. Include the emotions: {', '.join(t['emotions'])}.

4. Scenario Translation (200-250 words):
   Translate the following scenario into your emotional programming language: "{t['scenario']}"
   a) Write a short 'emotional program' that represents the likely emotional journey of a person going through this scenario.
   b) Include comments in your code to explain the emotional states and transitions.

5. Program Analysis (150-200 words):
   a) Explain how your program captures the nuances of the emotional experience in the given scenario.
   b) Discuss any challenges you encountered in translating emotions to code and how you addressed them.

6. Potential Applications (100-150 words):
   Propose two potential applications of your emotion-to-code translation system in fields such as psychology, AI, or human-computer interaction.

7. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or concerns related to representing human emotions as code.

Ensure your response demonstrates a deep understanding of both human emotions and programming concepts. Be creative in your approach while maintaining logical consistency in your system design. Use appropriate terminology from psychology and computer science.

Format your response with clear headings for each section and adhere to the specified word counts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The emotion-to-code system design is creative, logically consistent, and demonstrates understanding of both emotions and programming concepts.",
            "A visual representation of the emotion-to-code system is provided using ASCII art or a clear textual description.",
            f"The emotional vocabulary includes representations for the specified emotions: {', '.join(t['emotions'])}.",
            f"The 'emotional program' for the scenario '{t['scenario']}' is well-constructed and plausible.",
            "The program analysis shows insight into the challenges of translating emotions to code.",
            "The proposed applications are innovative and well-explained.",
            "Ethical considerations are thoughtfully addressed.",
            "The response demonstrates interdisciplinary knowledge and creative problem-solving.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
