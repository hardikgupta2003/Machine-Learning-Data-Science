multidimensional_dict = {
        'first_level': {
             'second_level_1': {
                     'third_level_1': 1,
                     'third_level_2': 2
               },
        'second_level_2': {
                    'third_level_3': 3,
                    'third_level_4': 4
                   }
              },
 'another_first_level': {
                'second_level_3': {
                             'third_level_5': 5,
                             'third_level_6': 6
                             },
              'second_level_4': {
                            'third_level_7': 7,
                            'third_level_8': 8
                    }
             }
        }
value = multidimensional_dict['first_level']['second_level_1']['third_level_2']
print(value)