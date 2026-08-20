"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    seat_letters = ['A', 'B', 'C', 'D']
    current_index = 0
    while current_index<number:
        yield seat_letters[current_index%4]
        current_index += 1
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    row_number,counter = 1,1
    seat_letters = generate_seat_letters(number)
    while counter<=number:
        seat_letter = next(seat_letters)
        yield str(row_number) + seat_letter
        counter += 1
        if seat_letter == 'D':
            row_number += 1 if row_number!=12 else 2


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passenger_seats_dict = {}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        passenger_seats_dict[passenger] = next(seats)
    return passenger_seats_dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        seat_code = seat_number + flight_id
        zero_filler = '0' * (12 - len(seat_code))
        yield seat_code + zero_filler