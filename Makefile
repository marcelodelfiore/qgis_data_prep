.PHONY: install run clean

install:
	pip install -r requirements.txt

run:
ifndef FILE
	$(error Usage: make run FILE=your_filename_without_extension)
endif
	python3 data_prep.py $(FILE)

clean:
	rm -f CSV/*.csv
