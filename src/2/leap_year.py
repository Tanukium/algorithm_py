def leap_year():
    result = []
    for i in range(1950, 2051):
        if i % 4 == 0:
            if i % 100 == 0 and i % 400 != 0:
                continue
            result.append(i)
    return result


if __name__ == "__main__":
    print(leap_year())
