class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols 
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self.__show_list.append(show)
        seats_layout = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats_layout

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print(f"Error: Show with id {show_id} does not exist.")
            return

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Error: Seat ({row}, {col}) is invalid.")
                return
    
            if self.__seats[show_id][row][col] == 1:
                print(f"Error: Seat ({row}, {col}) is already booked.")
                return
            self.__seats[show_id][row][col] = 1
        print(f"Seats {seat_list} successfully booked for show {show_id}.")

    def view_show_list(self):
        print("Shows running in this hall:")
        for show in self.__show_list:
            show_id, movie_name, time = show
            print(f"ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f"Error: Show with id {show_id} does not exist.")
            return

        print(f"Available seats for show {show_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.__seats[show_id][row][col], end=" ")
            print('\n')

hall1 = Hall(6, 6, 1)
hall1.entry_show("111", "Ammajan", "09:00")
hall1.entry_show("222", "habijabi", "12:00")
hall1.entry_show("333", "koijabi", "15:00")
hall1.entry_show("444", "koijabi", "18:00")
hall1.entry_show("555", "koijabi", "21:00")

check = True

while check:
    print('\n')
    print("1. View All Show Today")
    print("2. View Abailable Seat")
    print("3. Book Tiket")
    print("4. Exit")
    print('\n')

    option=int(input("Enter Option:"))

    print('\n')

    if option == 4:
        check = False
    if option == 1:
        hall1.view_show_list()
    if option == 2:
        id = input("Enter Show ID:")
        hall1.view_available_seats(id)
    if option == 3:
        showId = input("Enter the show ID:")
        colNo = int(input("Enter the column no:"))
        rowNo = int(input("Enter the row no:"))
        hall1.book_seats(showId, [(rowNo, colNo)])
