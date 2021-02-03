from unittest.mock import Mock

Example = Mock(return_value = "Anything")

print(Example())

Example.-

Example.return_value = 25

print(Example())

Example.speed.return_value = "25km/H"

print(Example.speed())