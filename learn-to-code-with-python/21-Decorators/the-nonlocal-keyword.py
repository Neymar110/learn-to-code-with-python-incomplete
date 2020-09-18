
def outer():
    def inner():
        global VAR
        VAR = "Var"
    inner()
    return VAR
print(outer())