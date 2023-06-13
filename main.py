def order_to_right(input_list):
    max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
    output_list = []

    for row in input_list:
        output_row = []
        for i, item in zip(row, max_lengths):
            output_value = str(i).rjust(item)
            output_row.append(output_value)
        output_list.append(output_row)

    return output_list


data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

output_data_right = order_to_right(data)
print("Output(order to right):")

for row in output_data_right:
    print(row)


def order_to_left(input_list):
  max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
  output_list = []

  for row in input_list:
    output_row = []
    for i, item in zip(row, max_lengths):
      output_value = str(i).ljust(item)
      output_row.append(output_value)
    output_list.append(output_row)

  return output_list

data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

output_data_left = order_to_left(data)
print("Output(order to left):")

for row in output_data_left:
  print(row)



expected_output_right = [[' 1', '  2', '  10', ' 150'],
                         ['10', '  2', '1000', '   2'],
                         [' 1', '120', '   1', '1000']]

expected_output_left = [['1 ', '2  ', '10  ', '150 '],
                        ['10', '2  ', '1000', '2   '],
                        ['1 ', '120', '1   ', '1000']]



assert order_to_right(data) == expected_output_right
assert order_to_left(data) == expected_output_left