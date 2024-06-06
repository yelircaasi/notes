# RL Games

## wizard

* model for each round: jester, wizard, trump, color A, color B, color C → how to achieve interchangeability between non-trump colors? will it learn this automatically if colors are assigned randomly to letters?
* states:
  * betting state: number of players, round number, trick number, cards in hand
  * playing state: number of players, round number, trick number, tricks to make, cards already played → probability of cards , cards in hand
* actions: bet made, card played
* policies:
  * betting policy: betting state → bet
  * playing policy: playing state → card
* → how to learn? simultaneously? iteratively? (seems better)
* [semanticscholar.org/paper/Application-of-reinforcement-learning-to-the-card-Backhus-Nonaka/346bc4eaad1a89e84aa8cda08b623973ec0a2fb7](https://www.semanticscholar.org/paper/Application-of-reinforcement-learning-to-the-card-Backhus-Nonaka/346bc4eaad1a89e84aa8cda08b623973ec0a2fb7)
* Combinatoric-probabilistic features:
* Probability that each player can beat each card
* Probability that each player wants to beat each card

## blackjack

## bridge

## canasta

## codenames

## haiclue

## hanabi

## lucky_numbers

## mastermind

## poker

## rook

## rush_hour

## scum

## skyjo

## stratego

## sushigo

## ticket_to_ride

## whist



# Brainstorming

* → use evolutionary algorithm?
* → combine RL and evolutionary algorithm?
* → compare end-to-end with system that uses dynamic internal marking of cards (”need to win” / “need to get rid of”, etc.) and with system that uses probability of winning with each card
* → comparing systems that focus solely on making the bet with systems that also try to ruin the game for others (aggressive strategy)
* → different vector for each number of cards → output vector a score (softmax?) over cards in the hand, → action is to play the highest-scoring card
    → drawback: many different models; advantage: each model is fixed-size and relatively straightforward: $N = \sum^{15}_{i=1} i = 120$ → or N = 15?
    → parameters:
        — $p_c(\textbf{c}) \in [0,1]^{k}$: probability of each card being out there — easy to calculate
        — $p_d(\textbf{c}) \in [0,1]^{k}$: probability of each card being played by someone else — calculate via MC

        — $w(\textbf{c}) \in [0,1]^{k}$: win probability of each card ← (remaining available to be made, wanted for each player, two probability vectors) — calculate via MC

        — $d(\textbf{c}) \in \mathbb{R}^{k}: ||d(c)||=1$: win desirability of each card ← (remaining available, wanted, two probability vectors, win probabilities) — calculate via MC? policy gradient?

        — $s(\textbf{c}) \in [0,1]$: overall hand strength ← (win probability, win desirability)

        — $u(\textbf{c}) \in \mathbb{R}^{k}$: score (utility) per card ← (win probability, win desirability, expected change in overall hand strength)

        — $m \in \{0, 1\}^{k}$: use a card mask to only update values for cards in my hand

        — alternative: recursive formulation, beginning with last card of the round

        — another option: $f(\textbf{c}) \in \{0,1\}^{211}$: card score distribution ← (surplus tricks, size 2k+1, cards in my hand, probability of cards still being out there, position in queue, cards already played) → dimensionality 2k+1+60+60+4+60 = 2k+185 → add number still wanted by each opponent
