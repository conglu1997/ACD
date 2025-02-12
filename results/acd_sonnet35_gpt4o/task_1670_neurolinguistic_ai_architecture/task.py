class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "brain_region": "Broca's area",
                "linguistic_function": "Syntactic processing",
                "ai_task": "Part-of-speech tagging and syntactic parsing",
                "example_sentence": "The cat chased the mouse through the garden."
            },
            "2": {
                "brain_region": "Wernicke's area",
                "linguistic_function": "Semantic processing",
                "ai_task": "Word sense disambiguation and semantic role labeling",
                "example_sentence": "The bank by the river had low interest rates."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture for language processing inspired by how the human brain processes language, specifically focusing on the function of {t['brain_region']} in {t['linguistic_function']}. Your goal is to create an AI system capable of performing {t['ai_task']}. Use the example sentence "{t['example_sentence']}" to illustrate your design's capabilities.

Your response should include:

1. Neuroscientific Basis (200-250 words):
   a) Explain the key functions of {t['brain_region']} in human language processing.
   b) Describe the neural mechanisms involved in {t['linguistic_function']}.
   c) Discuss any relevant neuroscientific theories or models related to this brain region and function.
   d) Explain how these principles could be applied to AI language processing.

2. AI Architecture Design (300-350 words):
   a) Propose a novel neural network architecture inspired by the neuroscientific principles you described.
   b) Explain how your design mimics or incorporates specific aspects of {t['brain_region']}'s function.
   c) Describe at least three key components of your architecture and their interactions.
   d) Explain how your architecture is specifically tailored to perform {t['ai_task']}.
   e) Illustrate how your architecture would process the example sentence provided.

3. Implementation Strategy (200-250 words):
   a) Outline a potential method for implementing your neural network architecture.
   b) Discuss any novel algorithms or data structures required.
   c) Explain how your implementation could be trained or optimized.
   d) Propose a dataset structure and size for training your model.

4. Comparative Analysis (150-200 words):
   Compare your proposed architecture with a current state-of-the-art approach for {t['ai_task']} in terms of:
   a) Potential advantages and limitations
   b) Biological plausibility
   c) Scalability and adaptability to other language processing tasks
   d) Expected performance on the given example sentence

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical considerations in developing AI systems that closely mimic human brain functions.
   b) Explore how your architecture might impact our understanding of human language processing.
   c) Propose potential applications of your system beyond natural language processing tasks.

Ensure your response demonstrates a deep understanding of both neuroscience and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations. Use appropriate technical terminology throughout your response and provide clear explanations where necessary.

Format your response with clear headings for each section and include the word count for each section in parentheses at the end. Your total response should be between 1000-1250 words.

Remember to refer to the example sentence when explaining your architecture's capabilities and expected performance.

Scoring Criteria:
Your response will be evaluated based on the depth of neuroscientific understanding, the innovation and feasibility of your AI architecture, the clarity and completeness of your implementation strategy, the quality of your comparative analysis, and the thoughtfulness of your ethical considerations. Adherence to the specified format and word count will also be considered."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['brain_region']} and its role in {t['linguistic_function']}, with clear explanations of relevant neuroscientific principles and their application to AI.",
            f"The proposed AI architecture innovatively incorporates principles from neuroscience related to {t['linguistic_function']} and is well-designed for {t['ai_task']}, with at least three key components clearly described.",
            f"The architecture's processing of the example sentence \"{t['example_sentence']}\" is clearly illustrated and demonstrates the system's capabilities.",
            "The implementation strategy is well-thought-out, feasible, and includes specific details about training data, novel algorithms, and optimization methods.",
            "The comparative analysis shows a good understanding of current AI approaches and provides a balanced comparison in terms of advantages, limitations, biological plausibility, and expected performance.",
            "The ethical and practical implications are thoughtfully considered, with specific examples of potential applications and impacts on our understanding of human language processing.",
            "The response adheres to the specified format, including clear headings and word counts for each section, falls within the total word count range of 1000-1250 words, and consistently uses appropriate scientific terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
