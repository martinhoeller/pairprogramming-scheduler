#!/usr/bin/python

import sys


def calculatePairs(people):
    evenNumber = (len(people) % 2 == 0)

    weeks = len(people)
    if evenNumber:
        weeks = weeks - 1

    pairings = []
    for week in range(weeks):
        pairings.append([])

    for person_index, person in enumerate(people):
        for week in range(weeks):
            week_pairings = pairings[week]

            for partner_index, partner in enumerate(people):
                if not evenNumber:
                    if person_index == week or partner_index == week:
                        continue
                if (partner == person):
                    continue
                if (weekContainsPartner(week_pairings, partner)):
                    continue

                pair = (person, partner)

                if (pairingAlreadyExists(pairings, pair)):
                    continue

                week_pairings.append(pair)
                break

    # clean up pairings
    cleaned_pairings = []
    for week_pairing in pairings:
        cleaned_week_pairings = []
        for pair in week_pairing:
            inverse_pair = (pair[1], pair[0])
            if pair in cleaned_week_pairings or inverse_pair in cleaned_week_pairings:
                continue
            else:
                cleaned_week_pairings.append(pair)

        cleaned_pairings.append(cleaned_week_pairings)

    return cleaned_pairings


def weekContainsPartner(week_pairings, partner):
    flattened = [item[1] for item in week_pairings]
    return partner in flattened


def pairingAlreadyExists(pairings, pairing):
    flattened = [item for sublist in pairings for item in sublist]
    return pairing in flattened


def printHelp():
    print "Usage: "
    print "\tpython pair.py person1 person2 ..."
    print ""
    print "Provide at least two persons"
    print ""


if len(sys.argv) < 3:
    printHelp()
    exit(0)

people = sys.argv
people.pop(0)

pairings = calculatePairs(people)
for index, week_pairings in enumerate(pairings):
    print("Week " + str(index + 1) + ":")
    for pair in week_pairings:
        print("\t" + pair[0] + " / " + pair[1])
