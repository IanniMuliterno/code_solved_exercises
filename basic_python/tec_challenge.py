'''
QUESTION
I have a string that contains codes representing different genders ('W' for women, 'M' for men, and 'C' for other). I need to analyze this string and produce a
summary that shows the count of each gender, ordered from the most frequent gender to the least frequent.  The output should be in a compact format like '3W2M1C', 
where the number precedes the gender code. How can I write a function to do this?
'''

# ANSWER

def count_gender_from_string(string: str) -> str:
    """
    Counts the occurrences of characters representing genders ('W', 'M', 'C') within a string 
    and returns a string summarizing the counts in descending order of frequency.

    Args:
        string: The input string to analyze.

    Returns:
        A string representing the counts of each gender character, ordered from most frequent to least frequent.  
        The format is "{count1}{gender1}{count2}{gender2}{count3}{gender3}", where counts are integers and genders are 'W', 'M', or 'C'.  
        If a gender character is not found, its count will be 0.

    Example:
        count_gender_from_string("WWMMCCW") == "3W2M2C"
        count_gender_from_string("WMC") == "1W1M1C"
        count_gender_from_string("AAAA") == "0W0M0C"  # Handles cases where no gender characters are present.
    """
    dic = {'W': 0, 'M': 0, 'C': 0}

    for gender in dic.keys():
        dic[gender] = string.count(gender)

    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

    result = ''
    for key, value in dic.items():
        result += str(value) + key

    return result
