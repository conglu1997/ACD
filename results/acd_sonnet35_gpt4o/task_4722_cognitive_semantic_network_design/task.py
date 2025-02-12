import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_principle': 'Embodied Cognition',
                'linguistic_focus': 'Metaphor Theory',
                'ai_application': 'Sentiment Analysis',
                'example_sentence': 'The stock market is soaring to new heights.'
            },
            {
                'cognitive_principle': 'Prototype Theory',
                'linguistic_focus': 'Frame Semantics',
                'ai_application': 'Machine Translation',
                'example_sentence': 'She broke the news to her family over dinner.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel semantic network architecture incorporating the cognitive linguistics principle of {t['cognitive_principle']}, with a focus on {t['linguistic_focus']}, optimized for AI language processing in the context of {t['ai_application']}. Your response should include:

1. Architecture Overview (250-300 words):
   a) Describe the key components and structure of your semantic network.
   b) Explain how it incorporates the specified cognitive principle and linguistic focus.
   c) Discuss how it is optimized for the given AI application.
   d) Provide a high-level diagram or description of your network architecture.

2. Node and Edge Design (200-250 words):
   a) Detail the types of nodes in your network and the information they encode.
   b) Explain the nature of the edges and how they represent semantic relationships.
   c) Provide examples of how your design reflects the cognitive principle and linguistic focus.
   d) Illustrate with at least one specific node-edge-node example related to the given example sentence: "{t['example_sentence']}"

3. Information Processing (200-250 words):
   a) Describe how information flows through your network.
   b) Explain how your architecture handles ambiguity and context.
   c) Discuss any novel inference mechanisms in your design.
   d) Provide a step-by-step example of how your network would process the given example sentence.

4. Learning and Adaptation (200-250 words):
   a) Explain how your network can learn and update its structure from new data.
   b) Describe any bio-inspired learning mechanisms you've incorporated.
   c) Discuss how your architecture balances stability and plasticity.
   d) Provide an example of how your network might adapt when exposed to a new metaphor or frame.

5. Application to AI Task (200-250 words):
   a) Provide a detailed example of how your network would process a specific input for the given AI application.
   b) Analyze the potential advantages of your approach compared to traditional methods.
   c) Discuss any limitations or potential issues with your design.
   d) Propose a specific metric to quantify the improvement your system offers over existing approaches.
   e) Provide a quantitative estimate of the expected performance improvement over traditional methods, with justification.
   f) Discuss potential failure modes of your proposed architecture.

6. Evaluation and Testing (150-200 words):
   a) Propose methods to evaluate the performance of your semantic network.
   b) Describe potential experiments to test its efficacy in the given AI application.
   c) Suggest metrics for measuring improvements in language understanding or generation.
   d) Outline a hypothetical dataset that would be ideal for testing your system.
   e) Propose a novel metric specifically for evaluating the effectiveness of your semantic network in the given AI application.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of implementing your semantic network architecture.
   b) Propose two potential future enhancements or extensions of your design.
   c) Speculate on how this approach might influence the development of AI language models.
   d) Address potential dual-use concerns and propose safeguards.

Ensure your response demonstrates a deep understanding of cognitive linguistics, semantic networks, and artificial intelligence. Be creative and innovative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1350-1700 words.

Include a final section titled 'Summary' (50-100 words) that concisely recaps the key innovations, potential impact, and estimated performance improvement of your semantic network architecture."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response incorporates the cognitive principle of {t['cognitive_principle']} and focuses on {t['linguistic_focus']}.",
            f"The semantic network design is clearly optimized for {t['ai_application']}.",
            f"The design includes a specific example using the sentence: '{t['example_sentence']}'",
            "The architecture demonstrates a novel and creative approach to semantic networks.",
            "The response shows a deep understanding of cognitive linguistics, semantic networks, and artificial intelligence.",
            "The design is scientifically plausible and well-reasoned.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The response includes specific examples, diagrams, or illustrations as requested.",
            "The response provides a quantitative estimate of performance improvement over traditional methods.",
            "The response discusses potential failure modes of the proposed architecture.",
            "The response proposes a novel metric for evaluating the semantic network's effectiveness.",
            "The total word count is between 1350-1700 words.",
            "The response includes a concise summary section as specified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
