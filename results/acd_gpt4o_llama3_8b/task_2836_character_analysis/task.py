class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "character_info": "Alice is a young woman who starts her journey as a shy and introverted individual. She faces various challenges, including dealing with loss and finding her place in a new city. Throughout her journey, she meets different people who influence her growth. Analyze her character development based on the following excerpts:\n\n1. 'Alice looked around nervously as she stepped into the bustling city. She had never been away from her hometown before, and the noise and crowd overwhelmed her.'\n2. 'Over time, Alice found comfort in the small café around the corner. The barista, an older woman named Maria, always had a kind word for her.'\n3. 'The loss of her grandmother hit Alice hard. She spent weeks in her new apartment, barely speaking to anyone.'\n4. 'Alice finally joined a local book club. It was Maria who suggested it, and Alice found herself slowly opening up to the new people she met there.'\n5. 'Standing in front of the group at the book club meeting, Alice shared her thoughts confidently. She realized she had found a community that accepted her for who she was.'",
                "question": "Analyze how Alice's character develops throughout these excerpts. Provide a detailed analysis of her growth and the factors that influenced her transformation."
            },
            "2": {
                "character_info": "John is a middle-aged man who starts as a successful but unfulfilled corporate executive. He goes through a series of personal and professional challenges that lead to a significant transformation. Analyze his character development based on the following excerpts:\n\n1. 'John sat at his desk, staring at the endless rows of numbers on his screen. He felt a sense of emptiness despite his high salary and luxurious lifestyle.'\n2. 'One evening, John attended a charity event organized by his company. He met an old friend, Sarah, who had left the corporate world to start a non-profit organization.'\n3. 'Inspired by Sarah’s story, John began volunteering at the non-profit on weekends. He found a sense of fulfillment he hadn’t felt in years.'\n4. 'John faced backlash from his colleagues for spending too much time on volunteer work. He struggled to balance his corporate responsibilities and his newfound passion.'\n5. 'Ultimately, John decided to leave his corporate job and join Sarah’s non-profit full-time. He felt a sense of purpose and contentment in his new role.'",
                "question": "Analyze how John's character develops throughout these excerpts. Provide a detailed analysis of his growth and the factors that influenced his transformation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        character_info = t["character_info"]
        question = t["question"]
        return f"""Analyze the character development based on the following information:\n\n{character_info}\n\n{question}\n\nSubmit your analysis as a plain text string in the following format:\n\nAnalysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be coherent and logically structured.",
            "The analysis should accurately reflect the character's development as described in the excerpts.",
            "The analysis should identify key factors that influenced the character's transformation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
