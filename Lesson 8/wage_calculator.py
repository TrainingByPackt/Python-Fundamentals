import csv

output_data = []

with open('input.csv', 'r') as f:
    mock_data_reader = csv.reader(f)
    output_data = []
    line_count = 1

    for row in mock_data_reader: 
      if line_count != 1:
        row[1] = int(row[1]) * 15
        output_data.append(row)

      line_count += 1

with open('output.csv', 'w') as f:
    fields = ['name', 'wages']
    output_writer = csv.DictWriter(f, fieldnames=fields)

    output_writer.writeheader()

    for line in output_data:
      output_writer.writerow(
        {
          'name': line[0],
          'wages': line[1]
        }
      )
