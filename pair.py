def calculatePairs(people):
    weeks = len(people) - 1

    pairings = []
    for week in range(weeks):
        pairings.append([])

    for person in people:
        for week in range(weeks):
            week_pairings = pairings[week]

            for partner in people:
                if (partner == person):
                    continue
                if (weekContainsPartner(week_pairings, partner)):
                    continue

                pair = (person, partner)

                if (pairingAlreadyExists(pairings, pair)):
                    continue

                week_pairings.append(pair)
                break

    return pairings


def weekContainsPartner(week_pairings, partner):
    flattened = [item[1] for item in week_pairings]
    return partner in flattened


def pairingAlreadyExists(pairings, pairing):
    flattened = [item for sublist in pairings for item in sublist]
    return pairing in flattened


people = ["a", "b", "c", "d"]
pairings = calculatePairs(people)
for index, week_pairings in enumerate(pairings):
    print("Week " + str(index + 1) + ":")
    for pair in week_pairings:
        print("\t" + pair[0] + " + " + pair[1])
