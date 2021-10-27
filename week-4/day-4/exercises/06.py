# ake a list of magician’s names.
magician_list = ['Hodini','magician 1','magician 2']
# Pass the list to a function called show_magicians(),
def show_magicians():
    for magician in magician_list:
        print(magician)

#  which prints the name of each magician in the list.
# Write a function called make_great() that modifies the
#  list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great():
    for i in range(0,len(magician_list)):
        magician_list[i] += ' The great'
    return magician_list
make_great()   
show_magicians()
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been
#  modified.