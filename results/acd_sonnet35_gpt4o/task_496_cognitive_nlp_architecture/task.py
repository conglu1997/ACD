import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_processes = [
            {
                "process": "Semantic parsing",
                "linguistic_aspect": "Compositional semantics",
                "cognitive_principle": "Mental models",
                "ai_technique": "Graph neural networks"
            },
            {
                "process": "Syntactic analysis",
                "linguistic_aspect": "Phrase structure grammar",
                "cognitive_principle": "Working memory",
                "ai_technique": "Recursive neural networks"
            },
            {
                "process": "Pragmatic interpretation",
                "linguistic_aspect": "Speech act theory",
                "cognitive_principle": "Theory of mind",
                "ai_technique": "Reinforcement learning"
            },
            {
                "process": "Discourse comprehension",
                "linguistic_aspect": "Cohesion and coherence",
                "cognitive_principle": "Schema theory",
                "ai_technique": "Transformers with attention mechanisms"
            }
        ]
        return {
            "1": random.choice(language_processes),
            "2": random.choice(language_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical cognitive architecture for natural language processing, focusing on the process of {t['process']}. Your task is to create a detailed proposal for this cognitive NLP architecture, addressing the following points:

1. Architecture Overview (200-250 words):
   - Describe the key components of your cognitive NLP architecture.
   - Explain how it incorporates the linguistic aspect of {t['linguistic_aspect']} ({TaskFamily.get_explanation(t['linguistic_aspect'])}).
   - Discuss how the architecture utilizes the cognitive principle of {t['cognitive_principle']} ({TaskFamily.get_explanation(t['cognitive_principle'])}).
   - Outline how the AI technique of {t['ai_technique']} ({TaskFamily.get_explanation(t['ai_technique'])}) is integrated into the system.

2. Processing Pipeline (250-300 words):
   - Detail the step-by-step process of how your architecture handles language input and generates output.
   - Explain how each component interacts with others in the pipeline.
   - Discuss how the chosen linguistic aspect, cognitive principle, and AI technique contribute to each step.

3. Cognitive Plausibility (200-250 words):
   - Analyze how your architecture aligns with current understanding of human language processing.
   - Identify potential divergences from human cognition and justify your design choices.
   - Discuss how your architecture could inform or be informed by cognitive science research.

4. Technical Implementation (200-250 words):
   - Propose a high-level technical implementation of your architecture.
   - Discuss potential challenges in implementing this system and suggest solutions.
   - Explain how the system could be trained or optimized.

5. Visual Representation (Include a description of 100-150 words):
   - Create a flowchart or diagram that visually represents your cognitive NLP architecture.
   - Explain the key elements and connections in your visual representation.

6. Comparative Analysis (200-250 words):
   - Compare your proposed architecture with at least one existing NLP model or cognitive architecture.
   - Discuss the similarities and differences, highlighting the unique aspects of your design.

7. Evaluation and Limitations (150-200 words):
   - Suggest methods to evaluate the performance and cognitive plausibility of your architecture.
   - Discuss the limitations of your approach and potential areas for improvement.
   - Propose one future research direction to enhance the architecture.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence as they relate to language processing. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def get_explanation(term: str) -> str:
        explanations = {
            "Compositional semantics": "the principle that the meaning of a complex expression is determined by the meanings of its constituent expressions and the rules used to combine them",
            "Phrase structure grammar": "a type of grammar that models the structure of sentences using hierarchical phrase structures",
            "Speech act theory": "a theory that describes how language can be used to perform actions, such as making requests or giving commands",
            "Cohesion and coherence": "linguistic properties that contribute to the overall unity and flow of a text or discourse",
            "Mental models": "cognitive representations of real, hypothetical, or imaginary situations",
            "Working memory": "a cognitive system for temporarily holding and manipulating information",
            "Theory of mind": "the ability to attribute mental states to oneself and others",
            "Schema theory": "a theory about how knowledge is acquired, processed, and organized",
            "Graph neural networks": "a type of neural network designed to work with graph-structured data",
            "Recursive neural networks": "neural networks that can process structured inputs with a tree-like topology",
            "Reinforcement learning": "a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize a reward",
            "Transformers with attention mechanisms": "a type of neural network architecture that uses self-attention to process sequential data"
        }
        return explanations.get(term, "")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of linguistics, cognitive science, and artificial intelligence principles related to language processing.",
            f"The proposed architecture clearly incorporates the linguistic aspect of {t['linguistic_aspect']}.",
            f"The architecture effectively utilizes the cognitive principle of {t['cognitive_principle']}.",
            f"The AI technique of {t['ai_technique']} is well-integrated into the system design.",
            "The processing pipeline is logically explained and shows clear interactions between components.",
            "The discussion of cognitive plausibility demonstrates critical thinking about human language processing.",
            "The technical implementation proposal is feasible and addresses potential challenges.",
            "A visual representation of the architecture is provided and clearly explained.",
            "The comparative analysis demonstrates knowledge of existing models or architectures.",
            "The evaluation methods and limitations are thoughtfully considered.",
            "The response maintains scientific rigor while showcasing creativity in system design.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
