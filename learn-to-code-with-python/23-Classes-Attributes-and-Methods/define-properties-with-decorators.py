# class FootballPlayer():
#     def __init__(self, player, club):
#         self.player = player
#         self.club = club
    

#     def _get_club(self):
#         return print(self.club)

#     def _set_club(self, footbalclub):
#         self.footballclub = footbalclub
#         self.footballclub
    
#     club = property(_get_club, _set_club)

# Messi = FootballPlayer("Messi", "Barcelona")
# print(Messi._get_club)

class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0
        
    def _slices_eaten_getter(self):
        return self._slices_eaten
        
    def _slices_eaten_setter(self, num):
        if num < self.total_slices:
            self._slices_eaten = num
            
    def _percentage_getter(self):
        percentage1 = self._slices_eaten / self.total_slices * 100
        return percentage1
        
    slices_eaten = property(_slices_eaten_getter, _slices_eaten_setter)
    
    percentage = property(_percentage_getter)

cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage) 
# 0.25

# cheese.slices_eaten = 4
# print(cheese.percentage) 
# # 0.5

# cheese.slices_eaten = 10 
# # _slices_eaten should not change because there's only 8 slices in pie
# print(cheese.percentage) 
# 0.5
        
  