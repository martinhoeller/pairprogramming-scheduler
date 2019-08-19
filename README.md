# Pair Pogramming Scheduler
A script that creates a weekly schedule for pair programming sessions within a team.

## Usage
`python pair.py [start_date] [weeks] [names]`

* `[start_date]` as `DD-mm-YYYY`
* `[weeks]` the number of weeks to calculate
* `[names]` a list of all team members' names

Example: 

```
python pair.py 24-04-2019 6 Jimmy Janis Mick Joan
```

## Output
```
Roster:
Week 1:
	Jimmy / Janis
	Mick / Joan
Week 2:
	Jimmy / Mick
	Janis / Joan
Week 3:
	Jimmy / Joan
	Janis / Mick

Sessions:
2019-08-21 00:00:00:
	Jimmy / Janis
	Mick / Joan
2019-08-28 00:00:00:
	Jimmy / Mick
	Janis / Joan
2019-09-04 00:00:00:
	Jimmy / Joan
	Janis / Mick
2019-09-11 00:00:00:
	Jimmy / Janis
	Mick / Joan
```

The first part of the output is the repeating pairing roster for each week.
The second part are the concrete pairing sessions with the calculated dates.