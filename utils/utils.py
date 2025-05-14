
# Draw a line of stars with a specified character and margin
def draw_stars_line(n=50, char='*', margin=2):
    """
    Draw a line of stars with a specified character and margin.
    Parameters:
    n (int): Number of characters to print.
    char (str): Character to print.
    margin (int): Number of new lines to print after the line.
    Returns:
    None
    """
    padding  = "\n" * margin

    print(f"{padding}{char * n}", end= padding if margin > 0 else '')
