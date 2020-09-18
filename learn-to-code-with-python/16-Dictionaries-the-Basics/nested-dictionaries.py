family = {
    "Muturi" : {
        "Cucu and Guka" :{
            "Carole and Eston" :["Sheshi", "Shiro"],
            "Humphrey and Elizabeth" : ["David", "Isaac"],
            "Ruth and Bobby" : ["Ranja"],
            "Anne and Jonathan" : {"Jayda", "Ziva"}
        }
    },
    "Mutuku" : {
        "Cucu and Guka" : {
            "Irene" : [None],
            "Faith and Ablert" : [None],
            "Elizabeth and Humphrey" : ["David", "Isaac"],
            "Louise and Allan" : ["Ethan", "Ivan"],
            "Joyce" : [None]
        }
    }
}
# print(family["Muturi"]["Cucu and Guka"]["Ruth and Bobby"][0])
# print(len(family["Muturi"]["Cucu and Guka"]))
# print(family.get("Muturi"))
print(family.setdefault("Muturi1", "Fruits"))