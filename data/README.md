# Local dataset

This repository does not distribute the course dataset. Obtain an authorized
copy of the original EE4C12 CE_ARR data and place these files here:

```text
train_data.csv
val_data.csv
test_data.csv
```

The files have no header. Each row contains 250 ECG sample values and a
numeric label in column 251. Keep the supplied splits unchanged to compare
with the reported experiments.

| Numeric label | Beat type | Grouped label | AAMI class |
| ---: | --- | ---: | --- |
| 0 | N | 0 | N |
| 1 | / | 4 | Q |
| 2 | L | 0 | N |
| 3 | R | 0 | N |
| 4 | e | 0 | N |
| 5 | j | 0 | N |
| 6 | A | 1 | S |
| 7 | a | 1 | S |
| 8 | J | 1 | S |
| 9 | S | 1 | S |
| 10 | E | 2 | V |
| 11 | F | 3 | F |
| 12 | V | 2 | V |
| 13 | f | 4 | Q |
| 14 | Q | 4 | Q |

The original course documentation supplies this label convention. CSV files
and other local data formats are ignored by Git.
