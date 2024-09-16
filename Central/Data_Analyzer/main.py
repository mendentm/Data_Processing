import re
# Functionality includes: word count, search_keyword, lines with numbers, run_operation, add_operation
# search_keyword function in DataAnalyzer class update to count the number of times the keyword appears in the data.

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._read_file()
        self.operations = {
            'word_count': self.word_count,
            'search_keyword': self.search_keyword
        }
    
    def _read_file(self):
        # Reads the text file and returns the content as a list of lines
        with open(self.file_path, 'r') as file:
            return file.readlines()
    
    def word_count(self):
        # Counts the total number of words in the file.
        total_words = sum(len(line.split()) for line in self.data)
        return total_words
    
    def search_keyword(self, keyword):
        # Searches for a specific keyword in the data and returns the lines that contain the keyword.
        matching_lines = [line for line in self.data if re.search(keyword, line, re.IGNORECASE)]
        return matching_lines
    
    def run_operation(self, operation_name, *args):
        # Runs a specified operation if it's available in the operations dictionary.
        if operation_name in self.operations:
            return self.operations[operation_name](*args)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")
    
    def add_operation(self, name, function):
        #Adds a new operation to the analyzer.
        self.operations[name] = function

# Example of adding a custom operation
def count_lines_with_numbers(analyzer):
    # Counts lines that contain numbers.
    return sum(1 for line in analyzer.data if re.search(r'\d', line))

# Usage Example:
if __name__ == "__main__":
    # Initialize the DataAnalyzer with a file
    analyzer = DataAnalyzer('scraped_data.txt')

    # Run some predefined operations
    total_words = analyzer.run_operation('word_count')
    print(f"Total words: {total_words}")
    
    # Search for a specific keyword in the data
    keyword = 'page'
    results = analyzer.run_operation('search_keyword', keyword)
    print(f"Lines containing '{keyword}':")
    for line in results:
        print(line.strip())

    # Add a new operation
    analyzer.add_operation('count_lines_with_numbers', lambda: count_lines_with_numbers(analyzer))
    
    # Run the new operation
    lines_with_numbers = analyzer.run_operation('count_lines_with_numbers')
    print(f"Lines with numbers: {lines_with_numbers}")
