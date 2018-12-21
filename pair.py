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

    return pairings


def weekContainsPartner(week_pairings, partner):
    flattened = [item[1] for item in week_pairings]
    return partner in flattened


def pairingAlreadyExists(pairings, pairing):
    flattened = [item for sublist in pairings for item in sublist]
    return pairing in flattened


people = ["Kate", "Melissa", "Natalia", "Martin"]
pairings = calculatePairs(people)
for index, week_pairings in enumerate(pairings):
    print("Week " + str(index + 1) + ":")
    for pair in week_pairings:
        print("\t" + pair[0] + " + " + pair[1])
