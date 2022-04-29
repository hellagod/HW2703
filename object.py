class Hotel:
    types_count = 5
    SGL, DBL, TRPL, JS, S = 0, 1, 2, 3, 4

    class Room:
        kinds = ['одноместный номер', 'двухместный номер', 'трехместный номер', 'полулюкс', 'люкс']
        prices = [100, 200, 300, 500, 1000]

        def __init__(self, kind_id: int):
            self.kind = self.kinds[kind_id]
            self.price = self.prices[kind_id]
            self.is_busy = False

    def __init__(self):
        self._rooms = dict()

    def add_room(self, num: int, kind_id: int):
        if 0 <= kind_id < self.types_count:
            if not self._rooms.get(num) :
                self._rooms[num] = self.Room(kind_id)
            else:
                raise RuntimeError("Такая комната уже существует")
        else:
            raise RuntimeError("Такого типа нет")

    def occypy(self, room_id):
        if self._rooms[room_id]:
            if not self._rooms[room_id].is_busy:
                self._rooms[room_id].is_busy = True  # бронируем номер
            else:
                raise RuntimeError("Номер занят")
        else:
            raise RuntimeError("Такой комнаты нет")

    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_id):
        if self._rooms[room_id]:
            self._rooms[room_id].is_busy = False
        else:
            raise RuntimeError("Такой комнаты нет")

    def all_occypy(self):
        for i in self._rooms.keys():
            self._rooms[i].is_busy = True

    def all_free(self):
        for i in self._rooms.keys():
            self._rooms[i].is_busy = False

    def revenue(self):
        a = 0
        for i in self._rooms.keys():
            if self._rooms[i].is_busy:
                a += self._rooms[i].price
        return a

    def busy_count(self):
        a = 0
        for i in self._rooms.keys():
            if self._rooms[i].is_busy:
                a += 1
        return a

    def __str__(self):
        a = ''
        for i in self._rooms.keys():
            if not self._rooms[i].is_busy:
                a += 'Номер ' + str(i) + " свободен\n"
            else:
                a += 'Номер ' + str(i) + " занят\n"
        return a[:-1]


hotel = Hotel()
hotel.add_room(11, 0)
hotel.add_room(111, 1)
hotel.add_room(121, 1)
hotel.add_room(211, 2)
hotel.add_room(311, 3)
hotel.add_room(411, 4)
hotel.add_room(13, 0)
print(hotel)


hotel.all_occypy()
print(hotel)

print(hotel.revenue())

hotel.all_free()
print(hotel)

print(hotel.revenue())


hotel.occypy(13)

hotel.occypy(121)

hotel.occypy(411)

print(hotel)
print(hotel.revenue())
print(hotel.busy_count())

hotel.free(13)

hotel.free(121)

hotel.free(411)

print(hotel)



