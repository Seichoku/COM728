def observed():
    observations = []
    for obsv in range(7):
        print("Please Enter an observation")
        obsv = str(input())
        observations.append(obsv)
    return observations


def run():
    print("Counting Observations....")
    observations = observed()
    obsv_set = set()
    for elements in observations:
        data = (elements, observations.count(elements))
        obsv_set.add(data)

    for data in obsv_set:
        print(f"{data[0]} observed {data[1]} times.")


run()
