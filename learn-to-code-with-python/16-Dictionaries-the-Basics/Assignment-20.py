nba_finals = {

  "Game 1": {

    "date": "05/05/2019",

    "location": "San Francisco",

    "statistics": {

      "points": 200,

      "rebounds": 20,

      "assists": 25

    }

  }

}
# print(nba_finals["Game 1"] ["statistics"]["rebounds"])

my_dict = {

  "a": {

    1: 2,

    3: 4,

    5: {

      6: 7,

      8: 9

    }

  }

}
# print(len(my_dict["a"]))

mystery = {

  "a": 2

}
print(mystery.setdefault("A", 5))

print(mystery.setdefault("a", 10))

print(mystery.setdefault("B", 30))

print(mystery.setdefault("B", 40))
