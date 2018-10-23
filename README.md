# ApproximateWordCorrect

# Installation

There is a necessary library for this project: jellyfish  
Install jellyfish from PyPI using pip installer:

	pip3 install jellyfish

# Example Usage

After open terminal or any command line tool you're using:  

	use cd command navigate to the/assignment1 folder 
	Python3 kt.py -f FilePath -g/-d/ (or -n 2/3)

	-g is choosing Levenshtein Distance.
	-d is choosing Damerau-Levenshtein Distance.
	-n is choosing N-gram, and this should be followed by a number n to indicate the substring  length.

Running Tests:
	pip3 install jellyfish
	cd Users/sichenzhao/Desktop/kt/assignment1
	python3 kt.py -f /Users/*/Desktop/ -g

Noted that this project is coded using python3. And you can only run one method with one setting at a time.

# Output

After finish all calculation, there will be the result about this run. And if you want more specific details, you can find corresponding log file in the folder /LOG, and each run will create two seperate files. 

The Accuracy file example:  

	5,agin                 this is the headword from misspell.txt  
	----------  
	agin                   this is the single prediction return from the system  
	again                  this is corresponding word in correct.txt  

	6,aginst
	----------  
	against   * 
	against 

If the return word is match with the correct word, there will be a * mark behind it. The precision will be shown at the end of this file.

The Precision file example:  

	7,ahain
	----------  
	again   *  
	alain
	amain
	arain
	chain
	ghain
	hain
	again

The structure of this file is similar to the accuracy file and precision, recall will be shown at the end of this file.  
Noted that the result files will be covered by another run on the same setting.
