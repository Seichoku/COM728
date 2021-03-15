def observed():
    observations = []
    for observation in range(5):
        print("Please Enter an observation")
        observation = str(input())
        observations.append(observation)
    return observations


def remove_observations(observations):
    print("DO you wish to remove observations??")

