import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_theories = [
            {
                "name": "Conceptual Metaphor Theory",
                "key_concepts": ["source domain", "target domain", "mapping"],
                "example": "LOVE IS A JOURNEY"
            },
            {
                "name": "Image Schema Theory",
                "key_concepts": ["containment", "path", "force", "balance"],
                "example": "OUT OF THE FRYING PAN INTO THE FIRE"
            },
            {
                "name": "Frame Semantics",
                "key_concepts": ["frame", "frame elements", "semantic roles"],
                "example": "The waiter brought the check"
            }
        ]
        return {str(i+1): theory for i, theory in enumerate(random.sample(linguistic_theories, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality interface that allows users to manipulate language and concepts in a three-dimensional space, based on the theory of {t['name']} from cognitive linguistics. Your design should incorporate the key concepts of {', '.join(t['key_concepts'])}. Use the example '{t['example']}' to illustrate how your interface would work.

Your response should include:

1. Interface Overview (250-300 words):
   a) Describe the overall look and feel of your VR interface.
   b) Explain how users interact with linguistic elements in the 3D space.
   c) Discuss how your design incorporates the principles of embodied cognition.

2. Key Features (200-250 words):
   a) Detail 3-4 key features of your interface, explaining how each relates to {t['name']}.
   b) Describe how users can manipulate or create new linguistic constructs using these features.
   c) Explain how your interface represents abstract concepts in a spatial format.

3. User Interaction Scenario (200-250 words):
   a) Provide a step-by-step walkthrough of how a user would interact with your interface to explore or create the example '{t['example']}'.
   b) Explain how this interaction demonstrates the key concepts of {', '.join(t['key_concepts'])}.
   c) Describe the visual and tactile feedback the user receives during this interaction.

4. Cognitive Benefits Analysis (150-200 words):
   a) Discuss potential cognitive benefits of using your VR interface for language learning or conceptual understanding.
   b) Explain how your interface might enhance users' grasp of {t['name']}.
   c) Propose a hypothesis about how this type of spatial-linguistic interaction might affect brain activity or cognitive processing.

5. Technical Implementation (150-200 words):
   a) Outline the key technical components needed to create your VR interface.
   b) Discuss any challenges in implementing your design and propose solutions.
   c) Suggest how machine learning or AI could be incorporated to enhance the interface's functionality.

6. Ethical Considerations and Limitations (100-150 words):
   a) Address potential ethical concerns or limitations of your VR language interface.
   b) Discuss how your interface design accounts for accessibility and inclusivity.
   c) Consider potential unintended consequences of spatializing language and concepts.

Ensure your response demonstrates a deep understanding of cognitive linguistics, virtual reality technology, and user interface design. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['name']} and accurately incorporates its key concepts",
            "The VR interface design is innovative, plausible, and effectively combines linguistic theory with spatial interaction",
            "The user interaction scenario clearly illustrates how the interface works and relates to the given example",
            "The analysis of cognitive benefits is well-reasoned and grounded in current understanding of cognition and language processing",
            "The technical implementation section addresses key challenges and proposes realistic solutions",
            "The response considers ethical implications and limitations of the proposed interface"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
