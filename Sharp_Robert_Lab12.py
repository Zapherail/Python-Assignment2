#Sharp, Robert

def main():
    #Creating a list of songs
    songs = ['Life is Good', 'Him', 'Bars No Jutsu']
    #Opening file to be written to pg.292
    outfile = open('songs.txt', 'w')
    print('Songs to be written into the file:')
    #Adding list to file pg.292-294, skype video
    for song in songs:
        outfile.write(song + '\n')
        #Closing outfile
    outfile.close()
    for song in songs:
        print(song, sep='')

    second_part()


def second_part():
    #Opening file for reading pg.294-295, skype video
    infile = open('songs.txt', 'r')
    #Saving songs to memory pg.295
    song_list = infile.read()
    #closing file
    infile.close()
    #Printing information from the file that was read.
    print('Songs read from the file:')
    print(song_list)

main()
