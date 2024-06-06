# Bitext Alignment

* Data structures:
* text segment structures: string array?
* alignment structure: text segment structures, corresponding alignment index arrays → how to most structure indices to allow for efficient frequent shifting of indices? mutable struct?
* n x m grid of alignment scores → filled in on “diagonal” (relative positional overlap) and within k of the “diagonal” to be learned with a max-margin approach: softmax regression over features?
* geometric grid, where side lengths represent relative weight → use to find diagonal
* feature vector for each proposed alignment: punctuation counts, stop word counts, capitalization counts (where applicable), word length, relative word length, relative character length, basic part of speech counts, etc. → tensor? dataframe with vector entries? → einsum notation for computations?
* n x m score matrix
* segment type annotations (predicted probabilities, types: paragraph, chapter title, page number, footnote):  → to feature vector?
* Scoring Models: TODO: [Draw diagram](https://app.diagrams.net/)
* concatenation of both feature vectors (→ their difference will be learned internally in the small neural network) as input to a small scoring model (FFNN?)
    * trained by max margin: gold alignment given 1, each alignment in both directions with neighbors no further than j positions away scored 0 → triplet loss?
    * 1 basic relative weight-based model (linear regression likely sufficient) and many language-pair-specific models (FFNN likely superior)
* Triplet / Siamese network to learn sentence pair scores from a relatively small set of function words (stop words) (and other very high-frequency lemmas?):
* sentence → representation → aggregation → dense embedding model (except for models where aggregation and embedding occur together) → dot product / cosine distance as score (to be minimized)
* Key assumption: this score will be - with very high probability - higher for correct than for incorrect alignments (especially for true alignments vs neighboring alignments)
* → idea: add normalized length measures (character, token)
    * function-word translation probabilities - using a small set of frequent (i.e. function) words, their co-occurrence probabilities (or perhaps relative probabilities → log-odds ratio?) can be used to generate a score for each sentence pair
    * bag-of-words-based score
    * expanded bag-of-words-based scores (many variations possible): use positional encodings / positional embeddings (as in Transformer, or more simply one-hot for word being in part k → see part about 2D input)? additional token types such as before/after function words, i.e. words mapped to likely types
    → how to use positional encodings?
    * very low-dimensional embeddings for k most frequent words (PCA or other dimensionality reduction technique from pre-trained)
    * 2D input, convolutional element → variation on each model below
    * LSTM-based embeddings
    * simple encoder-decoder-based embeddings
    * Transformer/attention-based embeddings
* Approaches:
* 1. Relative Weight-Based (i.e. length-based)
    1. paragraph
    2. sentence
* 2. Content overlap-based
    1. lexicon-based
        1. stop-words (N most frequent) - more efficient
        2. larger or even practically-full lexicon (or lemma) set to learn co-occurrence probabilities from - less efficient, greater accuracy possible → see above
        3. recognition and use of proper nouns
        4. word embedding-based? → see above
    2. punctuation-based
    3. consecutive n-gram overlap scores (with transliteration mapping rules)
* 3. Neural approach
    1. one idea: all easy-to-compute features as input to alignment model (cf. non-neural?)
        1. baseline language-agnostic model from relative weight-based features
        2. language pair-specific additional features: bigrams, punctuation, stop words (→ possibly better to have overlap of possible translations of stop words, potentially weighted by translation probability), proper noun recognition, etc.
* 4. Parameter tuning from training data (for all or most of the above) - possible (more primitive) alternative to the neural approach
* 5. binary predictor for matching segment pairs: match / no match → possibility of using and tuning word embeddings
* → embed sentence and use triplet network training to maximize “closeness” of respective embeddings
* → predict PoS for all words, use filler PoS embeddings for all words not in stop words, punctuation, N most common lemmas
* → embed each token, use two sequence models to each output a “sentence” (text unit) embedding, tor input to triplet loss
* → use beam search on the output of this to find most likely alignments
* 6. translation-based approach
    1. full neural / statistical MT
    2.  → [opennmt.net/,](https://opennmt.net/,)
* [huggingface.co/docs/transformers/model_doc/marian](https://huggingface.co/docs/transformers/model_doc/marian)
* [marian-nmt.github.io/](https://marian-nmt.github.io/)
     [opus.nlpl.eu/Opus-MT/](https://opus.nlpl.eu/Opus-MT/)
* 7. RL-based approach: advantage of relatively small action space, typically limited number of look-aheads → how to parametrize environment, policy, etc.? → which algorithm(s) to use?
* Other ideas:
* use “breakpoints” - likely paragraph, section, chapter etc. breaks → indicator of likelihood of certain alignments (naturally not ironclad)
* proper noun anchoring approach: identify proper nouns (NER + pattern matching?) → different approaches for different language pairs
* Modules
* Noiser: take clean and aligned texts (alignment data structure) and add noise, split some segments, combine some segments, to imitate look of Wiktionary or Project Gutenberg, etc. formats → input to training algorithms, with ground truth available (use break point tags to keep track of equivalences → one set for each version, clean and noisy, and in master data structure both)


  * alignment

        let "word" = "lemma" in what follows

        given 2 sentences which may be a match:

        what
         is the probability of word ai and word bj co-occurring in a correct
        match vs in an incorrect match? -> ratio, i.e. certainty gain

        add up log certainty gain for all relevant word pairs found in the sentence

        find most predictive words (i.e. word pairs)

Also negative aspect? -> words highly likely to be translated with another word should decrease certainty if it is not found


* alignment

        let "word" = "lemma" in what follows

        given 2 sentences which may be a match:

        what
         is the probability of word ai and word bj co-occurring in a correct
        match vs in an incorrect match? -> ratio, i.e. certainty gain

        add up log certainty gain for all relevant word pairs found in the sentence

        find most predictive words (i.e. word pairs)

Also negative aspect? -> words highly likely to be translated with another word should decrease certainty if it is not found![Selection_003.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/e74f0423-4454-4dd0-ae43-e45cbc541e73/2b09fb99-064d-4c2f-8e04-8d7ff2938ddc/Selection_003.png)



FIXME### Relevant Algorithms

* 1. Beam Search (adapted to bitex alignment
* 2. Anchor point seeded beam search
    1. diagonal max overlap
    2. k steps in either direction for $4k^2$  possible alignments
    3. search over proposed alignments, narrowing the search space as much as possible when high-quality alignments are found
    4. → see Bitext Alignment (2) for ideas on how to implement this
    5. above, but with max lookahead, before selecting anchor points above a certain threshold and continuing from there
* 3. multilingual alignment with modified version of 1. (more than 2 languages at a time for greater robustness)
* → [en.wikipedia.org/wiki/Category:Search_algorithms](https://en.wikipedia.org/wiki/Category:Search_algorithms)
* 1. RL-powered search?
* 2. Score grid traversal: 7 lookaheads (possible next alignments), need to re-evaluate 4 of those to see if alignment scores improve after combining segments
* 3. anchor traversal: once p reliable good anchors are found (scores above a pre-determined threshold), reduce search space to feasible paths between anchors → algorithm to compute permissible paths / re-compute diagonals
* 4.

## Notes

* alignment rules: U{1:n} from both directions? blocks allowed? unaligned words also allowed?

```latex
* P = \textbf{1}(\textrm{max}(\textrm{rowsoftmax}(Z), \textrm{colsoftmax}(Z)) > \tau)
* Z_{[m \times n]} = L^{B}_{[m \times h]} (L_{[n \times h]}^{A})^T

= R_{[m \times n]}^{B} V_{[n \times h]}^{B} (R_{[n \times m]}^{A} V_{[m \times h]}^{A} )^T

= Q_{[m \times h]}^{A} (K^{B})^T_{[h \times n]} V_{[n \times h]}^{B} (Q_{[n \times h]}^{B} (K^{A})^T_{[h \times m]} V_{[m \times h]}^{A})^T

= W_{Q[m \times m]}^{A} X_{[m \times h]}^{A} (W_{K[n \times n]}^{B} X_{[n \times h]}^{B})^T W_{V[n \times n]}^{B} X_{[n \times h]}^{B} (W_{Q[n \times n]}^{B} X_{[n \times h]}^{B} (W_{K[m \times m]}^{A} X_{[m \times h]}^{A})^T W_{V[m \times m]}^{A} X_{[m \times h]}^{A}

)^T
```

* align English with LA, GRC, FR, DE, ES, RU, ZH (start with DE, FR, RU); write package for realignment: x:y, y:z → x:z (need to flag ambiguities and fix manually)
* data for EN-DE: 10k from bibles | 10k Tatoeba (300k total) | 20k from classic literature | 10k from film subtitles | 10k from TED talks | 10k from YouTube | 10k from assorted non-fiction: documentation, reports | 10k from media: GlobalVoices, CafeBabel, EuroNews, SwissInfo (especially)
* → search arxiv, neurips, acl for neural alignment
* 6 languages → 21 pairs; 7 languages → 28 pairs, 8 → 36, 9 → 45
* 10,000 aligned sentence pairs each
* baseline word alignments: cross-lingual BERT similarity matrix (normalized weighted dot product? cosine similarity?) → add small-valued diagonal-normal matrix (multiplied by learnable scalar?) to learned alignments to slightly favor diagonal alignments (serve as tiebreaker) → learnable tiebreaker matrix per language pair
* loss: cross-entropy?
* operation: umax: union max: x → x in {rowmax(X), colmax(X)}
* add Project Syndicate to parallel text dataset, Eurozine, ereb.eu,
* alignment scheme:
* i=j for minimal (100%)
* i:j for strict (additional)
* i;j for bisurjective (additional)
* (i-j)<>(k-l) for MWE additional pairs
* i<>j for non-literal corresponding pairs
* characters: = , : ;  ’><’ ‘<>’ ( ) . ?
* output 3- or 4-dimensional tensor to account for different classes of alignments? k different heads?

```latex
* A_{[4, h]} (\vec{v} \otimes \vec{w} )_{[h, 1]} = \vec{p}_{[4, 1]} (?)

```
* modulating matrix C; enables k different outputs for different alignment levels

```latex
* A_i = L^B_{[m, h]} C_{i[h, h]} (L^A)^T_{[h, n]}, i \in \{1,2,...,k\}

```


```
* i \in [j-3, j + diff + 3]
* r > c: j-3 \leq i \leq j+d+3
* c > c: i-3 \leq j \leq i+d+3

```
