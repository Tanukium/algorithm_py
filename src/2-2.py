def era_convert(year):
    if year not in range(1868, 2021):
        raise ValueError("This year is not in 1869~2020!!")

    era_dict = {
        1868: "Meiji",
        1912: "Taisei",
        1926: "Shouwa",
        1989: "Heisei",
        2019: "Reiwa"
    }

    era = ""
    era_year = 0
    for key in era_dict:
        if year >= key:
            era = era_dict[key]
            era_year = year - key + 1
    result = "{}, {}".format(era, era_year)
    return result


if __name__ == "__main__":
    print(era_convert(1937))
    print(era_convert(1945))
    print(era_convert(2021))
