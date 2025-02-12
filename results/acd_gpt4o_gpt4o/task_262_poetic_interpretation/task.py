class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "The Road Not Taken\n\nTwo roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence: \nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference."
            },
            "2": {
                "poem": "Ode to a Nightingale\n\nMy heart aches, and a drowsy numbness pains\nMy sense, as though of hemlock I had drunk,\nOr emptied some dull opiate to the drains\nOne minute past, and Lethe-wards had sunk: \n'Tis not through envy of thy happy lot,\nBut being too happy in thine happiness,—\nThat thou, light-winged Dryad of the trees\nIn some melodious plot\nOf beechen green, and shadows numberless,\nSingest of summer in full-throated ease.\n\nO, for a draught of vintage! that hath been\nCool'd a long age in the deep-delved earth,\nTasting of Flora and the country green,\nDance, and Provençal song, and sunburnt mirth!\nO for a beaker full of the warm South,\nFull of the true, the blushful Hippocrene,\nWith beaded bubbles winking at the brim,\nAnd purple-stained mouth;\nThat I might drink, and leave the world unseen,\nAnd with thee fade away into the forest dim: \n\nFade far away, dissolve, and quite forget\nWhat thou among the leaves hast never known,\nThe weariness, the fever, and the fret\nHere, where men sit and hear each other groan;\nWhere palsy shakes a few, sad, last gray hairs,\nWhere youth grows pale, and spectre-thin, and dies;\nWhere but to think is to be full of sorrow\nAnd leaden-eyed despairs,\nWhere Beauty cannot keep her lustrous eyes,\nOr new Love pine at them beyond to-morrow.\n\nAway! away! for I will fly to thee,\nNot charioted by Bacchus and his pards,\nBut on the viewless wings of Poesy,\nThough the dull brain perplexes and retards: \nAlready with thee! tender is the night,\nAnd haply the Queen-Moon is on her throne,\nCluster'd around by all her starry Fays;\nBut here there is no light,\nSave what from heaven is with the breezes blown\nThrough verdurous glooms and winding mossy ways.\n\nI cannot see what flowers are at my feet,\nNor what soft incense hangs upon the boughs,\nBut, in embalmed darkness, guess each sweet\nWherewith the seasonable month endows \nThe grass, the thicket, and the fruit-tree wild;—\nWhite hawthorn, and the pastoral eglantine;\nFast fading violets cover'd up in leaves;\nAnd mid-May's eldest child,\nThe coming musk-rose, full of dewy wine,\nThe murmurous haunt of flies on summer eves.\n\nDarkling I listen; and, for many a time\nI have been half in love with easeful Death,\nCall'd him soft names in many a mused rhyme,\nTo take into the air my quiet breath;\nNow more than ever seems it rich to die,\nTo cease upon the midnight with no pain,\nWhile thou art pouring forth thy soul abroad\nIn such an ecstasy!\nStill wouldst thou sing, and I have ears in vain—\nTo thy high requiem become a sod.\n\nThou wast not born for death, immortal Bird!\nNo hungry generations tread thee down;\nThe voice I hear this passing night was heard\nIn ancient days by emperor and clown: \nPerhaps the self-same song that found a path\nThrough the sad heart of Ruth, when, sick for home,\nShe stood in tears amid the alien corn;\nThe same that oft-times hath\nCharm'd magic casements, opening on the foam\nOf perilous seas, in faery lands forlorn.\n\nForlorn! the very word is like a bell\nTo toll me back from thee to my sole self!\nAdieu! the fancy cannot cheat so well\nAs she is fam'd to do, deceiving elf.\nAdieu! adieu! thy plaintive anthem fades\nPast the near meadows, over the still stream,\nUp the hill-side; and now 'tis buried deep\nIn the next valley-glades: \nWas it a vision, or a waking dream?\nFled is that music:—Do I wake or sleep?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and analyze the given poem. Provide insights into its meaning, themes, and use of literary devices.

Poem: {t['poem']}

Your response should include:
1. A brief summary of the poem's content.
2. An analysis of the main themes and messages conveyed by the poem.
3. Identification and interpretation of key literary devices used in the poem (e.g., metaphors, similes, imagery).
4. An overall interpretation of the poem's meaning and significance.

Please provide your response in plain text format, ensuring it is well-structured and demonstrates a deep understanding of the poem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief summary of the poem's content.",
            "The analysis should cover the main themes and messages of the poem.",
            "The response should identify and interpret key literary devices used in the poem.",
            "The overall interpretation should reflect a deep understanding of the poem's meaning and significance.",
            "The response should be well-structured and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
