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

output_data = order_to_right(data)

for row in output_data:
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

output_data = order_to_left(data)

for row in output_data:
  print(row)
