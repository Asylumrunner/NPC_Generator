# NPC_Generator
A Python app that generates quick NPCs for tabletop RPGs

# Overview
I run a number of tabletop RPGs for a variety of groups, and one of the hardest parts for me is coming up with distinct personalities for non-player characters on the spot. So, I decided to write myself an application that could automatically generate NPCs, at least in the broad strokes, on my behalf.

This application is has three primary modes of operation, designed to be maximally available for any use case.

The first use case is for at-table play of a tabletop RPG, during which I personally prefer to not have a laptop or phone. For this purpose, the application is designed to produce .csv files compatible with [CardMaker](https://github.com/nhmkdev/cardmaker), a neat application that can read in csv data to quickly develop sheets of printable cards. With this, I can programatically populate a card sheet with NPC details, then print out a deck for physical use at the table.

The second use case is for online games played over Roll20, which frequently use Discord as the primary space for play. In this case, a Discord bot using the same codebase has been created, which can easily be invited into channels and made to generate characters with the command

```
!generate <number of characters> <space separated list of attributes>
```

(In the interest of not flooding channels with characters, maximum characters per command is limited to 5 with the Disocrd bot.)

The third use case is for other developers, hoping to consume this information in order to create even more robust GMing tools. For this purpose, an RESTful API has been developed which can be consumed in order to generate characters.

There is a future use-case for this application, which is as the beating heart of an Android application designed to generate characters on the fly on a phone, but as that application will require a translation of this codebase into Java/Kotlin, as well as significant UI work, it is to be considered separate to this project.

# How It Works
Characters generated by this application have three primary components. The first is a name, randomly selected from a list generated by hitting the random name API provided by [http://uinames.com](http://uinames.com). These names are originally given in their native alphabet, so python's unidecode function is used to convert them to printable English, a method that still produces some occasional bugs but is generally successful.

Characters also have a set of three personality traits randomly assigned to them. These are pulled from a list of character traits randomly, such that no trait is shared between characters.

The last aspect of a character are approximate statistical attributes. Most RPGs use some sort of numerical system to represent characters' attributes, but using any of those systems in this application would limit its usefulness. Instead, the user may enter the set of attributes they want to use, or use the default D&D stats. Then, the application will go through every attribute for every character, and decide if the character is, in that stat, pathetically inept, lower than average, average, better than average, or exceptional. The numbers are weighted such that average score are more likely than non-average scores.

Then, this list of characters is returned to the user, with a chance to review them and regenerate them before submission. Upon submission, the characters are exported as a CSV, ready to be used by CardMaker to generate a quick-reference deck of NPCs.
