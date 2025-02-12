class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "pre_singularity_language": "English",
                "trigger_event": "Global adoption of brain-computer interfaces",
                "time_frame": "50 years"
            },
            "2": {
                "pre_singularity_language": "Mandarin Chinese",
                "trigger_event": "Discovery of alien linguistic artifacts",
                "time_frame": "100 years"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation of language evolution leading to and following a hypothetical 'syntactic singularity', where the complexity and generative power of a language's syntax increases exponentially. Your simulation should start with {t['pre_singularity_language']} as the base language and be triggered by the event: {t['trigger_event']}. Model the evolution over a {t['time_frame']} period.

        Your response should include the following sections:

        1. Theoretical Framework (250-300 words):
           a) Define the concept of a 'syntactic singularity' and its potential implications for language and cognition.
           b) Explain how the trigger event could lead to a syntactic singularity.
           c) Discuss relevant theories from linguistics and cognitive science that inform your simulation design.

        2. Simulation Design (300-350 words):
           a) Outline the key components and parameters of your simulation.
           b) Explain how your simulation models the increasing complexity of syntax over time.
           c) Describe any novel algorithms or approaches used in your simulation.
           d) Discuss how your simulation accounts for the interaction between language change and cognitive/social factors.

        3. Language Evolution Stages (250-300 words):
           a) Describe at least three distinct stages in the evolution towards and beyond the syntactic singularity.
           b) For each stage, provide an example sentence showcasing the increasing syntactic complexity.
           c) Explain how these changes in syntax might affect semantics and pragmatics.

        4. Cognitive and Social Implications (200-250 words):
           a) Analyze how the evolving language might impact cognitive processes and social interactions.
           b) Discuss potential challenges in communication and comprehension as the language complexity increases.
           c) Speculate on how society might adapt to or cope with these linguistic changes.

        5. Post-Singularity Scenarios (200-250 words):
           a) Describe two potential outcomes of the syntactic singularity in your simulation.
           b) Discuss whether the post-singularity language would still be recognizable or usable by pre-singularity speakers.
           c) Speculate on the long-term implications for human cognition and communication.

        6. Simulation Validation and Limitations (150-200 words):
           a) Propose methods to validate your simulation against current theories of language evolution.
           b) Discuss the limitations of your simulation and potential areas for improvement.
           c) Suggest how empirical data could be collected to refine the simulation, if possible.

        Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and complex systems modeling.",
            "The simulation design is innovative and plausible, incorporating relevant theories and novel approaches.",
            "The language evolution stages are clearly described with appropriate examples.",
            "The cognitive and social implications of the syntactic singularity are thoroughly analyzed.",
            "The post-singularity scenarios are creative and logically consistent with the simulation design.",
            "The response addresses the validation and limitations of the simulation appropriately.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
