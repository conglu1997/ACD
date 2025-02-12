import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            'confirmation_bias',
            'availability_heuristic',
            'anchoring_effect',
            'framing_effect',
            'dunning_kruger_effect',
            'bandwagon_effect',
            'sunk_cost_fallacy',
            'negativity_bias',
            'hindsight_bias',
            'overconfidence_effect'
        ]
        
        linguistic_aspects = [
            'lexical_choice',
            'syntactic_structure',
            'semantic_interpretation',
            'pragmatic_inference',
            'discourse_coherence'
        ]
        
        task1 = {
            'cognitive_bias': random.choice(cognitive_biases),
            'linguistic_aspect': random.choice(linguistic_aspects)
        }
        
        task2 = {
            'cognitive_bias': random.choice(cognitive_biases),
            'linguistic_aspect': random.choice(linguistic_aspects)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual language model that incorporates the cognitive bias of '{t['cognitive_bias']}' in the linguistic aspect of '{t['linguistic_aspect']}'. Your response should include:

1. Cognitive Bias Explanation (100-150 words):
   Briefly explain the chosen cognitive bias and its typical manifestation in human cognition.

2. Linguistic Aspect Analysis (100-150 words):
   Analyze how the chosen linguistic aspect typically functions in natural language processing and generation.

3. Integration Mechanism (200-250 words):
   Describe in detail how you would integrate the cognitive bias into the language model's processing of the chosen linguistic aspect. Include any necessary algorithms, rules, or heuristics.

4. Example Generation (100-150 words):
   Provide an example of how your model would process or generate language, demonstrating the influence of the cognitive bias on the linguistic aspect.

5. Comparative Analysis (150-200 words):
   Compare and contrast how your biased language model's output might differ from that of a traditional, unbiased language model. Discuss potential implications for AI systems and human-AI interaction.

6. Ethical Considerations (100-150 words):
   Discuss potential ethical implications of implementing cognitive biases in AI language models, considering both positive and negative consequences.

7. Research Applications (100-150 words):
   Propose a potential research application or experiment using your biased language model that could contribute to our understanding of human cognition or improve AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive bias and linguistic aspect.",
            "The integration mechanism is well-explained, innovative, and scientifically plausible.",
            "The example effectively illustrates the influence of the cognitive bias on the linguistic aspect.",
            "The comparative analysis shows insightful understanding of both traditional and biased language models.",
            "The ethical considerations are thoughtfully explored, considering multiple perspectives.",
            "The proposed research application is innovative and has potential to contribute to cognitive science or AI.",
            "The response maintains a high level of interdisciplinary integration throughout.",
            "The answer is well-structured, clear, and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
