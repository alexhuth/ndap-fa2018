# filename = "labels.txt"

def parse_labels(filename):
    """Load labels from the file specified in filename.
    
    Assumes that each line of the file is whitespace-delimited, and has this
    structure:
      index gif_file label label label label ...
    with an arbitrary number of labels per line.

    Returns a list of dictionaries, where each contains the keys "index",
    "labels" (which returns a list of labels), and "gif_file".
    """
    f = open(filename)

    labels = [] # create an empty list
    for line in f:
        words = line.split() # split the line into words

        line_dict = dict(index=int(words[0]), # create a dict from words
                         gif_file=words[1],
                         labels=words[2:])
        
        labels.append(line_dict) # append dict to the complete list
    
    return labels