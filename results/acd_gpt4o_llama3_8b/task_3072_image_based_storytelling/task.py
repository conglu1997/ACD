class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "images": [
                    "https://placeholder.com/image1.jpg",
                    "https://placeholder.com/image2.jpg",
                    "https://placeholder.com/image3.jpg"
                ]
            },
            "2": {
                "story": "Once upon a time, in a small village, there lived a brave young girl named Aria. One day, she discovered a hidden path leading to a magical forest. As she ventured deeper, she encountered various mystical creatures and uncovered ancient secrets that changed her life forever."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "images" in t:
            return """You are given a sequence of images. Your task is to generate a coherent and imaginative narrative based on the visual information provided in the images. Ensure that your narrative connects the images in a logical and engaging manner. Submit your narrative as a plain text string in the following format:\n\nNarrative: [Your narrative here]\n\nImages:\n1. {t['images'][0]}\n2. {t['images'][1]}\n3. {t['images'][2]}\n\nInstructions:\n1. Analyze the sequence of images carefully.\n2. Create a narrative that logically connects the events or scenes depicted in the images.\n3. Ensure that your narrative is engaging and imaginative.\n4. Submit your narrative as a plain text string in the format provided."""
        else:
            return """You are given a narrative. Your task is to generate a sequence of images that visually represent the key events and scenes described in the narrative. Ensure that your images are coherent and accurately reflect the story. Submit your images as descriptions in a plain text string in the following format:\n\nImages: [Your image descriptions here]\n\nNarrative:\n{t['story']}\n\nInstructions:\n1. Read the narrative carefully.\n2. Create a sequence of images that visually represent the key events or scenes described in the narrative.\n3. Ensure that your images are coherent and accurate.\n4. Submit your images as descriptions in a plain text string in the format provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should logically connect the events or scenes depicted in the images.",
            "The narrative should be engaging and imaginative.",
            "If generating images, the descriptions should accurately reflect the key events or scenes described in the narrative.",
            "The submission format should match the specified format in the instructions.",
            "The submission should demonstrate coherence and logical connections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
