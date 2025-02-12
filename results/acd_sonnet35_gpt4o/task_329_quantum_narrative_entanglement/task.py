import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum teleportation",
            "quantum decoherence"
        ]
        story_elements = [
            "a love triangle",
            "a time travel paradox",
            "a murder mystery",
            "a philosophical dilemma",
            "an ethical decision"
        ]
        writing_styles = [
            "stream of consciousness",
            "epistolary",
            "non-linear narrative",
            "unreliable narrator",
            "second-person perspective"
        ]
        
        tasks = {
            "1": {
                "quantum_concept1": random.choice(quantum_concepts),
                "quantum_concept2": random.choice(quantum_concepts),
                "story_element": random.choice(story_elements),
                "writing_style": random.choice(writing_styles)
            },
            "2": {
                "quantum_concept1": random.choice(quantum_concepts),
                "quantum_concept2": random.choice(quantum_concepts),
                "story_element": random.choice(story_elements),
                "writing_style": random.choice(writing_styles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (400-500 words) that incorporates the quantum computing concepts of {t['quantum_concept1']} and {t['quantum_concept2']}, includes {t['story_element']}, and is written in the {t['writing_style']} style. Your story should adhere to the following guidelines:

1. The narrative structure should mimic quantum entanglement, where two or more story elements are interconnected in such a way that the state of one element cannot be described independently of the others.

2. Incorporate at least three characters whose fates or decisions are 'entangled' in a way that reflects both chosen quantum concepts.

3. Use the chosen quantum concepts as both plot devices and metaphors for the characters' relationships or the story's themes.

4. Include at least one scene that takes place in a quantum computing laboratory or involves quantum computing technology.

5. The story should have a clear beginning, middle, and end, with a resolution that ties back to the quantum concepts.

6. After your story, provide a brief explanation (150-200 words) of:
   a) How your narrative structure mimics quantum entanglement
   b) How you incorporated the specific quantum concepts
   c) A comparison between each quantum concept and its classical counterpart, relating it to your story

7. Ensure that your story adheres to the {t['writing_style']} style throughout.

Ensure that your story is engaging, coherent, and accurately reflects the quantum concepts while creatively integrating {t['story_element']}. Your response will be evaluated based on scientific accuracy, narrative quality, and adherence to the specified writing style."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates the quantum concepts of {t['quantum_concept1']} and {t['quantum_concept2']}",
            f"The narrative includes {t['story_element']} as specified",
            f"The story is written consistently in the {t['writing_style']} style",
            "The story's structure mimics quantum entanglement with interconnected elements",
            "At least three characters with 'entangled' fates or decisions are present",
            "The quantum concepts are used as both plot devices and metaphors",
            "A scene in a quantum computing laboratory or involving quantum technology is included",
            "The story has a clear beginning, middle, and end with a resolution tied to the quantum concepts",
            "A brief explanation of the narrative structure, quantum concept incorporation, and comparison to classical counterparts is provided",
            "The story is engaging, coherent, and demonstrates creativity",
            "The submission falls within the specified word count ranges"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
