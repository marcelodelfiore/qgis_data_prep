# Usage:
# make install     => install dependencies
# make run FILE=your_file_name (without .xlsx) => run the script
# make clean       => remove all generated CSVs

install:
	pip install -r requirements.txt

run:
	python3 script.py $(FILE)

clean:
	rm -f ../CSV/*.csv
