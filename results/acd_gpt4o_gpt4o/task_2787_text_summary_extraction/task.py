class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once. It's often used as a typing exercise or to display fonts and text layouts. Additionally, it helps in testing the functioning of keyboards and typewriters."
            },
            "2": {
                "text": "The Industrial Revolution, from the 18th to 19th centuries, transformed agrarian societies in Europe and America into industrial and urban ones. Manufacturing shifted from homes to factories, marked by powered machinery and mass production. The iron and textile industries and the steam engine were central. It led to more goods and improved living standards for some but also poor conditions for workers. This period saw significant social changes, including urbanization and new social classes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to read the given text and extract the key points. "
            "Then, provide a concise summary that captures the essence of the text. "
            "Ensure that the summary is coherent and includes the main ideas presented in the text. "
            "Your response should be in the following format: \n\n"
            "Summary: [Your concise summary here]\n\n"
            "Example: \n"
            "Text: The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once. It's often used as a typing exercise or to display fonts and text layouts. Additionally, it helps in testing the functioning of keyboards and typewriters.\n"
            "Summary: The sentence 'The quick brown fox jumps over the lazy dog' is a typing exercise that includes every letter of the alphabet and is used to test keyboards and fonts."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should include the main points from the original text.",
            "The summary should be concise and coherent.",
            "The summary should capture the essence of the text without missing critical information."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
