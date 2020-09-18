family = {
     "Cucu and Guka" : {
            "Carole and Eston" :["Sheshi", "Shiro"],
            "Humphrey and Elizabeth" : ["David", "Isaac"],
            "Ruth and Bobby" : ["Ranja"],
            "Anne and Jonathan" : {"Jayda", "Ziva"}
     }
}

def dictionarySearch (Dictionary, *args):
    for every_name in args:
        print(Dictionary[every_name])
print(dictionarySearch(family, "Cucu and Guka"))