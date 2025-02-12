import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            ("Physics", "Biology"),
            ("Chemistry", "Psychology"),
            ("Mathematics", "Sociology"),
            ("Computer Science", "Ecology"),
            ("Neuroscience", "Economics")
        ]
        concepts = {
            "Physics": ["gravity", "entropy", "quantum entanglement"],
            "Biology": ["natural selection", "symbiosis", "cellular respiration"],
            "Chemistry": ["catalysis", "bonding", "phase transition"],
            "Psychology": ["cognitive dissonance", "habituation", "intrinsic motivation"],
            "Mathematics": ["fractals", "chaos theory", "topology"],
            "Sociology": ["social stratification", "cultural diffusion", "collective behavior"],
            "Computer Science": ["recursion", "parallel processing", "machine learning"],
            "Ecology": ["food web", "succession", "carrying capacity"],
            "Neuroscience": ["neuroplasticity", "synaptic pruning", "default mode network"],
            "Economics": ["supply and demand", "opportunity cost", "game theory"]
        }
        
        task1 = random.choice(domains)
        task2 = random.choice(domains)
        while task2 == task1:
            task2 = random.choice(domains)
        
        return {
            "1": {
                "source_domain": task1[0],
                "target_domain": task1[1],
                "source_concept": random.choice(concepts[task1[0]]),
                "target_concept": random.choice(concepts[task1[1]])
            },
            "2": {
                "source_domain": task2[0],
                "target_domain": task2[1],
                "source_concept": random.choice(concepts[task2[0]]),
                "target_concept": random.choice(concepts[task2[1]])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and analyze a metaphor that connects the concept of {t['source_concept']} from {t['source_domain']} to the concept of {t['target_concept']} in {t['target_domain']}. Your response should include:

1. Metaphor Generation (100-150 words):
   Create a clear and concise metaphor that relates {t['source_concept']} to {t['target_concept']}. The metaphor should be original and insightful, demonstrating a deep understanding of both concepts.

2. Conceptual Analysis (200-250 words):
   a) Explain the key aspects of {t['source_concept']} in {t['source_domain']}.
   b) Describe the main features of {t['target_concept']} in {t['target_domain']}.
   c) Analyze how your metaphor connects these concepts, highlighting similarities and potential insights gained from this connection.

3. Implications and Applications (150-200 words):
   a) Discuss potential implications of this metaphorical connection for understanding or research in {t['target_domain']}.
   b) Propose a novel research question or hypothesis inspired by this metaphor.
   c) Suggest a practical application or experiment that could test or utilize this metaphorical connection.

4. Limitations and Critique (100-150 words):
   a) Identify potential limitations or weaknesses of the metaphor.
   b) Discuss how these limitations might affect the metaphor's utility in scientific or educational contexts.
   c) Propose a way to address or mitigate one of these limitations.

Ensure your response demonstrates a deep understanding of both domains and concepts involved. Use appropriate terminology and provide clear explanations for complex ideas. Be creative and thought-provoking in your approach while maintaining scientific accuracy.

Your total response should be between 550-750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all four required sections: Metaphor Generation, Conceptual Analysis, Implications and Applications, and Limitations and Critique.",
            "The generated metaphor is original, clear, and effectively connects the two given concepts.",
            "The conceptual analysis demonstrates a deep understanding of both the source and target concepts and their respective domains.",
            "The implications and applications section provides insightful ideas for future research or practical use of the metaphorical connection.",
            "The limitations and critique section shows critical thinking about the metaphor's strengths and weaknesses.",
            "The response uses appropriate terminology from both domains and explains complex ideas clearly.",
            "The overall response is creative and thought-provoking while maintaining scientific accuracy.",
            "The total response is between 550-750 words."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        return float(result) if result is not None else None
