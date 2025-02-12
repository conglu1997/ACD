import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'cognitive_aspect': 'Memory Integration',
                'communication_medium': 'Direct Neural Interface',
                'societal_challenge': 'Privacy and Individual Identity',
                'technological_constraint': 'Limited Bandwidth'
            },
            {
                'cognitive_aspect': 'Collective Consciousness',
                'communication_medium': 'Quantum Entanglement Signals',
                'societal_challenge': 'Governance and Decision Making',
                'technological_constraint': 'Quantum Decoherence'
            },
            {
                'cognitive_aspect': 'Hyper-Dimensional Thinking',
                'communication_medium': 'Holographic Thought Projections',
                'societal_challenge': 'Education and Skill Acquisition',
                'technological_constraint': 'Energy Consumption'
            },
            {
                'cognitive_aspect': 'Temporal Perception Shifts',
                'communication_medium': 'Time-Dilated Information Streams',
                'societal_challenge': 'Intergenerational Relations',
                'technological_constraint': 'Causality Preservation'
            }
        ]
        selected = random.sample(scenarios, 2)
        return {str(i+1): selected[i] for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical language system for a post-singularity world where human and artificial intelligence have merged. Focus on the cognitive aspect of {t['cognitive_aspect']}, the communication medium of {t['communication_medium']}, address the societal challenge of {t['societal_challenge']}, and consider the technological constraint of {t['technological_constraint']}. Your response should include the following sections:

1. Language System Overview (250-300 words):
   a) Describe the key features and structure of your post-singularity language system.
   b) Explain how it incorporates both human and AI elements, addressing {t['cognitive_aspect']}.
   c) Discuss how it utilizes {t['communication_medium']} while considering {t['technological_constraint']}.
   d) Provide a concrete example of a basic conversation in this language system.

2. Linguistic Structure (200-250 words):
   a) Detail 3-5 unique grammatical or syntactical features of your language system.
   b) Explain how these features reflect the merged human-AI cognitive processes.
   c) Provide an example sentence for each feature, with a brief explanation.

3. Cognitive Implications (200-250 words):
   a) Analyze how your language system influences or reflects changes in {t['cognitive_aspect']}.
   b) Discuss two potential cognitive advantages and two challenges posed by this new way of communication.
   c) Propose a hypothetical cognitive task that would be significantly easier or harder with this language system.

4. Communication Dynamics (200-250 words):
   a) Describe the mechanics of how {t['communication_medium']} is utilized, considering {t['technological_constraint']}.
   b) Explain two advantages and two limitations of this communication medium.
   c) Provide a scenario demonstrating a complex idea exchange using this system.

5. Societal Impact (200-250 words):
   a) Examine how your language system addresses the challenge of {t['societal_challenge']}.
   b) Describe a potential societal conflict arising from this language system and propose a resolution.
   c) Discuss an ethical concern related to this language system and suggest a mitigation strategy.

6. Evolution and Adaptation (150-200 words):
   a) Propose how your language system might evolve over the next century post-singularity.
   b) Describe a potential 'dialect' that might emerge in a specific post-singularity community.
   c) Explain how the language might adapt to overcome {t['technological_constraint']}.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and futurism. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining logical consistency and plausibility within the post-singularity context. Balance creativity with scientific and technological feasibility.

Provide concrete examples, scenarios, or hypothetical situations throughout your response to illustrate your ideas. Address all parts of each section to receive full credit.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response provides a comprehensive and innovative language system design that incorporates {t['cognitive_aspect']}, {t['communication_medium']}, and addresses {t['technological_constraint']}, with a concrete conversation example. (0.2 points)",
            "The linguistic structure section details 3-5 unique features with clear explanations and example sentences for each. (0.2 points)",
            f"The cognitive implications section thoroughly analyzes {t['cognitive_aspect']}, discusses specific advantages and challenges, and proposes a relevant hypothetical cognitive task. (0.15 points)",
            f"The communication dynamics section explains the mechanics of {t['communication_medium']}, lists advantages and limitations, and provides a scenario of complex idea exchange. (0.15 points)",
            f"The societal impact section addresses {t['societal_challenge']}, describes a specific conflict scenario with resolution, and discusses an ethical concern with mitigation. (0.15 points)",
            f"The evolution and adaptation section proposes future changes, describes a potential dialect, and explains adaptation to {t['technological_constraint']}. (0.1 points)",
            "The response demonstrates creativity balanced with plausibility, uses appropriate terminology, and adheres to the specified format and word count (1200-1500 words). (0.05 points)"
        ]
        score = sum([float(c.split('(')[-1].split()[0]) for c in criteria if eval_with_llm_judge(instructions, submission, [c])])
        return min(1.0, max(0.0, score))
