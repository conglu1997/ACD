import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_problems = [
            {
                'problem': 'Word sense disambiguation',
                'context': 'Determining the correct meaning of polysemous words in context'
            },
            {
                'problem': 'Sentiment analysis',
                'context': 'Identifying and categorizing opinions expressed in text'
            },
            {
                'problem': 'Named entity recognition',
                'context': 'Identifying and classifying named entities (e.g., person names, organizations) in text'
            },
            {
                'problem': 'Text summarization',
                'context': 'Generating concise and coherent summaries of longer texts'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(nlp_problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a semantic network-based language model and apply it to the natural language processing problem of {t['problem']}. Your response should include the following sections:

1. Semantic Network Design (250-300 words):
   a) Describe the key components and structure of your semantic network.
   b) Explain how your network represents lexical, syntactic, and semantic information.
   c) Discuss how your network incorporates context and relationships between concepts.
   d) Provide a simple diagram or schematic representation of your semantic network structure. The diagram should include at least 5 nodes and their connections, clearly labeled with the type of information they represent.

2. Cognitive Foundations (200-250 words):
   a) Explain how your semantic network model aligns with cognitive theories of language processing.
   b) Discuss any assumptions or simplifications in your model compared to human cognition.
   c) Describe how your model accounts for phenomena such as semantic priming or spreading activation.

3. Implementation Approach (200-250 words):
   a) Outline the algorithmic approach for implementing your semantic network model.
   b) Discuss data structures and computational techniques you would use.
   c) Address scalability and efficiency considerations for large-scale language processing.
   d) Provide a small code snippet or pseudocode (10-15 lines) illustrating a key part of your implementation, such as node creation or relationship traversal.

4. Application to {t['problem']} (250-300 words):
   a) Explain how your semantic network model can be applied to solve the given NLP problem.
   b) Describe the specific mechanisms or algorithms your model would use for this task.
   c) Discuss potential advantages of your approach compared to traditional methods.
   d) Address any limitations or challenges in applying your model to this problem.

5. Evaluation and Testing (150-200 words):
   a) Propose a method for evaluating the performance of your model on the given NLP task.
   b) Describe a potential experiment or benchmark to test your model's effectiveness.
   c) Discuss how you would measure and interpret the results.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications or biases that might arise from your semantic network model.
   b) Propose guidelines or safeguards to address these concerns in practical applications.

Ensure your response demonstrates a deep understanding of semantic networks, cognitive linguistics, and natural language processing. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section. Your total response should be between 1150-1450 words, not including the diagram and code snippet."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of semantic networks and their application to NLP.",
            "The semantic network design is well-explained and incorporates lexical, syntactic, and semantic information.",
            "The diagram includes at least 5 nodes with clear labels and connections.",
            "The cognitive foundations of the model are clearly articulated and aligned with established theories.",
            "The implementation approach is feasible and addresses scalability concerns.",
            "A relevant code snippet or pseudocode is provided to illustrate a key part of the implementation.",
            f"The application to {t['problem']} is well-reasoned and demonstrates potential advantages.",
            "The evaluation method and ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
