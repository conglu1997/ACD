import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        programming_concepts = [
            "loop",
            "conditional statement",
            "variable assignment",
            "function definition"
        ]
        vr_interactions = [
            "object manipulation",
            "teleportation",
            "scaling",
            "rotation"
        ]
        cognitive_aspects = [
            "spatial memory",
            "proprioception",
            "mental rotation",
            "embodied metaphors"
        ]
        
        return {
            "1": {
                "programming_concept": random.choice(programming_concepts),
                "vr_interaction": random.choice(vr_interactions),
                "cognitive_aspect": random.choice(cognitive_aspects)
            },
            "2": {
                "programming_concept": random.choice(programming_concepts),
                "vr_interaction": random.choice(vr_interactions),
                "cognitive_aspect": random.choice(cognitive_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a gesture-based programming language for virtual reality environments, focusing on the programming concept of '{t['programming_concept']}', the VR interaction of '{t['vr_interaction']}', and the cognitive aspect of '{t['cognitive_aspect']}'. Your response should include:\n\nNote: Embodied cognition refers to the theory that many features of human cognition are shaped by aspects of the body beyond the brain. In this context, consider how physical gestures and movements in VR can influence and enhance the programming experience and cognitive processes.\n\n1. Gesture Language Design (250-300 words):\n   a) Describe the core principles and structure of your gesture-based programming language.\n   b) Explain how it incorporates the specified programming concept, VR interaction, and cognitive aspect.\n   c) Provide examples of basic gestures and their corresponding programming functions.\n   d) Discuss how your language leverages embodied cognition principles.\n\n2. Simple Program Implementation (200-250 words):\n   a) Describe a simple program that can be implemented using your gesture-based language.\n   b) Provide a step-by-step 'gestural code' for this program, explaining each gesture and its function.\n   c) Discuss how this implementation differs from traditional text-based programming.\n\n3. Cognitive Implications Analysis (200-250 words):\n   a) Analyze how using this gesture-based language might affect cognitive processes compared to traditional programming.\n   b) Discuss potential benefits and challenges for learning and using this language.\n   c) Explain how the specified cognitive aspect is particularly engaged or enhanced.\n\n4. Human-Computer Interaction Considerations (150-200 words):\n   a) Discuss how your gesture-based language might change the nature of human-computer interaction in programming.\n   b) Address potential accessibility issues and how they might be mitigated.\n   c) Propose ideas for user interface design that would support this gestural programming environment.\n\n5. Practical Applications and Limitations (150-200 words):\n   a) Suggest potential real-world applications for your gesture-based programming language.\n   b) Discuss limitations of your approach and areas for future development.\n   c) Compare the efficiency and expressiveness of your language to traditional programming methods.\n\nEnsure your response demonstrates a deep understanding of programming concepts, virtual reality interactions, and cognitive science principles. Be creative in your language design while maintaining logical consistency and usability. Use clear headings for each section of your response.\n\nYour total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of programming concepts, virtual reality interactions, and cognitive science principles.",
            "The gesture-based programming language design is innovative, logically consistent, and incorporates the specified programming concept, VR interaction, and cognitive aspect.",
            "The simple program implementation effectively illustrates the use of the gestural language.",
            "The cognitive implications analysis shows insight into how this approach might affect thinking and learning processes.",
            "The response addresses human-computer interaction considerations and practical applications thoughtfully.",
            "The overall response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
