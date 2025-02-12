class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "A young girl named Emma discovers a magical forest behind her house. One day, she meets a talking squirrel who needs her help to save the forest from an evil sorcerer. Emma must embark on a journey through the forest, facing various magical creatures and challenges, to defeat the sorcerer and restore peace."},
            "2": {"story": "In a distant future, humanity has colonized Mars. John, a scientist, uncovers a conspiracy that could threaten the entire colony. With time running out, he must find allies and expose the truth. John's journey takes him through the underground tunnels of Mars, encountering different factions and facing dangerous situations, ultimately leading to a showdown with the conspirators."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        story = t["story"]
        return f"""Transform the following short story into a screenplay format. Ensure that the screenplay includes scene descriptions, character dialogues, and any necessary action sequences. Use proper screenplay formatting conventions. Your screenplay should be coherent, logically structured, and capture the essence of the original story.

Short Story: {story}

Submit your screenplay as a plain text string in the following format:

Example:
INT. EMMA'S HOUSE - DAY

Emma, a young girl, looks out the window at the forest behind her house.

EMMA
(to herself)
I wonder what's out there.

EXT. MAGICAL FOREST - DAY

Emma steps into the forest and sees a squirrel.

SQUIRREL
Help me, Emma! The forest is in danger.

Your screenplay should be at least 500 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The screenplay should follow proper formatting conventions.", "The screenplay should be coherent and logically structured.", "The screenplay should capture the essence of the original story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
