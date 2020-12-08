# HackerRank Practice => Interview Preparation Kit => Warm-up Challenges => Jumping on the Clouds
def jumpingOnClouds(c):
    count = 0
    index = 0
    end_index = len(c) - 1
    while index < end_index:
        if index + 2 <= end_index:
            if c[index + 2] == 0:
                index += 2
                count += 1
            else:
                index += 1
                count += 1
        elif index + 1 <= end_index:
            index += 1
            count += 1
    return count