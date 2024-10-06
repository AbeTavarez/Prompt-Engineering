Here is a cheat sheet for the **Penn Treebank POS (Part-of-Speech) tags** used by NLTK:

### NLTK POS Tag Cheat Sheet

| **Tag** | **Meaning**               | **Example Words**         |
|---------|----------------------------|---------------------------|
| **CC**  | Coordinating conjunction    | and, but, or              |
| **CD**  | Cardinal number             | one, two, 3, 50           |
| **DT**  | Determiner                  | the, a, an, this          |
| **EX**  | Existential there           | there (as in "there is")  |
| **FW**  | Foreign word                | en, perestroika           |
| **IN**  | Preposition/subordinating conjunction | in, of, like, as     |
| **JJ**  | Adjective                   | quick, blue, happy        |
| **JJR** | Adjective, comparative      | quicker, better, larger   |
| **JJS** | Adjective, superlative      | quickest, best, largest   |
| **LS**  | List item marker            | 1., 2., A., B.            |
| **MD**  | Modal auxiliary             | can, could, will, should  |
| **NN**  | Noun, singular or mass      | dog, car, music           |
| **NNS** | Noun, plural                | dogs, cars, computers     |
| **NNP** | Proper noun, singular       | London, Jane, Microsoft   |
| **NNPS**| Proper noun, plural         | Americans, Smiths         |
| **PDT** | Predeterminer               | all, both, half           |
| **POS** | Possessive ending           | ’s, '                     |
| **PRP** | Personal pronoun            | I, he, she, they, it      |
| **PRP$**| Possessive pronoun          | my, his, their, its       |
| **RB**  | Adverb                      | quickly, very, silently   |
| **RBR** | Adverb, comparative         | faster, better, earlier   |
| **RBS** | Adverb, superlative         | fastest, best, earliest   |
| **RP**  | Particle                    | up, off, out              |
| **SYM** | Symbol                      | $, %, &, +                |
| **TO**  | "to" (as preposition or infinitive) | to (as in "to go")   |
| **UH**  | Interjection                | oh, wow, uh               |
| **VB**  | Verb, base form             | eat, run, go, jump        |
| **VBD** | Verb, past tense            | ate, ran, went, jumped    |
| **VBG** | Verb, gerund/present participle | eating, running, going |
| **VBN** | Verb, past participle       | eaten, run, gone          |
| **VBP** | Verb, non-3rd person singular present | eat, run, go        |
| **VBZ** | Verb, 3rd person singular present | eats, runs, goes       |
| **WDT** | Wh-determiner               | which, that, whatever     |
| **WP**  | Wh-pronoun                  | who, what, whom           |
| **WP$** | Possessive wh-pronoun       | whose                     |
| **WRB** | Wh-adverb                   | where, when, why          |

### POS Tag Categories

- **Nouns**: 
  - `NN` (singular noun), 
  - `NNS` (plural noun), 
  - `NNP` (singular proper noun), 
  - `NNPS` (plural proper noun)
  
- **Verbs**:
  - `VB` (base form), 
  - `VBD` (past tense), 
  - `VBG` (gerund/present participle), 
  - `VBN` (past participle), 
  - `VBP` (non-3rd person singular present), 
  - `VBZ` (3rd person singular present)
  
- **Adjectives**:
  - `JJ` (adjective), 
  - `JJR` (comparative adjective), 
  - `JJS` (superlative adjective)
  
- **Adverbs**:
  - `RB` (adverb), 
  - `RBR` (comparative adverb), 
  - `RBS` (superlative adverb)

- **Pronouns**:
  - `PRP` (personal pronoun),
  - `PRP$` (possessive pronoun),
  - `WP` (wh-pronoun),
  - `WP$` (possessive wh-pronoun)

- **Determiners**:
  - `DT` (determiner),
  - `PDT` (predeterminer),
  - `WDT` (wh-determiner)

- **Conjunctions**:
  - `CC` (coordinating conjunction),
  - `IN` (preposition or subordinating conjunction)

### Special Tags

- **EX**: Represents the word "there" when it’s used existentially (e.g., "There is a dog").
- **MD**: Modal verbs like "can," "could," "will," etc.
- **POS**: Possessive endings (e.g., "’s" in "John’s").
- **TO**: The preposition or infinitive "to."
- **UH**: Interjections (e.g., "oh", "wow").
- **FW**: Foreign words (e.g., words from other languages).

This cheat sheet should help you understand the POS tags that NLTK assigns to words when you use `nltk.pos_tag()`!