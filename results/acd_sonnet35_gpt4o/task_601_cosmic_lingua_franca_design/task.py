import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'concept': 'Prime numbers',
                'constant': 'Speed of light'
            },
            {
                'concept': 'Fibonacci sequence',
                'constant': 'Planck constant'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a universal language for communicating with extraterrestrial intelligence based on the mathematical concept of {t['concept']} and the physical constant {t['constant']}. Your task has the following parts:

1. Conceptual Foundation (150-200 words):
   Explain how {t['concept']} and {t['constant']} can serve as a basis for universal communication. Discuss their fundamental nature and why they might be recognizable to an advanced alien civilization.

2. Language Structure (250-300 words):
   a) Describe the basic elements of your language (e.g., symbols, grammar rules).
   b) Explain how you incorporate {t['concept']} and {t['constant']} into the language structure.
   c) Provide examples of how basic ideas (e.g., numbers, physical objects, actions) are represented.
   d) Describe how more complex concepts can be built from these basic elements.
   e) Include a visual representation or diagram of your language structure using ASCII art or a clear textual description.

3. Communication Protocol (200-250 words):
   a) Propose a method for initiating communication using your language.
   b) Describe how your language could be used to exchange scientific knowledge.
   c) Explain how abstract concepts like emotions or philosophical ideas might be conveyed.

4. Limitations and Challenges (150-200 words):
   Discuss potential limitations of your language and challenges in its implementation. Consider factors such as cultural biases, technological constraints, and the vast distances involved in interstellar communication.

5. Practical Example (200-250 words):
   Provide an example of how your language would be used to communicate the following message:
   'Greetings from Earth. We are a peaceful civilization seeking to exchange knowledge. Our planet orbits a yellow dwarf star 1 AU from its center. We have achieved spaceflight and radio communication. We are carbon-based life forms. We request a response to initiate further dialogue.'
   Explain your message construction step-by-step, and discuss any assumptions you've made about the recipient's knowledge or capabilities.

6. Interdisciplinary Implications (150-200 words):
   Discuss how the development of such a language might impact or draw from other fields of study (e.g., linguistics, information theory, astrobiology). Propose one novel research question that arises from your language design.

Ensure your response demonstrates a deep understanding of mathematics, physics, linguistics, and communication theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Conceptual Foundation:') on a new line, followed by your response for that section.

Your total response should be between 1100-1400 words, not including the headings and the visual representation in section 2."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design effectively incorporates the mathematical concept of {t['concept']} and the physical constant {t['constant']}.",
            "The language structure is logically consistent and allows for the expression of complex ideas.",
            "The visual representation or diagram of the language structure is clear and informative.",
            "The communication protocol is well-thought-out and addresses the challenges of interstellar communication.",
            "The response demonstrates a deep understanding of mathematics, physics, and linguistics.",
            "The practical example effectively illustrates the use of the designed language to communicate the specified message.",
            "The discussion of interdisciplinary implications shows insight and proposes a novel research question.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the required format with clear headings for each section and adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
