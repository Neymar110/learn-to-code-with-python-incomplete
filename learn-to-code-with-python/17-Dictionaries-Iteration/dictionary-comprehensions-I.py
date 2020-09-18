

Football_teams_and_their_stars = {
  "Barcelona" : {
    "Messi" : {
      "Age" : 33,
      "Height" : "5 feet 7 inches",
      "Date of Birth" : "24 June 1987"
    },
    "Suarez": {
      "Age" : 33,
      "Height" : "6 foot",
      "Date of Birth" : "24 January 1987",
    },
    "Pique" : {
      "Age" : 33,
      "Height" : "6 foot 4 inches",
      "Date of Birth" : "2 February 1987",
    },
    "Marc-andre ter stegen" : {
      "Age" : 28,
      "Height" : "6 feet 2 inches",
      "Date of Birth" : "30 April 1992",
    }
  },
  "Man City" : {
    "Kun Aguero" : {
      "Age" : 32,
      "Height" : "5 foot 6 inches",
      "Date of Birth" : "2 June 1988",
    },
    "Kevin De Bruyne" : {
      "Age" : 29,
      "Height" : "5 foot 11 inches",
      "Date of Birth" : "28 June 1991"
    },
    "Raheem Stering" : {
      "Age" : 25,
      "Height" : "5 feet 5 inches",
      "Date of Birth" : "8 December 1994",
    },
    "Ederson" : {
      "Age" : 27,
      "Height" : "6 feet 1 inch",
      "Date of Birth" :"17 August 1993"
    }
  },
  "PSG" : {
    "Neymar" : {
      "Age" : 28,
      "Height" : "5 feet 7 inches",
      "Date of Birth" :"5 February 1992"
    },
    "Mbappe" : {
      "Age" : 21,
      "Height" : "5 feet 8 inches",
      "Date of Birth" :"20 December 1998"
    },
    "Cavani" : {
      "Age" : 33,
     "Height" :"6 foot",
      "Date of Birth" :"14 February 1987"
    },
    "Di Maria" : {
      "Age" : 32,
      "Height" :"5 feet 9 inches",
      "Date of Birth" :"14 February 1988"
    }
  },
}

def Football_teams_and_their_stars_iteration_function(dictionary):
  for every_team in dictionary:
    for every_player in dictionary[every_team]:
      print(f"{every_player}")
    return "Done!!!!!"

print(Football_teams_and_their_stars_iteration_function(Football_teams_and_their_stars))