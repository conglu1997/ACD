import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_frameworks = [
            'Utilitarianism',
            'Kantian deontology',
            'Virtue ethics',
            'Existentialism',
            'Pragmatism',
            'Stoicism'
        ]
        societal_aspects = [
            'Governance',
            'Education',
            'Economy',
            'Justice system',
            'Healthcare',
            'Environmental policy'
        ]
        
        return {
            "1": {
                "framework": random.choice(philosophical_frameworks),
                "aspect": random.choice(societal_aspects)
            },
            "2": {
                "framework": random.choice(philosophical_frameworks),
                "aspect": random.choice(societal_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical society based on the philosophical framework of {t['framework']}, focusing particularly on the societal aspect of {t['aspect']}. Your response should include:

1. Philosophical Foundation (250-300 words):
   a) Explain the key principles of {t['framework']} and how they would form the basis of your society.
   b) Discuss how these principles would specifically influence the chosen aspect of {t['aspect']}.
   c) Address any potential conflicts or challenges in applying this philosophical framework to a real-world society.

2. Societal Design (350-400 words):
   a) Describe the structure and functioning of your hypothetical society, with a focus on {t['aspect']}.
   b) Explain how the philosophical principles are reflected in the society's institutions and practices.
   c) Discuss how this society would handle potential conflicts or ethical dilemmas related to {t['aspect']}.
   d) Compare and contrast your society's approach to {t['aspect']} with current real-world approaches.
   e) Provide a specific example or case study illustrating how your society would address a particular issue related to {t['aspect']}.

3. Implications and Consequences (250-300 words):
   a) Analyze the potential positive outcomes of implementing this philosophical framework in society, particularly in relation to {t['aspect']}.
   b) Discuss potential negative consequences or unintended effects that might arise.
   c) Consider how this society might interact with or be perceived by other societies with different philosophical foundations.

4. Implementation Strategy (200-250 words):
   a) Propose a step-by-step approach for transitioning a current society towards your hypothetical model.
   b) Discuss potential challenges in implementation and how they might be overcome.
   c) Suggest metrics or indicators to measure the success of the transition.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of designing and implementing a society based on a specific philosophical framework.
   b) Address concerns about individual freedom, diversity of thought, and potential ideological conflicts.
   c) Propose ethical guidelines for the use of philosophical principles in societal design.

6. Critical Analysis and Future Perspectives (200-250 words):
   a) Reflect on the limitations and potential biases in your societal design.
   b) Discuss how your society might evolve or adapt over time in response to changing circumstances or new philosophical insights.
   c) Consider potential technological advancements that could impact your proposed society and how it might adapt to them.
   d) Suggest areas for further philosophical or social research that could enhance the understanding and implementation of your proposed society.

Ensure your response demonstrates a deep understanding of the chosen philosophical framework and its potential real-world applications. Use appropriate terminology from philosophy and social sciences, providing clear explanations where necessary. Be creative and speculative in your approach while maintaining logical consistency and addressing practical considerations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['framework']} and its application to {t['aspect']}.",
            "The proposed society is logically consistent with the given philosophical framework.",
            "The analysis of implications and consequences is thorough and balanced.",
            "The implementation strategy is practical and well-reasoned.",
            "Ethical considerations are addressed thoughtfully and comprehensively.",
            "The critical analysis shows awareness of limitations and potential for future development.",
            "The response includes a specific example or case study related to the chosen societal aspect.",
            "The discussion of potential technological impacts is insightful and relevant.",
            "The response is well-structured, coherent, and demonstrates creativity while maintaining philosophical rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
