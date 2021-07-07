# strip-spreadsheet
Strip a spreadsheet of extra spaces and blank-celled rows

## Usage
```shell
python3 main.py input.csv [-o <ouput_file_name.csv>]
```

### Arguments
- possissional arguments: 
The CSV input file.
- optional arguments:
`-o <new_sheet>`

NOTE: the if `-o` argument was not specified, the script write the new sheet to `input_cleaned.csv`.
