import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Proto-Indo-European",
                "time_period": "4500-2500 BCE",
                "key_features": ["Synthetic", "Fusional", "Noun cases", "Verb aspects"]
            },
            {
                "name": "Classical Latin",
                "time_period": "75 BCE - 3rd century CE",
                "key_features": ["Synthetic", "Fusional", "Noun cases", "Verb conjugations"]
            },
            {
                "name": "Old English",
                "time_period": "5th - 11th century CE",
                "key_features": ["Synthetic", "Fusional", "Noun cases", "Grammatical gender"]
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language evolution simulator and use it to model an alternate linguistic history for {t['name']}. Your task involves the following steps:

1. Simulator Design (250-300 words):
   a) Describe the key components and mechanisms of your language evolution simulator.
   b) Explain how it models changes in phonology, morphology, syntax, and semantics over time.
   c) Discuss how your simulator incorporates factors such as language contact, sociolinguistic variables, and historical events.
   d) Provide a simple flowchart or pseudocode representation of your simulator's main algorithm. Use ASCII characters or a structured text description for the flowchart.

2. Historical Context (150-200 words):
   a) Briefly describe the actual historical development of {t['name']} from {t['time_period']} to the present day.
   b) Identify key linguistic changes and the factors that influenced them.

3. Alternate History Simulation (250-300 words):
   a) Using your simulator, model an alternate history for {t['name']} from {t['time_period']} to the present day.
   b) Introduce a significant historical change or counterfactual scenario that would affect language development.
   c) Describe the resulting alternate language, highlighting how it differs from the actual historical outcome.
   d) Explain the chain of linguistic changes that led to this alternate form.
   e) Provide at least two concrete examples of words or phrases in your alternate language, showing how they evolved from their original form.

4. Linguistic Analysis (200-250 words):
   a) Compare and contrast the features of your alternate language with those of the actual historical language.
   b) Analyze how the alternate history affected the development of at least three of the following: phonology, morphology, syntax, semantics, or pragmatics.
   c) Discuss any unexpected or emergent features in your alternate language.

5. Implications and Applications (150-200 words):
   a) Discuss how your simulator and alternate history model could contribute to our understanding of linguistic change.
   b) Propose two potential applications of your simulator in fields such as historical linguistics, language preservation, or language pedagogy.
   c) Suggest how this approach might inform predictions about future language evolution.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using simulations to model alternate linguistic histories.
   b) Address concerns related to linguistic diversity, cultural heritage, and the potential misuse of such technology.

Ensure your response demonstrates a deep understanding of historical linguistics, computational modeling, and creative problem-solving. Use appropriate linguistic terminology and provide clear explanations. Be creative in your alternate history scenario while maintaining linguistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words, not including the flowchart or pseudocode representation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a detailed design of a language evolution simulator with clear explanations of its components and mechanisms, including a flowchart or pseudocode representation.",
            "The alternate history scenario should be creative yet linguistically plausible, demonstrating a deep understanding of historical linguistics.",
            "The response must provide at least two concrete examples of words or phrases in the alternate language, showing their evolution from the original form.",
            "The linguistic analysis should accurately compare the alternate language with the actual historical language, using appropriate terminology and covering at least three linguistic aspects (e.g., phonology, morphology, syntax).",
            "The response should demonstrate interdisciplinary knowledge application, combining linguistics, historical analysis, and computational modeling.",
            "Ethical considerations related to simulating alternate linguistic histories must be addressed thoughtfully.",
            "The response must adhere to the specified word limits for each section and the overall word count (1100-1400 words, excluding flowchart/pseudocode)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
