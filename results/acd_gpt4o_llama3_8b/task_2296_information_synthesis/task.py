class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "synthesis",
                "texts": [
                    "Text 1: The ancient city of Alexandria was founded by Alexander the Great in 331 BC and quickly became a major center of Hellenistic culture and learning. It housed the famous Library of Alexandria, one of the largest and most significant libraries of the ancient world.",
                    "Text 2: The Great Library of Alexandria was an institution that aimed to collect all the knowledge of the known world. Scholars from various cultures and disciplines gathered there to study and share their knowledge.",
                    "Text 3: Despite its fame, the Library of Alexandria faced numerous challenges, including political conflicts, fires, and eventual decline. Its destruction remains a topic of debate among historians, with various accounts attributing it to different events.",
                    "Text 4: The legacy of the Library of Alexandria continues to influence modern libraries and educational institutions, symbolizing the pursuit of knowledge and the importance of cultural exchange.",
                    "Text 5: Archaeological findings suggest that the Library was part of a larger research institution known as the Mouseion, which included lecture halls, gardens, and living quarters for scholars.",
                    "Text 6: Some historical accounts attribute the final destruction of the Library of Alexandria to the Muslim conquest of Alexandria in the 7th century, while others suggest it was already in decline due to earlier events.",
                ],
                "summary_length": "200 words"
            },
            "2": {
                "task_type": "synthesis",
                "texts": [
                    "Text 1: In recent years, renewable energy sources such as solar and wind power have gained significant attention as alternatives to fossil fuels. These energy sources are considered more sustainable and environmentally friendly.",
                    "Text 2: Solar power harnesses energy from the sun using photovoltaic cells, while wind power generates electricity through wind turbines. Both methods have seen technological advancements, making them more efficient and cost-effective.",
                    "Text 3: Despite their benefits, renewable energy sources face challenges such as intermittent supply and the need for substantial initial investment. Integrating these sources into existing energy grids requires careful planning and infrastructure development.",
                    "Text 4: Governments and organizations worldwide are investing in renewable energy projects, driven by the need to reduce carbon emissions and combat climate change. Public awareness and support for renewable energy are also growing.",
                    "Text 5: A significant barrier to widespread adoption of renewable energy is the current infrastructure, which often relies on centralized power plants. Transitioning to decentralized renewable energy systems requires extensive upgrades and investment.",
                    "Text 6: Innovations such as energy storage solutions and smart grids are emerging to address the issues of supply intermittency and integration, further enhancing the feasibility of renewable energy systems.",
                ],
                "summary_length": "200 words"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        texts = '\n'.join(t["texts"])
        return f"You will be provided with multiple texts. Your task is to synthesize the information from these texts into a coherent and concise summary. Ensure that your summary captures the key points from all the texts provided and is no longer than {t['summary_length']}. Submit your summary as a plain text string. Here are the texts:\n{texts}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should capture the key points from all provided texts.",
            "The summary should be coherent and concise.",
            "The summary should not exceed the specified length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0