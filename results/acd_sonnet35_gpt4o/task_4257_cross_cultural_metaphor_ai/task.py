import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time",
            "love",
            "death",
            "freedom",
            "knowledge"
        ]
        cultures = [
            "Chinese",
            "Navajo",
            "Greek",
            "Egyptian",
            "Maori"
        ]
        example_metaphors = {
            "Chinese": {"time": "Time is money", "love": "Love is a journey"},
            "Navajo": {"knowledge": "Knowledge is a mountain", "death": "Death is going home"},
            "Greek": {"freedom": "Freedom is a bird", "love": "Love is a flame"},
            "Egyptian": {"time": "Time is a river", "death": "Death is a doorway"},
            "Maori": {"knowledge": "Knowledge is a treasure", "freedom": "Freedom is the open sea"}
        }
        task1 = {
            "concept": random.choice(concepts),
            "culture1": random.choice(cultures),
            "culture2": random.choice(cultures)
        }
        task2 = {
            "concept": random.choice(concepts),
            "culture1": random.choice(cultures),
            "culture2": random.choice(cultures)
        }
        task1["example1"] = example_metaphors[task1["culture1"]].get(task1["concept"], "")
        task1["example2"] = example_metaphors[task1["culture2"]].get(task1["concept"], "")
        task2["example1"] = example_metaphors[task2["culture1"]].get(task2["concept"], "")
        task2["example2"] = example_metaphors[task2["culture2"]].get(task2["concept"], "")
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting metaphors across different cultures and languages. Then, use this system to analyze and create metaphors for the concept of {t['concept']} in both {t['culture1']} and {t['culture2']} cultures. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-cultural metaphor generation and interpretation.
   b) Explain how your system integrates linguistic, cognitive, and cultural knowledge.
   c) Detail the processes involved in metaphor generation and interpretation.
   d) Discuss how your system handles cultural nuances and linguistic differences.

2. Cognitive and Linguistic Foundations (250-300 words):
   a) Explain the cognitive theories of metaphor that inform your system's design.
   b) Describe how your system models the relationship between language, thought, and culture.
   c) Discuss how your approach accounts for differences in conceptual metaphors across cultures.

3. Cultural Knowledge Integration (200-250 words):
   a) Explain how your system acquires and represents cultural knowledge.
   b) Describe the methods used to ensure cultural sensitivity and accuracy.
   c) Discuss how your system handles potential conflicts or misunderstandings between cultures.

4. Metaphor Analysis (250-300 words):
   a) Use your system to analyze existing metaphors for {t['concept']} in {t['culture1']} and {t['culture2']} cultures.
   b) Compare and contrast the metaphors from each culture, explaining their cultural significance.
   c) Discuss how these metaphors reflect different worldviews or values.
   d) Consider these example metaphors in your analysis (if available):
      {t['culture1']}: {t['example1']}
      {t['culture2']}: {t['example2']}

5. Novel Metaphor Generation (200-250 words):
   a) Use your system to generate a novel metaphor for {t['concept']} that would be meaningful in both {t['culture1']} and {t['culture2']} cultures.
   b) Explain the reasoning behind the generated metaphor.
   c) Discuss potential challenges in creating cross-culturally relevant metaphors.

6. Evaluation and Limitations (150-200 words):
   a) Propose methods for evaluating the effectiveness and cultural accuracy of your system.
   b) Discuss potential limitations or biases in your approach.
   c) Suggest areas for future improvement or research.

7. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI for cross-cultural communication and interpretation.
   b) Address potential risks of cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible use of such technology in real-world applications.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and AI technologies. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and AI technologies",
            "Provides a detailed and plausible system architecture for cross-cultural metaphor generation and interpretation",
            "Explains cognitive theories of metaphor and their application in the system design",
            "Describes methods for cultural knowledge integration and ensuring cultural sensitivity",
            "Includes a comparative analysis of metaphors for the given concept in the specified cultures, referencing the provided examples if available",
            "Generates a novel, cross-culturally relevant metaphor for the given concept",
            "Discusses evaluation methods, limitations, and ethical considerations of the proposed system",
            "Uses appropriate technical terminology and provides clear explanations for complex concepts",
            "Adheres to the specified word count and formatting requirements",
            "Includes all required sections with appropriate content and depth"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
