from string import ascii_uppercase


t = int(input())

letters = {
    'A': 2,
     'B': 2,
      'C': 2,
       'D': 3,
        'E': 3,
         'F': 3,
          'G': 4,
           'H': 4,
            'I': 4,
             'J': 5,
              'K': 5,
               'L': 5,
                'M': 6,
                 'N': 6,
                  'O': 6,
                   'P': 7,
                    'Q': 7,
                     'R': 7,
                      'S': 7,
                       'T': 8,
                        'U': 8,
                         'V': 8,
                          'W': 9,
                           'X': 9,
                            'Y': 9,
                             'Z': 9,
    }

for x in range(t):
    number = input().replace("-", "")[:10]
    
    line = []
    for x in number:
        if x in ascii_uppercase:
            line.append(str(letters[x]))
        else:
            line.append(x)
    
    print(line[0]+line[1]+line[2]+"-"+line[3]+line[4]+line[5]+"-"+line[6]+line[7]+line[8]+line[9])