# Run Score Function

Interpretation:

* 1 point per kilometer, at intensity __equivalent__ to 5k in 30:00 -> 5-star run
* flat 5k in 25:00 -> 7 points?
* more points for higher intensity
* 4-minute single kilometer may be worth 1 point
* 3 points for 13:30 km
* 12 points for 10 k in 60:00?
* 15 points
* more points for higher change in elevation

```tex
f(d, p, n, t, b)
```

* d: distance
* p: positive elevation gain
* n: absolute negative elevation change
* t: total time
* b: total break time

* average speed: d/a
* elevation gain: p-n
* flatness: -(p+n)/d
* break proportion b/t

Simple version: β1 speed + β2 (p+n)/d + β3 (b/t)

Better: polynomial regression problem or neural network.

Need to create a system of equations and solve it.

Use [calorie calculator](https://runbundle.com/tools/running-calorie-calculator) or [this](https://www.omnicalculator.com/sports/running-calorie) or [this](https://runnersconnect.net/calories/) or [this](http://hikingscience.blogspot.com/p/calculate-calories-burned_22.html)

Alternative approach: Calculate 100+ familiar routes (and their cross-product with different times) and order them all in terms of difficulty -> then find a scoring that respects the relative difficulty. -> or that __approximately__ respects it, with some degree of tolerance but overall optimizing some comparison-derived objective function.

Use ladder loss? Take a batch, calculate average pairwaise loss and backpropagate that to update the parameters.

Alternative: use physics to make exact calculations of the difficulty, work required, etc.

Another alternative: Calculate 1st and 2nd derivatives for each variable. And each composite variable?

Also record myself on maybe 20 different runs and, with a slight discounting factor to account for improving fitness over time, calculate a basic score function that works well for planning and journaling.

f(distance, elevationUp, elevationDown, totalTime, breakTime)

Learn how to solve this:

```tex
β_0 + β_1 l^{q_1} + β_2 p^{q_2} + β_3 n^{q_3} + β_4 t^{q_4} + β_5 b^{q_5} 
```

Iterative methods required?
