import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            {
                "problem": "Sorting algorithm",
                "context": "Data visualization",
                "creative_element": "Incorporate a gesture that represents data anomalies"
            },
            {
                "problem": "Pathfinding algorithm",
                "context": "Autonomous robotics",
                "creative_element": "Include a gesture for dynamic obstacle avoidance"
            }
        ]
        return {
            "1": computational_problems[0],
            "2": computational_problems[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on human gestures and use it to solve a computational problem. Your task involves the following steps:

1. Gesture-Based Language Design (250-300 words):
   a) Create a programming language where instructions are represented by human gestures.
   b) Define exactly 12 basic gestures and their corresponding programming concepts or operations.
   c) Explain how these gestures can be combined to form more complex instructions.
   d) Describe how your language handles common programming constructs (e.g., loops, conditionals, functions).
   e) Discuss any unique features or advantages of your gesture-based language.

2. Language Specification (200-250 words):
   a) Provide a formal specification of your language, including syntax and semantics.
   b) Explain how gestures are interpreted and executed in your language.
   c) Describe any constraints or limitations of your gesture-based approach.

3. Problem Solution (300-350 words):
   Using your gesture-based language, design a solution for the following computational problem: {t['problem']}
   a) Describe the algorithm in terms of the gestures used.
   b) Explain how your solution works, step by step.
   c) Compare your gesture-based solution with a traditional programming approach, highlighting differences in implementation and potential advantages/disadvantages.
   d) {t['creative_element']}

4. Context Application (200-250 words):
   Explain how your gesture-based solution could be applied in the context of {t['context']}.
   a) Describe a specific scenario where your solution would be useful.
   b) Discuss any advantages or limitations of using gesture-based programming in this context.
   c) Propose a novel application of your gesture-based language in this field.

5. Human-Computer Interaction Analysis (250-300 words):
   a) Analyze the ergonomics and usability of your gesture-based language.
   b) Discuss potential cognitive benefits or challenges for programmers using this language.
   c) Propose ideas for making your language more inclusive and accessible.
   d) Describe how your gesture-based language might influence or change programmers' thought processes.

Ensure your response demonstrates a deep understanding of programming concepts, human-computer interaction, and the specified problem domain. Be creative in your language design while maintaining practical feasibility. Use clear headings for each section of your response.

Format your response as follows:
[Section Number]. [Section Name]
[Your response for this section]

Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The gesture-based language design is creative, well-defined, and includes exactly 12 basic gestures covering essential programming concepts.",
            "The language specification is clear and comprehensively addresses syntax, semantics, and execution.",
            f"The solution for the {t['problem']} problem is correctly described using the gesture-based language and compared with a traditional programming approach.",
            f"The application in the context of {t['context']} is relevant, well-explained, and includes a novel proposal.",
            "The human-computer interaction analysis is insightful, considering usability, accessibility, and potential cognitive impacts.",
            f"The response incorporates the creative element: {t['creative_element']}",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
