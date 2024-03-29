# CISC320_pa1-Cows
SP2022 CISC320 Prof. Silber. Programming Assignment 1: Cows!


## Prof. Silber Instructions:

> Your dairy scientist friend heard about how well you handled the horse races in algorithmic problem 1, and wants you to help them with their cows. They have many, many herds with sensors on each of the cows. The owners of the cows need real-time reports on the cows status based on the ever-changing information coming in. They need you to create a program that can take in a stream of cow data and report the current status of all the cows. The sensors collect data about the cow's weight and milk production, and your system will report the:

> - Cow's lowest weight
> - Cow's latest weight
> - Cow's average milk production

> To achieve full credit for performance, you must use built-in data structures to achieve **O(1)** expected case performance for each row of input (a cow record). Your overall solution should run in at least average case **O(c*log(c)+r)**, where c is the number of cows and r is the number of rows of input (i.e., the number of cow records).

---
## Formal Specification

> **Problem:** Calculate, sort, and report minimum, most recent, and average of a sequence of records.

> **Input:** The filename of a local file containing a sequence of cow records, each on their own line. The first line will be the number of records to read, and is not included in the number of records. You can assume that each line will only contain one record. The records will come in ordered by the time they were collected.

> A cow record consists of three numbers and a letter, separated by spaces (in the form "Number, Letter, Number, Number"). All numbers will be 32-bit integers (i.e., no more than 2^31).

> - The first element is the Cow ID, a unique number representing that cow inside the dataset.
> - The second element is the Action Code, and will be either the letter "W", "M", or "T"
> - If the letter is "W", for "Weighing", then the third element will be the latest Weight of the cow (a number in pounds).
> - If the letter is "M", for "Milking", then the third element will be the amount of the Milk produced by the cow (a number in pounds).
> - If the letter is "T", for "Temperature", then the third element will be the current Temperature of the cow (a number in Fahrenheit).
> - The fourth element is the Timestamp, a number representing when the record was made.

### Example:
```
507 W 1000 1
1 M 6 2
1 W 1400 3
1 M 8 8
1 T 101 10
507 M 4 12
1 W 1700 15
1 M 7 16
507 M 8 20
```
> **Output:** A series of sorted cow status reports. Each line of output will contain four numbers:
> - The cow's ID
> - The cow's lowest weight
> - The cow's latest weight
> - The cow's average milk production (the sum of all the milkings divided by the number of milkings).

> If a cow doesn't have at least one weighing and at least one milking, then you should exclude it from the output. The cows should be sorted in ascending order based the status results: first by their lowest weight, than their latest weight, and finally by their highest average milk production. Truncate any decimals to become integers.
### Example
```
507 1000 1000 6
1 1400 1700 7
```
