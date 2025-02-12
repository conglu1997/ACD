import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_tasks = [
            {
                "name": "Semantic priming",
                "description": "Predict the facilitation effect in word recognition when a semantically related word is presented beforehand.",
                "example": "Given the prime word 'doctor', predict the recognition time for the target word 'nurse' compared to an unrelated word like 'table'."
            },
            {
                "name": "Lexical decision",
                "description": "Simulate the process of distinguishing real words from non-words, accounting for frequency and neighborhood effects.",
                "example": "Predict the response time and accuracy for classifying 'chair' (high-frequency word), 'zealot' (low-frequency word), and 'blick' (non-word)."
            },
            {
                "name": "Word association",
                "description": "Model the process of generating semantically related words given a cue word, considering both direct and indirect associations.",
                "example": "Given the cue word 'sun', generate a list of associated words (e.g., 'bright', 'yellow', 'sky', 'warm') and explain the association strengths."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(cognitive_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and interacts with a human-like mental lexicon, incorporating findings from neurolinguistics. Then, use your system to solve the cognitive task of {t['name']}: {t['description']}

Example task application: {t['example']}

Your response should include the following sections:

1. Mental Lexicon AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how your system represents and organizes lexical information (e.g., words, meanings, associations).
   c) Detail how your system incorporates neurolinguistic findings on mental lexicon structure and access.
   d) Discuss any machine learning or neural network approaches used in your system.
   e) Provide a diagram or detailed description of your system's architecture.
   f) Cite at least one relevant scientific study or paper to support your system design.

2. Neurolinguistic Integration (200-250 words):
   a) Identify at least three specific neurolinguistic findings or theories that your system incorporates.
   b) Explain how each finding is implemented in your AI model.
   c) Discuss how your system accounts for individual differences in mental lexicons.

3. Cognitive Task Solution (250-300 words):
   a) Describe how you apply your AI system to solve the given cognitive task.
   b) Provide a step-by-step explanation of how your system processes the task.
   c) Discuss any specific algorithms or methods used for this task.
   d) Present a sample output or result from your system for this task, using the provided example.

4. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your AI system.
   b) Discuss how you would validate your system's performance against human data.
   c) Identify potential limitations or biases in your approach.

5. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for our understanding of human language processing.
   b) Propose two novel applications of your AI system in fields such as education, therapy, or human-computer interaction.
   c) Explore any ethical considerations related to simulating and interacting with mental lexicons.

6. Future Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your AI system.
   b) Discuss how emerging technologies or research in neuroscience might further improve mental lexicon modeling.
   c) Propose a novel research question that could be explored using your system.

Ensure your response demonstrates a deep understanding of neurolinguistics, artificial intelligence, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, and number your paragraphs within each section. Adhere strictly to the word count guidelines for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must design an AI system that accurately simulates and interacts with a human-like mental lexicon, incorporating findings from neurolinguistics",
            f"The system must be applied to solve the cognitive task of {t['name']}: {t['description']}, using the provided example",
            "The response should demonstrate a deep understanding of neurolinguistics, artificial intelligence, and cognitive science",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should be well-structured, following the outlined sections and word count guidelines",
            "At least one relevant scientific study or paper must be cited to support the system design",
            "The response must include a sample output or result for the given task example"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
