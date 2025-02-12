class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference."""},
            "2": {"poem": """I met a traveler from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert. Near them on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them and the heart that fed.
And on the pedestal these words appear:
My name is Ozymandias, King of Kings;
Look on my Works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal Wreck, boundless and bare
The lone and level sands stretch far away."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given poem:

Poem:
{t['poem']}

Analyze the poem by addressing the following points:
1. Identify and explain the central themes of the poem.
2. Discuss the use of literary devices (e.g., metaphor, simile, symbolism) and how they contribute to the poem's meaning.
3. Provide an interpretation of the overall meaning or message of the poem.
4. Support your analysis with specific lines or phrases from the poem.

Submit your analysis as a plain text string. Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the poem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should identify and explain the central themes of the poem.", "The analysis should discuss the use of literary devices and how they contribute to the poem's meaning.", "The analysis should provide an interpretation of the overall meaning or message of the poem.", "The analysis should be supported by specific lines or phrases from the poem.", "The response should be well-structured, coherent, and demonstrate a deep understanding of the poem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
