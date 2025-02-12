import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'languages': ['English', 'Japanese', 'Swahili'],
                'sentences': [
                    'The cat chased the mouse in the garden.',
                    '猫が庭でネズミを追いかけた。',
                    'Paka aliwinda panya bustanini.'
                ]
            },
            '2': {
                'languages': ['Arabic', 'Russian', 'Quechua'],
                'sentences': [
                    'الطفل أكل التفاحة في المدرسة.',
                    'Учитель дал книгу ученику в классе.',
                    'Wayna urquta siqaspa inti lluqsimushaqta rikurqan.'
                ]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform semantic role labeling on the following sentences from different languages, then analyze and compare the results to uncover cross-linguistic patterns:

Semantic role labeling is the process of identifying the semantic relationships between predicates (usually verbs) and their associated participants and properties. Common semantic roles include Agent (the doer of the action), Patient (the entity affected by the action), Instrument (the means by which an action is performed), Location (where the action occurs), and Time (when the action occurs).

{', '.join(t['languages'])}:
{' '.join(t['sentences'])}

Your response should include:

1. Semantic Role Labeling (300-350 words):
   For each sentence:
   a) Identify the predicate and its arguments.
   b) Label each argument with its semantic role (e.g., Agent, Patient, Instrument, Location, Time).
   c) Explain your reasoning, especially for any challenging or ambiguous cases.

2. Cross-linguistic Analysis (250-300 words):
   a) Compare the semantic role structures across the given languages.
   b) Identify any similarities or differences in how semantic roles are expressed.
   c) Discuss any language-specific features that affect semantic role realization.

3. Theoretical Implications (200-250 words):
   a) Discuss how your findings relate to theories of universal grammar or linguistic universals.
   b) Explain any challenges to these theories posed by your analysis.
   c) Propose a hypothesis about semantic role realization across languages based on your observations.

4. Computational Modeling (200-250 words):
   a) Describe an approach for automatically performing cross-lingual semantic role labeling.
   b) Explain potential challenges in implementing such a system.
   c) Suggest ways to evaluate the performance of your proposed model.

5. Linguistic Insights (150-200 words):
   a) Discuss what your analysis reveals about the relationship between syntax and semantics across languages.
   b) Explain how this information could be useful for machine translation or other NLP tasks.

Ensure your response demonstrates a deep understanding of linguistic principles, semantic theories, and computational approaches to language analysis. Use appropriate terminology and provide clear explanations for complex concepts. Be thorough in your analysis while maintaining scientific rigor.

Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate word counts.",
            "The semantic role labeling is accurate and well-explained for each sentence.",
            "The cross-linguistic analysis identifies meaningful patterns and differences across the given languages.",
            "The discussion of theoretical implications demonstrates a deep understanding of linguistic theories.",
            "The proposed computational modeling approach is plausible and well-reasoned.",
            "The linguistic insights section provides valuable observations about the relationship between syntax and semantics.",
            "The response demonstrates a high level of expertise in linguistics and computational language analysis.",
            "The analysis is thorough, scientifically rigorous, and uses appropriate terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0