# Entity Mapping

* LCS with poetry
* Inferenzverfahren verfeinern
* Pfadgeneralisierung für Schleifen in den Daten
* Tests schreiben
* Create paths object for managing all relevant paths
* evaluation method for each rule -> check whether rule generalizes; bootstrap for mappings
* composite (multi-input) rules
* use protocol classes in Python

* UNA
* UNB - Interchange Header
* UNH - Message Header
* BGM - Begnning of Message
* (TSR) - transport service requirements
* MOA - monetary amount
* FTX+AAA - Free Text
* CNT+7 - Control Total
* CNT+11
* CNT+15
* TOD - terms of delivery or transport
* LOC - place / location identification
* 5 departure
* 7 delivery
* 8 destination
* RFF - reference
* GOR - governmental requirements
* DTM - date/ time / period
* NAD - name and address
* CTA - contact information
* COM - communication contact
* GID - goods item details
* MEA - measurements
* DIM - dimensions
* DOC - document / message details
* PCI - package identification
* GIN - goods identity number
* EQD - line item (?)
* TCC+INV - (?)
* MOA - monetary amount
* QTY - quantity
* MEA - measurements
* FTX - free text
* UNT - message trailer
* UNZ - interchange trailer
* FTX+AAA - goods description
* FTX+AAB
* FTX+DIN
* FTX_AAD
* WT - weight
* VOL - volume
* MTQ -m^2

* +KGM - kg

* +AAE - item gross weight

```

```tex
* y_i = f^*(\vec{x}) = argmax_{f_i} s(f_i)

```txt
* RL Model for DHL: (path, entity, all paths) -> (path, entity)                                            -> mapping: rules, constraints on rules

```tex
* a_t = \pi_\theta (\cdot | s_t)

```

* 0. path enumeration
* 1. recognition of corresponding entities (values)
   (rule-based) -> by type: string, num, date
* 2. raw path2path count matrix
* 3. Initialize mapping for each output path -> a priori probabilistic mapping
* 4. generate rule space -> as tree
   `f_i(path) = value` -> list of candidate rules
* 5. increment rule score for each rule generating correct output    operations:    * identit
  * numerical transformation (solve by e.g. regression
  * string operations: substring,character mapping, casing, substring transposition
